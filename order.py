def get_order(order: str) -> str:
    items = {1:"Burger", 2:"Fries", 3:"Chicken", 4:"Pizza", 5:"Sandwich", 6:"Onionrings", 7:"Milkshake", 8:"Coke"}
    formated_order = []
    result = ""
    while len(order) > 1:
        if order[0:2] == "bu":
            formated_order.append("Burger")
            order = order[len("Burger"):]
        elif order[0:2] == "fr":
            formated_order.append("Fries")
            order = order[len("Fries"):]
        elif order[0:2] == "ch":
            formated_order.append("Chicken")
            order = order[len("Chicken"):]
        elif order[0:2] == "pi":
            formated_order.append("Pizza")
            order = order[len("Pizza"):]
        elif order[0:2] == "sa":
            formated_order.append("Sandwich")
            order = order[len("Sandwich"):]
        elif order[0:2] == "on":
            formated_order.append("Onionrings")
            order = order[len("Onionrings"):]
        elif order[0:2] == "mi":
            formated_order.append("Milkshake")
            order = order[len("Milkshake"):]
        elif order[0:2] == "co":
            formated_order.append("Coke")
            order = order[4:]
        else:
            order = order[1:]
    order_keys = items.keys()
    order_keys_list = []
    for i in formated_order:
        for j in order_keys:
            if items[j] == i:
                order_keys_list.append(j)
    order_keys_list.sort()
    for position in order_keys_list:
        result += items[position] + " "
    return result[:-1]

get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza")