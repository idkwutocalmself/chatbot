import random
import time
your_hp = 3
your_att = 3
print('You have decided to try to conquer a kingdom (because why not?)')
error = "Invalid selection, try again."
def battle(your_hp, enemy_hp,your_att,enemy_att):
    enh = 1.5 * your_att
    ep = 4 * your_att
    while your_hp > 0 and enemy_hp > 0:
        normal = random.randint(1,10)
        enhanced = random.randint(1,3)
        epic = random.randint(1,3)
        print('Your hp: '+str(your_hp))
        print('Enemy hp: '+str(enemy_hp))
        en = random.randint(1,10)
        attack = input('How would you like to attack? \n[a] Normal attack (100% att) (90% chance success) \n[b] Enhanced attack (150% att) (66.6% chance success) \n[c] Epic attack (400% att) (33.3% chance success) \n> ')
        if attack == 'a':
            if normal == 1:
                print('OOF, you failed.')
            else:
                enemy_hp = enemy_hp - your_att
                print('SUCCESS! Enemy lost '+str(your_att)+' hp')
            if enemy_hp <= 0:
                return 'win'
        elif attack == 'b':
            if enhanced == 1:
                print('OOF, you failed.')
            else:
                enemy_hp = enemy_hp - enh
                print('SUCCESS! Enemy lost '+str(enh)+' hp')
            if enemy_hp <= 0:
                return 'win'
        elif attack == 'c':
            if epic == 1:
                enemy_hp = enemy_hp - ep
                print('SUCCESS! Enemy lost '+str(ep)+' hp')
            else:
                print('OOF, you failed.')
            if enemy_hp <= 0:
                return 'win'
            
        else:
            print(error)
            return(battle(your_hp, enemy_hp,your_att,enemy_att))
            
        if en > 1:
            your_hp = your_hp - enemy_att
            print('Enemy hits you by '+str(enemy_att)+' hp')
        else:
            print("You managed to dodge your enemy's attack. Nice!")
                
        if your_hp <= 0:
            return 'lose'
        
           
def area1(your_hp, your_att):
    time.sleep(1)
    print('Welcome (or welcome back) to the first area of the kingdom.')
    while 1:
        print('Your hp: '+str(your_hp))
        print('Your att: '+str(your_att))
        enemy = input('Which enemy would you like to fight? \n[a] A cat (1 hp 1 att) \n[b] A cow (8 hp 3 att) \n[c] A lion (35 hp 10 att) \n[d] An elephant (90 hp 25 att) \n[e] A dragon (165 hp 50 att) \n> ')
        if enemy == 'a' or enemy == 'b' or enemy == 'c' or enemy == 'd' or enemy == 'e':
            if enemy == 'a':
                result = battle(your_hp,1,your_att,1)
                if result == 'win':
                    time.sleep(1)
                    print('Congrats, you have defeated your enemy, a cat. Your reward:')
                    chance = random.randint(1,2)
                    time.sleep(3)
                    if chance  == 1:
                        print("Nothing. Oof.")
                    if chance == 2:
                        print("+3 hp!")
                        your_hp += 3
                else:
                    time.sleep(1)
                    print('You were killed by a cat. Better luck next time!')
                    break

            elif enemy == 'b':
                result = battle(your_hp,8,your_att,3)
                if result == 'win':
                    time.sleep(1)
                    print('Congrats, you have defeated your enemy, a cow. Your reward:')
                    chance = random.randint(1,3)
                    time.sleep(3)
                    if chance  == 1:
                        print("Nothing. Oof.")
                    if chance == 2:
                        print("+3 hp!")
                        your_hp += 3
                    if chance == 3:
                        print('+3 att!')
                        your_att += 3
                else:
                    time.sleep(1)
                    print('You were killed by a cow. Better luck next time!')
                    break
                
            elif enemy == 'c':
                result = battle(your_hp,35,your_att,10)
                if result == 'win':
                    time.sleep(1)
                    print('Congrats, you have defeated your enemy, a lion. Your reward:')
                    chance = random.randint(1,4)
                    time.sleep(3)
                    if chance  == 1:
                        print("Nothing. Oof.")
                    if chance == 2:
                        print("+3 hp!")
                        your_hp += 3
                    if chance == 3:
                        print("+3 att!")
                        your_att += 3
                    if chance == 4:
                        print("YAY!!! +8 hp!")
                        your_hp += 8
                else:
                    time.sleep(1)
                    print('You were killed by a lion. Better luck next time!')
                    break
                
            elif enemy == 'd':
                result = battle(your_hp,90,your_att,25)
                if result == 'win':
                    time.sleep(1)
                    print('Congrats, you have defeated your enemy, an elephant. Your reward:')
                    chance = random.randint(1,5)
                    time.sleep(3)
                    if chance  == 1:
                        print("Nothing. Oof.")
                    if chance == 2:
                        print("+3 hp!")
                        your_hp += 3
                    if chance == 3:
                        print("+3 att!")
                        your_att += 3
                    if chance == 4:
                        print("YAY!!! +8 hp!")
                        your_hp += 8
                    if chance == 5:
                        print("YAY!!! +8 att!")
                        your_att += 8
                else:
                    time.sleep(1)
                    print('You were killed by a elephant. Better luck next time!')
                    break
                
            elif enemy == 'e':
                result = battle(your_hp,165,your_att,50)
                if result == 'win':
                    time.sleep(1)
                    print('Congrats, you have defeated your enemy, a dragon. Your reward:')
                    chance = random.randint(1,6)
                    time.sleep(3)
                    if chance  == 1:
                        print("Nothing. Oof.")
                    if chance == 2:
                        print("+3 hp!")
                        your_hp += 3
                    if chance == 3:
                        print("+3 att!")
                        your_att += 3
                    if chance == 4:
                        print("YAY!!! +8 hp!")
                        your_hp += 8
                    if chance == 5:
                        print("YAY!!! +8 att!")
                        your_att += 8
                    if chance == 6:
                        print("JACKPOT!!! +15 hp and +15 att! You have also unlocked the next area.")
                        your_hp += 15
                        your_att += 15
                        area2(your_hp,your_att)
                        your_hp = 50
                        your_att = 50
                else:
                    time.sleep(1)
                    print('You were killed by a dragon. Better luck next time!')
                    break
                
            else:
                print(error)
        time.sleep(3)

