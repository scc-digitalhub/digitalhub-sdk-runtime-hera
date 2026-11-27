# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.plugins import (
    Action,
    BuilderDef,
    CrudPlugin,
    ExecFamily,
    ExecutableActions,
    RunBuilder,
    SourceBuilderMixin,
    Status,
    Task,
    TaskBuilder,
    TaskSpecWorkflow,
    WorkflowBuilder,
)

from digitalhub_runtime_hera.entities._commons.enums import Actions, EntityKinds
from digitalhub_runtime_hera.entities.run._base.entity import RunHeraRun
from digitalhub_runtime_hera.entities.run._base.spec import RunSpecHeraRun
from digitalhub_runtime_hera.entities.run._base.status import RunStatusHeraRun
from digitalhub_runtime_hera.entities.workflow.hera.crud import new_workflow_hera
from digitalhub_runtime_hera.entities.workflow.hera.entity import WorkflowHera
from digitalhub_runtime_hera.entities.workflow.hera.spec import WorkflowSpecHera

# Imported on first use: the entities register even when the runtime cannot be
# imported, and the import error is reported when a run executes locally.
RUNTIME_HERA_BUILDER = "digitalhub_runtime_hera.runtimes.builder:RuntimeHeraBuilder"

hera = ExecFamily(
    executable=BuilderDef(
        EntityKinds.WORKFLOW_HERA,
        WorkflowHera,
        WorkflowSpecHera,
        Status,
        base=WorkflowBuilder,
        mixins=(SourceBuilderMixin,),
        shortcuts=(CrudPlugin(new_workflow_hera),),
    ),
    actions={
        Actions.PIPELINE: Action(
            task=BuilderDef(EntityKinds.TASK_HERA_PIPELINE, Task, TaskSpecWorkflow, Status, base=TaskBuilder),
            run=BuilderDef(
                EntityKinds.RUN_HERA_PIPELINE, RunHeraRun, RunSpecHeraRun, RunStatusHeraRun, base=RunBuilder
            ),
        ),
        ExecutableActions.BUILD: Action(
            task=BuilderDef(EntityKinds.TASK_HERA_BUILD, Task, TaskSpecWorkflow, Status, base=TaskBuilder),
            run=BuilderDef(EntityKinds.RUN_HERA_BUILD, RunHeraRun, RunSpecHeraRun, RunStatusHeraRun, base=RunBuilder),
        ),
    },
    runtime_builder=RUNTIME_HERA_BUILDER,
)

entity_plugins = (*hera.plugins(),)
