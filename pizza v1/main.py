#version 1

#lists go here
menu = ["1: Cheese","2: Pepperoni","3: Hawaiian","4: Meat Lovers",
"5: Margherita","6: Vegetarian","7: Cheesy Garlic","8: Garlic Prawn",
"9: Mushroom Supreme","10: BBQ Chicken ","11: Meat Lovers Surpreme","12: Chicken Fajita",""
]
pizza_cost = ["$8.50","$8.50","$8.50","$8.50","$8.50","$8.50","$13.50","$13.50","$13.50","$13.50","$13.50","$13.50",""
]

toppings = ["1: Pepperoni", "2: Mushrooms", "3: Extra Cheese", "4: Onions", "5: Anchovies", "6: Olives", "7: Ham", "8: Bell Peppers"]

toppings_cost = ["$0.50","$0.50","$0.50","$0.50","$0.50","$0.50","$0.50","$0.50",""]

#validates name
def validate_name(question):
  error = ("Your name has numbers in it")
  
  valid = False
  while not valid:
        response = input(question)
        has_errors = ""
        
        #look at each character in string and if its a number, complain
        for letter in response:
            if letter.isdigit() == True:
                has_errors = "yes"
                break

        if response== "":
          print("Please type in your name!")
          continue

        elif has_errors !="":
            print(error)
            continue
          
        else:
          print("-----------------------------------------------------------------")
          return response

#costumers address, if there's no input, it returns response
def address_check(question):
   valid = False
   while not valid:
     response = input(question)
      
     if response =="":
        print("Please type in your address!")
        continue

     else:
       print("-----------------------------------------------------------------")
       return response

#numcheck function
def num_check(question):
  error = "Please type in a number"

  valid = False
  while not valid:
      response = input(question)
      has_errors = ""

#look at each character in string and if its a letter, complain
      for digit in response:
          if digit.isalpha() == True:
              has_errors = "yes"
              break
      if response== "":
        print("Please type in your phone number!")
        continue

      elif has_errors !="":
            print(error)
            continue
      
      else:
       print("-----------------------------------------------------------------")
       return response

def max_pizza(question):
  error = "Please enter a number between 1 and 5."

  valid = False
  while not valid:

    try:
      response=int(input(question))

      if  1<= response <=5:

        return response
      else:

        print(error)
        continue

    except ValueError:
      print(error)
      continue

#start of code
print("Pizza Order V1")
print("-----------------------------------------------------------------")
option = input("Would you like to have your order picked up or delivered? ")
if option == "delivery" or option == "Delivery" or option == "d" or option == "D":

  name = validate_name("What is your name? ")
  print("-----------------------------------------------------------------")
  adresss = address_check("What is your address? ")
  print("-----------------------------------------------------------------")
  phone = num_check("What's your phone number? ")
  print("-----------------------------------------------------------------")
  how_many = max_pizza("How many pizzas would you like? ")

  print("-----------------------------------------------------------------")

#prints pizza menu
  print("Pizza menu:")
  res = "\n".join("{} {}".format(x, y) for x, y in zip(menu, pizza_cost))
  print(res)

elif option == "pick up" or option =="Pick up" or option =="P" or option =="p":
   name = validate_name("What is your name? ")
   print("-----------------------------------------------------------------")
   how_many = max_pizza("How many pizzas would you like? ")

   print("-----------------------------------------------------------------")


   #prints pizza menu
   print("Pizza menu:")
   res = "\n".join("{} {}".format(x, y) for x, y in zip(menu, pizza_cost))
   print(res)

else:
  print("Please pick 'delivery' or 'pick up'.")
