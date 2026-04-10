import random
from typing import List, Dict


def compute_recommendations(order_id: str) -> List[Dict]:
    # Mock “AI”‑style recommendations
    return [
        {
            "product_id": f"rec-{i:03d}",
            "score": round(random.uniform(0.5, 0.99), 3),
            "reason": "co‑purchased",
        }
        for i in range(5)
    ]
