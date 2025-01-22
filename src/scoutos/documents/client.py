# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.collection_service_handlers_get_documents_response import CollectionServiceHandlersGetDocumentsResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.unchecked_base_model import construct_type
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.documents_create_request import DocumentsCreateRequest
from ..types.collection_service_handlers_create_document_response import CollectionServiceHandlersCreateDocumentResponse
from ..types.collection_service_handlers_get_document_response import CollectionServiceHandlersGetDocumentResponse
from .types.documents_update_request_value import DocumentsUpdateRequestValue
from ..types.collection_service_handlers_update_document_response import CollectionServiceHandlersUpdateDocumentResponse
from ..types.collection_service_handlers_delete_documents_response import (
    CollectionServiceHandlersDeleteDocumentsResponse,
)
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DocumentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, collection_id: str, table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectionServiceHandlersGetDocumentsResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersGetDocumentsResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.documents.list(
            collection_id="collection_id",
            table_id="table_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}/documents",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersGetDocumentsResponse,
                    construct_type(
                        type_=CollectionServiceHandlersGetDocumentsResponse,  # type: ignore
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
        collection_id: str,
        table_id: str,
        *,
        request: DocumentsCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersCreateDocumentResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        request : DocumentsCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersCreateDocumentResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.documents.create(
            collection_id="collection_id",
            table_id="table_id",
            request={"key": True},
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}/documents",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersCreateDocumentResponse,
                    construct_type(
                        type_=CollectionServiceHandlersCreateDocumentResponse,  # type: ignore
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
        self,
        collection_id: str,
        table_id: str,
        document_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersGetDocumentResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        document_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersGetDocumentResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.documents.get(
            collection_id="collection_id",
            table_id="table_id",
            document_id="document_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}/documents/{jsonable_encoder(document_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersGetDocumentResponse,
                    construct_type(
                        type_=CollectionServiceHandlersGetDocumentResponse,  # type: ignore
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
        collection_id: str,
        document_id: str,
        table_id: str,
        *,
        request: typing.Dict[str, DocumentsUpdateRequestValue],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersUpdateDocumentResponse:
        """
        Parameters
        ----------
        collection_id : str

        document_id : str

        table_id : str

        request : typing.Dict[str, DocumentsUpdateRequestValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersUpdateDocumentResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.documents.update(
            collection_id="collection_id",
            document_id="document_id",
            table_id="table_id",
            request={"key": True},
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}/documents/{jsonable_encoder(document_id)}",
            method="PUT",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersUpdateDocumentResponse,
                    construct_type(
                        type_=CollectionServiceHandlersUpdateDocumentResponse,  # type: ignore
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
        self,
        collection_id: str,
        table_id: str,
        document_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersDeleteDocumentsResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        document_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersDeleteDocumentsResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.documents.delete(
            collection_id="collection_id",
            table_id="table_id",
            document_id="document_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}/documents/{jsonable_encoder(document_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersDeleteDocumentsResponse,
                    construct_type(
                        type_=CollectionServiceHandlersDeleteDocumentsResponse,  # type: ignore
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

    def delete_batch(
        self,
        collection_id: str,
        table_id: str,
        *,
        request: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersDeleteDocumentsResponse:
        """
        Delete documents given a list of document ids.

        Parameters
        ----------
        collection_id : str

        table_id : str

        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersDeleteDocumentsResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.documents.delete_batch(
            collection_id="collection_id",
            table_id="table_id",
            request=["string"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}/documents/delete",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersDeleteDocumentsResponse,
                    construct_type(
                        type_=CollectionServiceHandlersDeleteDocumentsResponse,  # type: ignore
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


class AsyncDocumentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, collection_id: str, table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectionServiceHandlersGetDocumentsResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersGetDocumentsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.documents.list(
                collection_id="collection_id",
                table_id="table_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}/documents",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersGetDocumentsResponse,
                    construct_type(
                        type_=CollectionServiceHandlersGetDocumentsResponse,  # type: ignore
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
        collection_id: str,
        table_id: str,
        *,
        request: DocumentsCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersCreateDocumentResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        request : DocumentsCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersCreateDocumentResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.documents.create(
                collection_id="collection_id",
                table_id="table_id",
                request={"key": True},
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}/documents",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersCreateDocumentResponse,
                    construct_type(
                        type_=CollectionServiceHandlersCreateDocumentResponse,  # type: ignore
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
        self,
        collection_id: str,
        table_id: str,
        document_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersGetDocumentResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        document_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersGetDocumentResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.documents.get(
                collection_id="collection_id",
                table_id="table_id",
                document_id="document_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}/documents/{jsonable_encoder(document_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersGetDocumentResponse,
                    construct_type(
                        type_=CollectionServiceHandlersGetDocumentResponse,  # type: ignore
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
        collection_id: str,
        document_id: str,
        table_id: str,
        *,
        request: typing.Dict[str, DocumentsUpdateRequestValue],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersUpdateDocumentResponse:
        """
        Parameters
        ----------
        collection_id : str

        document_id : str

        table_id : str

        request : typing.Dict[str, DocumentsUpdateRequestValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersUpdateDocumentResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.documents.update(
                collection_id="collection_id",
                document_id="document_id",
                table_id="table_id",
                request={"key": True},
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}/documents/{jsonable_encoder(document_id)}",
            method="PUT",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersUpdateDocumentResponse,
                    construct_type(
                        type_=CollectionServiceHandlersUpdateDocumentResponse,  # type: ignore
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
        self,
        collection_id: str,
        table_id: str,
        document_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersDeleteDocumentsResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        document_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersDeleteDocumentsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.documents.delete(
                collection_id="collection_id",
                table_id="table_id",
                document_id="document_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}/documents/{jsonable_encoder(document_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersDeleteDocumentsResponse,
                    construct_type(
                        type_=CollectionServiceHandlersDeleteDocumentsResponse,  # type: ignore
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

    async def delete_batch(
        self,
        collection_id: str,
        table_id: str,
        *,
        request: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersDeleteDocumentsResponse:
        """
        Delete documents given a list of document ids.

        Parameters
        ----------
        collection_id : str

        table_id : str

        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersDeleteDocumentsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.documents.delete_batch(
                collection_id="collection_id",
                table_id="table_id",
                request=["string"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/collections/{jsonable_encoder(collection_id)}/tables/{jsonable_encoder(table_id)}/documents/delete",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CollectionServiceHandlersDeleteDocumentsResponse,
                    construct_type(
                        type_=CollectionServiceHandlersDeleteDocumentsResponse,  # type: ignore
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
