from sqlmodel import Session

from app.entity.product import Product
from app.infrastructure.persistence.product import ProductRepository
from app.presentation.common.common_response import NotFoundResourceException


class ProductService:
    def __init__(self, session: Session):
        self.repo = ProductRepository(session)

    def get_products(self) -> list[Product]:
        return self.repo.get_all()

    def get_product(self, num: int) -> Product:
        product = self.repo.get_by_num(num)
        if not product:
            raise NotFoundResourceException(id=num)
        return product

    def create_product(
        self,
        name: str,
        price: int,
        stock: int,
        category_id: int | None = None,
        provider_id: int | None = None,
    ) -> Product:
        new_product = Product(
            name=name,
            price=price,
            stock=stock,
            category_id=category_id,
            provider_id=provider_id,
        )
        return self.repo.create(new_product)

    def update_product(self, num: int, **kwargs) -> Product:
        product = self.get_product(num)
        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)
        return self.repo.update(product)

    def delete_product(self, num: int) -> None:
        product = self.get_product(num)
        self.repo.delete(product)
