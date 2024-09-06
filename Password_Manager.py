
#Showing already existing user and password
def view():
  with open('password.txt', 'r') as f:
    for line in f.readlines():
      data=line.rstrip()
      user,passw=data.split("|")
      print("User: ", user, "Password: ", passw)





#Adding new password to the text file, if text file is not created then it will be created. 
def add():
  name=input("Enter your name").lower()
  pwd=input("Enter password").lower()
  with open('password.txt', 'a') as f:
    f.write(name + "|"+ pwd + "\n")


#Asking user to add or view password
while True:
  mode=input("Would you like to add a new password or view existing ones(view, add), press q to quit?").lower()
  if mode=="q":
    break
  elif mode=="view":
    view()
  elif mode=="add":
    add()
  else:
    print("Invalid mode.")
