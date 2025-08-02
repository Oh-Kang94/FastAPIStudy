from pydantic import BaseModel, ConfigDict


class SignUp:

    class Request(BaseModel):
        name: str
        password: str

        model_config = ConfigDict(
            title="SignUp.Request",
            json_schema_extra={
                "examples": [
                    {
                        "name": "admin",
                        "password": "adminPw"
                    }
                ]
            },
        )
