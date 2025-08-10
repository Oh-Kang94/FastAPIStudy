import enum

from sqlalchemy import BigInteger, Column, ForeignKey, String
from sqlmodel import Enum, Field, Relationship, SQLModel


class Roles(enum.Enum):
    ADMIN = "ROLE_ADMIN"
    USER = "ROLE_USER"


class User(SQLModel, table=True):
    __tablename__: str = "user"

    id: int | None = Field(
        sa_column=Column(BigInteger, primary_key=True, autoincrement=True), default=None
    )
    uid: str = Field(String, unique=True)
    name: str = Field(String, max_length=255)
    password: str = Field(String, max_length=255)

    # Relationship to UserRole
    user_roles: list["UserRole"] = Relationship(back_populates="user")


class UserRole(SQLModel, table=True):
    __tablename__: str = "user_roles"

    user_id: int = Field(
        sa_column=Column(BigInteger, ForeignKey("user.id"), primary_key=True)
    )
    roles: Roles = Field(sa_column=Column(type_=Enum(Roles), default=Roles.ADMIN))

    # Relationship to User
    user: User | None = Relationship(back_populates="user_roles")
