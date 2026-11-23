# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.spec import RunSpecWorkflow


class RunSpecHeraRun(RunSpecWorkflow):
    """RunSpecHeraRun specifications."""

    source: dict | None = None
    build: dict | None = None
    parameters: dict | None = None
