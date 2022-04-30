"""Define data models."""
from pydantic import BaseModel, Field


class RootResponseBodySchema(BaseModel):
    """`root` endpoint response body JSON schema."""

    message: str = Field(None, example="Hello World!")


class CalcOneRepMaxRequestBodySchema(BaseModel):
    """`calc_1rm` endpoint request body JSON schema."""

    weight: float = Field(
        None,
        gt=0,
        le=2000,
        title="Weight",
        description=("Weight must be greater than 0 and "
                     "less than or equal to 2000."),
    )
    reps: int = Field(
        None,
        gt=0,
        le=20,
        title="Reps",
        description=("Reps must be greater than 0 and "
                     "less than or equal to 20."),
    )

    class Config:
        """Set example values."""

        schema_extra = {"example": {"weight": 52.5, "reps": 10}}


class WeightAtEachPercentageOfOneRepMax(BaseModel):
    """Weight corresponding to each percentage of 1RM."""

    percentage: int
    weight: int


class CalcOneRepMaxResponseBodySchema(BaseModel):
    """`calc_1rm` endpoint response body JSON schema."""

    one_rep_max: int = Field(
        None,
        title="1RM",
        description="Return the calculated 1RM."
    )
    weights: list[WeightAtEachPercentageOfOneRepMax] = Field(
        None,
        title="Weights",
        description="Return weights (each percentage of 1RM)."
    )

    class Config:
        """Set example values."""

        schema_extra = {
            "example": {
                "one_rep_max": 70,
                "weights": [
                    {"percentage": 95, "weight": 67},
                    {"percentage": 90, "weight": 63},
                    {"percentage": 85, "weight": 60},
                    {"percentage": 80, "weight": 56},
                    {"percentage": 75, "weight": 53},
                    {"percentage": 70, "weight": 49},
                    {"percentage": 65, "weight": 46},
                    {"percentage": 60, "weight": 42},
                    {"percentage": 55, "weight": 39},
                    {"percentage": 50, "weight": 35},
                    {"percentage": 45, "weight": 32},
                    {"percentage": 40, "weight": 28},
                    {"percentage": 35, "weight": 25},
                    {"percentage": 30, "weight": 21},
                    {"percentage": 25, "weight": 18},
                    {"percentage": 20, "weight": 14},
                ],
            }
        }
