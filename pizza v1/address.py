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
#testrun
adresss = address_check("What is your address? ")
print("-----------------------------------------------------------------")