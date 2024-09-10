# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.eval_service_handlers_get_document_response import EvalServiceHandlersGetDocumentResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.documents_create_request import DocumentsCreateRequest
from ..types.eval_service_handlers_create_document_response import EvalServiceHandlersCreateDocumentResponse
from ..types.document_content import DocumentContent
from ..types.eval_service_handlers_update_document_response import EvalServiceHandlersUpdateDocumentResponse
from ..types.eval_service_handlers_delete_document_response import EvalServiceHandlersDeleteDocumentResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DocumentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, collection_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EvalServiceHandlersGetDocumentResponse:
        """
        Parameters
        ----------
        collection_id : str

        document_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalServiceHandlersGetDocumentResponse
            Successful Response

        Examples
        --------
        from scoutos import ScoutosApi

        client = ScoutosApi(
            api_key="YOUR_API_KEY",
        )
        client.documents.get(
            collection_id="collection_id",
            document_id="document_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/documents/{jsonable_encoder(document_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    EvalServiceHandlersGetDocumentResponse,
                    parse_obj_as(
                        type_=EvalServiceHandlersGetDocumentResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
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
        collection_id: str,
        *,
        request: DocumentsCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EvalServiceHandlersCreateDocumentResponse:
        """
        Parameters
        ----------
        collection_id : str

        request : DocumentsCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalServiceHandlersCreateDocumentResponse
            Successful Response

        Examples
        --------
        from scoutos import DocumentDataInput, ScoutosApi

        client = ScoutosApi(
            api_key="YOUR_API_KEY",
        )
        client.documents.create(
            collection_id="collection_id",
            request=DocumentDataInput(),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/documents",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    EvalServiceHandlersCreateDocumentResponse,
                    parse_obj_as(
                        type_=EvalServiceHandlersCreateDocumentResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
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
        collection_id: str,
        document_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        columns: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        content: typing.Optional[typing.Sequence[DocumentContent]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EvalServiceHandlersUpdateDocumentResponse:
        """
        Parameters
        ----------
        collection_id : str

        document_id : str

        id : typing.Optional[str]

        columns : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        display_name : typing.Optional[str]

        content : typing.Optional[typing.Sequence[DocumentContent]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalServiceHandlersUpdateDocumentResponse
            Successful Response

        Examples
        --------
        from scoutos import ScoutosApi

        client = ScoutosApi(
            api_key="YOUR_API_KEY",
        )
        client.documents.update(
            collection_id="collection_id",
            document_id="document_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/documents/{jsonable_encoder(document_id)}",
            method="PUT",
            json={
                "id": id,
                "columns": columns,
                "display_name": display_name,
                "content": content,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    EvalServiceHandlersUpdateDocumentResponse,
                    parse_obj_as(
                        type_=EvalServiceHandlersUpdateDocumentResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
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
        self, collection_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EvalServiceHandlersDeleteDocumentResponse:
        """
        Delete a document given a document_id.

        Parameters
        ----------
        collection_id : str

        document_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalServiceHandlersDeleteDocumentResponse
            Successful Response

        Examples
        --------
        from scoutos import ScoutosApi

        client = ScoutosApi(
            api_key="YOUR_API_KEY",
        )
        client.documents.delete(
            collection_id="collection_id",
            document_id="document_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/documents/{jsonable_encoder(document_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    EvalServiceHandlersDeleteDocumentResponse,
                    parse_obj_as(
                        type_=EvalServiceHandlersDeleteDocumentResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncDocumentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, collection_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EvalServiceHandlersGetDocumentResponse:
        """
        Parameters
        ----------
        collection_id : str

        document_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalServiceHandlersGetDocumentResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScoutosApi

        client = AsyncScoutosApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.documents.get(
                collection_id="collection_id",
                document_id="document_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/documents/{jsonable_encoder(document_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    EvalServiceHandlersGetDocumentResponse,
                    parse_obj_as(
                        type_=EvalServiceHandlersGetDocumentResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
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
        collection_id: str,
        *,
        request: DocumentsCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EvalServiceHandlersCreateDocumentResponse:
        """
        Parameters
        ----------
        collection_id : str

        request : DocumentsCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalServiceHandlersCreateDocumentResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScoutosApi, DocumentDataInput

        client = AsyncScoutosApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.documents.create(
                collection_id="collection_id",
                request=DocumentDataInput(),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/documents",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    EvalServiceHandlersCreateDocumentResponse,
                    parse_obj_as(
                        type_=EvalServiceHandlersCreateDocumentResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
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
        collection_id: str,
        document_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        columns: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        content: typing.Optional[typing.Sequence[DocumentContent]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EvalServiceHandlersUpdateDocumentResponse:
        """
        Parameters
        ----------
        collection_id : str

        document_id : str

        id : typing.Optional[str]

        columns : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        display_name : typing.Optional[str]

        content : typing.Optional[typing.Sequence[DocumentContent]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalServiceHandlersUpdateDocumentResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScoutosApi

        client = AsyncScoutosApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.documents.update(
                collection_id="collection_id",
                document_id="document_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/documents/{jsonable_encoder(document_id)}",
            method="PUT",
            json={
                "id": id,
                "columns": columns,
                "display_name": display_name,
                "content": content,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    EvalServiceHandlersUpdateDocumentResponse,
                    parse_obj_as(
                        type_=EvalServiceHandlersUpdateDocumentResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
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
        self, collection_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EvalServiceHandlersDeleteDocumentResponse:
        """
        Delete a document given a document_id.

        Parameters
        ----------
        collection_id : str

        document_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalServiceHandlersDeleteDocumentResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScoutosApi

        client = AsyncScoutosApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.documents.delete(
                collection_id="collection_id",
                document_id="document_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/documents/{jsonable_encoder(document_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    EvalServiceHandlersDeleteDocumentResponse,
                    parse_obj_as(
                        type_=EvalServiceHandlersDeleteDocumentResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)