# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing
from collections.abc import Callable
from pathlib import Path

from digitalhub.entities.workflow.crud import get_workflow
from digitalhub.plugins import EntityRef, fetch_source
from digitalhub.utils.generic_utils import decode_base64_string, import_function
from digitalhub.utils.logger.logger import get_logger

if typing.TYPE_CHECKING:
    from digitalhub.plugins import Workflow

logger = get_logger(__file__)
DEFAULT_PY_FILE = "main.py"


def _get_workflow_file_path(path: Path, handler: str) -> Path:
    """
    Get workflow file path from handler.

    Parameters
    ----------
    path : Path
        Root path where the workflow source is located.
    handler : str
        Workflow handler.

    Returns
    -------
    Path
        Path to the workflow Python file.
    """
    if ":" in handler:
        handler_parts = handler.split(":")[0].split(".")
        return Path(path, *handler_parts).with_suffix(".py")
    return path.with_suffix(".py")


def _extract_handler_function_name(handler: str) -> str:
    """
    Extract function name from handler string.

    Parameters
    ----------
    handler : str
        Handler string.

    Returns
    -------
    str
        Function name.
    """
    if ":" in handler:
        return handler.split(":")[-1]
    return handler


def get_dhcore_workflow(workflow_string: str) -> Workflow:
    """
    Get DHCore workflow.

    Parameters
    ----------
    workflow_string : str
        Workflow string in format 'workflow://project/name:uuid'.

    Returns
    -------
    Workflow
        DHCore workflow.
    """
    ref = EntityRef.parse(workflow_string)
    logger.info(f"Getting workflow {ref.name}:{ref.id}.")
    try:
        return get_workflow(ref.name, project=ref.project, entity_id=ref.id)
    except Exception as e:
        msg = f"Error getting workflow {ref.name}:{ref.id}. Exception: {e.__class__}. Error: {e.args}"
        logger.exception(msg)
        raise RuntimeError(msg) from e


def save_workflow_source(path: Path, source_spec: dict) -> Path:
    """
    Save workflow source from various sources.

    Parameters
    ----------
    path : Path
        Path where to save the workflow source.
    source_spec : dict
        Workflow source spec.

    Returns
    -------
    Path
        Path to the workflow Python file.
    """
    base64 = source_spec.get("base64")
    source = source_spec.get("source")
    handler: str = source_spec["handler"]

    # Base64-encoded source
    if base64 is not None:
        path.mkdir(parents=True, exist_ok=True)
        file_path = path / DEFAULT_PY_FILE
        file_path.write_text(decode_base64_string(base64))
        return file_path

    if source is None:
        raise RuntimeError("Workflow source not found in spec.")

    fetch_source(path, source)
    return _get_workflow_file_path(path, handler)


def get_hera_pipeline(name: str, source: Path, handler: str) -> Callable:
    """
    Get Hera pipeline by importing it from source.

    Parameters
    ----------
    name : str
        Name of the workflow.
    source : Path
        Path to the workflow source file.
    handler : str
        Handler of the workflow.

    Returns
    -------
    Callable
        Hera pipeline function.
    """
    try:
        function_name = _extract_handler_function_name(handler)
        return import_function(source, function_name)
    except Exception as e:
        msg = f"Error getting '{name}' Hera pipeline. Exception: {e.__class__}. Error: {e.args}"
        logger.exception(msg)
        raise RuntimeError(msg) from e
