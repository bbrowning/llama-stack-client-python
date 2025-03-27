# File written by hand oof....

from __future__ import annotations

from typing import Dict, Type, Union, Iterable, Optional, cast

import httpx

from ..types import sdg_function_register_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import DataWrapper
from .._base_client import make_request_options
from ..types.sdg_fn import SDGFn
from ..types.sdg_fn_params_param import SDGFnParamsParam
from ..types.sdg_function_list_response import SDGFunctionListResponse

__all__ = ["SDGFunctionsResource", "AsyncSDGFunctionsResource"]


class SDGFunctionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SDGFunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return SDGFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SDGFunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return SDGFunctionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        sdg_fn_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SDGFn:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sdg_fn_id:
            raise ValueError(f"Expected a non-empty value for `sdg_fn_id` but received {sdg_fn_id!r}")
        return self._get(
            f"/v1/sdg-functions/{sdg_fn_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SDGFn,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SDGFunctionListResponse:
        return self._get(
            "/v1/sdg-functions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[SDGFunctionListResponse]._unwrapper,
            ),
            cast_to=cast(Type[SDGFunctionListResponse], DataWrapper[SDGFunctionListResponse]),
        )

    def register(
        self,
        *,
        description: str,
        sdg_fn_id: str,
        params: SDGFnParamsParam | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/sdg-functions",
            body=maybe_transform(
                {
                    "description": description,
                    "sdg_fn_id": sdg_fn_id,
                    "params": params,
                    "provider_id": provider_id,
                },
                sdg_function_register_params.SDGFunctionRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def unregister(
        self,
        sdg_fn_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sdg_fn_id:
            raise ValueError(f"Expected a non-empty value for `sdg_fn_id` but received {sdg_fn_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/sdg-functions/{sdg_fn_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSDGFunctionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSDGFunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSDGFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSDGFunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncSDGFunctionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        sdg_fn_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SDGFn:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sdg_fn_id:
            raise ValueError(f"Expected a non-empty value for `sdg_fn_id` but received {sdg_fn_id!r}")
        return await self._get(
            f"/v1/sdg-functions/{sdg_fn_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SDGFn,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SDGFunctionListResponse:
        return await self._get(
            "/v1/sdg-functions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[SDGFunctionListResponse]._unwrapper,
            ),
            cast_to=cast(Type[SDGFunctionListResponse], DataWrapper[SDGFunctionListResponse]),
        )

    async def register(
        self,
        *,
        sdg_fn_id: str,
        metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/sdg-functions",
            body=await async_maybe_transform(
                {
                    "sdg_fn_id": sdg_fn_id,
                    "input_dataset_schema": input_dataset_schema,
                    "metadata": metadata,
                    "provider_id": provider_id,
                },
                sdg_function_register_params.SDGFunctionRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def unregister(
        self,
        sdg_fn_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sdg_fn_id:
            raise ValueError(f"Expected a non-empty value for `sdg_fn_id` but received {sdg_fn_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/sdg-functions/{sdg_fn_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SDGFunctionsResourceWithRawResponse:
    def __init__(self, sdg_functions: SDGFunctionsResource) -> None:
        self._sdg_functions = sdg_functions

        self.retrieve = to_raw_response_wrapper(
            sdg_functions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            sdg_functions.list,
        )
        self.register = to_raw_response_wrapper(
            sdg_functions.register,
        )
        self.unregister = to_raw_response_wrapper(
            sdg_functions.unregister,
        )


class AsyncSDGFunctionsResourceWithRawResponse:
    def __init__(self, sdg_functions: AsyncSDGFunctionsResource) -> None:
        self._sdg_functions = sdg_functions

        self.retrieve = async_to_raw_response_wrapper(
            sdg_functions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            sdg_functions.list,
        )
        self.register = async_to_raw_response_wrapper(
            sdg_functions.register,
        )
        self.unregister = async_to_raw_response_wrapper(
            sdg_functions.unregister,
        )


class SDGFunctionsResourceWithStreamingResponse:
    def __init__(self, sdg_functions: SDGFunctionsResource) -> None:
        self._sdg_functions = sdg_functions

        self.retrieve = to_streamed_response_wrapper(
            sdg_functions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            sdg_functions.list,
        )
        self.register = to_streamed_response_wrapper(
            sdg_functions.register,
        )
        self.unregister = to_streamed_response_wrapper(
            sdg_functions.unregister,
        )


class AsyncSDGFunctionsResourceWithStreamingResponse:
    def __init__(self, sdg_functions: AsyncSDGFunctionsResource) -> None:
        self._sdg_functions = sdg_functions

        self.retrieve = async_to_streamed_response_wrapper(
            sdg_functions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            sdg_functions.list,
        )
        self.register = async_to_streamed_response_wrapper(
            sdg_functions.register,
        )
        self.unregister = async_to_streamed_response_wrapper(
            sdg_functions.unregister,
        )
