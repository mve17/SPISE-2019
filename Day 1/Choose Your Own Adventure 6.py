name=input("Please Enter Your Name: ")

intro_text='''
You've woken up with a splitting headache. Fumbling in the dark, your hand brushes against a cold metallic object in the sand.
Maybe it will be useful. Would you like to take it with you? [y/n] '''

intro_response=input("\nBad news, "+name+". "+intro_text)

if intro_response=='y':
   holding_metal_object=True
else:
   holding_metal_object=False

fire_text='''
\n As your eyes adjust to the darkness, you notice outlines of a forest behind you---as well as a faint light further on the beach.
Perhaps a distant campfire? Would you like to investigate? [y/n] ''' 
response_2=input(fire_text)

if response_2=='n':
   killed_by_animal_text='''
                     \nYou hear snapping sounds in the forest behind you.
                     Suddenly, a roar breaks the silence and you find yourself thrown to the
                     ground. Everything fades to black. 
                     '''
   print(killed_by_animal_text)

else:
   campfire_text='''\nAs you approach the campfire you overhear a low conversation around the fire. You
hear words like iron, distaster, steel, sabatoge, missing. You're not sure if they're
friendly, but it's starting to get cold and it feels like your only chance. You step into the light and
receive a warm welcome. After a routine security check, they say, they'll set you up with some dinner.'''
   print(campfire_text)

   if holding_metal_object:
      print('''\nA man comes forward with some sort of device to use for the security check.
As it passes over your pocket, the device emits a shriek and a light flashes. The man steps back hurredly
and you find yourself pushed away from the campfire and told in no uncertain terms to not come back. It's gotten extremely
cold, you don't think you'll survive the night''')

   else:
      print('''\nThe security check goes smoothly. Good thing you didn't pick up that metal object... You get a plate of food. You're
still not sure where you are, but you know that you're safe for now. THE END.''')
   
