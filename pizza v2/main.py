#version 2

#lists go here
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


#customer details
name = []
address = []
phone_number = []
delivery_or_pickup=[]

#functions go here

#contain options to specify whether the order is for pickup or delivery:
def pickup_delivery(question):

  valid = False
  while not valid:

    response = input(question)

    if response ==  "delivery" or response == "Delivery" or response == "d" or response == "D":
      
    #adds $3 delivery charge if chosen delivery

     total_cost.append(3)
     delivery_or_pickup.append("Delivery")
     print("You have chosen delivery...")
     print("-----------------------------------------------------------------")

     return response
     

    elif response  == "pick up" or response == "p" or response == "Pick up" or response == "P":
     delivery_or_pickup.append("Pickup")
     print("You have chosen pick-up...")
     print("-----------------------------------------------------------------")
     return response

    else:
      print("Please pick either pick-up or delivery!")
      continue

#validates name of customer
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
          name.append(response)
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
       address.append(response)
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
       phone_number.append(response)
       print("-----------------------------------------------------------------")
       return response

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
            















        return response
    
      else:
        print(error)
   
    except ValueError:
      print(error)

#shows order of customer
def order_reciept():
  if 'Pickup' in delivery_or_pickup: #if user has chosen pickup, only shows name and pizzas chosen
    print("Order reciept")
    print ("Name",name)
    print("Pizzas:",chosen)
    print("-----------------------------------------------------------------")

  elif 'Delivery' in delivery_or_pickup: #if user has chosen delivery, everything else will show up
    print("Order receipt")
    print("Name",name)
    print("Address:",address)
    print("Phone number:",phone_number)
    print("Pizzas:",chosen)

    print("-----------------------------------------------------------------")


#allows user to eiher continue or cancel order
def confirm_order(question):
  valid = False
  while not valid:
    response = input(question)

    #if user says yes, program will proceed
    if response == "Y" or response == "yes" or response =="y" or response =="Yes":
      print("-----------------------------------------------------------------")
      return response

    #if user cancels order, then order is cancelled and program stops.
    elif response == "Cancel" or response == "cancel" or response == "cancel order" or response == "Cancel order" or response == "C" or response =="no" or response =="No" or response =="N" or response =="n":
      print("-----------------------------------------------------------------")
      print("Okay, we will cancel your order..")
      print("Please come again!")
      exit()
    else:
      print("Please type in answer...")
      continue

#adds up all numbers together to make the total amount
def add_up():
  print("Your total cost is:",sum(total_cost))
  print("Order completed!")


#allows user to order again if they want to
def loop_begin(question):

  response = input(question)
  if response == "":

    main()

  else:
    exit()
  
#every function in order
def main():
  
  print("-----------------------------------------------------------------")
  print("Pizza Order V3") #version of code
  print("-----------------------------------------------------------------")
  #prints welcome
  print("Welcome to Pizza Place!")
  validate_name("What is your name? ")
  address_check("Where is your address? ")
  num_check("What is your phone number? ")
  choosing_pizza("How many pizzas would you like? (max number 5): ")
  pickup_delivery("Would you like pick up or delivery? ")
  order_reciept()
  confirm_order("Would you like to continue with your order? Please type 'cancel' to cancel your order: ")
  add_up()
  loop_begin("Press <enter> to order again or any other key to quit: ")

    
#prints everything in order
main()
