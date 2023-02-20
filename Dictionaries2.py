#cars = {
    #"model":"ford",
    #"year":1998,
    #"color":"red",
    #"country":"Kenya"

#}

#accessing dictionaries items
#print(cars["country"])

#person = {
 #   "name":"Cathy",
  #  "age":23,
   # "pets":{
    #        "dog":"x",
     #       "cat":"y",}
#}

#print(person["pets"]["cat"])


#integer keys
#teams = {
 #   23 : "a",
  #  56.67 : [34,451,34]
#}

#profile = {}
#profile["username"] = "user123"
#profile["age"] = 20
#profile["email"] = "user123@gmail.com"
 
profile = {}
def register():
    #ask for user name
    username = input("Enter user name: ")
    #ask for email
    email = input("Enter email: ")
    #ask for password
    password = input("Enter password: ")

    #store in a dictionary

    profile["username"] = username
    profile["email"] = email
    profile["password"] = password

def get_profile():
    #print user profile
    print(profile)

def change_username():
    new_name = input("Enter new username: ")
    profile["username"] = new_name

register()
get_profile()

change_username()
get_profile()







