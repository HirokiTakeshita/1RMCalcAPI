"""Create a FastAPI instance."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import calc_1rm, root


one_repetition_maximum_calc_api = FastAPI()

origins = [
    "http://localhost:3000",
]

one_repetition_maximum_calc_api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

one_repetition_maximum_calc_api.include_router(root.router)
one_repetition_maximum_calc_api.include_router(calc_1rm.router)
