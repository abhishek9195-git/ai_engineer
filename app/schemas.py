from pydantic import BaseModel, Field
from enum import Enum 


class ShipmentStatus(str, Enum):
    placed = "Placed"
    in_transit = "In Transit"
    out_for_delivery = "Out for delivery"
    delivered = "Delivered"

class BaseShipment(BaseModel):
    title: str = Field(max_length=30, description="Title of the shipment")
    price: float = Field(gt=0, lt=100000)
    currency: str = Field(default='INR')

class ShipmentRead(BaseShipment):
    status: ShipmentStatus

class ShipmentCreate(BaseShipment):
    pass

class ShipmentUpdate(BaseModel):
    status: ShipmentStatus # intentionally, Only status should be updated