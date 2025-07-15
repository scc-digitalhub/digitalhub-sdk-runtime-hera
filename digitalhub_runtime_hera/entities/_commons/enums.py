# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from enum import Enum


class EntityKinds(Enum):
    """
    Entity kinds.
    """

    WORKFLOW_HERA = "kfp"
    TASK_HERA_PIPELINE = "kfp+pipeline"
    TASK_HERA_BUILD = "kfp+build"
    RUN_HERA = "kfp+run"


class TaskActions(Enum):
    """
    Task actions.
    """

    PIPELINE = "pipeline"
    BUILD = "build"
