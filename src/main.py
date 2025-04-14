"""Main module."""

from fastapi import FastAPI

from dotenv import load_dotenv
from pydantic import BaseModel


from src.schema.tenant_schema import TenantSchema
from src.schema.contracts_schema import ContractSchema
from src.controllers.tenant_controller import TenantController
from src.controllers.contract_controller import ContractController
from src.shared.plugins import load_routes_plugin


class HealthResponse(BaseModel):
    message: str = "ok"


def create_app() -> FastAPI:
    """App Factory function.

    Returns:
        FastAPI: Server Instance.
    """
    app = FastAPI()
    load_dotenv()

    # app.add_route(router)

    @app.get("/")
    async def health_check() -> HealthResponse:
        return HealthResponse(message="ok")

    @app.post("/tenant")
    async def tenant(tenant: TenantSchema) -> TenantSchema | None:
        result = await TenantController().create_tenant(tenant)
        return result

    @app.post("/contract")
    async def create_contract(contract: ContractSchema) -> ContractSchema | None:
        return await ContractController().create_contract(contract)

    load_routes_plugin(app)

    return app


app = create_app()
