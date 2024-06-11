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

confirm_order("Would you like to continue? Type in 'cancel' to cancel.")