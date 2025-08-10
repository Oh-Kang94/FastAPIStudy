from pydantic import BaseModel, ConfigDict


class SignIn:
    class Request(BaseModel):
        id: str
        password: str

        model_config = ConfigDict(
            title="SignIn.Request",
            json_schema_extra={"examples": [{"id": "admin", "password": "adminPw"}]},
        )
