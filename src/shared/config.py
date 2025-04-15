import logging

logger = logging.getLogger("uvicorn")


swagger_config = {
    "title": "Contracts API",
    "description": "Simple API for managing contracts.",
    "summary": "This API allows performing CRUD operations on contracts and parties to manage contractual agreements.",
    "version": "0.0.1",
    "contact": {
        "name": "Marcel Fox",
        "url": "https://marcelfox.com",
        "email": "marcelfox@live.com",
    },
    "license_info": {
        "name": "MIT",
        "url": "https://mit-license.org/",
    },
    "swagger_ui_parameters": {"syntaxHighlight.theme": "obsidian"},
}

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "tenant": "d86c3676220f4775acb15b0b403869ea",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "tenant": "d86c3676220f4775acb15b0b403869ea",
        "disabled": True,
    },
}
