# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["SDGFnParamsParam", "InstructLabSDGFnParams"]


class InstructLabSDGFnParams(TypedDict, total=False):
    type: Required[Literal["instructlab_sdg"]]

    pipeline_yaml: Optional[str] = None
    extra_configs: Optional[Dict[str, str]] = None
    chat_templates: Optional[Dict[str, str]] = None


SDGFnParamsParam: TypeAlias = Union[InstructLabSDGFnParams]
