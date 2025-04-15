## Swagger

<br />

## Health Check
### `GET /`
**Summary:** Health Check
**Response:**
- `200 OK`: Returns a `HealthResponse`

---

<br />

## Tenant
### `GET /tenant/{tenant_id}`
**Summary:** Get Tenant
**Path Parameters:**
- `tenant_id` (integer, required)
**Responses:**
- `200 OK`: `TenantSchema-Output` or `null`
- `422 Unprocessable Entity`: `HTTPValidationError`

<br />

### `PUT /tenant/{tenant_id}`
**Summary:** Update Tenant
**Path Parameters:**
- `tenant_id` (integer, required)
**Request Body:** `TenantSchema-Input`
**Responses:**
- `200 OK`: `TenantSchema-Output` or `null`
- `422 Unprocessable Entity`: `HTTPValidationError`

<br />

### `DELETE /tenant/{tenant_id}`
**Summary:** Delete Tenant
**Path Parameters:**
- `tenant_id` (integer, required)
**Responses:**
- `200 OK`: Generic response
- `422 Unprocessable Entity`: `HTTPValidationError`


<br />

### `POST /tenant/`
**Summary:** Create Tenant
**Request Body:** `TenantSchema-Input`
**Responses:**
- `200 OK`: `TenantSchema-Output`
- `422 Unprocessable Entity`: `HTTPValidationError`

---

<br />

## Pulse
### `POST /pulse/`
**Summary:** Save Pulse
**Request Body:** `PulseSchema`
**Responses:**
- `200 OK`: `UsageSchema`
- `422 Unprocessable Entity`: `HTTPValidationError`

---

<br />

## Usage
### `GET /usage/{usage_id}`
**Summary:** Get Usage
**Path Parameters:**
- `usage_id` (integer, required)
**Responses:**
- `200 OK`: `UsageSchema` or `null`
- `422 Unprocessable Entity`: `HTTPValidationError`

<br />

### `PUT /usage/{usage_id}`
**Summary:** Update Usage
**Path Parameters:**
- `usage_id` (integer, required)
**Request Body:** `UsageSchema`
**Responses:**
- `200 OK`: `UsageSchema`
- `422 Unprocessable Entity`: `HTTPValidationError`

<br />

### `DELETE /usage/{usage_id}`
**Summary:** Delete Usage
**Path Parameters:**
- `usage_id` (integer, required)
**Responses:**
- `200 OK`: Generic response
- `422 Unprocessable Entity`: `HTTPValidationError`

<br />

### `POST /usage/`
**Summary:** Create Usage
**Request Body:** `UsageSchema`
**Responses:**
- `200 OK`: `UsageSchema`
- `422 Unprocessable Entity`: `HTTPValidationError`

---

<br />

## Contract
### `GET /contract/{contract_id}`
**Summary:** Get Contract
**Query Parameters:**
- `id` (integer, required)
**Responses:**
- `200 OK`: `ContractResponseSchema` or `null`
- `422 Unprocessable Entity`: `HTTPValidationError`

<br />

### `PUT /contract/{contract_id}`
**Summary:** Update Contract
**Path Parameters:**
- `contract_id` (integer, required)
**Request Body:** `ContractSchema`
**Responses:**
- `200 OK`: `ContractResponseSchema` or `null`
- `422 Unprocessable Entity`: `HTTPValidationError`

<br />

### `DELETE /contract/{contract_id}`
**Summary:** Delete Contract
**Path Parameters:**
- `contract_id` (integer, required)
**Responses:**
- `200 OK`: Generic response
- `422 Unprocessable Entity`: `HTTPValidationError`

<br />

### `POST /contract/`
**Summary:** Create Contract
**Request Body:** `ContractSchema`
**Responses:**
- `200 OK`: `ContractResponseSchema`
- `422 Unprocessable Entity`: `HTTPValidationError`

---

<br />

## Schemas

### HealthResponse
- `message`: string

<br />

### PulseSchema
- `tenant`: string
- `product_sku`: string
- `used_amount`: number
- `use_unit`: string

<br />

### UsageSchema
- `id`: integer or null
- `total_usage`: number
- `total_amount`: number
- `invoice_value`: number
- `paid`: boolean or null
- `info`: string or null
- `created_at`: datetime or null
- `updated_at`: datetime or null

<br />

### TenantSchema (Input/Output)
- `id`: integer or null
- `tenant_id`: string or null
- `email`: string
- `contract_id`: integer or null
- `created_at`: datetime or null
- `updated_at`: datetime or null
- `contract`: `ContractResponseSchema` or null

<br />

### ContractSchema
- `id`: integer or null
- `sku`: `SkuEnum`
- `rate`: number
- `unit`: number
- `price`: number
- `usage_id`: integer or null
- `effective_date`: datetime
- `created_at`: datetime or null
- `updated_at`: datetime or null

<br />

### ContractResponseSchema
- `id`: integer
- `sku`: `SkuEnum`
- `rate`: number
- `unit`: number
- `price`: number
- `effective_date`: datetime
- `usage`: `UsageSchema`
- `created_at`: datetime or null
- `updated_at`: datetime or null

<br />

### SkuEnum
- `memory`, `cpu`, `storage`

<br />

### HTTPValidationError
- `detail`: list of `ValidationError`

<br />

### ValidationError
- `loc`: list of strings or integers
- `msg`: string
- `type`: string

[Return to README](../README.md)
