# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing
from typing import Any

from digitalhub.entities.run._base.entity import Run

if typing.TYPE_CHECKING:

    from digitalhub_runtime_hera.entities.run._base.spec import RunSpecHeraRun
    from digitalhub_runtime_hera.entities.run._base.status import RunStatusHeraRun


class RunHeraRun(Run):
    """
    RunHeraRun class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecHeraRun
        self.status: RunStatusHeraRun

    def _setup_execution(self) -> None:
        """
        Setup run execution.
        """

    def result(self, result_name: str) -> Any:
        """
        Get result by name.

        Parameters
        ----------
        result_name : str
            Name of the result.

        Returns
        -------
        Any
            The result.
        """
        return self.results().get(result_name)

    def results(self) -> dict:
        """
        Get results.

        Returns
        -------
        dict
            The results.
        """
        if self.status.results is None:
            return {}
        return self.status.results
