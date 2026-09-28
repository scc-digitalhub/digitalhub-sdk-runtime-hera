# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.workflow.crud import new_workflow

from digitalhub_runtime_hera.entities.workflow.hera.builder import WorkflowHeraBuilder

if typing.TYPE_CHECKING:
    from digitalhub_runtime_hera.entities.workflow.hera.entity import WorkflowHera


def new_workflow_hera(
    project: str,
    name: str,
    source: dict | None = None,
    code: str | None = None,
    code_src: str | None = None,
    handler: str | None = None,
    lang: str | None = None,
    image: str | None = None,
    tag: str | None = None,
    uuid: str | None = None,
    version: str | None = None,
    description: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = False,
) -> WorkflowHera:
    """
    Create a Hera workflow entity.

    Parameters
    ----------
    project : str
        Project name.
    name : str
        Workflow name.
    source : dict, optional
        Workflow source configuration.
    code : str, optional
        Workflow source code as plain text.
    code_src : str, optional
        Local path or URI pointing to the workflow source code.
    handler : str, optional
        Workflow entrypoint.
    lang : str, optional
        Source code language hint.
    image : str, optional
        Workflow container image.
    tag : str, optional
        Container image tag.
    uuid : str, optional
        Workflow identifier.
    version : str, optional
        Workflow version.
    description : str, optional
        Human-readable workflow description.
    labels : list[str], optional
        Workflow labels.
    embedded : bool, default=False
        Whether to embed the workflow specification in the project specification.

    Returns
    -------
    WorkflowHera
        Created Hera workflow entity.
    """
    if code is not None and code_src is not None:
        raise ValueError("Only one of 'code' or 'code_src' can be provided.")

    return new_workflow(
        project=project,
        name=name,
        kind=WorkflowHeraBuilder.ENTITY_KIND,
        uuid=uuid,
        version=version,
        description=description,
        labels=labels,
        embedded=embedded,
        source=source,
        code=code,
        code_src=code_src,
        handler=handler,
        lang=lang,
        image=image,
        tag=tag,
    )
