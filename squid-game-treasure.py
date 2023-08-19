print("********Welcome to Squid game*******")
print("Your mission is to find the Craziest Lottery Ever")

choose_path = input("PeekABoo : Choose the path that takes to golden buddha : Right or Left.\n").lower()

if(choose_path == "Left") :
    choose_voyage = input("Voyage : Will you swim or wait someone to rescue ? : Swim or Wait.\n").lower()
    if(choose_voyage == "Wait") :
        choose_door = input("PickADoor : Will you go into ? : Red or Yellow or Blue.\n").lower()
        if(choose_door == "Red") :
            print("Ayyoyo : You've got a ticking bomb....!!!")
        elif(choose_door == "Yellow") :
            print("Wonderful honey : You found the Sugar candy treasure....")
        elif(choose_door == "Blue") :
            print("Death Trap : You've got a leapord's cage......Sorry")
        else :
            print("Sorry champ : You've picked the wrong one.....")
    else:
        print("Sorry buddy : You're in a Whales hungery bowl....oops")
else :
    print("Sorry honey, you've missed the chance : You'll go into the cave....")