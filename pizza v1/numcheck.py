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

phone = num_check("What's your phone number? ")
print("-----------------------------------------------------------------")