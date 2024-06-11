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

how_many = max_pizza("How many pizzas would you like? ")