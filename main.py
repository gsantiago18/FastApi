from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    editorial: str
    is_offer: bool

app = FastAPI()

itemsbd = []

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/newitem/")
async def create_item(item: Item):
    itemsbd.append(item)
    return f"Item creado con el id {item.id} y el nombre: {item.name}"


@app.put("/itemsupd/{item_id}")
async def update_item(item_id: int, item: Item):
    if not item.is_offer:
        return {"error": "El item no es una oferta"}
    if not item.editorial:
        return {"error": "El item no tiene editorial"}
    
    return f"Item con id {item_id} actualizado con el nombre {item.name}"


@app.get("/allitems/")
async def get_all_items():
    return {"items": itemsbd}


@app.delete("/itemdelete/{item_id}")
async def delete_item(item_id: int):
    for item in itemsbd:
        if item.id == item_id:
            itemsbd.remove(item)
            return f"Item con id {item_id} eliminado con exito"
        
    return {"error": "Item no encontrado"}
    