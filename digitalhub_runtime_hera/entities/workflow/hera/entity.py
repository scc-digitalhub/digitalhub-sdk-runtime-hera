# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.plugins import ExecutableBuildMixin, SourceEntityMixin, Workflow
from digitalhub.utils.file_utils import eval_py_type

if typing.TYPE_CHECKING:
    from digitalhub.plugins import Status

    from digitalhub_runtime_hera.entities.workflow.hera.spec import WorkflowSpecHera


class WorkflowHera(SourceEntityMixin, ExecutableBuildMixin, Workflow):
    """
    WorkflowHera class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: WorkflowSpecHera
        self.status: Status

    def _is_inlineable_source(self, path: str) -> bool:
        return eval_py_type(path)
