# Token API Endpoints

## POST /token/
**Summary:** Login
**Operation ID:** `login_token__post`

### Request Body Schema: `Body_login_token__post`
| Field          | Type   | Required | Description                         |
|----------------|--------|----------|-------------------------------------|
| grant_type     | string | No       | Must match pattern `^password$`     |
| username       | string | Yes      | Username for login                  |
| password       | string | Yes      | Password for login                  |
| scope          | string | No       | Scope of access (default: `""`)     |
| client_id      | string | No       | Optional client identifier          |
| client_secret  | string | No       | Optional client secret              |

### Responses
- **200**: Successful Response
- **422**: Validation Error

---

## GET /token/hello
**Summary:** Hello
**Operation ID:** `hello_token_hello_get`

### Responses
- **200**: Successful Response (string)

---

## Security Scheme

### OAuth2PasswordBearer
- **Type:** `oauth2`
- **Flow:** `password`
- **Token URL:** `/token`
