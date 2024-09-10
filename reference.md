# Reference
<details><summary><code>client.<a href="src/scoutos/client.py">get_collections_v_2_collections_get</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import ScoutosApi

client = ScoutosApi(
    api_key="YOUR_API_KEY",
)
client.get_collections_v_2_collections_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/scoutos/client.py">create_collection_v_2_collections_post</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import ScoutosApi

client = ScoutosApi(
    api_key="YOUR_API_KEY",
)
client.create_collection_v_2_collections_post()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_img_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**columns:** `typing.Optional[typing.Sequence[CollectionConfigInputColumnsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/scoutos/client.py">get_collection_v_2_collections_collection_id_get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import ScoutosApi

client = ScoutosApi(
    api_key="YOUR_API_KEY",
)
client.get_collection_v_2_collections_collection_id_get(
    collection_id="collection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/scoutos/client.py">update_collection_v_2_collections_collection_id_put</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import ScoutosApi

client = ScoutosApi(
    api_key="YOUR_API_KEY",
)
client.update_collection_v_2_collections_collection_id_put(
    collection_id="collection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**collection_display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_img_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**columns:** `typing.Optional[typing.Sequence[CollectionConfigInputColumnsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/scoutos/client.py">delete_collection_v_2_collections_collection_id_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a collection given a collection_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import ScoutosApi

client = ScoutosApi(
    api_key="YOUR_API_KEY",
)
client.delete_collection_v_2_collections_collection_id_delete(
    collection_id="collection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/scoutos/client.py">get_documents_v_2_collections_collection_id_documents_get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import ScoutosApi

client = ScoutosApi(
    api_key="YOUR_API_KEY",
)
client.get_documents_v_2_collections_collection_id_documents_get(
    collection_id="collection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/scoutos/client.py">create_document_v_2_collections_collection_id_documents_post</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import DocumentData, ScoutosApi

client = ScoutosApi(
    api_key="YOUR_API_KEY",
)
client.create_document_v_2_collections_collection_id_documents_post(
    collection_id="collection_id",
    request=DocumentData(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateDocumentV2CollectionsCollectionIdDocumentsPostRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/scoutos/client.py">get_document_v_2_collections_collection_id_documents_document_id_get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import ScoutosApi

client = ScoutosApi(
    api_key="YOUR_API_KEY",
)
client.get_document_v_2_collections_collection_id_documents_document_id_get(
    collection_id="collection_id",
    document_id="document_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/scoutos/client.py">update_document_v_2_collections_collection_id_documents_document_id_put</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import ScoutosApi

client = ScoutosApi(
    api_key="YOUR_API_KEY",
)
client.update_document_v_2_collections_collection_id_documents_document_id_put(
    collection_id="collection_id",
    document_id="document_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**columns:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[typing.Sequence[DocumentContent]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/scoutos/client.py">delete_document_v_2_collections_collection_id_documents_document_id_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a document given a document_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import ScoutosApi

client = ScoutosApi(
    api_key="YOUR_API_KEY",
)
client.delete_document_v_2_collections_collection_id_documents_document_id_delete(
    collection_id="collection_id",
    document_id="document_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Workflows
<details><summary><code>client.workflows.<a href="src/scoutos/workflows/client.py">execute_stream</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import ScoutosApi

client = ScoutosApi(
    api_key="YOUR_API_KEY",
)
response = client.workflows.execute_stream(
    workflow_id="string",
    revision_id="string",
    session_id="string",
    input={"string": 1},
)
for chunk in response:
    yield chunk

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Dict[str, ReqBodyInputValue]` 
    
</dd>
</dl>

<dl>
<dd>

**revision_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workflows.<a href="src/scoutos/workflows/client.py">execute</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import ScoutosApi

client = ScoutosApi(
    api_key="YOUR_API_KEY",
)
client.workflows.execute(
    workflow_id="workflow_id",
    input={"key": 1},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Dict[str, ReqBodyInputValue]` 
    
</dd>
</dl>

<dl>
<dd>

**revision_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