def area2(your_hp, your_att):
    time.sleep(2)
    print("Welcome (or welcome back) to area 2! You will face a new set of enemies in this area (and don't worry, you can still earn nothing from battles).")
    time.sleep(2)
    while 1:
        print('Your hp: '+str(your_hp))
        print('Your att: '+str(your_att))
        enemy = input('Which enemy would you like to fight? \n[a] A wizard (2000 hp 5 att) \n[b] An ent (2500 hp 10 att) \n[c] A tank (5000 hp 10 att) \n[d] A godzilla (3000 hp 35 att) \n[e] An enhanced dragon (2000 hp 300 att) \n> ')
        if enemy == 'a' or enemy == 'b' or enemy == 'c' or enemy == 'd' or enemy == 'e':
            if enemy == 'a':
                result = battle(your_hp,2000,your_att,5)
                if result == 'win':
                    time.sleep(1)
                    print('Congrats, you have defeated your enemy, a wizard. Your reward:')
                    chance = random.randint(1,2)
                    time.sleep(3)
                    if chance  == 1:
                        print("Nothing. Oof.")
                    if chance == 2:
                        print("+20 hp!")
                        your_hp += 20
                else:
                    time.sleep(1)
                    print('You were killed by a wizard. You have to go back to area 1, and your hp and att both decrease!')
                    return 1
       
            elif enemy == 'b':
                result = battle(your_hp,2500,your_att,10)
                if result == 'win':
                    time.sleep(1)
                    print('Congrats, you have defeated your enemy, an ent. Your reward:')
                    chance = random.randint(1,3)
                    time.sleep(3)
                    if chance  == 1:
                        print("Nothing. Oof.")
                    if chance == 2:
                        print("+20 hp!")
                        your_hp += 20
                    if chance == 3:
                        print('+20 att!')
                        your_att += 20
                else:
                    time.sleep(1)
                    print('You were killed by an ent. You have to go back to area 1, and your hp and att both decrease!')
                    return 1
                
            elif enemy == 'c':
                result = battle(your_hp,5000,your_att,10)
                if result == 'win':
                    time.sleep(1)
                    print('Congrats, you have defeated your enemy, a tank. Your reward:')
                    chance = random.randint(1,4)
                    time.sleep(3)
                    if chance  == 1:
                        print("Nothing. Oof.")
                    if chance == 2:
                        print("+20 hp!")
                        your_hp += 20
                    if chance == 3:
                        print("+20 att!")
                        your_att += 20
                    if chance == 4:
                        print("+15 hp and +15 att!")
                        your_hp += 15
                        your_att += 15
                else:
                    time.sleep(1)
                    print('You were killed by a tank. You have to go back to area 1, and your hp and att both decrease!')
                    return 1
                
            elif enemy == 'd':
                result = battle(your_hp,3000,your_att,35)
                if result == 'win':
                    time.sleep(1)
                    print('Congrats, you have defeated your enemy, a godzilla. Your reward:')
                    chance = random.randint(1,5)
                    time.sleep(3)
                    if chance  == 1:
                        print("Nothing. Oof.")
                    if chance == 2:
                        print("+20 hp!")
                        your_hp += 20
                    if chance == 3:
                        print("+20 att!")
                        your_att += 20
                    if chance == 4:
                        print("YAY!!! +40 hp!")
                        your_hp += 40
                    if chance == 5:
                        print("YAY!!! +40 att!")
                        your_att += 40
                else:
                    time.sleep(1)
                    print('You were killed by a godzilla. You have to go back to area 1, and your hp and att both decrease!')
                    return 1
                
            elif enemy == 'e':
                result = battle(your_hp,2000,your_att,300)
                if result == 'win':
                    time.sleep(1)
                    print('Congrats, you have defeated your enemy, an enhanced dragon. Your reward:')
                    chance = random.randint(1,6)
                    time.sleep(3)
                    if chance  == 1:
                        print("Nothing. Oof.")
                    if chance == 2:
                        print("+20 hp!")
                        your_hp += 20
                    if chance == 3:
                        print("+20 att!")
                        your_att += 20
                    if chance == 4:
                        print("YAY!!! +40 hp!")
                        your_hp += 40
                    if chance == 5:
                        print("YAY!!! +40 att!")
                        your_att += 40
                    if chance == 6:
                        print("JACKPOT!!! +60 hp and +60 att! You have also unlocked the next area.")
                        your_hp += 60
                        your_att += 60
                        area3(your_hp,your_att)
                        your_hp = 100
                        your_att = 100
                else:
                    time.sleep(1)
                    print('You were killed by an enhanced dragon. You have to go back to area 1, and your hp and att both decrease!')
                    return 1
                
            else:
                print(error)
        time.sleep(3)
        
