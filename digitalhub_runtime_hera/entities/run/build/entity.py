# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_hera.entities.run._base.entity import RunHeraRun

if typing.TYPE_CHECKING:
    from digitalhub_runtime_hera.entities.run.build.spec import RunSpecHeraRunBuild
    from digitalhub_runtime_hera.entities.run.build.status import RunStatusHeraRunBuild


class RunHeraRunBuild(RunHeraRun):
    """
    RunHeraRunBuild class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecHeraRunBuild
        self.status: RunStatusHeraRunBuild
