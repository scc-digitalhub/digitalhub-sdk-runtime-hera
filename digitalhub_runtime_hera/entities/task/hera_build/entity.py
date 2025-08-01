# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.task._base.entity import Task

if typing.TYPE_CHECKING:
    from digitalhub.entities._base.entity.metadata import Metadata

    from digitalhub_runtime_hera.entities.task.hera_build.spec import TaskSpecHeraBuild
    from digitalhub_runtime_hera.entities.task.hera_build.status import TaskStatusHeraBuild


class TaskHeraBuild(Task):
    """
    TaskHeraBuild class.
    """

    def __init__(
        self,
        project: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: TaskSpecHeraBuild,
        status: TaskStatusHeraBuild,
        user: str | None = None,
    ) -> None:
        super().__init__(project, uuid, kind, metadata, spec, status, user)

        self.spec: TaskSpecHeraBuild
        self.status: TaskStatusHeraBuild