def area3(your_hp, your_att):
    time.sleep(2)
    print("Welcome (or welcome back) to area 3! You will face a new set of enemies in this area (and don't worry, you can still earn nothing from battles).")
    time.sleep(2)
    while 1:
        print('Your hp: '+str(your_hp))
        print('Your att: '+str(your_att))
        enemy = input('Which enemy would you like to fight? \n[a] A killer robot (500 hp 400 att) \n[b] An attack helicopter (1000 hp 250 att) \n[c] A kraken (20000 hp 20 att) \n[d] A chimera (4000 hp 200 att) \n[e] An epic dragon (50000 hp 100 att) \n> ')
        if enemy == 'a' or enemy == 'b' or enemy == 'c' or enemy == 'd' or enemy == 'e':
            if enemy == 'a':
                result = battle(your_hp,500,your_att,300)
                if result == 'win':
                    time.sleep(1)
                    print('Congrats, you have defeated your enemy, a killer robot. Your reward:')
                    chance = random.randint(1,2)
                    time.sleep(3)
                    if chance  == 1:
                        print("Nothing. Oof.")
                    if chance == 2:
                        print("+50 hp!")
                        your_hp += 50
                else:
                    time.sleep(1)
                    print('You were killed by a killer robot. You have to go back to area 2, and your hp and att both decrease!')
                    return 1
       
            elif enemy == 'b':
                result = battle(your_hp,1000,your_att,250)
                if result == 'win':
                    time.sleep(1)
                    print('Congrats, you have defeated your enemy, an ent. Your reward:')
                    chance = random.randint(1,3)
                    time.sleep(3)
                    if chance  == 1:
                        print("Nothing. Oof.")
                    if chance == 2:
                        print("+50 hp!")
                        your_hp += 50
                    if chance == 3:
                        print('+50 att!')
                        your_att += 50
                else:
                    time.sleep(1)
                    print('You were killed by an ent. You have to go back to area 2, and your hp and att both decrease!')
                    return 1
                
            elif enemy == 'c':
                result = battle(your_hp,20000,your_att,20)
                if result == 'win':
                    time.sleep(1)
                    print('Congrats, you have defeated your enemy, a kraken. Your reward:')
                    chance = random.randint(1,4)
                    time.sleep(3)
                    if chance  == 1:
                        print("Nothing. Oof.")
                    if chance == 2:
                        print("+50 hp!")
                        your_hp += 50
                    if chance == 3:
                        print("+50 att!")
                        your_att += 50
                    if chance == 4:
                        print("+35 hp and +35 att!")
                        your_hp += 35
                        your_att += 35
                else:
                    time.sleep(1)
                    print('You were killed by a kraken. You have to go back to area 2, and your hp and att both decrease!')
                    return 1
                
            elif enemy == 'd':
                result = battle(your_hp,4000,your_att,200)
                if result == 'win':
                    time.sleep(1)
                    print('Congrats, you have defeated your enemy, a chimera. Your reward:')
                    chance = random.randint(1,5)
                    time.sleep(3)
                    if chance  == 1:
                        print("Nothing. Oof.")
                    if chance == 2:
                        print("+50 hp!")
                        your_hp += 50
                    if chance == 3:
                        print("+50 att!")
                        your_att += 50
                    if chance == 4:
                        print("YAY!!! +75 hp!")
                        your_hp += 75
                    if chance == 5:
                        print("YAY!!! +75 att!")
                        your_att += 75
                else:
                    time.sleep(1)
                    print('You were killed by a chimera. You have to go back to area 2, and your hp and att both decrease!')
                    return 1
                
            elif enemy == 'e':
                result = battle(your_hp,50000,your_att,100)
                if result == 'win':
                    time.sleep(1)
                    print('Congrats, you have defeated your enemy, an epic dragon. Your reward:')
                    chance = random.randint(1,6)
                    time.sleep(3)
                    if chance  == 1:
                        print("Nothing. Oof.")
                    if chance == 2:
                        print("+50 hp!")
                        your_hp += 50
                    if chance == 3:
                        print("+50 att!")
                        your_att += 50
                    if chance == 4:
                        print("YAY!!! +75 hp!")
                        your_hp += 75
                    if chance == 5:
                        print("YAY!!! +75 att!")
                        your_att += 75
                    if chance == 6:
                        print("JACKPOT!!! +100 hp and +100 att!")
                        your_hp += 100
                        your_att += 100
                        if your_hp >= 5000 and your_att >= 5000:
                            time.sleep(3)
                            print('You hear a crash as you kill the epic dragon. The boss dragon is coming!')
                            time.sleep(3)
                            print('BOSS DRAGON: Impressive! You have defeated all of your other enemies. You were so close to conquering this kingdom, but yet so far. You have to defeat me first! MWAHAHAHA!')
                            time.sleep(5)
                            print("BOSS DRAGON: This battle isn't like all your other battles. Your stats wouldn't matter. I hope you're ready!")
                            time.sleep(4)
                            print('BOSS DRAGON: Consider yourself lucky to get here at all.')
                            time.sleep(2)
                            input('Press Enter to continue to your FINAL BATTLE')
                            time.sleep(1)
                            result = finalbattle(1000, 1000, 100)
                            if result == 'win':
                                print('''BOSS DRAGON: WOW you're good! This kingdom is officially yours.''')
                                time.sleep(1)
                                print('But unfortunately, unless you want to keep playing, this game is over now.')
                                time.sleep(2)
                            else:
                                print('BOSS DRAGON: WAHAHAHA! You were defeated! NOW GO BACK TO AREA 2, AND TRY AGAIN!')
                                return 1
                        else:
                            print('To continue to your final battle, make sure that your hp and attack are both at or above 5000.')
                else:
                    time.sleep(1)
                    print('You were killed by an epic dragon. You have to go back to area 2, and your hp and att both decrease!')
                    return 1
            else:
                print(error)
        time.sleep(3)

