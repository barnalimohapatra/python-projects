from fastapi import FastAPI, HTTPException
from typing import List, Dict

app = FastAPI(title="E-Commerce Catalog Service")


# Load products only once at startup
from async_service.loaders.product_loader import load_products

all_products = load_products()
product_map = {p["product_id"]: p for p in all_products}


@app.get("/")
async def root():
    return {"message": "E-Commerce Catalog Service"}


@app.get("/products", response_model=List[Dict])
async def get_all_products() -> List[Dict]:
    return all_products


@app.get("/products/batch")
async def get_product_batches(batch_size: int = 5):
    from async_service.utils.generators import batch_generator

    products = load_products()
    batches = list(batch_generator(products, batch_size))
    return {"batch_size": batch_size, "batches": batches}


@app.get("/orders/{order_id}/recommendations")
async def get_recommendations(order_id: str):
    from async_service.utils.recommenders import compute_recommendations

    recs = compute_recommendations(order_id)
    return {"order_id": order_id, "recommendations": recs}


@app.get("/products/{product_id}", response_model=Dict)
async def get_product_by_id(product_id: str) -> Dict:
    product = product_map.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

