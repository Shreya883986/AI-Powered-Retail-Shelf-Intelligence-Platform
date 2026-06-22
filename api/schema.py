from pydantic import BaseModel


class DemandInput(BaseModel):
    expected_stock: int
    actual_stock: int
    sales_amount: float


class StockInput(BaseModel):
    expected_stock: int
    quantity_sold: int
    sales_amount: float