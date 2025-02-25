# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.src_handlers_list_copilots_response import SrcHandlersListCopilotsResponse
from ..core.unchecked_base_model import construct_type
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.copilot_config_mode import CopilotConfigMode
from ..types.copilot_config_code_theme import CopilotConfigCodeTheme
from ..types.copilot_config_fab_value import CopilotConfigFabValue
from ..types.src_handlers_create_copilot_response import SrcHandlersCreateCopilotResponse
from ..types.src_handlers_get_copilot_response import SrcHandlersGetCopilotResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..types.src_handlers_update_copilot_response import SrcHandlersUpdateCopilotResponse
from ..types.src_handlers_delete_copilot_response import SrcHandlersDeleteCopilotResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CopilotsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        sort: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        start_at: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SrcHandlersListCopilotsResponse:
        """
        List all copilots in the organization

        Parameters
        ----------
        sort : typing.Optional[str]
            Field to sort by

        direction : typing.Optional[str]
            Sort in ascending or descending order

        start_at : typing.Optional[str]
            created_at to start at

        limit : typing.Optional[int]
            Limit of records to return

        query : typing.Optional[str]
            Search query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SrcHandlersListCopilotsResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.copilots.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/copilots",
            method="GET",
            params={
                "sort": sort,
                "direction": direction,
                "start_at": start_at,
                "limit": limit,
                "query": query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SrcHandlersListCopilotsResponse,
                    construct_type(
                        type_=SrcHandlersListCopilotsResponse,  # type: ignore
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

    def create(
        self,
        *,
        workflow_id: typing.Optional[str] = OMIT,
        img_url: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        mode: typing.Optional[CopilotConfigMode] = OMIT,
        code_theme: typing.Optional[CopilotConfigCodeTheme] = OMIT,
        colors: typing.Optional[typing.Dict[str, str]] = OMIT,
        fab: typing.Optional[typing.Dict[str, typing.Optional[CopilotConfigFabValue]]] = OMIT,
        loading_text: typing.Optional[str] = OMIT,
        message_placeholder: typing.Optional[str] = OMIT,
        initial_activity: typing.Optional[typing.Sequence[typing.Optional[typing.Any]]] = OMIT,
        allowed_origins: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SrcHandlersCreateCopilotResponse:
        """
        Parameters
        ----------
        workflow_id : typing.Optional[str]

        img_url : typing.Optional[str]

        display_name : typing.Optional[str]

        mode : typing.Optional[CopilotConfigMode]

        code_theme : typing.Optional[CopilotConfigCodeTheme]

        colors : typing.Optional[typing.Dict[str, str]]

        fab : typing.Optional[typing.Dict[str, typing.Optional[CopilotConfigFabValue]]]

        loading_text : typing.Optional[str]

        message_placeholder : typing.Optional[str]

        initial_activity : typing.Optional[typing.Sequence[typing.Optional[typing.Any]]]

        allowed_origins : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SrcHandlersCreateCopilotResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.copilots.create()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/copilots",
            method="POST",
            json={
                "workflow_id": workflow_id,
                "img_url": img_url,
                "display_name": display_name,
                "mode": mode,
                "code_theme": code_theme,
                "colors": colors,
                "fab": fab,
                "loading_text": loading_text,
                "message_placeholder": message_placeholder,
                "initial_activity": initial_activity,
                "allowed_origins": allowed_origins,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SrcHandlersCreateCopilotResponse,
                    construct_type(
                        type_=SrcHandlersCreateCopilotResponse,  # type: ignore
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

    def get(
        self, copilot_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SrcHandlersGetCopilotResponse:
        """
        Fetch app configuration by ID.

        Parameters
        ----------
        copilot_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SrcHandlersGetCopilotResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.copilots.get(
            copilot_id="copilot_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/copilots/{jsonable_encoder(copilot_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SrcHandlersGetCopilotResponse,
                    construct_type(
                        type_=SrcHandlersGetCopilotResponse,  # type: ignore
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

    def update(
        self,
        copilot_id: str,
        *,
        workflow_id: typing.Optional[str] = OMIT,
        img_url: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        mode: typing.Optional[CopilotConfigMode] = OMIT,
        code_theme: typing.Optional[CopilotConfigCodeTheme] = OMIT,
        colors: typing.Optional[typing.Dict[str, str]] = OMIT,
        fab: typing.Optional[typing.Dict[str, typing.Optional[CopilotConfigFabValue]]] = OMIT,
        loading_text: typing.Optional[str] = OMIT,
        message_placeholder: typing.Optional[str] = OMIT,
        initial_activity: typing.Optional[typing.Sequence[typing.Optional[typing.Any]]] = OMIT,
        allowed_origins: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SrcHandlersUpdateCopilotResponse:
        """
        Parameters
        ----------
        copilot_id : str

        workflow_id : typing.Optional[str]

        img_url : typing.Optional[str]

        display_name : typing.Optional[str]

        mode : typing.Optional[CopilotConfigMode]

        code_theme : typing.Optional[CopilotConfigCodeTheme]

        colors : typing.Optional[typing.Dict[str, str]]

        fab : typing.Optional[typing.Dict[str, typing.Optional[CopilotConfigFabValue]]]

        loading_text : typing.Optional[str]

        message_placeholder : typing.Optional[str]

        initial_activity : typing.Optional[typing.Sequence[typing.Optional[typing.Any]]]

        allowed_origins : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SrcHandlersUpdateCopilotResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.copilots.update(
            copilot_id="copilot_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/copilots/{jsonable_encoder(copilot_id)}",
            method="PUT",
            json={
                "workflow_id": workflow_id,
                "img_url": img_url,
                "display_name": display_name,
                "mode": mode,
                "code_theme": code_theme,
                "colors": colors,
                "fab": fab,
                "loading_text": loading_text,
                "message_placeholder": message_placeholder,
                "initial_activity": initial_activity,
                "allowed_origins": allowed_origins,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SrcHandlersUpdateCopilotResponse,
                    construct_type(
                        type_=SrcHandlersUpdateCopilotResponse,  # type: ignore
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

    def delete(
        self, copilot_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SrcHandlersDeleteCopilotResponse:
        """
        Parameters
        ----------
        copilot_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SrcHandlersDeleteCopilotResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.copilots.delete(
            copilot_id="copilot_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/copilots/{jsonable_encoder(copilot_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SrcHandlersDeleteCopilotResponse,
                    construct_type(
                        type_=SrcHandlersDeleteCopilotResponse,  # type: ignore
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


class AsyncCopilotsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        sort: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        start_at: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SrcHandlersListCopilotsResponse:
        """
        List all copilots in the organization

        Parameters
        ----------
        sort : typing.Optional[str]
            Field to sort by

        direction : typing.Optional[str]
            Sort in ascending or descending order

        start_at : typing.Optional[str]
            created_at to start at

        limit : typing.Optional[int]
            Limit of records to return

        query : typing.Optional[str]
            Search query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SrcHandlersListCopilotsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.copilots.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/copilots",
            method="GET",
            params={
                "sort": sort,
                "direction": direction,
                "start_at": start_at,
                "limit": limit,
                "query": query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SrcHandlersListCopilotsResponse,
                    construct_type(
                        type_=SrcHandlersListCopilotsResponse,  # type: ignore
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

    async def create(
        self,
        *,
        workflow_id: typing.Optional[str] = OMIT,
        img_url: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        mode: typing.Optional[CopilotConfigMode] = OMIT,
        code_theme: typing.Optional[CopilotConfigCodeTheme] = OMIT,
        colors: typing.Optional[typing.Dict[str, str]] = OMIT,
        fab: typing.Optional[typing.Dict[str, typing.Optional[CopilotConfigFabValue]]] = OMIT,
        loading_text: typing.Optional[str] = OMIT,
        message_placeholder: typing.Optional[str] = OMIT,
        initial_activity: typing.Optional[typing.Sequence[typing.Optional[typing.Any]]] = OMIT,
        allowed_origins: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SrcHandlersCreateCopilotResponse:
        """
        Parameters
        ----------
        workflow_id : typing.Optional[str]

        img_url : typing.Optional[str]

        display_name : typing.Optional[str]

        mode : typing.Optional[CopilotConfigMode]

        code_theme : typing.Optional[CopilotConfigCodeTheme]

        colors : typing.Optional[typing.Dict[str, str]]

        fab : typing.Optional[typing.Dict[str, typing.Optional[CopilotConfigFabValue]]]

        loading_text : typing.Optional[str]

        message_placeholder : typing.Optional[str]

        initial_activity : typing.Optional[typing.Sequence[typing.Optional[typing.Any]]]

        allowed_origins : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SrcHandlersCreateCopilotResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.copilots.create()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/copilots",
            method="POST",
            json={
                "workflow_id": workflow_id,
                "img_url": img_url,
                "display_name": display_name,
                "mode": mode,
                "code_theme": code_theme,
                "colors": colors,
                "fab": fab,
                "loading_text": loading_text,
                "message_placeholder": message_placeholder,
                "initial_activity": initial_activity,
                "allowed_origins": allowed_origins,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SrcHandlersCreateCopilotResponse,
                    construct_type(
                        type_=SrcHandlersCreateCopilotResponse,  # type: ignore
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

    async def get(
        self, copilot_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SrcHandlersGetCopilotResponse:
        """
        Fetch app configuration by ID.

        Parameters
        ----------
        copilot_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SrcHandlersGetCopilotResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.copilots.get(
                copilot_id="copilot_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/copilots/{jsonable_encoder(copilot_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SrcHandlersGetCopilotResponse,
                    construct_type(
                        type_=SrcHandlersGetCopilotResponse,  # type: ignore
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

    async def update(
        self,
        copilot_id: str,
        *,
        workflow_id: typing.Optional[str] = OMIT,
        img_url: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        mode: typing.Optional[CopilotConfigMode] = OMIT,
        code_theme: typing.Optional[CopilotConfigCodeTheme] = OMIT,
        colors: typing.Optional[typing.Dict[str, str]] = OMIT,
        fab: typing.Optional[typing.Dict[str, typing.Optional[CopilotConfigFabValue]]] = OMIT,
        loading_text: typing.Optional[str] = OMIT,
        message_placeholder: typing.Optional[str] = OMIT,
        initial_activity: typing.Optional[typing.Sequence[typing.Optional[typing.Any]]] = OMIT,
        allowed_origins: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SrcHandlersUpdateCopilotResponse:
        """
        Parameters
        ----------
        copilot_id : str

        workflow_id : typing.Optional[str]

        img_url : typing.Optional[str]

        display_name : typing.Optional[str]

        mode : typing.Optional[CopilotConfigMode]

        code_theme : typing.Optional[CopilotConfigCodeTheme]

        colors : typing.Optional[typing.Dict[str, str]]

        fab : typing.Optional[typing.Dict[str, typing.Optional[CopilotConfigFabValue]]]

        loading_text : typing.Optional[str]

        message_placeholder : typing.Optional[str]

        initial_activity : typing.Optional[typing.Sequence[typing.Optional[typing.Any]]]

        allowed_origins : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SrcHandlersUpdateCopilotResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.copilots.update(
                copilot_id="copilot_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/copilots/{jsonable_encoder(copilot_id)}",
            method="PUT",
            json={
                "workflow_id": workflow_id,
                "img_url": img_url,
                "display_name": display_name,
                "mode": mode,
                "code_theme": code_theme,
                "colors": colors,
                "fab": fab,
                "loading_text": loading_text,
                "message_placeholder": message_placeholder,
                "initial_activity": initial_activity,
                "allowed_origins": allowed_origins,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SrcHandlersUpdateCopilotResponse,
                    construct_type(
                        type_=SrcHandlersUpdateCopilotResponse,  # type: ignore
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

    async def delete(
        self, copilot_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SrcHandlersDeleteCopilotResponse:
        """
        Parameters
        ----------
        copilot_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SrcHandlersDeleteCopilotResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.copilots.delete(
                copilot_id="copilot_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/copilots/{jsonable_encoder(copilot_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SrcHandlersDeleteCopilotResponse,
                    construct_type(
                        type_=SrcHandlersDeleteCopilotResponse,  # type: ignore
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
