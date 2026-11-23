# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

import pytest
from pydantic import ValidationError

from digitalhub_runtime_hera.entities.run.build.builder import RunHeraRunBuildBuilder
from digitalhub_runtime_hera.entities.workflow.hera.builder import WorkflowHeraBuilder
from digitalhub_runtime_hera.entities.workflow.hera.models import BuildValidator, SourceValidator


def test_workflow_spec_validates_nested_runtime_models() -> None:
    spec = WorkflowHeraBuilder().build_spec(
        source={"source": "main.py", "handler": "main"},
        build={"base64": "encoded"},
    )

    assert isinstance(spec.source, SourceValidator)
    assert isinstance(spec.build, BuildValidator)


def test_workflow_spec_requires_source_and_rejects_invalid_nested_values() -> None:
    builder = WorkflowHeraBuilder()

    with pytest.raises(ValidationError):
        builder.build_spec()

    with pytest.raises(ValidationError):
        builder.build_spec(source={"source": "main.py", "handler": "main", "lang": "invalid"})


def test_hera_builder_routes_top_level_source_arguments() -> None:
    builder = WorkflowHeraBuilder()

    workflow = builder.build(
        kind=builder.ENTITY_KIND,
        project="project",
        name="workflow",
        code="from hera import Workflow",
        handler="main",
    )

    assert workflow.spec.source.base64 == "ZnJvbSBoZXJhIGltcG9ydCBXb3JrZmxvdw=="
    assert workflow.spec.source.handler == "main"


def test_hera_run_builder_requires_workflow_reference() -> None:
    spec = RunHeraRunBuildBuilder().build_spec(workflow="workflow", task="task")

    assert spec.workflow == "workflow"
