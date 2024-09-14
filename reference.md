# Reference
## Workflows
<details><summary><code>client.workflows.<a href="src/scoutos/workflows/client.py">run_stream</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
response = client.workflows.run_stream(
    workflow_id="string",
    revision_id="string",
    session_id="string",
    environment="production",
    input={"string": True},
    streaming=True,
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

**environment:** `typing.Optional[Environment]` 
    
</dd>
</dl>

<dl>
<dd>

**streaming:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.workflows.<a href="src/scoutos/workflows/client.py">run</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
client.workflows.run(
    workflow_id="workflow_id",
    input={"key": True},
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

**environment:** `typing.Optional[Environment]` 
    
</dd>
</dl>

<dl>
<dd>

**streaming:** `typing.Optional[bool]` 
    
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

## Collections
<details><summary><code>client.collections.<a href="src/scoutos/collections/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
client.collections.get(
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

<details><summary><code>client.collections.<a href="src/scoutos/collections/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
client.collections.create()

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

<details><summary><code>client.collections.<a href="src/scoutos/collections/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
client.collections.update(
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

<details><summary><code>client.collections.<a href="src/scoutos/collections/client.py">delete</a>(...)</code></summary>
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
from scoutos import Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
client.collections.delete(
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

## Documents
<details><summary><code>client.documents.<a href="src/scoutos/documents/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
client.documents.get(
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

<details><summary><code>client.documents.<a href="src/scoutos/documents/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import DocumentDataInput, Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
client.documents.create(
    collection_id="collection_id",
    request=DocumentDataInput(),
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

**request:** `DocumentsCreateRequest` 
    
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

<details><summary><code>client.documents.<a href="src/scoutos/documents/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
client.documents.update(
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

<details><summary><code>client.documents.<a href="src/scoutos/documents/client.py">delete</a>(...)</code></summary>
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
from scoutos import Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
client.documents.delete(
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

