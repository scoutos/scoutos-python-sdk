# Reference
<details><summary><code>client.<a href="src/scoutos/client.py">info_handler_info_get</a>()</code></summary>
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
client.info_handler_info_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">get_info_v_2_triggers_info_get</a>()</code></summary>
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
client.get_info_v_2_triggers_info_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">get_info_v_2_index_info_get</a>()</code></summary>
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
client.get_info_v_2_index_info_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">get_info_v_2_workflows_info_get</a>()</code></summary>
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
client.get_info_v_2_workflows_info_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">get_info_v_2_collections_info_get</a>()</code></summary>
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
client.get_info_v_2_collections_info_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">parse_file_v_2_files_parse_post</a>(...)</code></summary>
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
client.parse_file_v_2_files_parse_post()

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

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**return_text:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_integrations_integrations_get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all integrations for an organization
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
client.get_integrations_integrations_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">get_integration_integrations_integration_id_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific integration for an organization by its ID.
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
client.get_integration_integrations_integration_id_get(
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_integration_connections_integrations_integration_id_connections_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all integrations for an organization
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
client.get_integration_connections_integrations_integration_id_connections_get(
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

<details><summary><code>client.<a href="src/scoutos/client.py">connect_integration_integrations_integration_id_connect_post</a>(...)</code></summary>
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
client.connect_integration_integrations_integration_id_connect_post(
    integration_id="integration_id",
    auth_type="api_key",
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

**integration_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**auth_type:** `ConnectIntegrationRequestAuthType` 
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">handle_send_message_integrations_slack_send_post</a>(...)</code></summary>
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
client.handle_send_message_integrations_slack_send_post(
    channel_id="channel_id",
    text="text",
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

**channel_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**thread_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**blocks:** `typing.Optional[typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]]]` 
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**icon_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">handle_add_reaction_integrations_slack_react_post</a>(...)</code></summary>
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
client.handle_add_reaction_integrations_slack_react_post(
    channel_id="channel_id",
    emoji_name="emoji_name",
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

**channel_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**emoji_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**thread_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">handle_get_thread_integrations_slack_thread_get</a>(...)</code></summary>
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
client.handle_get_thread_integrations_slack_thread_get(
    channel_id="channel_id",
    thread_id="thread_id",
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

**channel_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**thread_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">handle_get_team_info_integrations_slack_team_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Handles the request to get Slack team info
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
client.handle_get_team_info_integrations_slack_team_get(
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

<details><summary><code>client.<a href="src/scoutos/client.py">handle_list_channels_integrations_slack_channels_get</a>(...)</code></summary>
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
client.handle_list_channels_integrations_slack_channels_get()

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

**team_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">handle_migrate_integrations_integrations_migrate_post</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Migrate integration tokens from Neon to Firestore with KMS encryption.

This endpoint accepts a list of organization IDs and migrates their Slack and Notion tokens.
It fetches tokens from the Neon database and stores them in Firestore,
encrypting the tokens using KMS.

NOTE: Not a public endpoint - used for internal database migration
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
client.handle_migrate_integrations_integrations_migrate_post()

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

<details><summary><code>client.<a href="src/scoutos/client.py">handle_notion_oauth_integrations_notion_oauth_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Handle Notion OAuth token upsert

Args:
    request: The FastAPI request object
    body: The request body containing the access token and metadata

Returns:
    Response indicating success

Raises:
    HTTPException: If there's an error during the process
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
client.handle_notion_oauth_integrations_notion_oauth_post(
    access_token="access_token",
    metadata={"key": "value"},
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

**access_token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**integrated_service_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">exchange_mcp_auth_mcp_authorization_post</a>(...)</code></summary>
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
client.exchange_mcp_auth_mcp_authorization_post(
    code="code",
    state="state",
    url="url",
    name="name",
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

**code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**state:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">connect_mcp_mcp_connect_post</a>(...)</code></summary>
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
client.connect_mcp_mcp_connect_post(
    url="url",
    name="name",
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

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">delete_mcp_connection_mcp_servers_connection_id_delete</a>(...)</code></summary>
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
client.delete_mcp_connection_mcp_servers_connection_id_delete(
    connection_id="connection_id",
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

**connection_id:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_mcp_servers_mcp_servers_get</a>()</code></summary>
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
client.get_mcp_servers_mcp_servers_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">get_info_inbox_info_get</a>()</code></summary>
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
client.get_info_inbox_info_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">handle_get_sessions_inbox_sessions_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Process an interaction request through the environment.

Args:
    request: The FastAPI request
    session_id: The ID of the session
    interaction_request: The interaction request data

Returns:
    Span with the results of the interaction attached to its attributes
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
client.handle_get_sessions_inbox_sessions_get()

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

**search:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">handle_get_notifications_inbox_notifications_get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Process an interaction request through the environment.

Args:
    request: The FastAPI request
    session_id: The ID of the session
    interaction_request: The interaction request data

Returns:
    Span with the results of the interaction attached to its attributes
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
client.handle_get_notifications_inbox_notifications_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">handle_get_session_by_id_inbox_session_id_get</a>(...)</code></summary>
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
client.handle_get_session_by_id_inbox_session_id_get(
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

**session_id:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">handle_transcribe_inbox_session_id_transcribe_post</a>(...)</code></summary>
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
client.handle_transcribe_inbox_session_id_transcribe_post(
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

**session_id:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">upload_private_files_inbox_session_id_files_post</a>(...)</code></summary>
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
client.upload_private_files_inbox_session_id_files_post(
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

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**files:** `from __future__ import annotations

typing.List[core.File]` — See core.File for more documentation
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">handle_get_session_messages_inbox_session_id_messages_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Process an interaction request through the environment.

Args:
    request: The FastAPI request
    session_id: The ID of the session
    interaction_request: The interaction request data

Returns:
    Span with the results of the interaction attached to its attributes
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
client.handle_get_session_messages_inbox_session_id_messages_get(
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

**session_id:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">handle_message_inbox_session_id_messages_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Process an interaction request through the environment.

Args:
    request: The FastAPI request
    session_id: The ID of the session
    interaction_request: The interaction request data

Returns:
    Span with the results of the interaction attached to its attributes
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
from scoutos import (
    Scout,
    ScoutUser,
    SrcAppHttpRoutesInboxHandleMessageIncomingMessage,
)

client = Scout(
    api_key="YOUR_API_KEY",
)
client.handle_message_inbox_session_id_messages_post(
    session_id="session_id",
    messages=[
        SrcAppHttpRoutesInboxHandleMessageIncomingMessage(
            content="content",
            content_type="text/plain",
        )
    ],
    participants=[
        ScoutUser(
            id="id",
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

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Sequence[SrcAppHttpRoutesInboxHandleMessageIncomingMessage]` 
    
</dd>
</dl>

<dl>
<dd>

**participants:** `typing.Sequence[
    SrcAppHttpRoutesInboxHandleMessageInteractionRequestParticipantsItem
]` 
    
</dd>
</dl>

<dl>
<dd>

**history:** `typing.Optional[
    typing.Sequence[SrcAppHttpRoutesInboxHandleMessageIncomingMessage]
]` 
    
</dd>
</dl>

<dl>
<dd>

**files:** `typing.Optional[typing.Sequence[FilesAttribute]]` 
    
</dd>
</dl>

<dl>
<dd>

**ephemeral_agent_revision:** `typing.Optional[AgentRevision]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">handle_post_session_participant_inbox_sessions_session_id_participants_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Process an interaction request through the environment.

Args:
    request: The FastAPI request
    session_id: The ID of the session
    interaction_request: The interaction request data

Returns:
    Span with the results of the interaction attached to its attributes
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
from scoutos import Participant, Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
client.handle_post_session_participant_inbox_sessions_session_id_participants_post(
    session_id="session_id",
    request=[
        Participant(
            id="id",
            type="scout_user",
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

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Sequence[Participant]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">handle_cancel_session_inbox_session_id_cancel_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel ongoing agent response for a session.

Args:
    request: The FastAPI request
    session_id: The ID of the session to cancel

Returns:
    CancelResponse with cancellation status
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
client.handle_cancel_session_inbox_session_id_cancel_post(
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

**session_id:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_info_money_get</a>()</code></summary>
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
client.get_info_money_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">get_billing_accounts_get</a>()</code></summary>
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
client.get_billing_accounts_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">get_usage_accounts_usage_get</a>(...)</code></summary>
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
client.get_usage_accounts_usage_get()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/scoutos/client.py">get_invoices_accounts_invoices_get</a>()</code></summary>
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
client.get_invoices_accounts_invoices_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">create_portal_session_accounts_portal_get</a>()</code></summary>
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
client.create_portal_session_accounts_portal_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">get_workflow_usage_accounts_usage_workflows_get</a>()</code></summary>
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
client.get_workflow_usage_accounts_usage_workflows_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">get_notifications_notifications_get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will pull any org facing notifications for the app to display
Mostly billing related so far
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
client.get_notifications_notifications_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">change_billing_plan_accounts_plan_put</a>(...)</code></summary>
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
client.change_billing_plan_accounts_plan_put(
    name="plan_1",
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

**name:** `PlanTypes` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">stripe_webhook_hooks_stripe_post</a>()</code></summary>
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
client.stripe_webhook_hooks_stripe_post()

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

<details><summary><code>client.<a href="src/scoutos/client.py">renew_plans_crons_renew_plans_post</a>()</code></summary>
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
client.renew_plans_crons_renew_plans_post()

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

<details><summary><code>client.<a href="src/scoutos/client.py">daily_billing_tasks_crons_free_plan_usage_post</a>()</code></summary>
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
client.daily_billing_tasks_crons_free_plan_usage_post()

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

<details><summary><code>client.<a href="src/scoutos/client.py">billing_hourly_crons_billing_hourly_post</a>()</code></summary>
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
client.billing_hourly_crons_billing_hourly_post()

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

<details><summary><code>client.<a href="src/scoutos/client.py">list_spans_traces_trace_id_spans_get</a>(...)</code></summary>
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
client.list_spans_traces_trace_id_spans_get(
    trace_id="trace_id",
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

**trace_id:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">seed_agents_onboarding_seed_agents_post</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manually seed default agent personas for a new organization.
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
client.seed_agents_onboarding_seed_agents_post()

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

<details><summary><code>client.<a href="src/scoutos/client.py">send_followup_emails_onboarding_followup_emails_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send follow-up emails to users who registered on specific days.

This endpoint is designed to be called by cron jobs or manual triggers
to send onboarding follow-up emails.
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
client.send_followup_emails_onboarding_followup_emails_post()

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

**request:** `typing.Optional[FollowupEmailRequest]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">find_me_me_get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current authenticated user's information.
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
client.find_me_me_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">update_me_me_put</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the current authenticated user's information.
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
client.update_me_me_put()

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

**favorites:** `typing.Optional[typing.Sequence[typing.Dict[str, str]]]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">list_tags_tags_get</a>()</code></summary>
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
client.list_tags_tags_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">create_tag_tags_post</a>(...)</code></summary>
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
client.create_tag_tags_post(
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_tag_tags_tag_id_get</a>(...)</code></summary>
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
client.get_tag_tags_tag_id_get(
    tag_id="tag_id",
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

**tag_id:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">update_tag_tags_tag_id_put</a>(...)</code></summary>
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
client.update_tag_tags_tag_id_put(
    tag_id="tag_id",
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

**tag_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">interact_handler_world_agent_id_session_id_interact_post</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import Scout, SrcAppHttpRoutesWorldInteractIncomingMessage

client = Scout(
    api_key="YOUR_API_KEY",
)
client.interact_handler_world_agent_id_session_id_interact_post(
    agent_id="agent_id",
    messages=[
        SrcAppHttpRoutesWorldInteractIncomingMessage(
            content="content",
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

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Sequence[SrcAppHttpRoutesWorldInteractIncomingMessage]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">interact_handler_world_agent_id_interact_post</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import Scout, SrcAppHttpRoutesWorldInteractIncomingMessage

client = Scout(
    api_key="YOUR_API_KEY",
)
client.interact_handler_world_agent_id_interact_post(
    agent_id="agent_id",
    messages=[
        SrcAppHttpRoutesWorldInteractIncomingMessage(
            content="content",
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

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Sequence[SrcAppHttpRoutesWorldInteractIncomingMessage]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">list_agents_agents_get</a>()</code></summary>
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
client.list_agents_agents_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">upsert_agent_agents_post</a>(...)</code></summary>
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
client.upsert_agent_agents_post(
    agent="agent",
    revision="revision",
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

**agent:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**revision:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**activate:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**agent_image:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_active_agent_agents_agent_id_active_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an agent and its active revision by agent_id.
Verifies that the agent belongs to the actor's organization.
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
client.get_active_agent_agents_agent_id_active_get(
    agent_id="agent_id",
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

**agent_id:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_tools_agents_tools_get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get available tools for the organization.

Args:
    request: The FastAPI request

Returns:
    Span with the list of available tools attached to its attributes
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
client.get_tools_agents_tools_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">delete_agent_agents_agent_id_delete</a>(...)</code></summary>
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
client.delete_agent_agents_agent_id_delete(
    agent_id="agent_id",
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

**agent_id:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">expire_blobs_expire_blobs_post</a>()</code></summary>
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
client.expire_blobs_expire_blobs_post()

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
client.workflows.create_revision()

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
client.workflows.list()

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
client.workflows.create()

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

## Revisions
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
client.usage.get()

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
client.copilots.list()

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
client.triggers.list()

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
client.triggers.update_cron_auth_headers()

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
client.collections.list()

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

**await_completion:** `typing.Optional[bool]` — Whether to wait for document creation/update to complete
    
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

**await_completion:** `typing.Optional[bool]` — Whether to wait for document creation/update to complete
    
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
    document_id="document_id",
    table_id="table_id",
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

**document_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**table_id:** `str` 
    
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
<details><summary><code>client.syncs.<a href="src/scoutos/syncs/client.py">list</a>(...)</code></summary>
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
client.syncs.list(
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

