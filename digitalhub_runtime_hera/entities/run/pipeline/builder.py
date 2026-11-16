# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.builder import RunBuilder

from digitalhub_runtime_hera.entities._base.runtime_entity.builder import RuntimeEntityBuilderHera
from digitalhub_runtime_hera.entities._commons.enums import EntityKinds
from digitalhub_runtime_hera.entities.run.pipeline.entity import RunHeraRunPipeline
from digitalhub_runtime_hera.entities.run.pipeline.spec import RunSpecHeraRunPipeline
from digitalhub_runtime_hera.entities.run.pipeline.status import RunStatusHeraRunPipeline


class RunHeraRunPipelineBuilder(RunBuilder, RuntimeEntityBuilderHera):
    """
    RunHeraRunPipelineBuilder runer.
    """

    ENTITY_CLASS = RunHeraRunPipeline
    ENTITY_SPEC_CLASS = RunSpecHeraRunPipeline
    ENTITY_STATUS_CLASS = RunStatusHeraRunPipeline
    ENTITY_KIND = EntityKinds.RUN_HERA_PIPELINE.value
