import time

print("You're in the bathroom washing you hands because you're a hygienic individual.")
print("There is no tissue to dry your hands with.")
print("")

decision_1=input("Do you wipe your hands on your pants? Yes or no? ")
print("")
time.sleep(2)

print("You turn off the bathroom light.")
print("")
time.sleep(2)

if decision_1=="Yes" or decision_1=="yes":
    print("You are not electrocuted.")
    print("")
    time.sleep(2)
    
    print("You enter the kitchen and hear a strange noise outside.")
    print("You decide to go outside.")
    decision_2=input("Do you grab a knife? Yes or no? ")
    print("")
    time.sleep(2)
    
    if decision_2=="Yes" or decision_2=="yes":
        print("When you go outside, you meet a serial killer.") 
        print("He has a knife.")
        print("")
        time.sleep(2)
        
        print("Your survival instincts kick in. You stab him with the knife before he can stab you with his.")
        print("")
        time.sleep(2)
        
        print("Congratulations, you survived but you're now a murderer.")
    else:
        print("When you go outside, You meet a serial killer.")
        print("He has a knife and you have nothing. ")
        print("")
        time.sleep(2)
        print("You are unable to defend yourself. The serial killer stabs you.")
        print("")
        time.sleep(2.5)
        print("You bleed out on your porch.")
        
else:
    print("You've been electrocuted. You die.")

