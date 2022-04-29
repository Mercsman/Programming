import math
print ()
print ('After traveling for some time away from home you are finally on your way back. Coming around a bend, you see a small shop ahead out here in the wilderness.')
print ('You feel fatigued from your journey and are down to your last 25 gold. You push open the door and hear a friendly gruff voice call out to you... ')
gold = int(25)
print()

# Round 1
print ('Welcome stranger! My name is Riff. You must be tired, tell me where have you come from? ')
background = input('Please select an option: THE FOREST, THE CITY, THE MOUNTAINS. ')
if(background.upper() == 'THE FOREST'):
    print ('Aye you have traveled far. ')
elif(background.upper() == 'THE CITY'):
    print ('City folk always seem tired after a journey HA HA!')
elif(background.upper() == 'THE MOUNTAINS'):
    print ('You are certainly a traveler stranger. Most never even go half as far as there. ')
else:
    print ('I see, odd place')
print()
    # Round 2
print ('Well what brings you here to my humble shop in the middle of nowhere? ')
reason = input('Please select an option: POTIONS, A WEAPON, REST. ')
# potions
if(reason.upper() == 'POTIONS'):
    print('Fair enough stranger. What kind would you like? ')
    potion = input('Please select an option: HEALING, STRENGTH, FLIGHT. ')
    if(potion.upper() == 'HEALING'):
        print('Adventurers always need them for sure heh. That will be 5 gold pieces please. ')
        gold = gold - 5
    if(potion.upper() == 'STRENGTH'):
        print('Looking for an extra boost are ya? Fair enough, that will be 8 gold pieces please. ')
        gold = gold - 8
    if(potion.upper() == 'FLIGHT'):
        print('Smart adventurers are always creative. That will be 6 gold pieces please. ')
        gold = gold - 6
    print ('Glad we had something you needed. ')
    print()
# weapons
elif(reason.upper() == 'A WEAPON'):
    print('Protection is always good, what are you looking for? ')
    weapon = input('Please select an option: SWORD, BOW, AXE, SPEAR. ')
    if(weapon.upper() == 'SWORD'):
        print('Fairly standard fair, but it is good quality I can assure ya. That will be 10 gold pieces please. ')
        gold = gold - 10
    if(weapon.upper() == 'BOW'):
        print('Sturdy, made from a yew tree. It will strike true as long as you aim right HA HA! That will be 8 gold pieces please. Arrows will be an additional 1 gold piece for twenty. ')
        gold = gold - 9
    if(weapon.upper() == 'AXE'):
        print('Not a standard wayfarer are you? Axes are the most popular these days but do solid work. That will be 6 gold pieces please. ')
        gold = gold - 6
    if(weapon.upper() == 'SPEAR'):
        print('Light enough to throw if you need, sturdy enough for close combat. A solid all around pick. That will be 8 gold pieces please. ')
        gold = gold - 8
    print('Pleasure doing business with ya. ')
    print()
# rest
elif(reason.upper() == 'REST'):
    print('Understandable, take your time stranger. You look like you could use it. ')
    rest = input('Please select how long you want to rest for: HALF HOUR, ONE HOUR, TWO HOURS. ')
    if(rest.upper() == 'HALF HOUR'):
        print ('Take your time stranger.')
    elif(rest.upper() == 'ONE HOUR'):
        print ("Safe rest isn't always easy to come by out in the wilderness. Take your time. ")
    elif(rest.upper() == 'TWO HOURS'):
        print ('You certainly are a weary one. You are safe here, take your time stranger. ')
    print('Glad to see you awake again! ')
    print()
else:
    print('I see, interesting choice. ')
# Round 3
print ('Well you know where to find me now, hopefully I will see you around. Did you need anything else before you left? ')
last = input('Please answer: YES or NO. ')
if(last.upper() == 'YES'):
    print ('Wonderful, have a look around. I got potions and weapons. ')
    # potion retry
    reason_2 = input('What would you like? POTION OR WEAPON ')
    if(reason_2.upper() == 'POTION'):
        print('Fair enough stranger. What kind would you like? ')
        potion = input('Please select an option: HEALING, STRENGTH, FLIGHT. ')
        if(potion.upper() == 'HEALING'):
            print('Adventurers always need them for sure heh. That will be 5 gold pieces please. ')
            gold = gold - 5
        if(potion.upper() == 'STRENGTH'):
            print('Looking for an extra boost are ya? Fair enough, that will be 8 gold pieces please. ')
            gold = gold - 8
        if(potion.upper() == 'FLIGHT'):
            print('Smart adventurers are always creative. That will be 6 gold pieces please. ')
            gold = gold - 6
    print ('Glad we had something you needed. ')
    print()
    # weapon retry
    if(reason_2.upper() == 'WEAPON'):
        print('Protection is always good, what are you looking for? ')
        weapon = input('Please select an option: SWORD, BOW, AXE, SPEAR. ')
        if(weapon.upper() == 'SWORD'):
            print('Fairly standard fair, but it is good quality I can assure ya. That will be 10 gold pieces please. ')
            gold = gold - 10
        if(weapon.upper() == 'BOW'):
            print('Sturdy, made from a yew tree. It will strike true as long as you aim right HA HA! That will be 8 gold pieces please. Arrows will be an additional 1 gold piece for twenty. ')
            gold = gold - 9
        if(weapon.upper() == 'AXE'):
            print('Not a standard wayfarer are you? Axes are the most popular these days but do solid work. That will be 6 gold pieces please. ')
            gold = gold - 6
        if(weapon.upper() == 'SPEAR'):
            print('Light enough to throw if you need, sturdy enough for close combat. A solid all around pick. That will be 8 gold pieces please. ')
            gold = gold - 8
    print('Pleasure doing business with ya. ')
    print()
elif(last.upper() == 'NO'):
    print('I see, no problem stranger. ')
    print()
else:
    print('I see, no problem stranger. ')
print('Be safe out there.')
print(f'You have {gold} pieces left.')
print('You step outside and again continue your journey. ')
print()