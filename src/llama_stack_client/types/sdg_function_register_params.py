# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared_params.return_type import ReturnType

__all__ = ["SDGFunctionRegisterParams"]


class SDGFunctionRegisterParams(TypedDict, total=False):
    description: Required[str]

    sdg_fn_id: Required[str]

    provider_id: str
