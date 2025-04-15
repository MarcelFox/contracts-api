# Contracts API

**Version**: 0.0.1

**License**: [MIT](https://mit-license.org/)

**Author**: [Marcel Fox](https://marcelfox.com)

**Contact**: [marcelfox@live.com](mailto:marcelfox@live.com)

<br />

## Description

Contracts API is a RESTful web service for managing contractual agreements and associated parties. It supports Create, Read, Update, and Delete (CRUD) operations on contracts and parties.

<br />

## Summary

This API allows performing CRUD operations on contracts and parties to manage contractual agreements.

<br />

## API Documentation

Interactive documentation is available at runtime:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

<br />

## Installation

<br />

### Prerequisites

- Python 3.11 or higher
- Docker (optional)

<br />

### Dependencies

All dependencies are listed in `requirements.txt`. Key libraries include:

- `fastapi`: Web framework for building APIs
- `uvicorn`: ASGI server for running FastAPI apps
- `sqlalchemy`: SQL toolkit and ORM
- `asyncpg`: PostgreSQL driver with async support
- `alembic`: Database migrations
- `pydantic`: Data validation and settings management
- `python-dotenv`: Environment variable management
- `email-validator`: Email format validation
- `rich`: CLI output formatting
- `typer`: CLI app builder
- `httpx`, `httptools`, `starlette`, `watchfiles`, `websockets`: Supporting async HTTP and server components

Full list is available in `requirements.txt`.

<br />

## Usage

The project can be executed using `make` commands. Ensure `make` is installed on your system.

<br />

### Run the application locally

```bash
make run
```

<br />

### Run the application using Docker

```bash
make run:docker
```

<br />

#### running docker dev mode

```bash
make run:docker-dev
```
<br />

## Docs

- [List of endpoints](docs/SWAGGER.md)
