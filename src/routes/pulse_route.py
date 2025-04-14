from fastapi import APIRouter

from src.schema.pulse_schema import PulseSchema
from src.controllers.pulse_controller import PulseController
from src.schema.usage_schema import UsageSchema
from src.shared.config import logger

router = APIRouter()

@router.post("/")
async def save_pulse(pulse: PulseSchema) -> UsageSchema | None:
    logger.info(f"Pulse -> {pulse}")
    result = await PulseController().save_pulse(pulse)
    # logger.info(f"Pulse saved with ID: {result}")
    return result
