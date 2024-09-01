name=input("Type your name: ")
print("Welcome to adventure game",  name)
option=input("You are at the end of road and you can go left or right, which way you want to go? ").lower()
if option=="left":
  user_input= input("You select left, you now reach to bridge, you can talk to stranger or not? yes/no ").lower()
  if user_input== "yes":
       print("You talk to stranger, You won")
  elif user_input== "no":
      print("You select no, and you lose")
  else:
      print("You select wrong option")

elif option=="right":
  user_input=input("You select right, you can now swim or walk: ").lower()
  if user_input== "swim":
    print("You select swim and shark ate you")
  elif user_input== "walk":
    print("You select walk and you ended up with water")
  else:
      print("You select wrong option")
else:
  print("You select wrong option")

print("Thank you for trying ", name)
