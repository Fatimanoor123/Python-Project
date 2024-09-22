#Print numbers from 1 to 100, but for multiples of 3, print "Fizz," for multiples of 5, print "Buzz," and for multiples of both 3 and 5, print "FizzBuzz."
def fizzBuzz():
  for num in range(1,101):
    if num%3==0 and num%5==0:
      print("FizzBuzz")
    elif num%3==0:
      print("Fizz")
    elif num%5==0:
      print("buzz")
    else:
      print(num)
fizzBuzz()
