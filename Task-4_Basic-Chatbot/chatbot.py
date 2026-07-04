print("Welcome back,sir")
while True:
    user = input("You: ").strip().lower()       #user=input("Enter Your Message : ")
    if(user=="hello"):
        print("bot: Hi")
    elif(user=="how are you"):
        print("bot: I am fine,thanks!")
    elif(user=="who are you"):
        print("bot: I am Nivasbot")    
    elif(user=="who created you"):
        print("bot: I am created by Nivas")    
    elif(user=="bye"):
        print("bot: Goodbye")
        break  
    else:
        print("bot: Sorry I can't understand")      
            
