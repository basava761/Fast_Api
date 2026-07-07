from fastapi import FastAPI

app = FastAPI()

# Path + Query parameters
@app.get("/users/{user_id}")
def get_user(user_id: int, active: bool = True, role: str = "member"):
    return {
        "user_id": user_id,
        "active": active,
        "role": role
    }

# Multiple query parameters
@app.get("/search")
def search_items(q: str = None, category: str = None, limit: int = 10):
    return {
        "query": q,
        "category": category,
        "limit": limit
    }

# Multiple path parameters
@app.get("/orders/{order_id}/items/{item_id}")
def get_order_item(order_id: int, item_id: int, detail: bool = False):
    return {
        "order_id": order_id,
        "item_id": item_id,
        "detail": detail
    }
