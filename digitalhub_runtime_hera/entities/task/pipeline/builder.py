# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.status import Status
from digitalhub.entities.task._base.builder import TaskBuilder

from digitalhub_runtime_hera.entities._base.runtime_entity.builder import RuntimeEntityBuilderHera
from digitalhub_runtime_hera.entities._commons.enums import EntityKinds
from digitalhub_runtime_hera.entities.task.pipeline.entity import TaskHeraPipeline
from digitalhub_runtime_hera.entities.task.pipeline.spec import TaskSpecHeraPipeline


class TaskHeraPipelineBuilder(TaskBuilder, RuntimeEntityBuilderHera):
    """
    TaskHeraPipelineBuilder pipelineer.
    """

    ENTITY_CLASS = TaskHeraPipeline
    ENTITY_SPEC_CLASS = TaskSpecHeraPipeline
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.TASK_HERA_PIPELINE.value
