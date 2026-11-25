# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.plugins import CrudPlugin, EntityPlugin

from digitalhub_runtime_hera.entities.run.build.builder import RunHeraRunBuildBuilder
from digitalhub_runtime_hera.entities.run.pipeline.builder import RunHeraRunPipelineBuilder
from digitalhub_runtime_hera.entities.task.build.builder import TaskHeraBuildBuilder
from digitalhub_runtime_hera.entities.task.pipeline.builder import TaskHeraPipelineBuilder
from digitalhub_runtime_hera.entities.workflow.hera.builder import WorkflowHeraBuilder
from digitalhub_runtime_hera.entities.workflow.hera.crud import new_workflow_hera

# Imported on first use: the entities register even when the runtime cannot be
# imported, and the import error is reported when a run executes locally.
RUNTIME_HERA_BUILDER = "digitalhub_runtime_hera.runtimes.builder:RuntimeHeraBuilder"

workflow_hera_plugin = EntityPlugin(
    builder=WorkflowHeraBuilder,
    shortcuts=(CrudPlugin(new_workflow_hera),),
    runtime_builder=RUNTIME_HERA_BUILDER,
)

entity_plugins = (
    workflow_hera_plugin,
    EntityPlugin(builder=TaskHeraPipelineBuilder, runtime_builder=RUNTIME_HERA_BUILDER),
    EntityPlugin(builder=TaskHeraBuildBuilder, runtime_builder=RUNTIME_HERA_BUILDER),
    EntityPlugin(builder=RunHeraRunBuildBuilder, runtime_builder=RUNTIME_HERA_BUILDER),
    EntityPlugin(builder=RunHeraRunPipelineBuilder, runtime_builder=RUNTIME_HERA_BUILDER),
)
