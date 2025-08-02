from pydantic import BaseModel, ConfigDict


class SignIn:

    class Request(BaseModel):
        name: str
        password: str

        model_config = ConfigDict(
            title="SignIn.Request",
            json_schema_extra={
                "examples": [
                    {
                        "name": "admin",
                        "password": "adminPw"
                    }
                ]
            },
        )
