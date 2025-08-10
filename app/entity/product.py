from datetime import datetime
from typing import Optional

from sqlmodel import (
    BigInteger,
    Column,
    DateTime,
    Field,
    ForeignKey,
    Integer,
    Relationship,
    SQLModel,
)

from app.entity.base import TimestampMixin

"""
    모든 모델을 하나의 파일에 정의할 경우:
        - 관계 테이블은 먼저 선언
        - 참조 순서 문제를 방지하기 위해 핵심 도메인 엔티티는 가장 마지막에 선언
"""


# 상품과 1:N 관계
class Category(SQLModel, table=True):
    __tablename__: str = "category"

    # 기본키 ID - BigInteger, 자동 증가
    id: int | None = Field(
        sa_column=Column(BigInteger, primary_key=True, autoincrement=True), default=None
    )

    # 고유한 코드 (nullable)
    code: str | None = Field(default=None, max_length=255, unique=True)

    # 카테고리 이름
    name: str | None = Field(default=None, max_length=255)

    # 관계: 하나의 카테고리는 여러 개의 상품을 가질 수 있음
    products: list["Product"] = Relationship(back_populates="category")


# 상품과 1:N 관계
class Provider(TimestampMixin, SQLModel, table=True):
    __tablename__: str = "provider"

    id: int | None = Field(
        sa_column=Column(BigInteger, primary_key=True, autoincrement=True), default=None
    )

    # 공급자 이름
    name: str | None = Field(default=None, max_length=255)

    # 관계: 하나의 공급자는 여러 개의 상품을 공급할 수 있음
    products: list["Product"] = Relationship(back_populates="provider")


# 다대다 관계 테이블: Producer - Product
# Producer 입장에서 관계 연결
class ProducerProducts(SQLModel, table=True):
    __tablename__: str = "producer_products"

    # 복합 기본키로 구성
    producer_id: int = Field(
        sa_column=Column(BigInteger, ForeignKey("producer.id"), primary_key=True)
    )
    products_num: int = Field(
        sa_column=Column(BigInteger, ForeignKey("product.num"), primary_key=True)
    )


# 다대다 관계 테이블: Product - Producer
# Product 입장에서 관계 연결
class ProductProducers(SQLModel, table=True):
    __tablename__: str = "product_producers"

    # 복합 기본키로 구성
    product_num: int | None = Field(
        sa_column=Column(BigInteger, ForeignKey("product.num"), primary_key=True)
    )
    producers_id: int | None = Field(
        sa_column=Column(BigInteger, ForeignKey("producer.id"), primary_key=True)
    )


# 생산자 모델 - 상품과 N:N 관계
class Producer(TimestampMixin, SQLModel, table=True):
    __tablename__: str = "producer"

    id: int | None = Field(
        sa_column=Column(BigInteger, primary_key=True, autoincrement=True), default=None
    )
    # 생산자 코드 및 이름
    code: str | None = Field(default=None, max_length=255)
    name: str | None = Field(default=None, max_length=255)

    # 관계: 생산자 하나는 여러 상품을 생산할 수 있음 (다대다 관계)
    products: list["Product"] = Relationship(
        back_populates="producers",
        link_model=ProducerProducts,  # 다대다 관계 테이블
    )


# 상품 모델 - 중심 엔티티
class Product(TimestampMixin, SQLModel, table=True):
    __tablename__: str = "product"

    # 기본키 - 상품 번호 (num)
    num: int | None = Field(
        sa_column=Column(BigInteger, primary_key=True, autoincrement=True), default=None
    )

    # 필수 필드: 상품 이름, 가격, 재고
    name: str = Field(max_length=255)
    price: int = Field(sa_column=Column(Integer))
    stock: int = Field(sa_column=Column(Integer))

    # 외래키: 카테고리, 공급자
    category_id: int | None = Field(
        sa_column=Column(BigInteger, ForeignKey("category.id")), default=None
    )
    provider_id: int | None = Field(
        sa_column=Column(BigInteger, ForeignKey("provider.id")), default=None
    )

    # 관계 설정
    category: Category | None = Relationship(back_populates="products")
    provider: Provider | None = Relationship(back_populates="products")

    # 1:1 관계 - 상품 상세 정보
    product_detail: Optional["ProductDetail"] = Relationship(back_populates="product")

    # 다대다 관계 - 여러 생산자와 연결됨
    producers: list[Producer] = Relationship(
        back_populates="products",
        link_model=ProductProducers,  # 연결 테이블 명시
    )


# 상품 상세 모델 - Product와 1:1 관계
class ProductDetail(SQLModel, table=True):
    __tablename__: str = "product_detail"

    id: int | None = Field(
        sa_column=Column(BigInteger, primary_key=True, autoincrement=True), default=None
    )

    # 상품 번호 - 유일하며 Product와 1:1 매핑
    product_number: int = Field(
        sa_column=Column(BigInteger, ForeignKey("product.num"), unique=True)
    )

    # 상세 설명
    description: str | None = Field(default=None, max_length=255)

    created_at: datetime | None = Field(sa_column=Column(DateTime()), default=None)
    updated_at: datetime | None = Field(sa_column=Column(DateTime()), default=None)

    # 관계: 상품 상세는 하나의 상품에만 속함
    product: Product | None = Relationship(back_populates="product_detail")
