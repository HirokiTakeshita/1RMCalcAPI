from fastapi import FastAPI


one_repetition_maximum_calc_api = FastAPI()


@one_repetition_maximum_calc_api.get("/")
def root():
    return "Hello World!"
