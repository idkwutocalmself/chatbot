import random
import time
money = 0
p = 0
rods = ['wood rod']
rod = 'wood rod'
bait = 50
h = "fish (f), shop (s), money (m), rods (r), prestige (p), coinflip (cf), bait (b)"
fishes = {'shrimp':1, 'trout':10, 'squid':50, 'jellyfish':250, 'stingray':1000, 'pufferfish':5000, 'swordfish': 25000, 'shark':100000, 'whale':500000, 'kraken':2500000}
shop = {'plastic rod':500,   'steel rod':5000,   'fiberglass rod':100000,   'titanium rod':500000,   'bronze rod':2500000,   'silver rod':25000000,   'golden rod':100000000,   'diamond rod':500000000,   'infinity rod': 2500000000}     
print(h)
while 1:
    print('Type your command:')
    c = input()
    if money < 5 and bait == 0:
        print('Oh no! You have no bait to go fishing and you do not have enough money to buy bait! You will have to restart!')
        break
    time.sleep(0.1)
    if c == 'h':
        print(h)
    elif c == 'fish' or c == 'f':
        print('You go fishing. You caught: ')
        time.sleep(2)
        caught = ''
        sold = money
        try:
            chestchance = random.randint(1,25-p)
        except:
            chestchance = 1
        chestquality = random.randint(1,26+p)
        if bait == 0:
            print('You are out of bait. Go buy some bait from the bait shop. You cannot fish without bait.')
        else:
            if rod == 'wood rod':
                for x in range(0,4+p):
                    w2 = random.randint(1,8)
                    if w2 >= 6 :
                        caught += 'A shrimp. '
                        money += 1
                    if w2 >=2 and w2 <= 5:
                        caught += 'A trout. '
                        money += 10
                    if w2 == 1:
                        caught += 'A squid. '
                        money += 50
                        
            if rod == 'plastic rod':
                for x in range(0,6+p):
                    w2 = random.randint(1,10)
                    if w2 == 6 or w2 == 7:
                        caught += 'A shrimp. '
                        money += 1
                    if w2 >=2 and w2 <= 5:
                        caught += 'A trout. '
                        money += 10
                    if w2 == 1 or w2 == 9 or w2 == 8:
                        caught += 'A squid. '
                        money += 50
                    if w2 == 10:
                        caught += 'A jellyfish. '
                        money += 250
                        

            if rod == 'steel rod':
                for x in range(0,8+p):
                    w2 = random.randint(1,12+p)
                    if w2 == 1:
                        caught += 'A trout. '
                        money += 10
                    if w2 > 1 and w2 <5:
                        caught += 'A squid. '
                        money += 50
                    if w2 > 5 and w2 <= 11:
                        caught += 'A jellyfish. '
                        money += 250
                    else:
                        caught += 'A stingray. '
                        money += 1000
            
            if rod == 'fiberglass rod':
                for x in range(0,10+p):
                    w2 = random.randint(1,12+p)
                    if w2 >= 1 and w2 < 4:
                        caught += 'A squid. '
                        money += 50
                    if w2 > 3 and w2 <= 8:
                        caught += 'A jellyfish. '
                        money += 250
                    else:
                        caught += 'A stingray. '
                        money += 1000

            if rod == 'titanium rod':
                for x in range(0,12+p):
                    w2 = random.randint(1,14+p)
                    if w2 >= 1 and w2 < 4:
                        caught += 'A jellyfish. '
                        money += 250
                    if w2 > 3 and w2 <= 13:
                        caught += 'A stingray. '
                        money += 1000
                    else:
                        caught += 'A pufferfish. '
                        money += 5000

            if rod == 'bronze rod':
                for x in range(0,14+p):
                    w2 = random.randint(1,16+p)
                    if w2 >= 1 and w2 < 6:
                        caught += 'A stingray. '
                        money += 1000
                    if w2 > 5 and w2 <= 15:
                        caught += 'A pufferfish. '
                        money += 5000
                    else:
                        caught += 'A swordfish. '
                        money += 25000
                        
            if rod == 'silver rod':
                for x in range(0,16+p):
                    w2 = random.randint(1,18+p)
                    if w2 >= 1 and w2 < 12:
                        caught += 'A swordfish. '
                        money += 25000
                    else:
                        caught += 'A shark. '
                        money += 100000
                
                        
            if rod == 'golden rod':
                for x in range(0,18+p):
                    w2 = random.randint(1,20+p)
                    if w2 >= 1 and w2 < 16:
                        caught += 'A shark. '
                        money += 100000
                    else:
                        caught += 'A whale. '
                        money += 500000

            if rod == 'diamond rod':
                for x in range(0,20+p):
                    w2 = random.randint(1,22+p)
                    if w2 >= 1 and w2 < 16:
                        caught += 'A whale. '
                        money += 500000
                    else:
                        caught += 'A kraken. '
                        money += 2500000

            if rod == 'infinity rod':
                for x in range(0,22+p):
                    w2 = random.randint(1,24+p)
                    if w2 >= 1 and w2 < 7:
                        caught += 'A whale. '
                        money += 500000
                    else:
                        caught += 'A kraken. '
                        money += 2500000
            print(caught)
            bait = bait - 1
            s = money - sold
            print("and you sold that for "+str(s)+" dollars.")
            if chestchance == 1:
                print('''And wait, what's this? You fished up a treasure chest!''')
                if chestquality <= 5:
                    print('...but it was empty.')
                elif chestquality > 5 and chestquality <= 10:
                    print('You opened it and found 50 bait in it! (Why would there be bait in a treasure chest...?') 
                    bait += 50
                elif chestquality > 10 and chestquality <= 25:
                    print('You opened it and found 5000 dollars!')
                    money += 5000
                else:
                    print('You opened it and found 250000 dollars!')
                    money += 250000
                          
    elif c == 'money' or c == 'm':
        print(money)
    
    elif c == 'shop' or c == 's':
        print(shop)
        print('Type the item you want to buy to buy it.')
        item = input()
        if item in shop.keys():
            if shop.get(item) > money:
                print('You do not have enough money to buy this!')
            else:
                rods.append(item)
                money = money-int(shop.get(item))
                shop.pop(item)
                print('You have successfully bought the '+item+'.')
        else:
            print('''What you are trying to buy isn't in the shop.''')

    elif c == 'r' or c == 'rods':
        print(rods)
        print('Your rod: '+rod+'. To switch rods, type the name of the rod you want to switch to.')
        new_rod = input()
        if new_rod in rods:
            rod = new_rod
            print('You have successfully switched rods.')
        else:
            print('You do not own this!')

    elif c == 'coinflip' or c == 'cf':
        print('How much would you like to bet?')
        bet = input()
        while 1:
            try:
                bet = int(bet)
                break
            except:
                if bet == 'all' or bet == 'max':
                    bet = money
                    break
                print('Please enter a positive integer instead')
                bet = int(input())
        if bet <= 0:
            print('Please enter a positive integer instead')
        else:
            if bet > money:
                print("You can't bet more than you have.")
            else:
                print('heads or tails?')
                hot = input()
                if hot != 'heads' and hot != 'tails':
                    print('Try again with heads or tails.')
                else:
                    prob = random.randint(1,2)
                    if prob == 1:
                        print('The coin landed on heads!')
                        if hot == 'tails':
                            print('You lost '+str(bet)+' dollars...')
                            money = money - bet
                        else:
                            print('You won '+str(bet)+' dollars!')
                            money += bet
                    else:
                        print('The coin landed on tails!')
                        if hot == 'tails':
                            print('You won '+str(bet)+' dollars!')
                            money += bet
                        else:
                            print('You lost '+str(bet)+' dollars...')
                            money = money - bet

    elif c == 'bait' or c == 'b':
        print('You have '+ str(bait) + ' bait right now. To buy more bait, type buy bait.')

    elif c == 'buy bait':
        print('How much bait do you want to buy? Each bait is 100 dollars.')
        amount = input()
        while 1:
            try:
                amount = int(amount)
                break
            except:
                print('Please enter a valid amount of bait.')
                amount = input()
        if 5*amount>money:
            print('You do not have enough money to buy this much bait.')
        else:
            money = money - 100*amount
            bait += amount
        
    elif c == 'p' or c == 'prestige':
        pres = 100000000000*(p+1)
        print('You need '+str(pres)+' dollars to prestige. To prestige, type reset')
        choice = input()
        if choice == 'reset':
            if money >= pres:
                ch = input('Are you sure you want to prestige and reset your progress? \n[y] yes \n[n] no n> ')
                if ch == 'y':
                    shop = {'plastic rod':500,   'steel rod':5000,   'fiberglass rod':30000,   'titanium rod':100000,   'bronze rod':500000,   'silver rod':5000000,  'golden rod':30000000,   'diamond rod':100000000,   'infinity rod': 1000000000}
                    rods = ['wood rod']
                    rod = 'wood rod'
                    p += 1
                    bait = 50
                    print('You have decided to reset your progress for a fishing boost.')
                else:
                    print('You decided not to prestige.')
            else:
                print("You haven't met the requirements to prestige yet.")

    else:
        print('Type h for a list of commands')
