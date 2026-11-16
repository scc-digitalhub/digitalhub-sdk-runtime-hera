# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.workflow._base.spec import WorkflowSpec

from digitalhub_runtime_hera.entities.workflow.hera.models import BuildValidator, HeraSourceCode


class WorkflowSpecHera(WorkflowSpec):
    """
    WorkflowSpecHera specifications.
    """

    source: HeraSourceCode
    build: BuildValidator | None = None
    workflow: str | None = None
    image: str | None = None
    tag: str | None = None
