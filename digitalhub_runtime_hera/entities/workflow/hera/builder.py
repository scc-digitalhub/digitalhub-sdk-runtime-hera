# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.status import Status
from digitalhub.entities._mixin.source.builder import SourceBuilderMixin
from digitalhub.entities.workflow._base.builder import WorkflowBuilder

from digitalhub_runtime_hera.entities._base.runtime_entity.builder import RuntimeEntityBuilderHera
from digitalhub_runtime_hera.entities._commons.enums import EntityKinds
from digitalhub_runtime_hera.entities.workflow.hera.entity import WorkflowHera
from digitalhub_runtime_hera.entities.workflow.hera.spec import WorkflowSpecHera


class WorkflowHeraBuilder(SourceBuilderMixin, WorkflowBuilder, RuntimeEntityBuilderHera):
    """
    WorkflowHera builder.
    """

    ENTITY_CLASS = WorkflowHera
    ENTITY_SPEC_CLASS = WorkflowSpecHera
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.WORKFLOW_HERA.value
