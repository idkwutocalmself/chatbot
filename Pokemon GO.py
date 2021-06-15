import random
import time

money = 0
prestige = 0
train = 0
team = ['Your team is empty. Add pokemons to your team.']
pets = []
print("Pokemon GO!")
time.sleep(3)
print('Please answer everything lowercased')
pokeball = 20
greatball = 0
ultraball = 0
npikachu = 0
nraichu = 0
nbulbasaur = 0
nivysaur = 0
nvenusaur = 0
nsquirtle = 0
nwartortle = 0
nblastoise = 0
ncharmandar = 0
ncharmeleon = 0
ncharizard = 0
raidbosses = {'centaur':(100,20),'manticore':(70,30),'chimera':(100,10),'dragon':(50,30),'harpy':(100,20),'cyclope':(80,30),'kraken':(100,25),'basilisk':(1000,10),'siren':(500,20),'hydra':(2000,10),'minotaur':(80,50)}
stats = {'pikachu':(6,5),'raichu':(20,20),'bulbasaur':(8,3),'ivysaur':(15,6),'venusaur':(30,10),'squirtle':(4,7),'wartortle':(8,13),'blastoise':(15,25),'charmandar':(3,8),'charmeleon':(6,15),'charizard':(11,29)}
desc = '''Pikachu (Level 1): 6 hp 5 att
Raichu (level 3): 20 hp 20 att
Bulbasaur (level 1): 8 hp 3 att
Ivysaur (level 2): 15 hp 6 att
Venusaur (level 3): 30 hp 10 att
Squirtle (level 1): 4 hp 7 att
Wartortle (level 2): 8 hp 13 att
Blastoise (level 3): 15 hp 25 att
Charmandar (level 1): 3 hp 8 att
Charmeleon (level 2): 6 hp 15 att
Charizard (level 3): 11 hp 29 att'''
def raidfight(team,boss,pokemons):
    pass
    

def catchp(caught):
    ca = random.randint(1,3)
    cau = random.randint(1,4)
    if caught == 100:
        print("OH MY GOD! YOU CAUGHT A LEVEL 3 RAICHU!!!")
        return 'omg'
    elif caught == 99 or caught == 98:
        if ca == 1:
            print("AWESOME! YOU CAUGHT A LEVEL 3 VENUSAUR!!!")
            return 'a'
        elif ca == 2:
            print("AMAZING! YOU CAUGHT A LEVEL 3 BLASTOISE!!!")
            return 'b'
        else:
            print("UNBELIEVABLE! YOU CAUGHT A LEVEL 3 CHARIZARD!!!")
            return 'c'
    elif caught <= 97 and caught >= 81:
        if ca == 1:
            print("Great! You caught a Level 2 ivysaur!!")
            return 'd'
        elif ca == 2:
            print("Nice! You caught a Level 2 wartortle!!")
            return 'e'
        else:
            print("Wow! You caught a Level 2 charmeleon!!")
            return 'f'
    else:
        if cau == 1:
            print("You caught a level 1 pikachu!")
            return 'g'
        elif cau == 2:
            print("You caught a level 1 bulbasaur!")
            return 'h'
        elif cau == 3:
            print("You caught a level 1 squirtle!")
            return 'i'
        else:
            print("You caught a level 1 charmandar!")
            return 'j'
            

while 1:
    time.sleep(1.5)
    sp = input('Which pokemon do you want to start off with? \n [a] Pikachu (6 hp 5 att) \n [b] Bulbasaur (8 hp 3 att) \n [c] Squirtle (4 hp 7 att) \n [d] Charmandar (3 hp 8 att) \n> ')
    time.sleep(1)
    if sp == 'a':
        print('Pikachu!')
        npikachu = npikachu + 1
        break
    elif sp == 'b':
        print('Bulbasaur!')
        nbulbasaur = nbulbasaur + 1
        break
    elif sp == 'c':
        print('Squirtle!')
        nsquirtle = nsquirtle + 1
        break
    elif sp == 'd':
        print('Charmandar!')
        ncharmandar = ncharmandar + 1
        break
    else:
        print('Invalid, try again')
