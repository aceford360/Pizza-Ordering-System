menu = ["1: Cheese","2: Pepperoni","3: Hawaiian","4: Meat Lovers",
"5: Margherita","6: Vegetarian","7: Cheesy Garlic","8: Garlic Prawn",
"9: Mushroom Supreme","10: BBQ Chicken ","11: Meat Lovers Surpreme","12: Chicken Fajita",""
]
pizza_cost = ["$8.50","$8.50","$8.50","$8.50","$8.50","$8.50","$13.50","$13.50","$13.50","$13.50","$13.50","$13.50",""
]

#prints pizza menu
print("Pizza menu:")
res = "\n".join("{} {}".format(x, y) for x, y in zip(menu, pizza_cost))
print(res)

