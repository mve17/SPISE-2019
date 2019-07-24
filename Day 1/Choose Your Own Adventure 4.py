player_name = input('Enter name: ')
print (player_name + ', you are walking through a dark alley and hear faint, eery sound from the corner ahead')
print('Do you want to turn around and head the way you came from? ')
answer_1 = input('y/n: ')
if answer_1 == 'n':
    print ('You continue walking and as you turn the corner, ')
    print('you are startled by a dark misty figure, the figure then makes its way to where you are standing')
    print ('Do you want to face the mysterious silhouette? ')
    answer_2 = input('y/n: ')
    if answer_2 == 'y':
        print('You walk forward and then BOOM!')
        print('The figure egulfs your body with all its evil spirits, Your eyes turn right into your socket, your skin burns of to reveal your fleshy interior,')
        print('you scream and instantaneously disappear into the wind')
    else:
        print('You turn around and a masked man excite you with his presence, He pulls out his gun and shoots you.')
        print('You then lay on the ground, bleeding with noone to save you. Then with one last breath you die')

else:
    print('You turn around and then a sharp pain stabs you in the chest as you get a heart attack and eventually dies')

    
