###guessing game
def main():
    print("welcome to the world of guessing game!!!!!!")
    attempt_limit=10
    print("There are only 10 attempts to find the correct value.")
    mode=input("choose a mode 1 for human_guess_mode and 2 for guess_by_machine_mode:")
    
    if mode == '1':
        human_guess_mode(attempt_limit)
    elif mode == '2':
        machine_guess_mode(attempt_limit)
    else:
        print("You have selected invalid mode.please restart the game.")
        


import random

def human_guess_mode(attempt_limit):
  print("I am just thinking of a number between the given limit 0 to 100 ")
  number_range=random.randint(0,100)
  print("Choose a number inside the range 0 to 100!!!")
  print("Keep the number in mind and enter the number when your chance comes to enter it.")
  attempts=0
  while attempts<attempt_limit:
      guessed_number=int(input("Enter the guessed number(0 to 100):"))
      attempts+=1
      try:
          guess=guessed_number
          if guess<0 or guess>100:
            print("please enter the number between o and 100")
            continue
          elif guess>number_range:
            print("Your guess failed.")
            print("The value is too high.Try Again.....")
          elif guess<number_range:
           print("Your guess failed")
           print("The value is less than the guessed value .Try Again....")
          else:
           print(f"Congratulations.You guessed it in {attempts} attempts.")
           break
      except ValueError:
          print("Your guess is not a valid .Please enter the number between 0 to 100")
      else:
          print("Sorry,attempt limit has reached.Better luck next time")     
#start the game
  
def machine_guess_mode(attempt_limit):
    least=0       
    high=100
    print("Think of a number between the given limit 0 to 100.")
    print("I will give the try to guess it.")
    attempts=0
    while least <= high and attempts < attempt_limit:
        attempts += 1
        
        guess= (least + high) // 2
        print("Enter h if the value is higher,l if the value is lower,c if the value is correct ")
        response=input(f"is your number {guess}?Enter 'h' if it is higher,enter 'l' if it is lower or 'c' if it is correct:")
        if response == 'h':
          least = guess + 1
        elif response == 'l':
          high = guess - 1
        elif response == 'c':
          print(f"yes!! finally I guessed the number in {attempts} attempts.")   
          break
        else:
          print("Invalid response. Please enter 'h','l','c'.")
    else:
        print("Sorry,I coundn't guess your number within the attempt limit.")

if __name__=="__main__":
    main()
        
    