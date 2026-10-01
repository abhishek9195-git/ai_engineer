from typing import Any

from fastapi import FastAPI, HTTPException, status

from .schemas import ShipmentRead, ShipmentCreate, ShipmentStatus, ShipmentUpdate
from .database import shipments, save
app = FastAPI()


# === GET ALL

# === GET BY ID
@app.get('/shipping', response_model=ShipmentRead)
def get_by_id(id: int):
    if id not in shipments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    shipment = shipments[id]
    return shipment
    # return Shipment(**shipment)


# === CREATE
@app.post('/shipping')
def create(shipment: ShipmentCreate) -> dict[str, int]:
   
    new_id = max(shipments.keys()) + 1
    shipments[new_id] = {
        'id': new_id,
        **shipment.model_dump(),
        'status': ShipmentStatus.placed
    }
    save()
    return {'id': new_id}


# === UPDATE
@app.put('/shipping')
def update(id: int, title: str, price: int, currency: str) -> dict[str, Any]:
    shipments[id] = {
        'title': title,
        'price': price,
        'currency': currency
    }
    save()
    return shipments[id]


# === PATCH
@app.patch("/shipping", response_model = ShipmentRead)
def update_shipment(id: int, body: ShipmentUpdate):
    shipments[id].update(body)
    save()
    return shipments[id]


# === DELETE
@app.delete("/{id}")
def delete (id: int) -> dict[str, str]:
    shipments.pop(id)
    return {'detail': f"Shipment with id #{id} is deleted successfully."}