#allows user to order again if they want to
def loop_begin(question):

  response = input(question)
  if response == "":

    main()

  else:
    exit()

loop_begin("Press <enter> to order again or any other key to quit: ")


def main():
  print("Hello")
  loop_begin("Press <enter> to order again or any other key to quit: ")

main()