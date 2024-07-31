#L1_Challenge3_Task1.py

"""Function takes number(n) and returns sum of numbers from 1-n and sum of multiples of 3 and 55"""
def ask_user_for_number():
  try:
    return int(input("Enter a number: "))
  except:
    print("Invalid Number!")

n = ask_user_for_number()
print(n)

def sum(n):
  total = 0
  numbers = []
  i = 1
  while i <= n:
    total += i
    numbers.append(i)
    i += 1
  return("Numbers: {} \nSum: {}".format(numbers, total))
print(sum(n))

def sum_of_multiples(n):
  total = 0
  numbers = []
  i = 1
  while i <= n:
    if i % 3 == 0 or i % 5 ==0:
      total += i
      numbers.append(i)
      i += 1
    else:
      i += 1
  return ("Multiples of 3 and 5 only: {} \nSum of multiples: {}".format(numbers, total))
print(sum_of_multiples(n))

"""Function takes another number(second_n) and chooses whether to return sum of numbers from 1-n or product of numbers 1-n"""
def options():
  second_n = ask_user_for_number()
  options = int(input("Choose from: \n1. The sum of numbers 1 to your number \n2. The product of numbers 1 to your number \nEnter your option: "))
  if options == 1:
    return sum(second_n)
  else:
    final_number = 1
    i = 1
    while i <= second_n:
      final_number *= i
      i += 1
    return ("Product: {}".format(final_number))

print(options())
