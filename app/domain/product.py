from dataclasses import dataclass
import uuid

@dataclass
class Product:
    id: str
    name: str
    price: float
    category: str
    is_available: bool = True

    @staticmethod
    def create(name: str, price: float, category: str, is_available: bool = True) -> "Product":
        return Product(
            id=str(uuid.uuid4()),
            name=name,
            price=price,
            category=category,
            is_available=is_available
        )
