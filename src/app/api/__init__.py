from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.datastructures import QueryParams

from app.services import determine_field_type, find_matching_template


class GetFormResponse(BaseModel):
    name: str


def setup_views(api: FastAPI):
    @api.post("/get_form")
    async def get_form(request: Request) -> GetFormResponse | dict:
        fields = {}
        data = await request.body()
        for key, value in QueryParams(data).items():
            fields[key] = determine_field_type(value)
        matching_template = find_matching_template(fields)
        if matching_template:
            return GetFormResponse(name=matching_template.name)
        return fields
