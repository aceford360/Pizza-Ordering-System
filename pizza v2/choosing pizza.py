menu = ["1: Cheese","2: Pepperoni","3: Hawaiian","4: Meat Lovers",
"5: Margherita","6: Vegetarian","7: Cheesy Garlic","8: Garlic Prawn",
"9: Mushroom Supreme","10: BBQ Chicken ","11: Meat Lovers Surpreme","12: Chicken Fajita",""
]
pizza_cost = ["$8.50","$8.50","$8.50","$8.50","$8.50","$8.50","$13.50","$13.50","$13.50","$13.50","$13.50","$13.50",""
]
toppings = ["1: Pepperoni", "2: Mushrooms", "3: Extra Cheese", "4: Onions", "5: Anchovies", "6: Olives", "7: Ham", "8: Bell Peppers"]

toppings_cost = ["$0.50","$0.50","$0.50","$0.50","$0.50","$0.50","$0.50","$0.50",""]

chosen = []

total_cost = []


# if user picks either 0 or more than 5, try again.
def choosing_pizza(question):
  error = "Please enter a number between 1 and 5."

  valid = False
  while not valid:

    try:
      response=int(input(question))

      if  1<= response <=5:
        print("-----------------------------------------------------------------")
        #prints menu
        print("Pizza Menu:")
        res = "\n".join("{} {}".format(x, y) for x, y in zip(menu, pizza_cost))
        print(res)
       
        for i in range(response):
          #repeats question based on previous input from user
          pizza = input("What pizza would you like? (choose from 1-12): ")
          if pizza == "1" or pizza == "2" or pizza == "3" or pizza == "4" or pizza == "5" or pizza == "6" or pizza == "7":
            total_cost.append(8.50) #adds price to total
            chosen.append(pizza)
            chosen.append("$8.50")#adds to list so that it can be shown in the reciept
            print("You have chosen:",(chosen))
            print("-----------------------------------------------------------------")
            #user can have toppings on their pizzas if they choose to
            optional_toppings = input("Would you like some toppings on your pizza? They cost $0.50: ")
            if optional_toppings == "yes" or optional_toppings == "Yes" or optional_toppings == "Y" or optional_toppings == "y":
              
              #prints toppings menu
              print("-----------------------------------------------------------------")
              print("Toppings:")
              res = "\n".join("{} {}".format(x, y) for x, y in zip(toppings, toppings_cost))
              print(res)

              #allows users to choose toppings from list
              choose_toppings = input("What toppings would you like? (choose a number from 1-8): ")

              if choose_toppings == "1":

                total_cost.append(0.50)
                chosen.append("w/ pepperoni")
                chosen.append("$0.50")
                print("You've chosen:",chosen)
                print("-----------------------------------------------------------------")

              elif choose_toppings =="2":
                total_cost.append(0.50)
                chosen.append("w/ mushrooms") 
                chosen.append("$0.50")
                print("You've chosen:",chosen)
                print("-----------------------------------------------------------------")#chosen toppings
              elif choose_toppings =="3":
                total_cost.append(0.50)
                chosen.append("w/ extra cheese")
                chosen.append("$0.50")
                print("You've chosen:",chosen)
                print("-----------------------------------------------------------------")
              elif choose_toppings =="4":
                total_cost.append(0.50)
                chosen.append("w/ onions")
                chosen.append("$0.50")
                print("You've chosen:",chosen)
                print("-----------------------------------------------------------------")
              elif choose_toppings =="5":
                total_cost.append(0.50)
                chosen.append("w/ anchovies")
                chosen.append("$0.50")
                print("You've chosen:",chosen)
                print("-----------------------------------------------------------------")
              elif choose_toppings =="6":
                total_cost.append(0.50)
                chosen.append("w/ olives")
                chosen.append("$0.50")
                print("You've chosen:",chosen)
                print("-----------------------------------------------------------------")
              elif choose_toppings =="7":
                total_cost.append(0.50)
                chosen.append("w/ ham")
                chosen.append("$0.50")
                print("You've chosen:",chosen)
                print("-----------------------------------------------------------------")
              elif choose_toppings =="8":
                total_cost.append(0.50)
                chosen.append("w/ bell peppers")
                chosen.append("$0.50")
                print("You've chosen:",chosen)
                print("-----------------------------------------------------------------")

                
                
              else:
                continue
                
              
                
          

          elif pizza == "8" or pizza == "9" or pizza == "10" or pizza == "11" or pizza == "12":
            total_cost.append(13.50)
            chosen.append(pizza)
            chosen.append("$13.50")
            print("You have chosen:",(chosen))
            print("-----------------------------------------------------------------")

          #user can have toppings on their pizzas if they choose to
            optional_toppings = input("Would you like some toppings on your pizza? They cost $0.50: ")
            if optional_toppings == "yes" or optional_toppings == "Yes" or optional_toppings == "Y" or optional_toppings == "y":
              
              #prints toppings menu
              print("-----------------------------------------------------------------")
              print("Toppings:")
              res = "\n".join("{} {}".format(x, y) for x, y in zip(toppings, toppings_cost))
              print(res)

              #allows users to choose toppings from list
              choose_toppings = input("What toppings would you like? (choose a number from 1-8): ")

              if choose_toppings == "1":

                total_cost.append(0.50)
                chosen.append("w/ pepperoni")
                chosen.append("$0.50")
                print("You've chosen:",chosen)
                print("-----------------------------------------------------------------")

              elif choose_toppings =="2":
                total_cost.append(0.50)
                chosen.append("w/ mushrooms") 
                chosen.append("$0.50")
                print("You've chosen:",chosen)
                print("-----------------------------------------------------------------")#chosen toppings
              elif choose_toppings =="3":
                total_cost.append(0.50)
                chosen.append("w/ extra cheese")
                chosen.append("$0.50")
                print("You've chosen:",chosen)
                print("-----------------------------------------------------------------")
              elif choose_toppings =="4":
                total_cost.append(0.50)
                chosen.append("w/ onions")
                chosen.append("$0.50")
                print("You've chosen:",chosen)
                print("-----------------------------------------------------------------")
              elif choose_toppings =="5":
                total_cost.append(0.50)
                chosen.append("w/ anchovies")
                chosen.append("$0.50")
                print("You've chosen:",chosen)
                print("-----------------------------------------------------------------")
              elif choose_toppings =="6":
                total_cost.append(0.50)
                chosen.append("w/ olives")
                chosen.append("$0.50")
                print("You've chosen:",chosen)
                print("-----------------------------------------------------------------")
              elif choose_toppings =="7":
                total_cost.append(0.50)
                chosen.append("w/ ham")
                chosen.append("$0.50")
                print("You've chosen:",chosen)
                print("-----------------------------------------------------------------")
              elif choose_toppings =="8":
                total_cost.append(0.50)
                chosen.append("w/ bell peppers")
                chosen.append("$0.50")
                print("You've chosen:",chosen)
                print("-----------------------------------------------------------------")


                
                
              else:
                print(""
                )
                continue
            















        print("done")
    
      else:
        print(error)
   
    except ValueError:
      print(error)

#adds up all numbers together to make the total amount
def add_up():
  print("Your total cost is:",sum(total_cost))

      
      
choosing_pizza("How many pizzas would you like? (max number 5): ")
add_up()