address = []

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
       print("done")
#test run
address_check("Where is your address? ")
