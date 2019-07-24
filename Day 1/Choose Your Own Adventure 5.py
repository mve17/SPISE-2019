print("Welcome to CHOOSE YOUR OWN ADVENTURE!")
username = input("Enter your username: ")

print("You are walking home one day when you find a $100 bill on the street. You're famished and could really use a bun and cheese right now. Unable to help yourself, you pick up the money and proceed to the tuck shop a few yards away. As you approach, the aroma of warm, fresh baked goods fill your nostrils, but a few feet away from your destination, you notice a young man begging for food. What do you do?")
print("1 - give the money to the young man")
print("2 - proceed to the tuck shop")

choice1 = input("[1/2]")

if choice1 == '1':
    print("You decide your hunger can wait. You approach the young man and offer him the $100 bill.")
##    import time.sleep(5)
    print("The man glares scornfully at the bill, and says in disgust, 'Since when hundred dollars can buy a box food?")
##    import time.sleep(5)
    print("What do you do?")
    print("1 - walk away")
    print("2 - argue")

    choice2 = input("[1/2] ")

    if choice2 == '1':
        print("You proceed to the counter and order your bun and cheese. On your way home, you see a small child frantically searching the ground where you had found the money. 'So hungry,' she groaned. 'Where is that money?' You stop in your tracks. What will you do now?")
        print("1 - give the child the bun and cheese")
        print("2 - keep walking and don't make eye contact")

        choice3 = input("[1/2] ")

        if choice3 == '1':
            print("You hand the child the bun and cheese, and apologise for what you did. The gratitude in the child's face fills you with such joy that you don't even miss having your snack. You walk home, feeling good that you didn't steal after all.")

        else:
            print("You keep walking, but the further away you get, the more uneasy you feel. A few meters from your apartment, the same man who had been begging at the tuck shop jumps out from nowhere and holds you up at knifepoint. You hand over everything on you except the bun and cheese, which the man doesn't demand. After he leaves, you let yourself into your room, too frightened and sick to your stomach to eat. You feel terrible for stealing that child's money and not returning it. Serves you right.")


    else:
        print("Beggars can't be choosers, you know. I'm offering you the money because you look like you could use it - either take it or leave it.")
##        import time.sleep(7)
        print("The man angrily snatches the bill from your hand and glares at you until you retreat. But you're not backing down because you don't take that kind of treatment from people you're helping out of the kindness of your heart. Suddenly, the man draws a knife, and several other intimidating characters begin to surround you. What now?")
        print("1 - call the police")
        print("2 - run")
        
        choice4 = input("[1/2] ")
        
        if choice4 == '1':
            print("Soon after you emergency dial the police, the shrieks of sirens and the flashing blue lights cause the gang to disperse. The police officers emerge from their vehicle and round up all the offenders. They are all loaded into the police car and taken to the station. You're safe!")

        else:
            print("You try to make a run for it, but the men are too fast. They grab you, gag your mouth and tie you up. You're tossed into a black bag and flung into a black van with tinted windows. The gang drives you off to the hinterlands and you're never heard from again.")


else:
    print("You're too hungry to help this time, so you proceed to purchase your bun and cheese. While standing in line, you feel something brush past you, but you don't pay it any mind. But after you've received your bun at the counter, you realise the money's missing! What do you do?")
    print("1 - run with the bun")
    print("2 - resolve to not have bun today")

    choice5 = input("[1/2] ")

    if choice5 == '1':
        print("You snatch the bun and run, but the security chases and eventually restrains you. You are taken to a police station where your parents are called in too. Once your parents get you out, they ground you for a whole year, and you have to do community service during that time.")

    else:
        print("You decide you don't really need the bun and walk home. You reflect on the fact that your losing the money was just karma in action, since you shouldn't have taken it up in the first place.")




print("THE END")
    
