# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import RunBuilder

from digitalhub_runtime_hera.entities._base.runtime_entity.builder import RuntimeEntityBuilderHera
from digitalhub_runtime_hera.entities._commons.enums import EntityKinds
from digitalhub_runtime_hera.entities.run._base.spec import RunSpecHeraRun
from digitalhub_runtime_hera.entities.run._base.status import RunStatusHeraRun
from digitalhub_runtime_hera.entities.run.build.entity import RunHeraRunBuild


class RunHeraRunBuildBuilder(RunBuilder, RuntimeEntityBuilderHera):
    """
    RunHeraRunBuildBuilder runer.
    """

    ENTITY_CLASS = RunHeraRunBuild
    ENTITY_SPEC_CLASS = RunSpecHeraRun
    ENTITY_STATUS_CLASS = RunStatusHeraRun
    ENTITY_KIND = EntityKinds.RUN_HERA_BUILD.value
