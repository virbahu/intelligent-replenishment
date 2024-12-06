import numpy as np
def calculate_smart_replenish(sku_list):
    orders = []
    for sku in sku_list:
        inv = sku["on_hand"]; demand = sku["avg_daily"]; lt = sku["lead_time"]
        ss = 1.645 * sku.get("std", demand*0.2) * (lt**0.5)
        rop = demand * lt + ss
        if inv <= rop:
            qty = max(sku.get("moq", 1), round(demand * lt * 2 - inv))
            orders.append({"sku": sku["sku"], "qty": qty, "urgency": "critical" if inv < demand*lt*0.5 else "normal"})
    return orders
if __name__=="__main__":
    skus = [{"sku":"A","on_hand":50,"avg_daily":15,"std":4,"lead_time":7,"moq":50},{"sku":"B","on_hand":500,"avg_daily":20,"std":6,"lead_time":14,"moq":100}]
    for o in calculate_smart_replenish(skus): print(o)
