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
client.parse_file_v_2_files_parse_post(
    return_text=True,
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

**client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[str]` 
    
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

**unfurl_links:** `typing.Optional[bool]` 
    
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
client.handle_get_sessions_inbox_sessions_get(
    search="search",
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

<details><summary><code>client.<a href="src/scoutos/client.py">handle_delete_session_inbox_session_id_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an inbox session and all its associated messages.

Args:
    request: The FastAPI request
    session_id: The ID of the session to delete

Returns:
    DeleteResponse with deletion status
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
client.handle_delete_session_inbox_session_id_delete(
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

**mentions:** `typing.Optional[typing.Sequence[Mention]]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">handle_rename_session_inbox_session_id_rename_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rename an inbox session by updating its title.

Args:
    request: The FastAPI request
    session_id: The ID of the session to rename
    rename_request: The request containing the new title

Returns:
    RenameResponse with rename status and new title
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
client.handle_rename_session_inbox_session_id_rename_post(
    session_id="session_id",
    title="title",
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

**title:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">execute_hook_webhooks_hook_id_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a hook trigger.

This is the main endpoint that external services call to trigger hooks.
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
client.execute_hook_webhooks_hook_id_get(
    hook_id="hook_id",
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

**hook_id:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">execute_hook_webhooks_hook_id_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a hook trigger.

This is the main endpoint that external services call to trigger hooks.
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
client.execute_hook_webhooks_hook_id_post(
    hook_id="hook_id",
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

**hook_id:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">delete_hook_webhooks_hook_id_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft delete a hook.
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
client.delete_hook_webhooks_hook_id_delete(
    hook_id="hook_id",
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

**hook_id:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">update_hook_webhooks_hook_id_patch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a hook's configuration.
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
client.update_hook_webhooks_hook_id_patch(
    hook_id="hook_id",
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

**hook_id:** `str` 
    
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

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**target_config:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**response_mode:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**allowed_methods:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**max_payload_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">list_hooks_webhooks_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all hooks for the current organization.
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
client.list_hooks_webhooks_get(
    target_type="target_type",
    target_id="target_id",
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

**target_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**target_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">create_hook_webhooks_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new hook for a workflow or other target.
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
from scoutos import Scout, WorkflowHookInput

client = Scout(
    api_key="YOUR_API_KEY",
)
client.create_hook_webhooks_post(
    request=WorkflowHookInput(
        name="name",
        target_id="target_id",
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

**request:** `CreateHookWebhooksPostRequest` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_hook_webhooks_hook_id_details_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a hook by its ID.
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
client.get_hook_webhooks_hook_id_details_get(
    hook_id="hook_id",
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

**hook_id:** `str` 
    
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
client.get_usage_accounts_usage_get(
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

<details><summary><code>client.<a href="src/scoutos/client.py">list_agent_sessions_observability_agents_agent_id_sessions_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List agent sessions for a given agent and date range.

Args:
    request: The FastAPI request
    agent_id: The ID of the agent
    start_date: Optional start date for filtering
    end_date: Optional end date for filtering

Returns:
    Response with list of agent sessions
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
import datetime

from scoutos import Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
client.list_agent_sessions_observability_agents_agent_id_sessions_get(
    agent_id="agent_id",
    start_date=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    end_date=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">list_agent_sessions_summary_observability_agents_agent_id_sessions_summary_get</a>(...)</code></summary>
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
client.list_agent_sessions_summary_observability_agents_agent_id_sessions_summary_get(
    agent_id="agent_id",
    start_date="start_date",
    end_date="end_date",
    limit=1,
    cursor="cursor",
    tool_filter="tool_filter",
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

**start_date:** `typing.Optional[str]` — Start date in ISO format
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — End date in ISO format
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of sessions per page
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Pagination cursor
    
</dd>
</dl>

<dl>
<dd>

**tool_filter:** `typing.Optional[str]` — Filter sessions by tool name
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_session_details_observability_agents_agent_id_sessions_session_id_details_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get full session details including all traces and spans for a specific session.

This endpoint is used when a user expands a session in the UI.
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
client.get_session_details_observability_agents_agent_id_sessions_session_id_details_get(
    agent_id="agent_id",
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

**agent_id:** `str` 
    
</dd>
</dl>

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

<details><summary><code>client.<a href="src/scoutos/client.py">get_agent_session_analytics_observability_agents_agent_id_analytics_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get session analytics data for a specific agent from spans table (hypertable).
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
import datetime

from scoutos import Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
client.get_agent_session_analytics_observability_agents_agent_id_analytics_get(
    agent_id="agent_id",
    start_date=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    end_date=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_agent_tool_usage_observability_agents_agent_id_tool_usage_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get tool usage statistics for a specific agent.

This endpoint aggregates tool invocations from spans data to show
which tools are most frequently used by an agent.
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
client.get_agent_tool_usage_observability_agents_agent_id_tool_usage_get(
    agent_id="agent_id",
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

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Start date in ISO format
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — End date in ISO format
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_agent_distinct_tools_observability_agents_agent_id_tools_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get distinct tools used by an agent.

This endpoint returns a clean list of all tools the agent has used
in the specified date range, with usage counts.
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
client.get_agent_distinct_tools_observability_agents_agent_id_tools_get(
    agent_id="agent_id",
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

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Start date in ISO format
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — End date in ISO format
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_pulse_feed_pulse_feed_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get pulse feed with enhanced filtering.

Returns both new pulse events and legacy agent interactions.
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
client.get_pulse_feed_pulse_feed_get(
    user_id="user_id",
    agent_ids="agent_ids",
    action_types="action_types",
    start_date="start_date",
    end_date="end_date",
    limit=1,
    include_children=True,
    min_significance=1.1,
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

**user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**agent_ids:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**action_types:** `typing.Optional[str]` 
    
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

**include_children:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**min_significance:** `typing.Optional[float]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">create_pulse_json_pulse_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create pulse from JSON data (existing endpoint)
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
client.create_pulse_json_pulse_post(
    description="description",
    agents=[{"key": "value"}],
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

**description:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**agents:** `typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**objects:** `typing.Optional[typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]]]` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**duration_minutes:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_entity_activities_pulse_activities_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get activities - either for a specific entity or with general filters
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
client.get_entity_activities_pulse_activities_get(
    entity_id="entity_id",
    entity_type="entity_type",
    involving_agent="involving_agent",
    on_object="on_object",
    of_type="of_type",
    with_outcome="with_outcome",
    since_days=1,
    limit=1,
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

**entity_id:** `typing.Optional[str]` — ID of the entity
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `typing.Optional[str]` — Type of entity (account, deal, user, etc)
    
</dd>
</dl>

<dl>
<dd>

**involving_agent:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**on_object:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**of_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**with_outcome:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**since_days:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">store_create_pulse_store_create_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new entity.

Example:
    POST /pulse/store/create
    {
        "type": "todo",
        "data": {
            "title": "Buy milk",
            "completed": false
        }
    }
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
client.store_create_pulse_store_create_post(
    type="type",
    data={"key": "value"},
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

**type:** `str` — Entity type (e.g., 'todo', 'note', 'task')
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Dict[str, typing.Optional[typing.Any]]` — Entity data
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — Optional tags
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">store_update_pulse_store_update_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an entity (partial updates).

Example:
    POST /pulse/store/update
    {
        "id": "todo_abc123",
        "updates": {
            "completed": true,
            "completed_at": "2024-01-01T12:00:00Z"
        }
    }
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
client.store_update_pulse_store_update_post(
    id="id",
    updates={"key": "value"},
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

**id:** `str` — Entity ID
    
</dd>
</dl>

<dl>
<dd>

**updates:** `typing.Dict[str, typing.Optional[typing.Any]]` — Partial updates to apply
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">store_get_tags_pulse_store_tags_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all unique tags across entities.

Example:
    GET /pulse/store/tags?type=file&prefix=folder:
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
client.store_get_tags_pulse_store_tags_get(
    type="type",
    prefix="prefix",
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

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">store_update_tags_pulse_store_tags_update_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add or remove tags from an entity.

Example:
    POST /pulse/store/tags/update
    {
        "id": "file-uuid",
        "add_tags": ["folder:marketing", "folder:campaigns"],
        "remove_tags": ["folder:archive"]
    }
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
client.store_update_tags_pulse_store_tags_update_post(
    id="id",
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

**id:** `str` — Entity ID
    
</dd>
</dl>

<dl>
<dd>

**add_tags:** `typing.Optional[typing.Sequence[str]]` — Tags to add
    
</dd>
</dl>

<dl>
<dd>

**remove_tags:** `typing.Optional[typing.Sequence[str]]` — Tags to remove
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">store_get_pulse_store_entity_id_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single entity.

GET /pulse/store/{entity_id}
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
client.store_get_pulse_store_entity_id_get(
    entity_id="entity_id",
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

**entity_id:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">store_delete_pulse_store_entity_id_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an entity.

DELETE /pulse/store/{entity_id}?soft=true
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
client.store_delete_pulse_store_entity_id_delete(
    entity_id="entity_id",
    soft=True,
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

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**soft:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">store_query_pulse_store_query_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query entities with filters.

Example:
    POST /pulse/store/query
    {
        "type": "file",
        "tags": ["folder:marketing"],
        "filter": {
            "completed": false
        },
        "limit": 50
    }
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
client.store_query_pulse_store_query_post()

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

**type:** `typing.Optional[str]` — Filter by entity type
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter by data fields
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — Filter by tags (must have ALL specified tags)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max results
    
</dd>
</dl>

<dl>
<dd>

**include_deleted:** `typing.Optional[bool]` — Include soft-deleted entities
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">store_query_fluent_pulse_store_query_fluent_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Powerful fluent query API with relationships and advanced filtering.

Example:
    POST /pulse/store/query/fluent
    {
        "select": "deal",
        "where": [
            {"field": "stage", "operator": "in", "value": ["negotiation", "proposal"]},
            {"field": "value", "operator": ">=", "value": 50000}
        ],
        "with": ["account", "contact"],
        "orderBy": [{"field": "value", "direction": "desc"}],
        "limit": 50
    }

Returns:
    {
        "ok": true,
        "data": [entity, ...],
        "total": 123,
        "includes": {
            "account": {entity_id: account_entity},
            "contact": {entity_id: contact_entity}
        }
    }
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
client.store_query_fluent_pulse_store_query_fluent_post(
    select="select",
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

**select:** `str` — Entity type to select
    
</dd>
</dl>

<dl>
<dd>

**where:** `typing.Optional[typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]]]` — WHERE conditions: [{field, operator, value}, ...]
    
</dd>
</dl>

<dl>
<dd>

**with_:** `typing.Optional[typing.Sequence[FluentQueryRequestWithItem]]` — Relations to include (auto-JOIN)
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Sequence[typing.Dict[str, str]]]` — Order by: [{field, direction}, ...]
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max results
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset for pagination
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[bool]` — Include total count
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[str]` — Group by field
    
</dd>
</dl>

<dl>
<dd>

**aggregations:** `typing.Optional[typing.Dict[str, typing.Dict[str, str]]]` — Aggregations: {alias: {function, field}}
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">store_batch_create_pulse_store_batch_create_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create multiple entities.

Example:
    POST /pulse/store/batch/create
    {
        "entities": [
            {"type": "todo", "data": {"title": "Task 1"}},
            {"type": "todo", "data": {"title": "Task 2"}}
        ]
    }
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
from scoutos import CreateEntityRequest, Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
client.store_batch_create_pulse_store_batch_create_post(
    entities=[
        CreateEntityRequest(
            type="type",
            data={"key": "value"},
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

**entities:** `typing.Sequence[CreateEntityRequest]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">list_entities_pulse_entities_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all entities extracted from activities.

Returns entities with their mention counts and metadata.
Used by the frontend ChannelEntitiesPanel.
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
client.list_entities_pulse_entities_get(
    limit=1,
    entity_type="entity_type",
    current_state=True,
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

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `typing.Optional[str]` — Filter by entity type
    
</dd>
</dl>

<dl>
<dd>

**current_state:** `typing.Optional[bool]` — Return only current state via quantum collapse
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">query_entities_pulse_entities_query_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query entities (agents or objects) across activities

Examples:

# Find all sales agents
{
    "entity_type": "agent",
    "tags": ["sales"],
    "include_stats": true
}

# Find documents involved in approved deals
{
    "entity_type": "object",
    "kinds": ["document", "contract"],
    "outcomes": ["approved"],
    "include_stats": true
}

# Find active users in last 7 days
{
    "entity_type": "agent",
    "kinds": ["user"],
    "time": {"last": "7d"},
    "min_activities": 5,
    "include_stats": true
}

# Find cross-functional agents (sales + engineering)
{
    "entity_type": "agent",
    "tags": ["sales", "engineering"],
    "group_by": "kind"
}
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
client.query_entities_pulse_entities_query_post()

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

**entity_type:** `typing.Optional[str]` — 'agent' or 'object'
    
</dd>
</dl>

<dl>
<dd>

**activity_filters:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter activities that entities appear in
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — Activities must have these tags
    
</dd>
</dl>

<dl>
<dd>

**outcomes:** `typing.Optional[typing.Sequence[str]]` — Activities must have these outcomes
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[typing.Sequence[str]]` — Activities must have these actions
    
</dd>
</dl>

<dl>
<dd>

**time:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Time range for activities
    
</dd>
</dl>

<dl>
<dd>

**kinds:** `typing.Optional[typing.Sequence[str]]` — Entity kinds to include (user, team, document, etc)
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.Sequence[str]]` — Entity roles to include
    
</dd>
</dl>

<dl>
<dd>

**current_state:** `typing.Optional[bool]` — Return only current state via quantum collapse
    
</dd>
</dl>

<dl>
<dd>

**include_stats:** `typing.Optional[bool]` — Include activity statistics for each entity
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[str]` — Group entities by field (kind, role)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**min_activities:** `typing.Optional[int]` — Minimum activities for entity to be included
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_entity_network_pulse_entities_entity_id_network_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the collaboration network around an entity

Returns entities connected to the target entity through shared activities
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
client.get_entity_network_pulse_entities_entity_id_network_get(
    entity_id="entity_id",
    depth=1,
    min_interactions=1,
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

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[int]` — Network depth
    
</dd>
</dl>

<dl>
<dd>

**min_interactions:** `typing.Optional[int]` — Minimum interactions to include connection
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_entity_network_pg_pulse_entities_entity_id_network_pg_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the collaboration network around an entity using PostgreSQL.

Returns entities connected to the target entity through shared activities.
This is optimized for PostgreSQL and uses efficient SQL queries instead of
multiple API calls.
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
client.get_entity_network_pg_pulse_entities_entity_id_network_pg_get(
    entity_id="entity_id",
    depth=1,
    min_interactions=1,
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

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[int]` — Network depth
    
</dd>
</dl>

<dl>
<dd>

**min_interactions:** `typing.Optional[int]` — Minimum interactions to include connection
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_entity_details_pulse_entities_entity_type_entity_id_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get detailed information about a specific entity

When current_state=true, uses quantum collapse to return only the latest state.
Otherwise includes all activities they've been involved in and collaboration patterns.
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
client.get_entity_details_pulse_entities_entity_type_entity_id_get(
    entity_type="entity_type",
    entity_id="entity_id",
    include_activities=True,
    time_range="time_range",
    current_state=True,
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

**entity_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**include_activities:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**time_range:** `typing.Optional[str]` — Time range like '7d', '30d'
    
</dd>
</dl>

<dl>
<dd>

**current_state:** `typing.Optional[bool]` — Return only current state via quantum collapse
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_schemas_pulse_schemas_get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all schemas for dynamic form generation.
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
client.get_schemas_pulse_schemas_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">search_activities_pulse_search_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Hybrid search for activities using PostgreSQL full-text and vector search.

Thin handler - delegates to PulseSearch domain API.
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
client.search_activities_pulse_search_post()

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

**query:** `typing.Optional[str]` — Search query text
    
</dd>
</dl>

<dl>
<dd>

**search_type:** `typing.Optional[SearchRequestSearchType]` — Type of search
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Additional filters to apply
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum results to return
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">search_entities_pulse_search_entities_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for entities with document content using hybrid search.

Thin handler - delegates to PulseSearch domain API.
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
client.search_entities_pulse_search_entities_post(
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

**query:** `str` — Search query text
    
</dd>
</dl>

<dl>
<dd>

**entity_ids:** `typing.Optional[typing.Sequence[str]]` — Specific entity IDs to search within
    
</dd>
</dl>

<dl>
<dd>

**entity_types:** `typing.Optional[typing.Sequence[str]]` — Entity types to search (file, note, etc)
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[EntitySearchRequestMode]` — Search mode
    
</dd>
</dl>

<dl>
<dd>

**return_format:** `typing.Optional[EntitySearchRequestReturnFormat]` — What to return - chunks, entity info, or full text
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max results
    
</dd>
</dl>

<dl>
<dd>

**similarity_threshold:** `typing.Optional[float]` — Minimum similarity score
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">update_search_indexes_pulse_search_update_indexes_post</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update search indexes for existing activities.

Thin handler - delegates to PulseSearch domain API.
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
client.update_search_indexes_pulse_search_update_indexes_post()

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

<details><summary><code>client.<a href="src/scoutos/client.py">get_distinct_values_pulse_search_distinct_field_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get distinct values for a specific field to help with query building.

Thin handler - delegates to PulseSearch domain API.
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
client.get_distinct_values_pulse_search_distinct_field_get(
    field="field",
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

**field:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">query_builder_pulse_query_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a declarative query using the powerful PulseQuery builder

This endpoint provides a more structured and powerful alternative to text-based search,
allowing complex filtering, aggregation, and business logic queries.

Examples:

# Find all activities by specific agents in last 7 days
{
    "agent_types": ["user"],
    "last_days": 7,
    "sort_by": "time"
}

# Customer journey analysis
{
    "customer_id": "customer_123",
    "last_days": 30,
    "sort_by": "time",
    "sort_direction": "asc"
}

# Revenue impact events with duration filters
{
    "revenue_impact": true,
    "min_duration_minutes": 5,
    "tags": ["sales", "deal"],
    "tag_mode": "all"
}

# Aggregated metrics by team
{
    "last_days": 14,
    "aggregate": true,
    "group_by": ["agent_type"],
    "team_name": "engineering"
}
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
client.query_builder_pulse_query_post()

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

**limit:** `typing.Optional[int]` — Maximum results to return
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset for pagination
    
</dd>
</dl>

<dl>
<dd>

**text_query:** `typing.Optional[str]` — Text to search in descriptions
    
</dd>
</dl>

<dl>
<dd>

**time_range_start:** `typing.Optional[dt.datetime]` — Start time for filtering
    
</dd>
</dl>

<dl>
<dd>

**time_range_end:** `typing.Optional[dt.datetime]` — End time for filtering
    
</dd>
</dl>

<dl>
<dd>

**last_hours:** `typing.Optional[int]` — Filter to last N hours
    
</dd>
</dl>

<dl>
<dd>

**last_days:** `typing.Optional[int]` — Filter to last N days
    
</dd>
</dl>

<dl>
<dd>

**agent_types:** `typing.Optional[typing.Sequence[str]]` — Filter by agent types
    
</dd>
</dl>

<dl>
<dd>

**agent_ids:** `typing.Optional[typing.Sequence[str]]` — Filter by specific agent IDs
    
</dd>
</dl>

<dl>
<dd>

**object_types:** `typing.Optional[typing.Sequence[str]]` — Filter by object types
    
</dd>
</dl>

<dl>
<dd>

**object_ids:** `typing.Optional[typing.Sequence[str]]` — Filter by specific object IDs
    
</dd>
</dl>

<dl>
<dd>

**action_types:** `typing.Optional[typing.Sequence[str]]` — Filter by action types
    
</dd>
</dl>

<dl>
<dd>

**action_statuses:** `typing.Optional[typing.Sequence[str]]` — Filter by action statuses
    
</dd>
</dl>

<dl>
<dd>

**specific_actions:** `typing.Optional[typing.Sequence[str]]` — Filter by specific action names
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — Tags to include
    
</dd>
</dl>

<dl>
<dd>

**exclude_tags:** `typing.Optional[typing.Sequence[str]]` — Tags to exclude
    
</dd>
</dl>

<dl>
<dd>

**tag_mode:** `typing.Optional[QueryBuilderRequestTagMode]` — Whether to match any or all tags
    
</dd>
</dl>

<dl>
<dd>

**min_duration_minutes:** `typing.Optional[float]` — Minimum duration in minutes
    
</dd>
</dl>

<dl>
<dd>

**max_duration_minutes:** `typing.Optional[float]` — Maximum duration in minutes
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Filter by customer ID
    
</dd>
</dl>

<dl>
<dd>

**team_name:** `typing.Optional[str]` — Filter by team
    
</dd>
</dl>

<dl>
<dd>

**deal_stages:** `typing.Optional[typing.Sequence[str]]` — Filter by deal stages
    
</dd>
</dl>

<dl>
<dd>

**revenue_impact:** `typing.Optional[bool]` — Filter for revenue impact events
    
</dd>
</dl>

<dl>
<dd>

**churn_risk:** `typing.Optional[bool]` — Filter for churn risk events
    
</dd>
</dl>

<dl>
<dd>

**escalation_level:** `typing.Optional[str]` — Filter by escalation level
    
</dd>
</dl>

<dl>
<dd>

**trace_id:** `typing.Optional[str]` — Filter by trace ID
    
</dd>
</dl>

<dl>
<dd>

**triggered_by:** `typing.Optional[str]` — Filter by triggering event
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[QueryBuilderRequestSortBy]` — Sort field
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[QueryBuilderRequestSortDirection]` — Sort direction
    
</dd>
</dl>

<dl>
<dd>

**count_only:** `typing.Optional[bool]` — Return only count, not full results
    
</dd>
</dl>

<dl>
<dd>

**explain:** `typing.Optional[bool]` — Include query explanation
    
</dd>
</dl>

<dl>
<dd>

**aggregate:** `typing.Optional[bool]` — Return aggregated results
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[typing.Sequence[QueryBuilderRequestGroupByItem]]` — Group by fields for aggregation
    
</dd>
</dl>

<dl>
<dd>

**group_by_tag_prefix:** `typing.Optional[str]` — Group by tag prefix (e.g., 'customer:')
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">query_builder_schema_pulse_query_schema_get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the schema for the query builder, showing all available filters and options
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
client.query_builder_schema_pulse_query_schema_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">upload_pulse_files_stream_pulse_files_stream_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload files to Pulse with activity tracking and optional RAG processing.
Returns a streaming response with progress updates.

Thin handler - delegates to PulseFiles domain API.
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
client.upload_pulse_files_stream_pulse_files_stream_post()

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

<details><summary><code>client.<a href="src/scoutos/client.py">get_pulse_files_pulse_files_get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get list of files for an organization.

Thin handler - delegates to PulseFiles domain API.
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
client.get_pulse_files_pulse_files_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">download_pulse_file_pulse_files_file_name_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a signed URL for downloading a file.

Thin handler - delegates to PulseFiles domain API.
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
client.download_pulse_file_pulse_files_file_name_get(
    file_name="file_name",
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

**file_name:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">delete_pulse_file_pulse_files_file_name_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a file and its associated chunks.

Thin handler - delegates to PulseFiles domain API.
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
client.delete_pulse_file_pulse_files_file_name_delete(
    file_name="file_name",
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

**file_name:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_file_chunks_pulse_files_file_name_chunks_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get RAG document chunks for a file.

Thin handler - delegates to PulseFiles domain API.
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
client.get_file_chunks_pulse_files_file_name_chunks_get(
    file_name="file_name",
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

**file_name:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">generate_ai_suggestion_pulse_security_questionnaire_ai_suggest_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate AI suggestion for a security question using RAG.

Thin handler - delegates to PulseQuestionnaire domain API.
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
client.generate_ai_suggestion_pulse_security_questionnaire_ai_suggest_post(
    question_id="question_id",
    question_text="question_text",
    category="category",
    questionnaire_id="questionnaire_id",
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

**question_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**question_text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**category:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**questionnaire_id:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">generate_batch_suggestions_pulse_security_questionnaire_batch_suggest_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate AI suggestions for multiple questions in batch.

Thin handler - delegates to PulseQuestionnaire domain API.
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
client.generate_batch_suggestions_pulse_security_questionnaire_batch_suggest_post(
    question_ids=["question_ids"],
    questionnaire_id="questionnaire_id",
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

**question_ids:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**questionnaire_id:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">update_questionnaire_files_pulse_security_questionnaire_questionnaire_id_files_put</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the selected files for a questionnaire.

Thin handler - delegates to PulseQuestionnaire domain API.
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
client.update_questionnaire_files_pulse_security_questionnaire_questionnaire_id_files_put(
    questionnaire_id="questionnaire_id",
    file_ids=["file_ids"],
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

**questionnaire_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file_ids:** `typing.Sequence[str]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_questionnaire_with_questions_pulse_security_questionnaire_questionnaire_id_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get questionnaire with all its questions loaded.

Thin handler - delegates to PulseQuestionnaire domain API.
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
client.get_questionnaire_with_questions_pulse_security_questionnaire_questionnaire_id_get(
    questionnaire_id="questionnaire_id",
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

**questionnaire_id:** `str` 
    
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

**favorites:** `typing.Optional[typing.Sequence[FavoriteRef]]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">find_all_scout_hooks_hooks_get</a>()</code></summary>
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
client.find_all_scout_hooks_hooks_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">create_scout_hook_hooks_post</a>(...)</code></summary>
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
client.create_scout_hook_hooks_post()

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

**hook_config:** `typing.Optional[ScoutHookConfigHttp]` 
    
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

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**triggering_events:** `typing.Optional[typing.Sequence[ScoutHookUpdateTriggeringEventsItem]]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">update_scout_hook_hooks_hook_id_put</a>(...)</code></summary>
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
client.update_scout_hook_hooks_hook_id_put(
    hook_id="hook_id",
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

**hook_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**hook_config:** `typing.Optional[ScoutHookConfigHttp]` 
    
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

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**triggering_events:** `typing.Optional[typing.Sequence[ScoutHookUpdateTriggeringEventsItem]]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">remove_scout_hook_hooks_hook_id_delete</a>(...)</code></summary>
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
client.remove_scout_hook_hooks_hook_id_delete(
    hook_id="hook_id",
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

**hook_id:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">rotate_api_keys_organization_rotate_keys_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rotate API keys for the current organization.

Delegates to ProfileManager for the actual business logic.
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
client.rotate_api_keys_organization_rotate_keys_post()

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

**confirm:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**grace_period_hours:** `typing.Optional[float]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">list_tools_tools_get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get available tools for the organization with full input schemas.

This endpoint delegates to the Tool domain API which provides:
- Tool authorization checking
- Schema retrieval from all sources
- Comprehensive tool information

Args:
    request: The FastAPI request

Returns:
    ListToolsResponse with detailed tool information
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
client.list_tools_tools_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">get_tool_tools_tool_name_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get detailed information about a specific tool.

This endpoint returns comprehensive information about a single tool including:
- Tool metadata (name, description, icon)
- Input schema
- Labels and categorization

Args:
    request: The FastAPI request
    tool_name: The name of the tool to retrieve

Returns:
    ToolDetails with comprehensive tool information

Raises:
    HTTPException: 404 if tool not found, 403 if not available
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
client.get_tool_tools_tool_name_get(
    tool_name="tool_name",
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

**tool_name:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">execute_tool_tools_tool_name_execute_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a specific tool.

This endpoint delegates to the Tool domain API which handles:
- Tool authorization
- Tool discovery from all sources
- Context injection
- Tool execution

Args:
    request: The FastAPI request
    tool_name: The name of the tool to execute (from path parameter)
    body: The tool execution request body

Returns:
    ExecuteToolResponse with execution result or error
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
client.execute_tool_tools_tool_name_execute_post(
    tool_name="tool_name",
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

**tool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**input_data:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Input data for the tool execution
    
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
    session_id="session_id",
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

**session_id:** `str` 
    
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
    session_id="session_id",
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

**agent_image:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">get_drive_drive_get</a>()</code></summary>
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
client.get_drive_drive_get()

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

<details><summary><code>client.<a href="src/scoutos/client.py">get_drive_file_drive_files_file_name_get</a>(...)</code></summary>
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
client.get_drive_file_drive_files_file_name_get(
    file_name="file_name",
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

**file_name:** `str` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">upload_files_to_drive_drive_files_post</a>(...)</code></summary>
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
client.upload_files_to_drive_drive_files_post()

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

<details><summary><code>client.<a href="src/scoutos/client.py">create_drive_crawl_drive_crawls_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Since we do not have domain apis for collections we have to import
the route functions and pass the request through.

We could get the org key and move this logic to the drive domain api
but we would then need to get the org secret key to make http requests
since importing into the drive domain api would cause circular dependencies.
Which then forces us to use network requests via scout sdk or httpx.

This is the lesser evil I.M.O.
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
from scoutos import Scout, SourceSyncGoogleDriveSettings

client = Scout(
    api_key="YOUR_API_KEY",
)
client.create_drive_crawl_drive_crawls_post(
    source_sync_settings=SourceSyncGoogleDriveSettings(),
    url="url",
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

**source_sync_settings:** `SrcAppHttpRoutesDriveCreateDriveCrawlPayloadSourceSyncSettings` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[Schedule]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">grant_access_drive_grant_post</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from scoutos import Resource, Scout

client = Scout(
    api_key="YOUR_API_KEY",
)
client.grant_access_drive_grant_post(
    agent_ids=["agent_ids"],
    resources=[
        Resource(
            resource_id="resource_id",
            resource_type="tables",
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

**agent_ids:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**resources:** `typing.Sequence[Resource]` 
    
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

<details><summary><code>client.<a href="src/scoutos/client.py">revoke_access_drive_revoke_post</a>(...)</code></summary>
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
client.revoke_access_drive_revoke_post(
    agent_ids=["agent_ids"],
    resource_ids=["resource_ids"],
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

**agent_ids:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**resource_ids:** `typing.Sequence[str]` 
    
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
    request={"key": "value"},
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

**request:** `typing.Optional[typing.Any]` 
    
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

