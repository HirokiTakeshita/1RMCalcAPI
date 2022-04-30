"""Define 'calc_1rm' API endpoint."""
from typing import Generator, Union

from fastapi import APIRouter, HTTPException, status

from api.models import calculators, schemas


router = APIRouter()


@router.post("/api/v1/calc_1rm",
             response_model=schemas.CalcOneRepMaxResponseBodySchema)
async def calc_one_rep_max(
    data: schemas.CalcOneRepMaxRequestBodySchema,
) -> dict[str, Union[int, Generator[dict[str, int], None, None]]]:
    """Request weight & reps and returns calculated 1RM & weights
       (each percentage of 1RM: 95% -> 20%, 5% intervals)."""
    if data.weight is None or data.reps is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Both weight and reps are required."
        )
    calculator = calculators.OneRepMaxCalculator()
    one_rep_max = calculator.get_one_rep_max_from_weight_and_reps(
        data.weight, data.reps
    )
    weights = calculator.get_weights_from_each_percentage_of_1rm(one_rep_max)
    return {"one_rep_max": one_rep_max, "weights": weights}
