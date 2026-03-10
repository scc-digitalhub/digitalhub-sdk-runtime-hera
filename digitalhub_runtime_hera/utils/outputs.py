# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._commons.enums import State
from digitalhub.utils.logger.logger import get_logger

logger = get_logger(__file__)


def build_status(build: dict) -> dict:
    """
    Build status.

    Parameters
    ----------
    build : dict
        The built workflow.

    Returns
    -------
    dict
        The status.
    """
    try:
        return {"state": State.COMPLETED.value, "results": build}
    except Exception as e:
        msg = f"Something got wrong during run status building. Exception: {e.__class__}. Error: {e.args}"
        logger.exception(msg)
        raise RuntimeError(msg) from e
