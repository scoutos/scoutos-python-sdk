# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..types.req_body_inputs_value import ReqBodyInputsValue
from ..types.environment import Environment
from ..core.request_options import RequestOptions
from ..types.workflow_run_event import WorkflowRunEvent
from ..core.jsonable_encoder import jsonable_encoder
import httpx_sse
from ..core.unchecked_base_model import construct_type
import json
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.workflow_run_response import WorkflowRunResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class WorkflowsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def run_stream(
        self,
        workflow_id: str,
        *,
        inputs: typing.Dict[str, ReqBodyInputsValue],
        revision_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        environment: typing.Optional[Environment] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[WorkflowRunEvent]:
        """
        Parameters
        ----------
        workflow_id : str

        inputs : typing.Dict[str, ReqBodyInputsValue]

        revision_id : typing.Optional[str]

        session_id : typing.Optional[str]

        environment : typing.Optional[Environment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[WorkflowRunEvent]


        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        response = client.workflows.run_stream(
            workflow_id="string",
            revision_id="string",
            session_id="string",
            environment="production",
            inputs={"string": True},
        )
        for chunk in response:
            yield chunk
        """
        with self._client_wrapper.httpx_client.stream(
            f"v2/workflows/{jsonable_encoder(workflow_id)}/execute",
            method="POST",
            params={
                "revision_id": revision_id,
                "session_id": session_id,
                "environment": environment,
            },
            json={
                "inputs": inputs,
                "streaming": True,
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    _event_source = httpx_sse.EventSource(_response)
                    for _sse in _event_source.iter_sse():
                        try:
                            yield typing.cast(
                                WorkflowRunEvent,
                                construct_type(
                                    type_=WorkflowRunEvent,  # type: ignore
                                    object_=json.loads(_sse.data),
                                ),
                            )
                        except:
                            pass
                    return
                _response.read()
                if _response.status_code == 422:
                    raise UnprocessableEntityError(
                        typing.cast(
                            HttpValidationError,
                            construct_type(
                                type_=HttpValidationError,  # type: ignore
                                object_=_response.json(),
                            ),
                        )
                    )
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    def run(
        self,
        workflow_id: str,
        *,
        inputs: typing.Dict[str, ReqBodyInputsValue],
        revision_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        environment: typing.Optional[Environment] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowRunResponse:
        """
        Parameters
        ----------
        workflow_id : str

        inputs : typing.Dict[str, ReqBodyInputsValue]

        revision_id : typing.Optional[str]

        session_id : typing.Optional[str]

        environment : typing.Optional[Environment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowRunResponse


        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.workflows.run(
            workflow_id="workflow_id",
            inputs={"key": True},
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/workflows/{jsonable_encoder(workflow_id)}/execute",
            method="POST",
            params={
                "revision_id": revision_id,
                "session_id": session_id,
                "environment": environment,
            },
            json={
                "inputs": inputs,
                "streaming": False,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WorkflowRunResponse,
                    construct_type(
                        type_=WorkflowRunResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncWorkflowsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def run_stream(
        self,
        workflow_id: str,
        *,
        inputs: typing.Dict[str, ReqBodyInputsValue],
        revision_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        environment: typing.Optional[Environment] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[WorkflowRunEvent]:
        """
        Parameters
        ----------
        workflow_id : str

        inputs : typing.Dict[str, ReqBodyInputsValue]

        revision_id : typing.Optional[str]

        session_id : typing.Optional[str]

        environment : typing.Optional[Environment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[WorkflowRunEvent]


        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            response = await client.workflows.run_stream(
                workflow_id="string",
                revision_id="string",
                session_id="string",
                environment="production",
                inputs={"string": True},
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v2/workflows/{jsonable_encoder(workflow_id)}/execute",
            method="POST",
            params={
                "revision_id": revision_id,
                "session_id": session_id,
                "environment": environment,
            },
            json={
                "inputs": inputs,
                "streaming": True,
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    _event_source = httpx_sse.EventSource(_response)
                    async for _sse in _event_source.aiter_sse():
                        try:
                            yield typing.cast(
                                WorkflowRunEvent,
                                construct_type(
                                    type_=WorkflowRunEvent,  # type: ignore
                                    object_=json.loads(_sse.data),
                                ),
                            )
                        except:
                            pass
                    return
                await _response.aread()
                if _response.status_code == 422:
                    raise UnprocessableEntityError(
                        typing.cast(
                            HttpValidationError,
                            construct_type(
                                type_=HttpValidationError,  # type: ignore
                                object_=_response.json(),
                            ),
                        )
                    )
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    async def run(
        self,
        workflow_id: str,
        *,
        inputs: typing.Dict[str, ReqBodyInputsValue],
        revision_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        environment: typing.Optional[Environment] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowRunResponse:
        """
        Parameters
        ----------
        workflow_id : str

        inputs : typing.Dict[str, ReqBodyInputsValue]

        revision_id : typing.Optional[str]

        session_id : typing.Optional[str]

        environment : typing.Optional[Environment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowRunResponse


        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workflows.run(
                workflow_id="workflow_id",
                inputs={"key": True},
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/workflows/{jsonable_encoder(workflow_id)}/execute",
            method="POST",
            params={
                "revision_id": revision_id,
                "session_id": session_id,
                "environment": environment,
            },
            json={
                "inputs": inputs,
                "streaming": False,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WorkflowRunResponse,
                    construct_type(
                        type_=WorkflowRunResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
