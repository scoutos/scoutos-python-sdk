# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.collection_service_handlers_create_table_response import CollectionServiceHandlersCreateTableResponse
from ..types.collection_service_handlers_delete_table_response import CollectionServiceHandlersDeleteTableResponse
from ..types.collection_service_handlers_get_table_response import CollectionServiceHandlersGetTableResponse
from ..types.collection_service_handlers_get_tables_response import CollectionServiceHandlersGetTablesResponse
from ..types.collection_service_handlers_table_sync_response import CollectionServiceHandlersTableSyncResponse
from ..types.collection_service_handlers_update_table_response import CollectionServiceHandlersUpdateTableResponse
from .raw_client import AsyncRawTablesClient, RawTablesClient
from .types.table_config_input_schema_item import TableConfigInputSchemaItem
from .types.table_data_schema_item import TableDataSchemaItem
from .types.tables_get_schema_response import TablesGetSchemaResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TablesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTablesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTablesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTablesClient
        """
        return self._raw_client

    def list(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectionServiceHandlersGetTablesResponse:
        """
        Parameters
        ----------
        collection_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersGetTablesResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.tables.list(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.list(collection_id, request_options=request_options)
        return _response.data

    def create(
        self,
        collection_id: str,
        *,
        table_display_name: typing.Optional[str] = OMIT,
        table_img_url: typing.Optional[str] = OMIT,
        table_description: typing.Optional[str] = OMIT,
        schema: typing.Optional[typing.Sequence[TableConfigInputSchemaItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersCreateTableResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_display_name : typing.Optional[str]

        table_img_url : typing.Optional[str]

        table_description : typing.Optional[str]

        schema : typing.Optional[typing.Sequence[TableConfigInputSchemaItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersCreateTableResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.tables.create(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.create(
            collection_id,
            table_display_name=table_display_name,
            table_img_url=table_img_url,
            table_description=table_description,
            schema=schema,
            request_options=request_options,
        )
        return _response.data

    def get(
        self, collection_id: str, table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectionServiceHandlersGetTableResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersGetTableResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.tables.get(
            collection_id="collection_id",
            table_id="table_id",
        )
        """
        _response = self._raw_client.get(collection_id, table_id, request_options=request_options)
        return _response.data

    def update(
        self,
        collection_id: str,
        table_id: str,
        *,
        table_display_name: typing.Optional[str] = OMIT,
        table_img_url: typing.Optional[str] = OMIT,
        table_description: typing.Optional[str] = OMIT,
        schema: typing.Optional[typing.Sequence[TableDataSchemaItem]] = OMIT,
        index_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersUpdateTableResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        table_display_name : typing.Optional[str]

        table_img_url : typing.Optional[str]

        table_description : typing.Optional[str]

        schema : typing.Optional[typing.Sequence[TableDataSchemaItem]]

        index_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersUpdateTableResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.tables.update(
            collection_id="collection_id",
            table_id="table_id",
        )
        """
        _response = self._raw_client.update(
            collection_id,
            table_id,
            table_display_name=table_display_name,
            table_img_url=table_img_url,
            table_description=table_description,
            schema=schema,
            index_id=index_id,
            request_options=request_options,
        )
        return _response.data

    def delete(
        self, collection_id: str, table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectionServiceHandlersDeleteTableResponse:
        """
        Delete a table given a collection_id and table_id.

        Parameters
        ----------
        collection_id : str

        table_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersDeleteTableResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.tables.delete(
            collection_id="collection_id",
            table_id="table_id",
        )
        """
        _response = self._raw_client.delete(collection_id, table_id, request_options=request_options)
        return _response.data

    def get_schema(
        self, collection_id: str, table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TablesGetSchemaResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TablesGetSchemaResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.tables.get_schema(
            collection_id="collection_id",
            table_id="table_id",
        )
        """
        _response = self._raw_client.get_schema(collection_id, table_id, request_options=request_options)
        return _response.data

    def sync(
        self,
        collection_id: str,
        table_id: str,
        *,
        request: typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersTableSyncResponse:
        """
        Sync a table with a list of documents.

        Parameters
        ----------
        collection_id : str

        table_id : str

        request : typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersTableSyncResponse
            Successful Response

        Examples
        --------
        from scoutos import Scout

        client = Scout(
            api_key="YOUR_API_KEY",
        )
        client.tables.sync(
            collection_id="collection_id",
            table_id="table_id",
            request=[{"key": "value"}],
        )
        """
        _response = self._raw_client.sync(collection_id, table_id, request=request, request_options=request_options)
        return _response.data


class AsyncTablesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTablesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTablesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTablesClient
        """
        return self._raw_client

    async def list(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectionServiceHandlersGetTablesResponse:
        """
        Parameters
        ----------
        collection_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersGetTablesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.list(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(collection_id, request_options=request_options)
        return _response.data

    async def create(
        self,
        collection_id: str,
        *,
        table_display_name: typing.Optional[str] = OMIT,
        table_img_url: typing.Optional[str] = OMIT,
        table_description: typing.Optional[str] = OMIT,
        schema: typing.Optional[typing.Sequence[TableConfigInputSchemaItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersCreateTableResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_display_name : typing.Optional[str]

        table_img_url : typing.Optional[str]

        table_description : typing.Optional[str]

        schema : typing.Optional[typing.Sequence[TableConfigInputSchemaItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersCreateTableResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.create(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            collection_id,
            table_display_name=table_display_name,
            table_img_url=table_img_url,
            table_description=table_description,
            schema=schema,
            request_options=request_options,
        )
        return _response.data

    async def get(
        self, collection_id: str, table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectionServiceHandlersGetTableResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersGetTableResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.get(
                collection_id="collection_id",
                table_id="table_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(collection_id, table_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        collection_id: str,
        table_id: str,
        *,
        table_display_name: typing.Optional[str] = OMIT,
        table_img_url: typing.Optional[str] = OMIT,
        table_description: typing.Optional[str] = OMIT,
        schema: typing.Optional[typing.Sequence[TableDataSchemaItem]] = OMIT,
        index_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersUpdateTableResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        table_display_name : typing.Optional[str]

        table_img_url : typing.Optional[str]

        table_description : typing.Optional[str]

        schema : typing.Optional[typing.Sequence[TableDataSchemaItem]]

        index_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersUpdateTableResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.update(
                collection_id="collection_id",
                table_id="table_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            collection_id,
            table_id,
            table_display_name=table_display_name,
            table_img_url=table_img_url,
            table_description=table_description,
            schema=schema,
            index_id=index_id,
            request_options=request_options,
        )
        return _response.data

    async def delete(
        self, collection_id: str, table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CollectionServiceHandlersDeleteTableResponse:
        """
        Delete a table given a collection_id and table_id.

        Parameters
        ----------
        collection_id : str

        table_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersDeleteTableResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.delete(
                collection_id="collection_id",
                table_id="table_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(collection_id, table_id, request_options=request_options)
        return _response.data

    async def get_schema(
        self, collection_id: str, table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TablesGetSchemaResponse:
        """
        Parameters
        ----------
        collection_id : str

        table_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TablesGetSchemaResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.get_schema(
                collection_id="collection_id",
                table_id="table_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_schema(collection_id, table_id, request_options=request_options)
        return _response.data

    async def sync(
        self,
        collection_id: str,
        table_id: str,
        *,
        request: typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CollectionServiceHandlersTableSyncResponse:
        """
        Sync a table with a list of documents.

        Parameters
        ----------
        collection_id : str

        table_id : str

        request : typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CollectionServiceHandlersTableSyncResponse
            Successful Response

        Examples
        --------
        import asyncio

        from scoutos import AsyncScout

        client = AsyncScout(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tables.sync(
                collection_id="collection_id",
                table_id="table_id",
                request=[{"key": "value"}],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sync(
            collection_id, table_id, request=request, request_options=request_options
        )
        return _response.data
