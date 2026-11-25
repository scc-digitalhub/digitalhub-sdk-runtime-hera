# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

import pytest
from digitalhub.factory.registry import registry
from pydantic import ValidationError

from digitalhub_runtime_hera.entities._commons.enums import EntityKinds
from digitalhub_runtime_hera.entities.workflow.hera.models import BuildValidator, SourceValidator


def test_workflow_spec_validates_nested_runtime_models() -> None:
    spec = registry.get_entity_builder(EntityKinds.WORKFLOW_HERA.value).build_spec(
        source={"source": "main.py", "handler": "main"},
        build={"base64": "encoded"},
    )

    assert isinstance(spec.source, SourceValidator)
    assert isinstance(spec.build, BuildValidator)


def test_workflow_spec_requires_source_and_rejects_invalid_nested_values() -> None:
    builder = registry.get_entity_builder(EntityKinds.WORKFLOW_HERA.value)

    with pytest.raises(ValidationError):
        builder.build_spec()

    with pytest.raises(ValidationError):
        builder.build_spec(source={"source": "main.py", "handler": "main", "lang": "invalid"})


def test_hera_builder_routes_top_level_source_arguments() -> None:
    builder = registry.get_entity_builder(EntityKinds.WORKFLOW_HERA.value)

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
    spec = registry.get_entity_builder(EntityKinds.RUN_HERA_BUILD.value).build_spec(workflow="workflow", task="task")

    assert spec.workflow == "workflow"
