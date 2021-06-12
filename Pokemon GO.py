import random
import time

money = 0
prestige = 0
team = ['Your team is empty. Add pokemons to your team.']
strteam = str(team)
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
pokemons = {'pikachu':npikachu,'raichu':nraichu,'bulbasaur':nbulbasaur,'ivysaur':nivysaur,'venusaur':nvenusaur,'squirtle':nsquirtle,'wartortle':nwartortle,'blastoise':nblastoise,'charamandar':ncharamandar,'charmeleon':ncharameleon,'charizard':ncharizard}
stats = {'pikachu':(6,5),'raichu':(20,20),'bulbasaur':(8,3),'ivysaur':(15,6),'venusaur':(30,10),'squirtle':(4,7),'wartortle':(8,13),'blastoise':(15,25),'charamandar':(3,8),'charmeleon':(6,15),'charizard':(11,29)}
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
def catch(caught):
    ca = random.randint(1,3)
    cau = random.randint(1,4)
    if caught == 100:
        print("OH MY GOD! YOU CAUGHT A LEVEL 3 RAICHU!!!")
        nraichu += 1
    elif caught == 99 or caught == 98:
        if ca == 1:
            print("AWESOME! YOU CAUGHT A LEVEL 3 VENUSAUR!!!")
            nvenusaur += 1
        elif ca == 2:
            print("AMAZING! YOU CAUGHT A LEVEL 3 BLASTOISE!!!")
            nblastoise += 1
        else:
            print("UNBELIEVABLE! YOU CAUGHT A LEVEL 3 CHARIZARD!!!")
            ncharizard += 1
    elif caught <= 97 and caught >= 81:
        if ca == 1:
            print("Great! You caught a Level 2 ivysaur!!")
            nivysaur += 1
        elif ca == 2:
            print("Nice! You caught a Level 2 wartortle!!")
            nwartortle += 1
        else:
            print("Wow! You caught a Level 2 charmeleon!!")
            ncharmeleon += 1
    else:
        if cau == 1:
            print("You caught a level 1 pikachu!")
            npikachu += 1
        elif cau == 2:
            print("You caught a level 1 bulbasaur!")
            nbulbasaur += 1
        elif cau == 3:
            print("You caught a level 1 squirtle!")
            nsquirtle += 1
        else:
            print("You caught a level 1 charmandar!")
            ncharmandar += 1
            


