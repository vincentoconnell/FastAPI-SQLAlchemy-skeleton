from fastapi import APIRouter

from app.core.example_models.output import OutputExample
from app.core.example_models.input import InputExample

router = APIRouter()


@router.get("/example", tags=["example get"])
def example_get():
    return {"msg": "Test!"}


@router.post("/example", response_model=OutputExample, tags=["example post"])
def example_endpoint(inputs: InputExample):
    return {"a": inputs.a, "b": inputs.b, "result": inputs.a * inputs.b}
