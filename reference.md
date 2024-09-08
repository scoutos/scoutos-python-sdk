# Reference
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

