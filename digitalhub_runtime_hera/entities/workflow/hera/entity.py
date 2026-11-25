# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.plugins import SourceEntityMixin, Workflow
from digitalhub.utils.file_utils import eval_py_type

from digitalhub_runtime_hera.entities._commons.enums import Actions

if typing.TYPE_CHECKING:
    from digitalhub.plugins import Status

    from digitalhub_runtime_hera.entities.workflow.hera.spec import WorkflowSpecHera


class WorkflowHera(SourceEntityMixin, Workflow):
    """
    WorkflowHera class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: WorkflowSpecHera
        self.status: Status

    def _is_inlineable_source(self, path: str) -> bool:
        return eval_py_type(path)

    def build(
        self,
        wait: bool = True,
        log_info: bool = True,
        extensions: list[dict] | None = None,
        **kwargs,
    ):
        """Build the workflow using the build action."""
        return super().run(
            Actions.BUILD.value,
            wait=wait,
            log_info=log_info,
            extensions=extensions,
            **kwargs,
        )

    def run(
        self,
        action: str,
        wait: bool = False,
        log_info: bool = True,
        extensions: list[dict] | None = None,
        auto_build: bool = False,
        **kwargs,
    ):
        """Run the workflow, building it when no workflow is built."""
        if auto_build and self.spec.workflow is None:
            self.build(wait=True, log_info=log_info)
            self.refresh()

        return super().run(
            action,
            wait=wait,
            log_info=log_info,
            extensions=extensions,
            **kwargs,
        )
