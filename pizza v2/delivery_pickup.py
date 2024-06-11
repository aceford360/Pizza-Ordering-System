total_cost = []
delivery_or_pickup=[]

address = []
phone_number = []
delivery_or_pickup=[]

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

     print("done")
     

    elif response  == "pick up" or response == "p" or response == "Pick up" or response == "P":
     delivery_or_pickup.append("Pickup")
     print("You have chosen pick-up...")
     print("-----------------------------------------------------------------")
     print("done")

    else:
      print("Please pick either pick-up or delivery!")
      continue

def order_reciept():
  if 'Pickup' in delivery_or_pickup: #if user has chosen pickup, only shows name and pizzas chosen
    print("You have chosen pickup")
    print("-----------------------------------------------------------------")

  elif 'Delivery' in delivery_or_pickup: #if user has chosen delivery, everything else will show up
    print("You have chosen delivery")
    print("Address:",address)
    print("Phone number:",phone_number)

    print("-----------------------------------------------------------------")



#test run
pickup_delivery("Would you like pick up or delivery? ")
order_reciept()
