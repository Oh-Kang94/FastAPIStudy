from pydantic import BaseModel, ConfigDict

from app.entity.user import User


class SignUp:
    class Request(BaseModel):
        id: str
        name: str
        password: str

        model_config = ConfigDict(
            title="SignUp.Request",
            json_schema_extra={
                "examples": [{"id": "admin", "name": "admin", "password": "adminPw"}]
            },
        )

        def toEntity(self) -> User:
            return User(uid=self.id, name=self.name, password=self.password)
