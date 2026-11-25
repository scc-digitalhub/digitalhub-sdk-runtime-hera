# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from enum import Enum
from typing import ClassVar

from digitalhub.plugins import HandlerSourceCode
from pydantic import BaseModel, ConfigDict, Field


class SourceLang(Enum):
    """
    Source code language.
    """

    PYTHON = "python"


class HeraSourceCode(HandlerSourceCode):
    """Source code model for Hera workflows."""

    DEFAULT_LANG: ClassVar[str | None] = "python"
    REQUIRE_HANDLER: ClassVar[bool] = True
    lang: SourceLang = Field(default=SourceLang.PYTHON.value)


SourceValidator = HeraSourceCode


class BuildLang(Enum):
    """
    Build language.
    """

    YAML = "yaml"


class BuildValidator(BaseModel):
    """
    Build params.
    """

    model_config = ConfigDict(use_enum_values=True)

    base64: str = None
    "Argo workflow (base64 encoded)."

    lang: BuildLang = Field(default=BuildLang.YAML.value)
    "Argo workflow language (hint)."
