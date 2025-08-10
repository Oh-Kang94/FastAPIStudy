from sqlmodel import Session, select

from app.entity.product import Product


class ProductRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Product]:
        return list(self.session.exec(select(Product)))

    def get_by_num(self, num: int) -> Product | None:
        return self.session.exec(select(Product).where(Product.num == num)).first()

    def create(self, product: Product) -> Product:
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product

    def update(self, product: Product) -> Product:
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product

    def delete(self, product: Product) -> None:
        self.session.delete(product)
        self.session.commit()
