"""
Lists
Student Project
Project Title: Movie Finder
"""

import random  # Import the random module

# all the important list
#account keeps the users user_saves = [] saved.(not using yet)
account = []
#passwords and users keep the users password saved
passwords = []
users = []
#user_saves would save the users 3 movies so when they log back in they'll be reminded what they got the last time
user_saves = []
#Login and choosing is true so everything can keep running until they're done in that section.
Login = True
choosing = True

# All the Movie genres that will be randomized for the user!
horror = ["MA", "Sinister", "Abigail", "BirdBox", "Ring", "Us", "Smile", "Scream", "IT"]
action = ["Sonic The Hedgehog 3", "Fast and Furious", "Spiderman: Across the Spider-Verse", "Transformer", "Venom", "Deadpool", "John Wick", "Lego Movie", "Kung Fu Panda"]
comedy = ["Friday", "Rush Hour", "Ted", "Coming To America", "Sausage Party", "White Men Can't Jump", "Rango", "Shrek", "Penguins"]

# This is where the login loop starts
while Login:
    username = input("Enter your username, or create one by typing 'A': ").strip()
    if username in users:
        password = input("Enter Your Password: ").strip()
        #Using .strip() on line 28 and 30 so the text is spaced and look and juicy!
        
        
        user_index = users.index(username)
        if passwords[user_index] == password:
            print("You Successfully Logged Into your account!")
 # This will only work if the user already ran the code before
            while choosing:
                genre_choice = input("What genre would you like to watch? Horror, Action, Comedy? ").strip().upper()


                # Recommend 3 random movies from selected genre
                if genre_choice == "HORROR":
                    print("You should watch:", random.sample(horror, 3))
                elif genre_choice == "ACTION":
                    print("You should watch:", random.sample(action, 3))
                elif genre_choice == "COMEDY":
                    print("You should watch:", random.sample(comedy, 3))
                #I used sample over choice because i kept getting an error when
                #i used choice, sample was able to choose 3 random elements
                #from the list and thats what i needed!!
                

                else:
                    print("Sorry, but That is not a genre, try again.")
                    continue  # Keep asking until the user FINALLY types one of the options
                
                print("Logging out... See you next time!")
                break  
            # Exit the loop to log the user out
                
            #This is what happens when the user gives a bad 
        else:
            print("Incorrect password. Try again.")
    #line 63 lets the user choose upper and lower case a's so there would be no problem.
    elif username.upper() == "A":
        login_user = input("Create a username: ").strip()
        password_user = input("Create a password: ").strip()

        if login_user not in users:
            #appending so if the user tries to create a new user with the same user or password, they'll get line 73
            
            users.append(login_user)
            passwords.append(password_user)
            print("You have successfully created an account")
        else:
            print("Sorry, this username is already taken.")
            
            
#Not in use#######################################################################
#if username in user_saves:
#             print("Here were your last selected Movies: ", user_saves[username])
##################################################################################