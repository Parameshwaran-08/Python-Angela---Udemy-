print("""

888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888 


""")

print("Welcome to treasure island. Your mission is to find the treasure !")

direction = input("Do you want to go left or right. Type right or left !\n").lower()
if direction == "right":
    print("You are fucked.")

elif direction == "left":
    wait = input("Do you want to wait for the boat or swim across the lake. Type wait or swim !\n").lower()
    if wait == "swim":
        print("You are fucked.")
    elif wait == "wait":
        door = input("which door you want to enter ? Type red, blue or yellow !\n")
        if door == "blue":
            print("You are fucked.")
        elif door == "yellow":
            print("You are fucked.")
        elif door == "red":
            print("You have fucking won the treasure !")
