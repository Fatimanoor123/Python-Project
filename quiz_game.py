print('Hello, Welcome to the quiz game!')
ans=input('Do you want to play?')
score=0
if ans!="yes":
  quit()

print("Let's play :)")
answer=input('what is GPU?')
if answer.lower()=='graphic processing unit':
  print('Correct!')
  score +=1
else:
  print("Incorrect!")
answer_1=input('what is CPU?')
if answer_1.lower()=='central processing unit':
  print('Correct!')
  score +=1
else:
  print("Incorrect!")
answer_2=input('what is RAM?')
if answer_2.lower()=='random access memory':
  print('Correct!')
  score +=1
else:
  print("Incorrect!")
print("You get" + str(score)  + "Scores")