while 1:
    time.sleep(1)
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
    petchance = random.raindint(1,2)
    for x in strteam:
        if x == "'" or x == '[' or x == ']':
            strteam.replace(x,"")
    something = random.randint(3,7)
    time.sleep(1.5)
    w = input('What do you want to do? \n[a] Search for pokemon to catch \n[b] Search for materials \n[c] Search for raids to fight in \n[d] Go home \n[e] See pokemon descriptions \n[f] Change your team \n[g] Sell pokemons \n[h] Manage your pets \n[i] prestige \n> ')
    if w == 'a':
            if pokeball == 0 and greatball == 0 and ultraball == 0:
            print('You have no pokeballs')
    else:
        ps = random.randint(1,5)
        if ps <= 2:
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
                    catch = random.randint(1,20 - prestige)
                else:
                    catch = 1
                use = input("There's a wild pokemon! Which ball do you want to use to try to catch it?\n[a] Pokeball (" + 'pokeball' + ") \n[b] Greatball (" + 'greatball' + ")\n[c] Ultraball (" + 'ultraball' + ")\n> ")
                if use == 'a':
                    if pokeball == 0:
                        print('You have no pokeballs! The pokemon ran away. Next time, check your inventory before you select.')
                    else:
                        if catch <= 10:
                            catch(caught)
                        else:
                            print('You missed, and it ran away!')
                    pokeball = pokeball - 1
                elif use == 'b':
                    if pokeball == 0:
                        print('You have no greatballs! The pokemon ran away. Next time, check your inventory before you select.')
                    else:
                        if catch <= 15:
                            catch(caught)
                        else:
                            print('You missed, and it ran away!')
                    greatball = greatball - 1
                elif use == 'c':
                    if pokeball == 0:
                        print('You have no ultraballs! The pokemon ran away. Next time, check your inventory before you select.')
                    else:
                        if catch <= 19:
                            catch(caught)
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
        search = input('Where would you search? \n[a] The city \n[b] The forest \n[c] The lake \n[d] The desert \n[e] The mountain')
        chance = random.randint(1-prestige,840)
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
                    rustle = input('You were searching, but you hear rustling in the leaves. What do you do? \n[a] Ignore it \n[b] Check it out \n>')
                    time.sleep(1)
                    if rustle = 'a':
                        print('You kept searching, but you found nothing.')
                    else:
                        if something == 5:
                            print('''Wow! a pokemon jumped out, and you caught it without a pokeball! Let's see what you caught...''')
                            catch(caught)
                        else:
                            print('''It was just some birds. You decide to have a picnic next to that tree.''')
                else:
                    print("WAIT WHAT'S THIS??? YOU FOUND A DOG! DOES IT LIKE YOU?")
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
                    rustle = input('You were searching, but you hear rustling in the leaves. What do you do? \n[a] Ignore it \n[b] Check it out \n>')
                    time.sleep(1)
                    if rustle = 'a':
                        print('You kept searching, but you found nothing.')
                    else:
                        if something == 5:
                            print('''Wow! a pokemon jumped out, and you caught it without a pokeball! Let's see what you caught...''')
                            catch(caught)
                        else:
                            print('''It was just the wind. You decide to have a picnic next to that tree.''')
                else:
                    print("WAIT WHAT'S THIS??? YOU FOUND A MONKEY! DOES IT LIKE YOU?")
                    if petchance == 1:
                        if 'monkey' in pets:
                            print('Two monkeys are too much to take care of, so you leave it behind.')
                        else:
                            print("IT DOES! YOU GET A NEW PET!")
                            pets.append('monkey')
                    else:
                        print('''It's growling at you. You decide to get out of the way.''')
                        

            elif search == 'c':
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
                    rustle = input('You were searching, but you hear rustling in the leaves. What do you do? \n[a] Ignore it \n[b] Check it out \n>')
                    time.sleep(1)
                    if rustle = 'a':
                        print('You kept searching, but you found nothing.')
                    else:
                        if something == 5:
                            print('''Wow! a pokemon jumped out, and you caught it without a pokeball! Let's see what you caught...''')
                            catch(caught)
                        else:
                            print('''It was just some birds. You decide to have a picnic next to that tree.''')
                else:
                    print("WAIT WHAT'S THIS??? YOU FOUND A DOG! DOES IT LIKE YOU?")
                    if petchance == 1:
                        print("IT DOES! YOU GET A NEW PET!")
                        pets.append('dog')
                    else:
                        print('''It's growling at you. You decide to get out of the way.''')


            elif search == 'd':
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
                    rustle = input('You were searching, but you hear rustling in the leaves. What do you do? \n[a] Ignore it \n[b] Check it out \n>')
                    time.sleep(1)
                    if rustle = 'a':
                        print('You kept searching, but you found nothing.')
                    else:
                        if something == 5:
                            print('''Wow! a pokemon jumped out, and you caught it without a pokeball! Let's see what you caught...''')
                            catch(caught)
                        else:
                            print('''It was just some birds. You decide to have a picnic next to that tree.''')
                else:
                    print("WAIT WHAT'S THIS??? YOU FOUND A DOG! DOES IT LIKE YOU?")
                    if petchance == 1:
                        print("IT DOES! YOU GET A NEW PET!")
                        pets.append('dog')
                    else:
                        print('''It's growling at you. You decide to get out of the way.''')
            elif search == 'e':
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
                    rustle = input('You were searching, but you hear rustling in the leaves. What do you do? \n[a] Ignore it \n[b] Check it out \n>')
                    time.sleep(1)
                    if rustle = 'a':
                        print('You kept searching, but you found nothing.')
                    else:
                        if something == 5:
                            print('''Wow! a pokemon jumped out, and you caught it without a pokeball! Let's see what you caught...''')
                            catch(caught)
                        else:
                            print('''It was just some birds. You decide to have a picnic next to that tree.''')
                else:
                    print("WAIT WHAT'S THIS??? YOU FOUND A DOG! DOES IT LIKE YOU?")
                    if petchance == 1:
                        print("IT DOES! YOU GET A NEW PET!")
                        pets.append('dog')
                    else:
                        print('''It's growling at you. You decide to get out of the way.''')



                    
            
