staff_selected=False
sword_selected=False
hard_heart=False
pure_heart=False
import time
print('Once upon a time, in a land far, far away, there was a wizard named-')
time.sleep(5)
print("It seems we have a bit of a problem. I've forgotten the wizard's name.")
time.sleep(5)
print("Easily rectified, don't worry. We'll just use your name.")
time.sleep(5)
name=input("What's your name, listener? ")
print(name+'. How lovely! Well, the great and powerful wizard '+name+' was travelling throughout the land in search of a rare treasure.')
time.sleep(8)
print(name+' heard tell of two legendary relics waiting to be found by some brave adventurer, the Staff of Eternal Peace, and the Sword of Endless Power.')
time.sleep(7)
print('Since the wizard has your name, I declare the story yours henceforth and forever. Choose your path, '+name+'.')
time.sleep(5)
treasure=input('STAFF or SWORD? ')
while sword_selected==False and staff_selected==False: 
    if treasure=='STAFF':
            staff_selected=True
    else:
       if treasure=='SWORD':
            sword_selected=True
    if sword_selected==False and staff_selected==False:
        print("Eh? I didn't quite get that. Just pick one, " +name+'.')
        time.sleep(3)
        treasure=input('And use ALL CAPS, it helps me hear you better. ')
if sword_selected==True:      
    print('Excellent choice. '+name+' wished to use the sword to slay the Great Dragon, who had been terrorizing the kingdom for centuries.')
    time.sleep(6)
    print(name +' travelled over mountains and deserts, rivers and swamps, following the map to the fabled location of the Sword.')
    time.sleep(9)
else:
    print('Wonderful! ' +name+' wished to use the staff to end the Great War, which had been plaguing the kingdom for decades.')
    time.sleep(6)
    print(name +' travelled over mountains and deserts, rivers and swamps, following the map to the fabled location of the Staff.')
    time.sleep(9)
print('On the way, she met an old beggar lady, who asked for a penny. With plenty to spare, '+name+' shared, right?')
time.sleep(5)
shared_money=input("I hope you did, but it's your choice. YES or NO? ")
while hard_heart==False and pure_heart==False: 
    if shared_money=='YES':
            pure_heart=True
            print("'Well, how kind of you!' she exclaimed. She gave "+name+" a hug that would make even a great wizard feel warm and fuzzy inside.")
    else:
       if shared_money=='NO':
            hard_heart=True
            print("'Well, how kind of you,' she muttered, along with some other strong language "+name+" didn't quite hear.")
            time.sleep(5)
            print("I'm a little disappointed in "+name+".")
    if pure_heart==False and hard_heart==False:
        print("Eh? I didn't quite get that. Just pick one, " +name+'.')
        time.sleep(3)
        shared_money=input('And use ALL CAPS, it helps me hear you better. ')   
time.sleep(6)
print('Well, ahem, anyway...')
time.sleep(2)
print('Eventually, the wizard reached the Cave of Mysteries, nestled high in the mountainous Far Lands.')
time.sleep(6)
print(name+' ventured into the darkness, following the glow of light that ancient books had said the relic would give.')
time.sleep(9)
print('And there it was! Marvelous!')
if treasure=='STAFF':
            print('As she approached the Staff, '+name+' was overwhelmed by the light it spread out, and the feeling of joy that the end of the war was soon.')
            time.sleep(9)
            print('The cave shook as a voice thundered, "All those who would wield my Staff must be pure of heart!"')
            time.sleep(6)
else:
       if treasure=='SWORD':
           print('As she approached the Sword, '+name+' was overwhelmed by the light it spread out, and the feeling of joy that the dragon would soon be slain.')
           time.sleep(9)
           print('The cave shook as a voice thundered, "All those who would wield this Sword must be pure of heart!"')
           time.sleep(6)
print('Well, then, '+name+' picked up the treasure that had been worth all those journeys and trials...')
if pure_heart==True:
      if treasure=='STAFF':
        time.sleep(7)
        print('...and wished silently to bring peace to all the kingdom.')
        time.sleep(6)
        print('And although '+name+' could not see what the wish had done, all the soldiers dropped their swords, and stepped out of their shiny suits of armor.')
        time.sleep(7)
        print('Each one felt nothing but love in their hearts and they knew that the War, and all wars, were over forever.')
        time.sleep(8)
        print('And '+name+' saw, coming toward her in the darkness, the old lady she had helped! "I am the Guardian of Relics," she said.')
        time.sleep(6)
        print('"The task of protecting treasures for those who would use them well was left for me. You have passed my test, and saved the kingdom!"' )
        time.sleep(8)
        print('"Now go on, and find a new adventure!"')
        time.sleep(5)
        print('THE END')
        time.sleep(10)
      else:
            if treasure=='SWORD':
                print('and set off again to find the lair of the dragon.')
                time.sleep(6)
                print(name+' approached the mountaintop where the dragon had made its nest of gold and bones, the first in a century who had had the bravery to try.')
                time.sleep(7)
                print('A crowd had gathered behind her, hoping to witness the spectacle of a fiery battle between a dragon and a wizard.')
                time.sleep(8)
                print('As the dragon emerged from its cave, a glint of light from the sword caught its eye, and it shrank back, whimpering.')
                time.sleep(6)
                print(name+"'s crowd of followers gasped in shock." )
                time.sleep(8)
                print(name+" charged ahead, sworn drawn. There was a burst of green light, and the dragon was gone.")
                time.sleep(5)
                print('And '+name+' saw, stepping out of the crowd, the old lady she had helped! "I am the Guardian of Relics," she said.')
                time.sleep(6)
                print('"The task of protecting treasures for those who would use them well was left for me. You have passed my test, and saved the kingdom!"' )
                time.sleep(8)
                print('"Now go on, and find a new adventure!"')
                time.sleep(5)
                print(name+' returned to her village a hero in search of a new villain to fight.')
                time.sleep(8)
                print('THE END')
                time.sleep(10)
else:
    time.sleep(20)
    print("Oh no.. you see, I'm sorry, um, well, I didn't think it would end like this...")
    time.sleep(7)
    print('The power was too much for '+name+'. The speck of darkness that was nestled in her heart took over.')
    time.sleep(8)
    print(name+' heard the voice of the old lady she had refused to help. She was whispering "I wanted this one to succeed... well, the true Chosen One shall come someday."')
    time.sleep(15)
    print(name+' screamed, feeling the final pain of the darkness overtaking her soul, and the cave went dark, and '+name+' never emerged from its shadows.')
    time.sleep(8)
    print('THE END')
    time.sleep(10)

    
    
    
    
     
