# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

import pytest
from pydantic import ValidationError

from digitalhub_runtime_hera.entities.workflow.hera.builder import WorkflowHeraBuilder
from digitalhub_runtime_hera.entities.workflow.hera.models import BuildValidator, SourceValidator


def test_workflow_spec_validates_nested_runtime_models() -> None:
    spec = WorkflowHeraBuilder().build_spec(
        source={"source": "main.py"},
        build={"base64": "encoded"},
    )

    assert isinstance(spec.source, SourceValidator)
    assert isinstance(spec.build, BuildValidator)


def test_workflow_spec_requires_source_and_rejects_invalid_nested_values() -> None:
    builder = WorkflowHeraBuilder()

    with pytest.raises(ValidationError):
        builder.build_spec()

    with pytest.raises(ValidationError):
        builder.build_spec(source={"lang": "invalid"})
