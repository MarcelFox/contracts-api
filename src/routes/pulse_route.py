from fastapi import APIRouter

from src.controllers.pulse_controller import PulseController
from src.schema.pulse_schema import PulseSchema
from src.schema.usage_schema import UsageSchema
from src.shared.config import logger

router = APIRouter()


@router.post("/")
async def save_pulse(pulse: PulseSchema) -> UsageSchema:
    logger.info(f"Pulse -> {pulse}")
    return await PulseController().save_pulse(pulse)
