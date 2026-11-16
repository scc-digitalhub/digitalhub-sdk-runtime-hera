# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.factory.plugins import CrudPlugin, EntityPlugin

from digitalhub_runtime_hera.entities.run.build.builder import RunHeraRunBuildBuilder
from digitalhub_runtime_hera.entities.run.pipeline.builder import RunHeraRunPipelineBuilder
from digitalhub_runtime_hera.entities.task.build.builder import TaskHeraBuildBuilder
from digitalhub_runtime_hera.entities.task.pipeline.builder import TaskHeraPipelineBuilder
from digitalhub_runtime_hera.entities.workflow.hera.builder import WorkflowHeraBuilder
from digitalhub_runtime_hera.entities.workflow.hera.crud import new_workflow_hera

try:
    from digitalhub_runtime_hera.runtimes.builder import RuntimeHeraBuilder
except ImportError as e:
    from digitalhub.utils.logger.logger import get_logger

    get_logger(__name__).debug(f"Error importing runtime builder: {e}")
    RuntimeHeraBuilder = None

workflow_hera_plugin = EntityPlugin(
    builder=WorkflowHeraBuilder,
    shortcuts=(CrudPlugin(new_workflow_hera),),
    runtime_builder=RuntimeHeraBuilder,
)

entity_plugins = (
    workflow_hera_plugin,
    EntityPlugin(builder=TaskHeraPipelineBuilder, runtime_builder=RuntimeHeraBuilder),
    EntityPlugin(builder=TaskHeraBuildBuilder, runtime_builder=RuntimeHeraBuilder),
    EntityPlugin(builder=RunHeraRunBuildBuilder, runtime_builder=RuntimeHeraBuilder),
    EntityPlugin(builder=RunHeraRunPipelineBuilder, runtime_builder=RuntimeHeraBuilder),
)
