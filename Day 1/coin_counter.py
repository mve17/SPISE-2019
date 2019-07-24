print("Welcome to Coin Cointer\n")
one_cent=input("How many pennies? ")
five_cent=input("How many nickles? ")
ten_cent=input("How many dimes? ")
twenty_five_cent=input("How many quarters? ")
total_cents=int(one_cent)+5*int(five_cent)+10*int(ten_cent)+25*int(twenty_five_cent)
dollars=total_cents/100
print("\nThat comes to $"+str(dollars))

