# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.status import Status
from digitalhub.entities.task._base.builder import TaskBuilder

from digitalhub_runtime_hera.entities._base.runtime_entity.builder import RuntimeEntityBuilderHera
from digitalhub_runtime_hera.entities._commons.enums import EntityKinds
from digitalhub_runtime_hera.entities.task.build.entity import TaskHeraBuild
from digitalhub_runtime_hera.entities.task.build.spec import TaskSpecHeraBuild


class TaskHeraBuildBuilder(TaskBuilder, RuntimeEntityBuilderHera):
    """
    TaskHeraBuildBuilder builder.
    """

    ENTITY_CLASS = TaskHeraBuild
    ENTITY_SPEC_CLASS = TaskSpecHeraBuild
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.TASK_HERA_BUILD.value
