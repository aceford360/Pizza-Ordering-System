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

name = validate_name("What is your name? ")
print("-----------------------------------------------------------------")
