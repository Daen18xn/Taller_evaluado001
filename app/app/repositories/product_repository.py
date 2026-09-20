from typing import List, Optional
from app.domain.product import Product

class ProductRepository:
    def __init__(self):
        self._products: dict[str, Product] = {}

    def save(self, product: Product) -> Product:
        self._products[product.id] = product
        return product

    def find_by_id(self, product_id: str) -> Optional[Product]:
        return self._products.get(product_id)

    def find_all(self) -> List[Product]:
        return list(self._products.values())

    def update(self, product: Product) -> Product:
        self._products[product.id] = product
        return product

    def delete(self, product_id: str) -> bool:
        if product_id in self._products:
            del self._products[product_id]
            return True
        return False
