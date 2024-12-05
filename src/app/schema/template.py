from pydantic import BaseModel


class Template(BaseModel):
    id: str
    name: str
    fields: dict[str, str]
