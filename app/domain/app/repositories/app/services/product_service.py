from typing import List, Optional
from app.domain.product import Product
from app.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    def create_product(self, name: str, price: float, category: str, is_available: bool = True) -> Product:
        product = Product.create(name=name, price=price, category=category, is_available=is_available)
        return self.product_repo.save(product)

    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        return self.product_repo.find_by_id(product_id)

    def get_products(
        self, 
        category: Optional[str] = None, 
        order_by: Optional[str] = None, 
        direction: str = "asc", 
        page: int = 1, 
        limit: int = 10
    ) -> List[Product]:
        products = self.product_repo.find_all()

        
        if category:
            products = [p for p in products if p.category.lower() == category.lower()]

        
        if order_by and hasattr(Product, order_by):
            reverse = True if direction.lower() == "desc" else False
            products = sorted(products, key=lambda x: getattr(x, order_by), reverse=reverse)

        
        start = (page - 1) * limit
        end = start + limit
        return products[start:end]