time.sleep(1.5)
while 1:
    pokemons = {'pikachu':npikachu,'raichu':nraichu,'bulbasaur':nbulbasaur,'ivysaur':nivysaur,'venusaur':nvenusaur,'squirtle':nsquirtle,'wartortle':nwartortle,'blastoise':nblastoise,'charmandar':ncharmandar,'charmeleon':ncharmeleon,'charizard':ncharizard}
    strteam = str(team)
    strteam.replace("'","")
    strteam.replace("[","")
    strteam.replace("]","")
    time.sleep(1)
    something = random.randint(3,7)
    time.sleep(1.5)
    if prestige >= 75:
        caught = 1
    else:
        caught = random.randint(25,100-prestige)
    petchance = random.randint(1,2)
    w = input('What do you want to do? \n[a] Search for pokemon to catch \n[b] Search for materials \n[c] Search for raids to fight in \n[d] Go home \n[e] See pokemon descriptions \n[f] Change your team \n[g] Sell pokemons \n[h] Manage your pets \n[i] prestige \n> ')
    if w == 'a':
            if pokeball == 0 and greatball == 0 and ultraball == 0:
                print('You have no pokeballs')
            else:
                ps = random.randint(1,300-train)
                if ps <= 200:
                    time.sleep(0.75)
                    print('You hear rusling in the leaves...')
                    time.sleep(0.75)
                    if prestige >= something:
                        po = 1
                    else:
                        po = random.randint(1,something-prestige)
                    if po == 1:
                        if prestige >= 75:
                            caught = 1
                        else:
                            caught = random.randint(25,100-prestige)
                        if prestige >= 20:
                            catch = 1
                        else:
                            catch = random.randint(1,20 - prestige)
                        use = input("There's a wild pokemon! Which ball do you want to use to try to catch it?\n[a] Pokeball (" + 'pokeball' + ") \n[b] Greatball (" + 'greatball' + ")\n[c] Ultraball (" + 'ultraball' + ")\n> ")
                        if use == 'a':
                            if pokeball == 0:
                                print('You have no pokeballs! The pokemon ran away. Next time, check your inventory before you select.')
                            else:
                                if catch <= 10:
                                    c = catchp(caught)
                                    if c == 'omg':
                                        nraichu += 1
                                    elif c == 'a':
                                        nvenusaur += 1
                                    elif c == 'b':
                                        nblastoise += 1
                                    elif c == 'c':
                                        ncharizard += 1
                                    elif c == 'd':
                                        nivysaur += 1
                                    elif c == 'e':
                                        nwartortle += 1
                                    elif c == 'f':
                                        ncharmeleon += 1
                                    elif c == 'g':
                                        npikachu += 1
                                    elif c == 'h':
                                        nbulbasaur += 1
                                    elif c == 'i':
                                        nsquirtle += 1
                                    else:
                                        ncharmandar += 1
                                else:
                                    print('You missed, and it ran away!')
                            pokeball = pokeball - 1
                        elif use == 'b':
                            if pokeball == 0:
                                print('You have no greatballs! The pokemon ran away. Next time, check your inventory before you select.')
                            else:
                                if catch <= 15:
                                    c = catchp(caught)
                                    if c == 'omg':
                                        nraichu += 1
                                    elif c == 'a':
                                        nvenusaur += 1
                                    elif c == 'b':
                                        nblastoise += 1
                                    elif c == 'c':
                                        ncharizard += 1
                                    elif c == 'd':
                                        nivysaur += 1
                                    elif c == 'e':
                                        nwartortle += 1
                                    elif c == 'f':
                                        ncharmeleon += 1
                                    elif c == 'g':
                                        npikachu += 1
                                    elif c == 'h':
                                        nbulbasaur += 1
                                    elif c == 'i':
                                        nsquirtle += 1
                                    else:
                                        ncharmandar += 1
                                else:
                                    print('You missed, and it ran away!')
                            greatball = greatball - 1
                        elif use == 'c':
                            if pokeball == 0:
                                print('You have no ultraballs! The pokemon ran away. Next time, check your inventory before you select.')
                            else:
                                if catch <= 19:
                                    c = catchp(caught)
                                    if c == 'omg':
                                        nraichu += 1
                                    elif c == 'a':
                                        nvenusaur += 1
                                    elif c == 'b':
                                        nblastoise += 1
                                    elif c == 'c':
                                        ncharizard += 1
                                    elif c == 'd':
                                        nivysaur += 1
                                    elif c == 'e':
                                        nwartortle += 1
                                    elif c == 'f':
                                        ncharmeleon += 1
                                    elif c == 'g':
                                        npikachu += 1
                                    elif c == 'h':
                                        nbulbasaur += 1
                                    elif c == 'i':
                                        nsquirtle += 1
                                    else:
                                        ncharmandar += 1
                                else:
                                    print('You missed, and it ran away!')
                            ultraball = ultraball - 1
                        else:
                            print('On your next oppertunity, make sure you select one of the choices.')
                    else:
                        time.sleep(0.75)
                        print('...but it was only the wind.')
                else:
                    time.sleep(0.75)
                    print('''You searched everywhere, but you can't find anything.''')
            
    elif w == 'b':
        search = input('Where would you search? \n[a] The city \n[b] The forest \n[c] The lake \n[d] The desert \n[e] The mountain \n> ')
        chance = random.randint(1-prestige,840-train)
        if chance > 350:
            print('You searched hard, but you found nothing.')
        else:
            if search == 'a':
                print('You searched the city...')
                time.sleep(2)
                if chance > 300 and chance <=350:
                    print('You found 3 dollars dropped by some careless person.')
                    money += 3
                elif chance > 200 and chance <= 300:
                    print('You found a pokeball now why did you find it in the trash can.')
                    pokeball += 1
                elif chance > 175 and chance <= 200:
                    print('You found a greatball in a chicken coop... someone must have thought it was an egg.')
                    greatball += 1
                elif chance > 100 and chance <= 175:
                    print('You were searching, but apparently you decided to go to a theme park nearby.')
                elif chance > 3 and chance <= 100:
                    rustle = input('You were searching, but you hear rustling in the leaves. What do you do? \n[a] Ignore it \n[b] Check it out \n> ')
                    time.sleep(1)
                    if rustle == 'a':
                        print('You kept searching, but you found nothing.')
                    else:
                        if something == 5:
                            print('''Wow! a pokemon jumped out, and you caught it without a pokeball! Let's see what you caught...''')
                            c = catchp(caught)
                            if c == 'omg':
                                nraichu += 1
                            elif c == 'a':
                                nvenusaur += 1
                            elif c == 'b':
                                nblastoise += 1
                            elif c == 'c':
                                ncharizard += 1
                            elif c == 'd':
                                nivysaur += 1
                            elif c == 'e':
                                nwartortle += 1
                            elif c == 'f':
                                ncharmeleon += 1
                            elif c == 'g':
                                npikachu += 1
                            elif c == 'h':
                                nbulbasaur += 1
                            elif c == 'i':
                                nsquirtle += 1
                            else:
                                ncharmandar += 1
                        else:
                            print('''It was just some birds. You decide to have a picnic next to that tree.''')
                else:
                    print("WAIT WHAT'S THIS??? YOU FOUND A DOG! DOES IT LIKE YOU?")
                    time.sleep(1)
                    if petchance == 1:
                        if 'dog' in pets:
                            print('It licks your face! You decide to give it back to its owner. You already have a dog anyway.')
                        else:
                            print("IT DOES! YOU GET A NEW PET!")
                            pets.append('dog')
                    else:
                        print('''It's growling at you. You decide to get out of the way.''')
            elif search == 'b':
                print('You searched the forest...')
                time.sleep(2)
                if chance > 300 and chance <=350:
                    print('''You found a greatball, nice find (but the concerning thing is that you found it in a bird's nest).''')
                    greatball += 1
                elif chance > 200 and chance <= 300:
                    print('You found a pokeball... but it had landed on your head.')
                    pokeball += 1
                elif chance > 175 and chance <= 200:
                    print('You found an ultraball! But is that a baby bird in it...?')
                    ultraball += 1
                elif chance > 100 and chance <= 175:
                    print('You were searching, but you found a nice fruit tree and ate.')
                elif chance > 3 and chance <= 100:
                    rustle = input('You were searching, but you hear rustling in the leaves. What do you do? \n[a] Ignore it \n[b] Check it out \n> ')
                    time.sleep(1)
                    if rustle == 'a':
                        print('You kept searching, but you found nothing.')
                    else:
                        if something == 5:
                            print('''Wow! a pokemon jumped out, and you caught it without a pokeball! Let's see what you caught...''')
                            c = catchp(caught)
                            if c == 'omg':
                                nraichu += 1
                            elif c == 'a':
                                nvenusaur += 1
                            elif c == 'b':
                                nblastoise += 1
                            elif c == 'c':
                                ncharizard += 1
                            elif c == 'd':
                                nivysaur += 1
                            elif c == 'e':
                                nwartortle += 1
                            elif c == 'f':
                                ncharmeleon += 1
                            elif c == 'g':
                                npikachu += 1
                            elif c == 'h':
                                nbulbasaur += 1
                            elif c == 'i':
                                nsquirtle += 1
                            else:
                                ncharmandar += 1
                        else:
                            print('''It was just the wind. You decide to have a picnic next to that tree.''')
                else:
                    time.sleep(1)
                    print("WAIT WHAT'S THIS??? YOU FOUND A MONKEY! DOES IT LIKE YOU?")
                    if petchance == 1:
                        if 'monkey' in pets:
                            print('It likes you! But two monkeys are too much to take care of, so you leave it behind.')
                        else:
                            print("IT DOES! YOU GET A NEW PET!")
                            pets.append('monkey')
                    else:
                        print('''It throws mangoes at you. You catch a few then run away.''')
            elif search == 'c':
                print('You searched the lake...')
                time.sleep(2)
                if chance > 300 and chance <=350:
                    print('You found 2 dollars worth of coins at the bottom of the lake.')
                    money += 2
                elif chance > 200 and chance <= 300:
                    print('You found a greatball why did the fish try to eat it.')
                    greatball += 1
                elif chance > 175 and chance <= 200:
                    print('You found a pokeball, but it is covered in mud.')
                    pokeball += 1
                elif chance > 3 and chance <= 100:
                    print('You were searching, but you got distracted by some fish.')
                elif chance > 100 and chance <= 175:
                    rustle = input('You were searching, but you see rustling in the kelp. What do you do? \n[a] Ignore it \n[b] Check it out \n> ')
                    time.sleep(1)
                    if rustle == 'a':
                        print('You kept searching, but you found nothing.')
                    else:
                        if something == 5:
                            print('''Wow! a pokemon jumped out, and you caught it without a pokeball! Let's see what you caught...''')
                            c = catchp(caught)
                            if c == 'omg':
                                nraichu += 1
                            elif c == 'a':
                                nvenusaur += 1
                            elif c == 'b':
                                nblastoise += 1
                            elif c == 'c':
                                ncharizard += 1
                            elif c == 'd':
                                nivysaur += 1
                            elif c == 'e':
                                nwartortle += 1
                            elif c == 'f':
                                ncharmeleon += 1
                            elif c == 'g':
                                npikachu += 1
                            elif c == 'h':
                                nbulbasaur += 1
                            elif c == 'i':
                                nsquirtle += 1
                            else:
                                ncharmandar += 1
                        else:
                            print('''It was just a wave. You decide to get out of the water since you might get entangled in the kelp.''')
                else:
                    print("WAIT WHAT'S THIS??? YOU FOUND A TURTE! DOES IT LIKE YOU?")
                    time.sleep(1)
                    if petchance == 1:
                        if 'turtle' in pets:
                            print("It plays tag with you, but you have to leave it behind.")
                        else:
                            print("IT DOES! YOU GET A NEW PET!")
                            pets.append('turtle')
                    else:
                        print('''It's runs away. I guess it's not in a playful mood.''')


            elif search == 'd':
                print('You searched the desert...')
                time.sleep(2)
                if chance > 300 and chance <=350:
                    print('You found 3 dollars... why would there be a purse in the middle of the desert?')
                    money += 3
                elif chance > 200 and chance <= 300:
                    print('You found a pokeball in an oasis.')
                    pokeball += 1
                elif chance > 175 and chance <= 200:
                    print('You found a greatball stuck on a cactus... you accidetally poked yourself getting it down. Ouch!')
                    greatball += 1
                elif chance > 100 and chance <= 175:
                    print('You were searching, but apparently it was too hot and you rested in the shade drinking water.')
                elif chance > 3 and chance <= 100:
                    rustle = input('You were searching, but you see the sand moving. What do you do? \n[a] Ignore it \n[b] Check it out \n> ')
                    time.sleep(1)
                    if rustle == 'a':
                        print('You kept searching, but you found nothing.')
                    else:
                        if something == 5:
                            print('''Wow! a pokemon jumped out, and you caught it without a pokeball! Let's see what you caught...''')
                            c = catchp(caught)
                            if c == 'omg':
                                nraichu += 1
                            elif c == 'a':
                                nvenusaur += 1
                            elif c == 'b':
                                nblastoise += 1
                            elif c == 'c':
                                ncharizard += 1
                            elif c == 'd':
                                nivysaur += 1
                            elif c == 'e':
                                nwartortle += 1
                            elif c == 'f':
                                ncharmeleon += 1
                            elif c == 'g':
                                npikachu += 1
                            elif c == 'h':
                                nbulbasaur += 1
                            elif c == 'i':
                                nsquirtle += 1
                            else:
                                ncharmandar += 1
                        else:
                            print('''It was just a desert rat. You decide to follow it, but it led you too far so you went back.''')
                else:
                    print("WAIT WHAT'S THIS??? YOU FOUND A CAMEL! DOES IT LIKE YOU?")
                    if petchance == 1:
                        if 'camel' in pets:
                            print("You and the camel start running around, but the the camel was too fast and you lost sight of it.")
                        else:
                            print("IT DOES! YOU GET A NEW PET!")
                            pets.append('camel')
                    else:
                        print('''It looks annoyed. You go away.''')
            elif search == 'e':
                print('You searched the mountain...')
                time.sleep(2)
                if chance > 300 and chance <=350:
                    print('You found 5 dollars worth of gold in the gravel next to a river.')
                    money += 5
                elif chance > 200 and chance <= 300:
                    print('You found 2 dollars hmm why was it under a foot of snow.')
                    money += 2
                elif chance > 175 and chance <= 200:
                    print('You found an ultraball under a large rock, but it took you forever to lift.')
                    ultraball += 1
                elif chance > 100 and chance <= 175:
                    print('You were searching, but apparently you decided to go to a theme park nearby.')
                elif chance > 3 and chance <= 100:
                    rustle = input('You were searching, but you see some stirring in the rock. What do you do? \n[a] Ignore it \n[b] Check it out \n> ')
                    time.sleep(1)
                    if rustle == 'a':
                        print('You kept searching, but you found nothing.')
                    else:
                        if something == 5:
                            print('''Wow! a pokemon jumped out, and you caught it without a pokeball! Let's see what you caught...''')
                            c = catchp(caught)
                            if c == 'omg':
                                nraichu += 1
                            elif c == 'a':
                                nvenusaur += 1
                            elif c == 'b':
                                nblastoise += 1
                            elif c == 'c':
                                ncharizard += 1
                            elif c == 'd':
                                nivysaur += 1
                            elif c == 'e':
                                nwartortle += 1
                            elif c == 'f':
                                ncharmeleon += 1
                            elif c == 'g':
                                npikachu += 1
                            elif c == 'h':
                                nbulbasaur += 1
                            elif c == 'i':
                                nsquirtle += 1
                            else:
                                ncharmandar += 1
                        else:
                            print('''The rock was just a bit unstable. You run away in case if the rock crashed down.''')
                else:
                    print("WAIT WHAT'S THIS??? YOU FOUND A GOAT! DOES IT LIKE YOU?")
                    if petchance == 1:
                        if 'goat' in pets:
                            print('It kicks up some dirt, then disappeared.')
                        else:
                            print("IT DOES! YOU GET A NEW PET!")
                            pets.append('goat')
                    else:
                        print('''It ran away. You're too scared of falling down to chase it.''')
    elif w == 'c':
        if team == [] or team == ['Your team is empty. Add pokemons to your team.']:
            print('''Your team is empty, and you can't do a raid without a team.''')
        else:
            pr = random.randint(1,10)
            rb = random.randint(1,9)
            if pr == 1:
                print('You hear a rumble.')
    elif w == 'd':
        inv = '''Welcome home! Here are your
Pokemons:
Pikachu: {}
Raichu: {}
Bulbasaur: {}
Ivysaur: {}
Venusaur: {}
Squirtle: {}
Wartortle: {}
Blastoise: {}
Charmandar: {}
Charmeleon: {}
Charizard: {}

Pokeballs:
Pokeball: {}
Greatball: {}
ultraball: {}

Team: {}

Money: {}

Prestige: {}'''.format(npikachu,nraichu,nbulbasaur,nivysaur,nvenusaur,nsquirtle,nwartortle,nblastoise,ncharmandar,ncharmeleon,ncharizard,pokeball,greatball,ultraball,strteam,money,prestige)
        print(inv)
    elif w == 'e':
        print(desc)
    elif w == 'f':
        while 1:
            time.sleep(1)
            print('Your current team: ' + str(team) +'.')
            time.sleep(1)
            if team == ['Your team is empty. Add pokemons to your team.']:
                team = []
            choice = input('Type c to change team. Type anything else to exit. \n> ')
            if choice == 'c':
                addpok = input('What pokemon would you like to add to your team? Type x to exit \n> ')
                if addpok == 'x':
                    break
                if addpok in pokemons:
                    if pokemons[addpok] == 0:
                        print('You do not own this pokemon.')
                    else:
                        if len(team) == 3:
                            replace = input('Your team has the maximum amount of pokemons! What position on your team would you like the new pokemon to replace (1-3)? Type x to exit. \n> ')
                            if replace == 'x':
                                break
                            while 1:
                                try:    
                                    replace = int(replace)
                                except:
                                    print('Invalid, try again.')
                                    replace = input('Your team has the maximum amount of pokemons! What position on your team would you like the new pokemon to replace? Type x to exit. \n> ')
                            while replace > 3 or replace < 1 and replace != 'x':
                                print('Enter an integer between 1 and 3 inclusive.')
                                replace = input('Your team has the maximum amount of pokemons! What position on your team would you like the new pokemon to replace? Type x to exit. \n> ')
                            if team[replace] == 'pikachu':
                                npikachu = npikachu + 1
                            elif team[replace] == 'bulbasaur':
                                nbulbasaur = nbulbasaur + 1
                            elif team[replace] == 'squirtle':
                                nsquirtle = nsquirtle + 1
                            elif team[replace] == 'charmandar':
                                ncharmandar = ncharmandar + 1
                            elif team[replace] == 'raichu':
                                nraichu = nraichu + 1
                            elif team[replace] == 'ivysaur':
                                nivysaur = nivysaur + 1
                            elif team[replace] == 'blastoise':
                                nblastoise = nblastoise + 1
                            elif team[replace] == 'charizard':
                                ncharizard += 1
                            elif team[replace] == 'venusaur':
                                nvenusaur += 1
                            elif team[replace] == 'charmeleon':
                                ncharmeleon += 1
                            else:
                                nwartortle += 1
                            team[replace] = addpok
                        else:
                            team.append(addpok)
                        if addpok == 'pikachu':
                            npikachu = npikachu - 1
                        elif addpok == 'bulbasaur':
                            nbulbasaur = nbulbasaur - 1
                        elif addpok == 'squirtle':
                            nsquirtle = nsquirtle - 1
                        elif addpok == 'charmandar':
                            ncharmandar = ncharmandar - 1
                        elif addpok == 'raichu':
                            nraichu = nraichu - 1
                        elif addpok == 'ivysaur':
                            nivysaur = nivysaur - 1
                        elif addpok == 'blastoise':
                            nblastoise = nblastoise - 1
                        elif addpok == 'charizard':
                            ncharizard -= 1
                        elif addpok == 'venusaur':
                            nvenusaur -= 1
                        elif addpok == 'charmeleon':
                            ncharmeleon -= 1
                        else:
                            nwartortle -= 1
                        print('You have successfully changed your team.')
                else:
                    print('This pokemon does not exist.')
            else:
                break
    elif w == 'g':
        print('''Level 1 pokemons sell for 3 dollars. Level 2 pokemons sell for 10 dollars. Level 3 pokemons sell for 25 dollars.''')
        time.sleep(2)
        sell = input('Which pokemon would you like to sell? \n> ')
        if sell in pokemons:
            if pokemons[sell] == 0:
                print('You do not own this pokemon.')
            else:
                count = input('How many copies of that pokemon would you like to sell? \n> ')
                while 1:
                    try:
                        count = int(count)
                        break
                    except:
                        print('Invaild, try again.')
                        count = input('How many copies of that pokemon would you like to sell? \n> ')
                if count > pokemons[sell]:
                    print("You do not have this many copies of that pokemon.")
                else:
                    zero = 0
                    for stat in stats[sell]:
                        zero += stat
                    if zero == 11:
                        money += 3*count
                    elif zero == 40:
                        money += 25*count
                    else:
                        money += 10*count
                    if sell == 'pikachu':
                        npikachu = npikachu - count
                    elif sell == 'bulbasaur':
                        nbulbasaur = nbulbasaur - count
                    elif sell == 'squirtle':
                        nsquirtle = nsquirtle - count
                    elif sell == 'charmandar':
                        ncharmandar = ncharmandar - count
                    elif sell == 'raichu':
                        nraichu = nraichu - count
                    elif sell == 'ivysaur':
                        nivysaur = nivysaur - count
                    elif sell == 'blastoise':
                        nblastoise = nblastoise - count
                    elif sell == 'charizard':
                        ncharizard -= count
                    elif sell == 'venusaur':
                        nvenusaur -= count
                    elif sell == 'charmeleon':
                        ncharmeleon -= count
                    else:
                        nwartortle -= count
                    print('You successfully sold your pokemons.')
        else:
            print('''The pokemon you're trying to sell does not exist.''')
    elif w == 'h':
        if pets == []:
            print('You do not have any pets yet.')
        else:
            print("Your pets: " + str(pets) + '.')
            if train == 0:
                action = input('What do you want to do with them? \n[a] Train them \n[b] Play with them \n[c] Feed them')
                if action == 'a':
                    print('You train them, slightly increasing your chances in searching.')
                    train += 5
                elif action == 'b':
                    prob = random.randint(1,35)
                    print('You play tag with your pets...')
                    time.sleep(2)
                    if prob == 1:
                        print('WOW!!! YOUR PETS CAUGHT A POKEMON FOR YOU...')
                        c = catchp(caught)
                        if c == 'omg':
                            nraichu += 1
                        elif c == 'a':
                            nvenusaur += 1
                        elif c == 'b':
                            nblastoise += 1
                        elif c == 'c':
                            ncharizard += 1
                        elif c == 'd':
                            nivysaur += 1
                        elif c == 'e':
                            nwartortle += 1
                        elif c == 'f':
                            ncharmeleon += 1
                        elif c == 'g':
                            npikachu += 1
                        elif c == 'h':
                            nbulbasaur += 1
                        elif c == 'i':
                            nsquirtle += 1
                        else:
                            ncharmandar += 1
                elif action == 'c':
                    print('You feed your pets.')
                else:
                    print('Invalid.')
            else:
                action = input('What do you want to do with them? \n[a] Play with them \n[a] Feed them')
                if action == 'a':
                    prob = random.randint(1,35)
                    print('You play tag with your pets...')
                    time.sleep(2)
                    if prob == 1:
                        print('WOW!!! YOUR PETS CAUGHT A POKEMON FOR YOU...')
                        c = catchp(caught)
                        if c == 'omg':
                            nraichu += 1
                        elif c == 'a':
                            nvenusaur += 1
                        elif c == 'b':
                            nblastoise += 1
                        elif c == 'c':
                            ncharizard += 1
                        elif c == 'd':
                            nivysaur += 1
                        elif c == 'e':
                            nwartortle += 1
                        elif c == 'f':
                            ncharmeleon += 1
                        elif c == 'g':
                            npikachu += 1
                        elif c == 'h':
                            nbulbasaur += 1
                        elif c == 'i':
                            nsquirtle += 1
                        else:
                            ncharmandar += 1
                elif action == 'b':
                    print('You feed your pets.')
                else:
                    print('Invalid.')
    elif w == 'i':
        print('You need 5000 dollars to prestige.')
        if money >= 5000:
            pres = input('Would you like to reset your progress and prestige? (y/n) \n> ')
            if pres == 'y':
                prest = input('Are you sure? (y/n) \n> ')
                if prest == 'y':
                    money = 0
                    train = 0
                    team = ['Your team is empty. Add pokemons to your team.']
                    pokeball = 20
                    greatball = 0
                    ultraball = 0
                    npikachu = 0
                    nraichu = 0
                    nbulbasaur = 0
                    nivysaur = 0
                    nvenusaur = 0
                    nsquirtle = 0
                    nwartortle = 0
                    nblastoise = 0
                    ncharmandar = 0
                    ncharmeleon = 0
                    ncharizard = 0
                    pets = []
                    prestige += 1
                    print('Congrats! You are on prestige ' + str(prestige) + '! Your chances are now slightly higher.')
                else:
                    print('You have decided not to prestige.')
            else:
                print('You have decided not to prestige')







            
                

                    
            
