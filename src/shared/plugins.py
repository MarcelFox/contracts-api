import importlib
from pathlib import Path

from fastapi import FastAPI

from src.shared.config import logger


def load_routes_plugin(app: FastAPI):
    """Dynamically load routes for each domain under app.
    Router files must be named as 'src/app/DOMAIN/routes.py'.

    Args:
        app (FastAPI): FastAPI main instance.
    """
    base_path = Path("src/routes")

    for route_file in base_path.rglob("*_route.py"):
        module_path = route_file.relative_to(base_path).with_suffix("").as_posix()
        module_name = f"src.routes.{module_path.replace('/', '.')}"
        file_name = f"/{module_path.split('/')[0]}"
        prefix = file_name.split('_')[0]

        try:
            module = importlib.import_module(module_name)
            try:
                if hasattr(module, "router"):
                    logger.info(f"Loading routes from module '{module_name}'")
                    app.include_router(module.router, prefix=prefix, tags=[prefix])
                else:
                    logger.warn(f"Module {module_name} does not have a 'router' attribute.")
            except Exception as e:
                logger.error(f"Error loading routes from module '{module_name}': {e}")
        except ModuleNotFoundError:
            logger.error(f"Module {module_name} not found.")
