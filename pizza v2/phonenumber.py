phone_number = []

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
       print("done")

#test run
num_check("What is your phone number? ")