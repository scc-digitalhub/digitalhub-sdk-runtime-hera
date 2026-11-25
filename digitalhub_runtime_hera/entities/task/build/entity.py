# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.plugins import Task

if typing.TYPE_CHECKING:
    from digitalhub.plugins import Status

    from digitalhub_runtime_hera.entities.task.build.spec import TaskSpecHeraBuild


class TaskHeraBuild(Task):
    """
    TaskHeraBuild class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: TaskSpecHeraBuild
        self.status: Status