def finalbattle(your_hp,enemy_hp,enemy_att):
    while 1:
        mysterybox = random.randint(1,5)
        lifesteald = 30
        lifestealh = 30
        turnpass = False
        print('Your hp: '+str(your_hp))
        print('Enemy hp: '+str(enemy_hp))
        print('Enemy att: '+str(enemy_att))
        attack = input("What would you do? \n[a] Lifesteal (steals hp from the BOSS DRAGON) \n[b] Sabotage (decreases enemy attack by 10%) \n[c] Open mystery box (contains something, but you don't know what it is) \n> ")
        if attack == 'a':
            print('You have successfully stole hp from the BOSS DRAGON.')
            enemy_hp = enemy_hp - lifesteald
            your_hp = your_hp + lifestealh

        elif attack == 'b':
            print('''You have successfully decreased the BOSS DRAGON's att.''')
            enemy_att = 0.9*enemy_att

        elif attack == 'c':
            if mysterybox == 1:
                print('Lifesteal damage increased by 7!')
                lifesteald += 7
            elif mysterybox == 2:
                print('Lifesteal heal increased by 7!')
                lifestealh += 7
            elif mysterybox == 3:
                print('BOSS DRAGON att decreases by 20%!')
                enemy_att = 0.8 * enemy_att
            elif mysterybox == 4:
                print('Oh no! The BOSS DRAGON stole the box and increased its att by 10!')
                enemy_att += 10
            else:
                print('You get another turn.')
                turnpass = True
        else:
            print(error)
            return finalbattle(your_hp,enemy_hp,enemy_att)
        if enemy_hp <= 0:
            return 'win'
        if turnpass == True:
            pass
        else:
            print('You lost ' + str(enemy_att) + ' hp.')
            your_hp = your_hp - enemy_att
        if your_hp <= 0:
            return 'lose'

area1(3,3)
