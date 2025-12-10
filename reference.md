# Reference
## Workflows
<details><summary><code>client.workflows.<a href="src/scoutos/workflows/client.py">create_revision</a>(...)</code></summary>
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
client.workflows.create_revision(
    workflow_id="workflow_id",
    workflow_key="workflow_key",
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

**workflow_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_schema_version:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_img_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**blocks:** `typing.Optional[typing.Sequence[BlockInput]]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[typing.Sequence[WorkflowNoteInput]]` 
    
</dd>
</dl>

<dl>
<dd>

**placeholders:** `typing.Optional[typing.Sequence[PlaceholderInput]]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**is_tool:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.workflows.<a href="src/scoutos/workflows/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all workflows in the organization
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
client.workflows.list(
    sort="sort",
    direction="direction",
    start_at="start_at",
    limit=1,
    query="query",
    tags="tags",
    drive=True,
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

**sort:** `typing.Optional[str]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[str]` — Sort in ascending or descending order
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `typing.Optional[str]` — created_at to start at
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit of records to return
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search query
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[str]` — Filter by tags
    
</dd>
</dl>

<dl>
<dd>

**drive:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.workflows.<a href="src/scoutos/workflows/client.py">create</a>(...)</code></summary>
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
client.workflows.create(
    workflow_key="workflow_key",
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

**workflow_key:** `typing.Optional[str]` — A unique key to identify the workflow
    
</dd>
</dl>

<dl>
<dd>

**workflow_display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_schema_version:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_img_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**blocks:** `typing.Optional[typing.Sequence[BlockInput]]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[typing.Sequence[WorkflowNoteInput]]` 
    
</dd>
</dl>

<dl>
<dd>

**placeholders:** `typing.Optional[typing.Sequence[PlaceholderInput]]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**is_tool:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.workflows.<a href="src/scoutos/workflows/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch app configuration by ID.
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
client.workflows.get(
    workflow_id="workflow_id",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workflows.<a href="src/scoutos/workflows/client.py">update</a>(...)</code></summary>
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
client.workflows.update(
    workflow_id="workflow_id",
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

**workflow_display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_schema_version:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_img_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**blocks:** `typing.Optional[typing.Sequence[BlockInput]]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[typing.Sequence[WorkflowNoteInput]]` 
    
</dd>
</dl>

<dl>
<dd>

**placeholders:** `typing.Optional[typing.Sequence[PlaceholderInput]]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**is_tool:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.workflows.<a href="src/scoutos/workflows/client.py">delete</a>(...)</code></summary>
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
client.workflows.delete(
    workflow_id="workflow_id",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

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
    workflow_id="workflow_id",
    environment="environment",
    revision_id="revision_id",
    session_id="session_id",
)
for chunk in response.data:
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

**environment:** `typing.Optional[str]` 

Specifies the execution environment for the workflow. The available environments include:
- `production`: The production environment, where workflows are executed under live conditions.
- `staging`: A staging environment used for testing prior to production deployment.
- `development`: A development environment used for testing new changes.
- `console`: The console environment, runs latest changes on a workflow.
    
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

**inputs:** `typing.Optional[typing.Dict[str, WorkflowsRunStreamRequestInputsValue]]` 
    
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
    environment="environment",
    revision_id="revision_id",
    session_id="session_id",
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

**environment:** `typing.Optional[str]` 

Specifies the execution environment for the workflow. The available environments include:
- `production`: The production environment, where workflows are executed under live conditions.
- `staging`: A staging environment used for testing prior to production deployment.
- `development`: A development environment used for testing new changes.
- `console`: The console environment, runs latest changes on a workflow.
    
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

**inputs:** `typing.Optional[typing.Dict[str, WorkflowsRunRequestInputsValue]]` 
    
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

<details><summary><code>client.workflows.<a href="src/scoutos/workflows/client.py">run_with_config</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import Scout, WorkflowConfigInput

client = Scout(
    api_key="YOUR_API_KEY",
)
client.workflows.run_with_config(
    environment="environment",
    revision_id="revision_id",
    session_id="session_id",
    workflow_config=WorkflowConfigInput(),
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

**workflow_config:** `WorkflowConfigInput` 
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[str]` 

Specifies the execution environment for the workflow. The available environments include:
- `production`: The production environment, where workflows are executed under live conditions.
- `staging`: A staging environment used for testing prior to production deployment.
- `development`: A development environment used for testing new changes.
- `console`: The console environment, runs latest changes on a workflow.
    
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

**workflow_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**inputs:** `typing.Optional[
    typing.Dict[str, SrcHandlersWorkflowsExecuteWithConfigReqBodyInputsValue]
]` 
    
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

## WorkflowRevisions
<details><summary><code>client.workflow_revisions.<a href="src/scoutos/workflow_revisions/client.py">update</a>(...)</code></summary>
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
client.workflow_revisions.update(
    workflow_id="workflow_id",
    revision_id="revision_id",
    name="name",
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

**revision_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
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

## Revisions
<details><summary><code>client.revisions.<a href="src/scoutos/revisions/client.py">delete</a>(...)</code></summary>
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
client.revisions.delete(
    workflow_id="workflow_id",
    revision_id="revision_id",
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

**revision_id:** `str` 
    
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

<details><summary><code>client.revisions.<a href="src/scoutos/revisions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all app revisions in the organization
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
client.revisions.list(
    workflow_id="workflow_id",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.revisions.<a href="src/scoutos/revisions/client.py">update</a>(...)</code></summary>
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
client.revisions.update(
    workflow_id="workflow_id",
    revision_id="revision_id",
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

**revision_id:** `str` 
    
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

## Environments
<details><summary><code>client.environments.<a href="src/scoutos/environments/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all environments for a workflow in the organization
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
client.environments.list(
    workflow_id="workflow_id",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/scoutos/environments/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update deployments within a workflow environment
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
from scoutos import EnvironmentDeploymentConfig, Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
client.environments.update(
    workflow_id="workflow_id",
    environment_id="environment_id",
    name="name",
    description="description",
    deployments=[
        EnvironmentDeploymentConfig(
            revision_lookup="latest",
        )
    ],
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

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**deployments:** `typing.Sequence[EnvironmentDeploymentConfig]` 
    
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

## Usage
<details><summary><code>client.usage.<a href="src/scoutos/usage/client.py">get</a>(...)</code></summary>
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
client.usage.get(
    start_date="start_date",
    end_date="end_date",
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

**start_date:** `typing.Optional[str]` — Start date for the usage data
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — End date for the usage data
    
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

## WorkflowLogs
<details><summary><code>client.workflow_logs.<a href="src/scoutos/workflow_logs/client.py">list_logs</a>(...)</code></summary>
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
response = client.workflow_logs.list_logs(
    workflow_id="workflow_id",
    start_date="start_date",
    end_date="end_date",
    limit=1,
    session_id="session_id",
    status="status",
    cursor="cursor",
    summary_only=True,
)
for chunk in response.data:
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

**start_date:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**summary_only:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.workflow_logs.<a href="src/scoutos/workflow_logs/client.py">get_details</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get full log details for a specific workflow run.
Requires either session_id or workflow_run_id to identify the log.
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
client.workflow_logs.get_details(
    workflow_id="workflow_id",
    session_id="session_id",
    workflow_run_id="workflow_run_id",
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

**workflow_id:** `str` — The workflow ID
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` — The session ID to identify the log. Either session_id or workflow_run_id must be provided.
    
</dd>
</dl>

<dl>
<dd>

**workflow_run_id:** `typing.Optional[str]` — The workflow run ID to identify the log. Either session_id or workflow_run_id must be provided.
    
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

## Copilots
<details><summary><code>client.copilots.<a href="src/scoutos/copilots/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all copilots in the organization
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
client.copilots.list(
    sort="sort",
    direction="direction",
    start_at="start_at",
    limit=1,
    query="query",
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

**sort:** `typing.Optional[str]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[str]` — Sort in ascending or descending order
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `typing.Optional[str]` — created_at to start at
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit of records to return
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search query
    
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

<details><summary><code>client.copilots.<a href="src/scoutos/copilots/client.py">create</a>(...)</code></summary>
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
client.copilots.create()

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

**workflow_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**img_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[CopilotConfigMode]` 
    
</dd>
</dl>

<dl>
<dd>

**code_theme:** `typing.Optional[CopilotConfigCodeTheme]` 
    
</dd>
</dl>

<dl>
<dd>

**colors:** `typing.Optional[typing.Dict[str, str]]` 
    
</dd>
</dl>

<dl>
<dd>

**fab:** `typing.Optional[typing.Dict[str, typing.Optional[CopilotConfigFabValue]]]` 
    
</dd>
</dl>

<dl>
<dd>

**loading_text:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**message_placeholder:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**initial_activity:** `typing.Optional[typing.Sequence[typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**allowed_origins:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**powered_by:** `typing.Optional[str]` 
    
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

<details><summary><code>client.copilots.<a href="src/scoutos/copilots/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch copilot configuration by ID.
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
client.copilots.get(
    copilot_id="copilot_id",
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

**copilot_id:** `str` 
    
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

<details><summary><code>client.copilots.<a href="src/scoutos/copilots/client.py">update</a>(...)</code></summary>
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
client.copilots.update(
    copilot_id="copilot_id",
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

**copilot_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**img_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[CopilotConfigMode]` 
    
</dd>
</dl>

<dl>
<dd>

**code_theme:** `typing.Optional[CopilotConfigCodeTheme]` 
    
</dd>
</dl>

<dl>
<dd>

**colors:** `typing.Optional[typing.Dict[str, str]]` 
    
</dd>
</dl>

<dl>
<dd>

**fab:** `typing.Optional[typing.Dict[str, typing.Optional[CopilotConfigFabValue]]]` 
    
</dd>
</dl>

<dl>
<dd>

**loading_text:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**message_placeholder:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**initial_activity:** `typing.Optional[typing.Sequence[typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**allowed_origins:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**powered_by:** `typing.Optional[str]` 
    
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

<details><summary><code>client.copilots.<a href="src/scoutos/copilots/client.py">delete</a>(...)</code></summary>
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
client.copilots.delete(
    copilot_id="copilot_id",
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

**copilot_id:** `str` 
    
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

## Triggers
<details><summary><code>client.triggers.<a href="src/scoutos/triggers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All apis and effects are injected into every endpoint
via request.context. The request_context() utility can be used
to get Intellisense type-completion
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
client.triggers.list(
    action_type="workflow.execute",
    workflow_id="workflow_id",
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

**action_type:** `typing.Optional[ActionType]` — Filter by action type
    
</dd>
</dl>

<dl>
<dd>

**workflow_id:** `typing.Optional[str]` — Filter by workflow ID
    
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

<details><summary><code>client.triggers.<a href="src/scoutos/triggers/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import Scout, SlackTriggerConfigInput, SourceSync

client = Scout(
    api_key="YOUR_API_KEY",
)
client.triggers.create(
    request=SlackTriggerConfigInput(
        action=SourceSync(
            sync_id="sync_id",
        ),
    ),
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

**request:** `TriggersCreateRequest` 
    
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

<details><summary><code>client.triggers.<a href="src/scoutos/triggers/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import Scout, SlackTriggerConfigInput, SourceSync

client = Scout(
    api_key="YOUR_API_KEY",
)
client.triggers.update(
    trigger_id="trigger_id",
    request=SlackTriggerConfigInput(
        action=SourceSync(
            sync_id="sync_id",
        ),
    ),
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

**trigger_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `TriggersUpdateRequest` 
    
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

<details><summary><code>client.triggers.<a href="src/scoutos/triggers/client.py">delete</a>(...)</code></summary>
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
client.triggers.delete(
    trigger_id="trigger_id",
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

**trigger_id:** `str` 
    
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

<details><summary><code>client.triggers.<a href="src/scoutos/triggers/client.py">execute_slack</a>()</code></summary>
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
client.triggers.execute_slack()

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

<details><summary><code>client.triggers.<a href="src/scoutos/triggers/client.py">execute_cron</a>()</code></summary>
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
client.triggers.execute_cron()

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

<details><summary><code>client.triggers.<a href="src/scoutos/triggers/client.py">update_cron_auth_headers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Cloud Scheduler job Authorization headers for organizations.
Lists all Cloud Scheduler jobs and updates those matching the trigger pattern.

Args:
    dry_run: If True, only shows what would be updated without making changes
    test_org_id: If provided, only processes jobs for this specific organization ID

Only accessible to Scout internal organizations for security.
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
client.triggers.update_cron_auth_headers(
    dry_run=True,
    test_org_id="test_org_id",
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

**dry_run:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**test_org_id:** `typing.Optional[str]` 
    
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

## Integrations
<details><summary><code>client.integrations.<a href="src/scoutos/integrations/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all OAuth integrations for the organization

If service is 'all', returns integrations for all services.
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
client.integrations.list(
    service="service",
    fetch_icons=True,
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

**service:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fetch_icons:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.integrations.<a href="src/scoutos/integrations/client.py">list_channels</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all channels for a specific Slack workspace
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
client.integrations.list_channels(
    team_id="team_id",
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

**team_id:** `str` 
    
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

## Organizations
<details><summary><code>client.organizations.<a href="src/scoutos/organizations/client.py">delete_integration</a>(...)</code></summary>
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
client.organizations.delete_integration(
    integration_type="integration_type",
    integration_id="integration_id",
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

**integration_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `str` 
    
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
<details><summary><code>client.collections.<a href="src/scoutos/collections/client.py">list</a>(...)</code></summary>
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
client.collections.list(
    start_at="start_at",
    limit=1,
    query="query",
    tags="tags",
    sort="sort",
    drive=True,
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

**start_at:** `typing.Optional[str]` — created_at to start at
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit of records to return
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search query
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[str]` — Filter by tags
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort
    
</dd>
</dl>

<dl>
<dd>

**drive:** `typing.Optional[bool]` 
    
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

**tags:** `typing.Optional[typing.Sequence[str]]` 
    
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

**tags:** `typing.Optional[typing.Sequence[str]]` 
    
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

<details><summary><code>client.collections.<a href="src/scoutos/collections/client.py">list_syncs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Sources by Destination, specifically given a collection and table
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
client.collections.list_syncs(
    collection_id="collection_id",
    table_id="table_id",
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

**table_id:** `str` 
    
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

<details><summary><code>client.collections.<a href="src/scoutos/collections/client.py">get_views</a>(...)</code></summary>
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
client.collections.get_views(
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

<details><summary><code>client.collections.<a href="src/scoutos/collections/client.py">update_views</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import CollectionViewStateInput, Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
client.collections.update_views(
    collection_id="collection_id",
    view_state=CollectionViewStateInput(
        organization_id="organization_id",
        collection_id="collection_id",
    ),
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

**view_state:** `CollectionViewStateInput` 
    
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

<details><summary><code>client.collections.<a href="src/scoutos/collections/client.py">delete_views</a>(...)</code></summary>
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
client.collections.delete_views(
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

<details><summary><code>client.collections.<a href="src/scoutos/collections/client.py">list_individual_views</a>(...)</code></summary>
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
client.collections.list_individual_views(
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

<details><summary><code>client.collections.<a href="src/scoutos/collections/client.py">create_view</a>(...)</code></summary>
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
client.collections.create_view(
    collection_id="collection_id",
    name="name",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[CreateViewRequestType]` 
    
</dd>
</dl>

<dl>
<dd>

**emoji:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**table_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[CreateViewRequestSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `typing.Optional[ViewVisibility]` 
    
</dd>
</dl>

<dl>
<dd>

**shared_with:** `typing.Optional[typing.Sequence[str]]` 
    
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

<details><summary><code>client.collections.<a href="src/scoutos/collections/client.py">update_view</a>(...)</code></summary>
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
client.collections.update_view(
    collection_id="collection_id",
    view_id="view_id",
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

**view_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[UpdateViewRequestType]` 
    
</dd>
</dl>

<dl>
<dd>

**emoji:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[UpdateViewRequestSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `typing.Optional[ViewVisibility]` 
    
</dd>
</dl>

<dl>
<dd>

**shared_with:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Sequence[ViewFilter]]` 
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[ViewQueryInput]` 
    
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

<details><summary><code>client.collections.<a href="src/scoutos/collections/client.py">delete_view</a>(...)</code></summary>
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
client.collections.delete_view(
    collection_id="collection_id",
    view_id="view_id",
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

**view_id:** `str` 
    
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

## Tables
<details><summary><code>client.tables.<a href="src/scoutos/tables/client.py">list</a>(...)</code></summary>
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
client.tables.list(
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

<details><summary><code>client.tables.<a href="src/scoutos/tables/client.py">create</a>(...)</code></summary>
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
client.tables.create(
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

**table_display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**table_img_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**table_description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**schema:** `typing.Optional[typing.Sequence[TableConfigInputSchemaItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**icon_emoji:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**icon_asset_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**icon_fill:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**singular_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**plural_name:** `typing.Optional[str]` 
    
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

<details><summary><code>client.tables.<a href="src/scoutos/tables/client.py">get</a>(...)</code></summary>
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
client.tables.get(
    collection_id="collection_id",
    table_id="table_id",
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

**table_id:** `str` 
    
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

<details><summary><code>client.tables.<a href="src/scoutos/tables/client.py">update</a>(...)</code></summary>
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
client.tables.update(
    collection_id="collection_id",
    table_id="table_id",
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

**table_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**table_display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**table_img_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**table_description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**schema:** `typing.Optional[typing.Sequence[TableDataSchemaItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**icon_emoji:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**icon_asset_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**icon_fill:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**singular_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**plural_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**index_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.tables.<a href="src/scoutos/tables/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a table given a collection_id and table_id.
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
client.tables.delete(
    collection_id="collection_id",
    table_id="table_id",
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

**table_id:** `str` 
    
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

<details><summary><code>client.tables.<a href="src/scoutos/tables/client.py">get_schema</a>(...)</code></summary>
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
client.tables.get_schema(
    collection_id="collection_id",
    table_id="table_id",
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

**table_id:** `str` 
    
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

<details><summary><code>client.tables.<a href="src/scoutos/tables/client.py">sync</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sync a table with a list of documents.
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
client.tables.sync(
    collection_id="collection_id",
    table_id="table_id",
    request=[{"key": "value"}],
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

**table_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
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
<details><summary><code>client.documents.<a href="src/scoutos/documents/client.py">list</a>(...)</code></summary>
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
client.documents.list(
    collection_id="collection_id",
    table_id="table_id",
    limit=1,
    cursor="cursor",
    query="query",
    offset=1,
    sort_by="sort_by",
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

**table_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit of records to return
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to fetch next set of records
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search query
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset to fetch next set of records
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — Sort by field
    
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
from scoutos import Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
client.documents.create(
    collection_id="collection_id",
    table_id="table_id",
    job_id="job_id",
    sync_id="sync_id",
    await_completion=True,
    mode="mode",
    request={"key": True},
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

**table_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DocumentsCreateRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `typing.Optional[str]` — The job id responsible for the document creation/update
    
</dd>
</dl>

<dl>
<dd>

**sync_id:** `typing.Optional[str]` — The sync id the job belongs to thats responsible for the document creation/update
    
</dd>
</dl>

<dl>
<dd>

**await_completion:** `typing.Optional[bool]` — Whether to wait for document creation/update to complete
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[str]` — The mode to use for the document creation/update
    
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

<details><summary><code>client.documents.<a href="src/scoutos/documents/client.py">update_batch</a>(...)</code></summary>
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
client.documents.update_batch(
    collection_id="collection_id",
    table_id="table_id",
    job_id="job_id",
    sync_id="sync_id",
    await_completion=True,
    mode="mode",
    request={"key": True},
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

**table_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DocumentsUpdateBatchRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `typing.Optional[str]` — The job id responsible for the document creation/update
    
</dd>
</dl>

<dl>
<dd>

**sync_id:** `typing.Optional[str]` — The sync id the job belongs to thats responsible for the document creation/update
    
</dd>
</dl>

<dl>
<dd>

**await_completion:** `typing.Optional[bool]` — Whether to wait for document creation/update to complete
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[str]` — The mode to use for the document creation/update
    
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
    table_id="table_id",
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

**table_id:** `str` 
    
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
    table_id="table_id",
    document_id="document_id",
    request={},
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

**table_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Optional[DocumentsUpdateRequestValue]]` 
    
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
    table_id="table_id",
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

**table_id:** `str` 
    
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

<details><summary><code>client.documents.<a href="src/scoutos/documents/client.py">delete_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete documents given a list of document ids.
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
client.documents.delete_batch(
    collection_id="collection_id",
    table_id="table_id",
    request=["string"],
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

**table_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Sequence[str]` 
    
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

## Sources
<details><summary><code>client.sources.<a href="src/scoutos/sources/client.py">list</a>()</code></summary>
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
client.sources.list()

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

## Syncs
<details><summary><code>client.syncs.<a href="src/scoutos/syncs/client.py">list</a>()</code></summary>
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
client.syncs.list()

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

<details><summary><code>client.syncs.<a href="src/scoutos/syncs/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import (
    CollectionDestination,
    Mapping,
    Scout,
    SourceSyncGoogleDriveSettings,
    SyncConfigInput,
)

client = Scout(
    api_key="YOUR_API_KEY",
)
client.syncs.create(
    sync_config=SyncConfigInput(
        source_settings=SourceSyncGoogleDriveSettings(),
        destination=CollectionDestination(
            collection_id="collection_id",
            table_id="table_id",
        ),
        mapping=Mapping(),
    ),
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

**sync_config:** `SyncConfigInput` 
    
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

<details><summary><code>client.syncs.<a href="src/scoutos/syncs/client.py">get</a>(...)</code></summary>
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
client.syncs.get(
    sync_id="sync_id",
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

**sync_id:** `str` 
    
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

<details><summary><code>client.syncs.<a href="src/scoutos/syncs/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import (
    CollectionDestination,
    Mapping,
    Scout,
    SourceSyncGoogleDriveSettings,
    SyncConfigInput,
)

client = Scout(
    api_key="YOUR_API_KEY",
)
client.syncs.update(
    sync_id="sync_id",
    sync_config=SyncConfigInput(
        source_settings=SourceSyncGoogleDriveSettings(),
        destination=CollectionDestination(
            collection_id="collection_id",
            table_id="table_id",
        ),
        mapping=Mapping(),
    ),
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

**sync_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sync_config:** `SyncConfigInput` 
    
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

<details><summary><code>client.syncs.<a href="src/scoutos/syncs/client.py">delete</a>(...)</code></summary>
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
client.syncs.delete(
    sync_id="sync_id",
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

**sync_id:** `str` 
    
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

<details><summary><code>client.syncs.<a href="src/scoutos/syncs/client.py">execute</a>(...)</code></summary>
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
client.syncs.execute(
    sync_id="sync_id",
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

**sync_id:** `str` 
    
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

