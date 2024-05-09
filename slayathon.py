#Initializes stats
health = 0
healthmax = 0
gold = 0

looper = False

#difficulty selection,
difficulty = 0
def diff_select():
    global difficulty
    global health
    global healthmax
    global gold
    global looper
    
    #stats assigned here and modified in exo()
    health = 90
    healthmax = 90
    gold = 200
    
    if difficulty == 0:
        print("~~S-L-A-Y-A-T-H-O-N~~")
        print("")
        looperchoice = ""
        while True:
            looperchoice = input("Do you want chaining or single actions? ")
            looperchoice.lower()
            if "chain" in looperchoice:
                looper = True
                break
            elif "single" in looperchoice:
                break
    
    difficulty = input("Easy, Normal, or Hard? ")
    print("")
    difficulty = difficulty.upper()
    if "EASY" in difficulty:
        difficulty = 1
    elif "NORMAL" in difficulty:
        difficulty = 2
    elif "HARD" in difficulty:
        difficulty = 3
    elif "WRATH" in difficulty:
        difficulty = 4
        print("Good Luck, You'll need it...")
    elif "RELIC" in difficulty:
        print("All Items!")
        difficulty = 5
    else:
        print("Unknown input, setting difficulty to Normal.")
        difficulty = 2
    print("")

#:
    #poison for 3 with inflict
poisonkit = False
#:
    #heal for 8 with inflict, after combat heal 4
salamanderblood = False
#:
    #reflect the next attack with inflict, 50% chance to work, reflect 5 of the original damage, still take full
mirror = False
#:
    #passive, take triple damage, deal double damage, start with one less spirit
wrath = False
#:
    #15% chance to ambush an enemy and stab them with a deadly poison with inflict, the enemy deals one damage for 3 turns
sufferingnettle = False
#:
    #passive, negate the first inflict you get affected by
soulsafe = False
playersafe = False
#:
    #passive, you get double energy, but you cant see enemy intentions
blindbattery = False
#:
    #curses an enemy with inflict, enemy luck lowers by two if it succeeds, lowers personal luck by two if failed
cursedcoin = False
 
''':
Enemies will change type based on what value they have

BASE ENEMIES:
0 = none   1 - 3 = grub
4 & 5 = slime ball   6 & 7 = slime globe
8 - 10 = drob

HARD ENEMIES:
11 - 12 = Sentry   13 = Elite Drob   14 = Model

BOSSES:

15 = SUPER SLIME   16 = SENTRY CORE   17 = MODEL MOULD

'''

def shop():
    global poisonkit
    global salamanderblood
    global mirror
    global wrath
    global sufferingnettle
    global soulsafe
    global blindbattery
    global cursedcoin
    import random
    global gold
    
    print("On your Journey you Enter a Shop")
    print("In front of you on a counter are 3 pedestals.")
    print("")
    
    
    item1 = random.randint(1,3)
    item2 = random.randint(1,2)
    item3 = random.randint(1,3)
   
    label1 = ""
    label2 = ""
    label3 = ""
    
    common = 0
    rare = 0
    curse = 0
    
    price1 = 125
    price2 = 195
    price3 = 275
    
    while True:
    
        if item1 == 1 and poisonkit == False:
            label1 = "a Manual and Kit for making Poisons"
            common = 1
        elif item1 == 1 and poisonkit:
            label1 = "Out of Stock"
            common = 0
            price1 = 0
        elif item1 == 2 and salamanderblood == False:
            label1 = "a bowl of Salamander Blood"
            common = 2
        elif item1 == 2 and salamanderblood:
            label1 = "Out of Stock"
            common = 0
            price1 = 0
        elif item1 == 3 and mirror == False:
            label1 = "an Amulet with a small Mirror on it"
            common = 3
        elif item1 == 3 and mirror:
            label1 = "Out of Stock"
            common = 0
            price1 = 0
        
        if item2 == 1 and sufferingnettle == False:
            label2 = "a Needle coated in a strong Sedative"
            rare = 1
        elif item2 == 1 and sufferingnettle:
            label2 = "Out of Stock"
            rare = 0
            price2 = 0
        elif item2 == 2 and soulsafe == False:
            label2 = "a metal Safe with an Eye on it"
            rare = 2
        elif item2 == 2 and soulsafe:
            label2 = "Out of Stock"
            rare = 0
            price2 = 0
        
        if item3 == 1 and wrath == False:
            label3 = "a bottle containing a Wrathful Spirit"
            curse = 1
        elif item3 == 1 and wrath:
            label3 = "Out of Stock"
            curse = 0
            price3 = 0
        elif item3 == 2 and cursedcoin == False:
            label3 = "a Coin with a Skull on it"
            curse = 2
        elif item3 == 2 and cursedcoin:
            label1 = "Out of Stock"
            curse = 0
            price3 = 0
        elif item3 == 3 and blindbattery == False:
            label3 = "an Electric eel Without Eyes "
            curse = 3
        elif item3 == 3 and blindbattery:
            label3 = "Out of Stock"
            curse = 0
            price3 = 0
            
        print("On the left pedestal is " + label1 + ".")
        print("Price: " + str(price1))
        print("")
        print("On the middle pedestal is " + label2 + ".")
        print("Price: " + str(price2))
        print("")
        print("On the right pedestal is " + label3 + ".")
        print("Price: " + str(price3))
        print("")
        print("Gold: " + str(gold))
        choice = input("Do you wish to purchase an item or exit the shop? ").upper()
        if "PURCHASE" in choice:
            pedestal = input("Do you wish to buy the item on the left, right, or center pedestal? ").upper()
            if "LEFT" in pedestal:
                if gold >= price1:
                    if common == 1:
                        poisonkit = True
                        print("Bought the Poison Kit!")
                        print("You can now poison an enemy with inflict!")
                        common = 0
                        gold = gold - price1
                    elif common == 2:
                        salamanderblood = True
                        print("Bought the Salamander Blood!")
                        print("You can now heal yourself with inflict!")
                        print("You also heal after encounters now!")
                        common = 0
                        gold = gold - price1
                    elif common == 3:
                        mirror = True
                        print("Bought the Mirror Amulet!")
                        print("You can now reflect enemy attacks with inflict!")
                        common = 0
                        gold = gold - price1
                    else:
                        print("Invalid Choice")
                else:
                    print("Insufficient Funds.")
            elif "CENTER" in pedestal or "MIDDLE" in pedestal:
                if gold >= price2:
                    if rare == 1:
                        sufferingnettle = True
                        print("Bought the Needle of Suffering!")
                        print("You can now neutralize enemies with inflict!")
                        rare = 0
                        gold = gold - price2
                    elif rare == 2:
                        soulsafe = True
                        print("Bought the Soul Safe!")
                        print("You are immune to your first debuff!")
                        rare = 0
                        gold = gold - price2
                    else:
                        print("Invalid Choice")
                else:
                    print("Insufficient Funds")
            elif "RIGHT" in pedestal:
                if gold >= price3:
                    if curse == 1:
                        wrath = True
                        print("Bought the Bottled Wrath!")
                        print("You now take much more damage...")
                        print("Your spirit wavers...")
                        print("You deal much more damage!")
                        curse = 0
                        gold = gold - price3
                    elif curse == 2:
                        cursedcoin = True
                        print("Bought the Cursed Coin!")
                        print("Lower yours or the enemy's luck with inflict")
                        curse = 0
                        gold = gold - price3
                    elif curse == 3:
                        blindbattery = True
                        print("Bought the Eyeless Eel!")
                        print("Double Spirit!")
                        print("You can't determmine enemy intentions anymore...")
                        curse = 0
                        gold = gold - price3
                    else:
                        print("Invalid Choice")
                else:
                    print("Insufficient Funds")
            else:
                print("Invalid Input")
                print("")
        elif "EXIT" in choice or "LEAVE" in choice:
            break
        else:
            print("Invalid Input")
            print("")
    
def boss():
    import random
    a = random.randint(15,17)
    
    if a == 15:
        label1 = "SUPER SLIME"
    elif a == 16:
        label1 = "SENTRY CORE"
    elif a == 17:
        label1 = "MODEL MOULD"
        
    one = True
    global health
    global healthmax
    global gold
    global poisonkit
    global salamanderblood
    global mirror
    global wrath
    global sufferingnettle
    global soulsafe
    global blindbattery
    global cursedcoin
    
    ahp = 0
    ablock = 0
    apunchboost = 0
    adefendboost = 0
    abuff = 0
    astatus = 0
    aluck = 0
    apoison = 0
    asuffer = 0
    bsuffer = 0
    aintent = 0
    
    
    playerblock = 0
    playerpunchboost = 0
    playerdefendboost = 0
    playerluck = 0
    playerreflect = False
    protect = 0
    weak = 0
    
    #exclusive effects for the boss fights
    
    #poison, take 2 damage per action
    playerpoison = False
    
    #inflicts cost 2 energy per cast
    playervoid = False
    
    #33% chance to be stunned instead of doing an action, still uses energy even if stunned
    playerelectrified = False
    
    
    
    global playersafe
    playersafe = False
    if soulsafe:
        playersafe = True
    
    ''' Boss explainations:
    
    15 -S Slime
    -attacks once every 2 turns, each attack is giant, you passively have poison
    
    16 -Sentry Core
    -33% chance for you to be stunned per turn, every attack makes you weakened by 2
    
    17 -Model Mould
    -Moves twice a turn, while making inflicts and buffs cost double energy, becomes enraged at 50% health, which means it moves 3 times per turn
    '''
    
    if a == 15:
        playerpoison = True
        print("You enter the boss door...")
        print("S U P E R  S L I M E")
        label1 = "SUPER SLIME"
        print('''
        
        
        
        ''')
        ahp = 500
        cycle = 0
        print("The room is filled with a noxious gas...")
        if playersafe:
            print("You negate the effects of the boss room!")
            playerpoison = False
        print("You are poisoned!!!")
        print("")
        while ahp > 0 and health > 0:
            if asuffer > 0:
                asuffer = asuffer - 1
        
            if ahp > 0:
                print("")
                print(label1 + " hp: " + str(ahp))
                print("")
        
            cycle = cycle + 1
            if cycle == 1:
                aintent = random.randint(1,4)
            elif cycle == 2:
                cycle = 0
                aintent = 0
            if aintent == 0:
                aintent_label = "Bide"
            elif aintent == 1:
                aintent_label = "Crush"
            elif aintent == 2:
                aintent_label = "Shield"
            elif aintent == 3:
                aintent_label = "Spray"
            elif aintent == 4:
                aintent_label = "Grow"
            
            if blindbattery == False:
                print(label1 + " intends to " + aintent_label + ".")
            else:
                print("Enemy Intent Unknown.")
            
            
            '''
            Bide:
                Heal 2 ahp
            Crush:
                uplim = 30 + apunchboost
                health = health = random.randint(15,uplim)
            Shield:
                ablock = ablock + 2
            Spray:
                weak = weak + 4
            Grow:
                Heal 10 ahp
                apunchboost = apunchboost + random.randint(4,7)
                adefendboost = adefendboost + 2
            '''
        
        
            mana = 3
            if wrath:
                mana = 2
            if blindbattery == True:
                mana = mana * 2
        
            while mana > 0 and health > 0 and ahp > 0:
                print('''
            
            
            
                ''')
                print("Spirit: " + str(mana))
                print("")
                print("Health: " + str(health) + "/" + str(healthmax))
                print("")
                print("Block: " + str(playerblock))
                choice = input("Do you wish to attack, defend, buff, or inflict? ")
                choice = choice.upper()
            
            
                if choice == "ATTACK":
                    which = 1
                    if looper:
                        try:
                            chain = int(input("How many times do you wish to chain your action? "))
                        except ValueError:
                            chain = 1
                        if chain > mana:
                            chain = mana
                    for i in range(chain):
                        #enemy 1
                        if which == 1 and ahp > 0:
                            print("You attack the " + label1 + ".")
                            if ablock > 0:
                                print("You hit the " + label1 + "'s block!")
                                ablock = ablock - 1
                                mana = mana - 1
                            else:
                                attack = random.randint(7,11) + playerpunchboost - weak
                                if wrath:
                                    attack = attack * 3
                                if attack < 1:
                                    attack = 0
                                ahp = ahp - attack
                                mana = mana - 1
                                print("You dealt " + str(attack) + " damage!")
                                if ahp < 1:
                                    print("BOSS KILLED.")
                                else:
                                    print(label1 + " hp: " + str(ahp))
                        
                       
                    else:
                        print("invalid input.")
                elif choice == "BUFF":
                    if looper:
                        try:
                            chain = int(input("How many times do you wish to chain your action? "))
                        except ValueError:
                            chain = 1
                        if chain > mana:
                            chain = mana
                    for i in range(chain):
                        boost_type = random.randint(1,2)
                        if boost_type == 1:
                            print("Attack Boost!")
                            boostrng = 0
                            uplim = 3 + playerluck
                            if uplim < 0:
                                boostrng = 0
                            else:
                                boostrng = random.randint(1,uplim)
                            playerpunchboost = playerpunchboost + boostrng
                            print("Attack boosted by " + str(boostrng) + ", with a total boost of " + str(playerpunchboost) + ".")
                        elif boost_type == 2:
                            print("Defend boost!")
                            boostrng = 0
                            uplim = 4 + playerluck
                            if uplim < 0:
                                boostrng = 0
                            else:
                                boostrng = random.randint(1,uplim)
                            playerdefendboost = playerdefendboost + boostrng
                            print("Defend boosted by " + str(boostrng) + ", with a total boost of " + str(playerdefendboost) + ".")
                        mana = mana - 1
                elif choice == "DEFEND":
                    if looper:
                        try:
                            chain = int(input("How many times do you wish to chain your action? "))
                        except ValueError:
                            chain = 1
                        if chain > mana:
                            chain = mana
                    for i in range(chain):
                        blockrng = 0
                        uplim = 1 + playerdefendboost
                        if uplim < 0:
                            blockrng == 0
                        else:
                            blockrng = random.randint(-1,uplim)
                        if blockrng == 0:
                            print("Block Failed...")
                        elif blockrng > 0:
                            playerblock = playerblock + 1
                            print("Successful defend!")
                            print("Total block: " + str(playerblock))
                        mana = mana - 1
                elif choice == "INFLICT":
                    #boost luck
                    print("Inflict Chance")
                    #3% chance to be invincible one turn
                    print("Inflict Protect")
                
                    #Relics detailed at very top
                    if poisonkit == True:
                        print("Inflict Poison")
                    if salamanderblood == True:
                        print("Inflict Transfusion")
                    if mirror == True:
                        print("Inflict Reflection")
                    if sufferingnettle == True:
                        print("Inflict Suffering")
                    if cursedcoin == True:
                        print("Inflict Gamble")
                    inflict_type = input("What inflict would you like to use? ")
                    inflict_type = inflict_type.upper()
                    
                    #items will add more inflicts
                
                
                    if inflict_type == "CHANCE":
                        print("Luck increased!")
                        playerluck = playerluck + 2
                    elif inflict_type == "PROTECT":
                        uplim = 99 + playerluck
                        if uplim < 0:
                            protect = True
                        else:
                            protect = random.randint(0,uplim)
                        if protect < 96:
                            print("Protect Failed...")
                            protect = False
                    elif inflict_type == "POISON" and poisonkit:
                        which = 1
        
                        if which == "1" and ahp > 0:
                            print("You poison the " + label1 + ".")
                            apoison = apoison + 3
                        else:
                            print("Invalid Input")
                    elif inflict_type == "TRANSFUSION" and salamanderblood:
                        health = health + 8
                        if health > healthmax:
                            health = healthmax
                        print("You focus and heal 8 health points.")
                    elif inflict_type == "REFLECTION" and mirror == True:
                        uplim = 1 + playerluck
                        refrng = 0
                        if uplim < 1:
                            refrng = 0
                        else:
                            refrng = random.randint(0,uplim)
                        if refrng == 0:
                            print("Reflection Failed...")
                        else:
                            playerreflect = True
                            print("Reflection Successful!")
                    elif inflict_type == "SUFFERING" and sufferingnettle:
                        suffer_rng = 0
                        uplim = 99 + playerluck
                        if uplim < 0:
                            suffer_rng = 0
                        else: suffer_rng = random.randint(1,uplim)
                        which = 1
                        #enemy 1
                        if which == "1":
                            if suffer_rng < 85:
                                print("Ambush Failed...")
                            else:
                                asuffer = asuffer + 3
                                print("Ambush succeeded, " + label1 + " is now neutralized")
                        else:
                            inflict_type = ""
                    elif inflict_type == "GAMBLE" and cursedcoin:
                        gamble = random.randint(0,1)
                        which = 1
                        #enemy 1
                        if which == "1":
                            if gamble == 1:
                                print("Curse Backfired...")
                                playerluck = playerluck - 2
                            else:
                                aluck = aluck - 2
                                print(label1 + " was cursed successfully!")
                        else:
                            inflict_type = ""

                        
                    if inflict_type == "CHANCE" or inflict_type == "PROTECT" or (inflict_type == "GAMBLE" and cursedcoin) or (inflict_type == "POISON" and poisonkit) or (inflict_type == "TRANSFUSION" and salamanderblood) or (inflict_type == "SUFFERING" and sufferingnettle) or (inflict_type == "REFLECTION" and mirror):
                        mana = mana - 1
                    else:
                        print("Invalid Input")
            if ahp < 1 or health < 1:
                break
            print('''
            
            
            ''')
            
            if aintent == 0:
                print("The Slime Bides Its Time...")
                ahp = ahp + 2
                if ahp > 200:
                    ahp = 200
            elif aintent == 1:
                lowlim = 15 + apunchboost
                uplim = 30 + apunchboost
                crush = random.randint(lowlim,uplim)
                if asuffer > 0:
                    crush = 1
                if wrath:
                    crush = crush * 3
                health = health - crush
                print("The Slime Jumps And You Get Crushed!")
                print("You take " + str(crush) + " damage.")
            elif aintent == 2:
                ablock = ablock + 2
                print("The Slime Hardens Its Outside!")
            elif aintent == 3:
                if playersafe:
                    print("Inflict Negated!")
                    playersafe = False
                else:
                    weak = weak + 4
                    print("The Slime Sprays Acid At You.")
                    print("You are weakened!")
            elif aintent == 4:
                ahp = ahp + 10
                if ahp > 200:
                    ahp = 200
                apunchboost = apunchboost + random.randint(4,7)
                adefendboost = adefendboost + 2
                print("Slime Grows!")
                print("Slime's Stats Increase!")
        if ahp < 1 and health > 0:
            print("")
            print("YOU WON! GOOD JOB!")
            print("")
            diff_select()
            exo()
        else:
            print("")
            print("YOU LOST! BETTER LUCK NEXT TIME!")
            print("")
            diff_select()
            exo()
    elif a == 16:
        playerelectrified = True
        overclock = False
        print("You enter the boss door...")
        print("S E N T R Y   C O R E")
        label1 = "SENTRY CORE"
        print('''
        
        
        
        ''')
        ahp = 370
        print("The air is crackling...")
        if playersafe:
            print("You negate the effects of the boss room!")
            playerelectrified = False
        else:
            print("You are stunned!")
        print("")
        while ahp > 0 and health > 0:
            if asuffer > 0:
                asuffer = asuffer - 1
            #the player's actions
        
            if ahp > 0:
                print("")
                print(label1 + " hp: " + str(ahp))
                print("")
            
            aintent = random.randint(1,4)
            
            if overclock:
                aintent = 1
            
            if aintent == 1:
                aintent_label = "Burst"
            elif aintent == 2:
                aintent_label = "Barrier"
            elif aintent == 3:
                aintent_label = "Overclock"
            elif aintent == 4:
                aintent_label = "Charge"
            
            if blindbattery == False:
                print(label1 + " intends to " + aintent_label + ".")
            else:
                print("Enemy Intent Unknown.")
            
            ''':
            Burst:
                uplim = 25 + apunchboost
                damage = random.randint(20,uplim)
                if overclock:
                    damage = damage * 2
                    overclock = False
                health = health - damage
            Barrier:
                ablock = ablock + 3
            Overclock:
                overclock = True
            Charge:
                Heal 50 ahp
                apunchboost = apunchboost + random.randint(6,11)
            '''
        
        
            mana = 3
            if wrath:
                mana = 2
            if blindbattery == True:
                mana = mana * 2
        
            while mana > 0 and health > 0 and ahp > 0:
                print('''
            
            
            
                ''')
                stunchance = 0
                if playerelectrified:
                    stunchance = random.randint(1,3)
                    health = health - 3
                print("Spirit: " + str(mana))
                print("")
                print("Health: " + str(health) + "/" + str(healthmax))
                print("")
                print("Block: " + str(playerblock))
                choice = input("Do you wish to attack, defend, buff, or inflict? ")
                choice = choice.upper()
                chain = 1
            
                if stunchance == 1:
                    print("You were stunned...")
                    mana = mana - 1
                else:
                    if choice == "ATTACK":
                        which = 1
                        #enemy 1
                        if looper:
                            try:
                                chain = int(input("How many times do you wish to chain your action? "))
                            except ValueError:
                                chain = 1
                            if chain > mana:
                                chain = mana
                        for i in range(chain):
                            if which == 1 and ahp > 0:
                                print("You attack the " + label1 + ".")
                                if ablock > 0:
                                    print("You hit the " + label1 + "'s block!")
                                    ablock = ablock - 1
                                    mana = mana - 1
                                else:
                                    attack = random.randint(7,11) + playerpunchboost - weak
                                    if wrath:
                                        attack = attack * 3
                                    if attack < 1:
                                        attack = 0
                                    ahp = ahp - attack
                                    mana = mana - 1
                                    print("You dealt " + str(attack) + " damage!")
                                    if ahp < 1:
                                        print("BOSS KILLED.")
                                    else:
                                        print(label1 + " hp: " + str(ahp))
                        
                       
                            else:
                                print("invalid input.")
                    elif choice == "BUFF":
                        if looper:
                            try:
                                chain = int(input("How many times do you wish to chain your action? "))
                            except ValueError:
                                chain = 1
                            if chain > mana:
                                chain = mana
                        for i in range(chain):
                            boost_type = random.randint(1,2)
                            if boost_type == 1:
                                print("Attack Boost!")
                                boostrng = 0
                                uplim = 2 + playerluck
                                if uplim < 0:
                                    boostrng = 0
                                else:
                                    boostrng = random.randint(1,uplim)
                                playerpunchboost = playerpunchboost + boostrng
                                print("Attack boosted by " + str(boostrng) + ", with a total boost of " + str(playerpunchboost) + ".")
                            elif boost_type == 2:
                                print("Defend boost!")
                                boostrng = 0
                                uplim = 4 + playerluck
                                if uplim < 0:
                                    boostrng = 0
                                else:
                                    boostrng = random.randint(1,uplim)
                                playerdefendboost = playerdefendboost + boostrng
                                print("Defend boosted by " + str(boostrng) + ", with a total boost of " + str(playerdefendboost) + ".")
                            mana = mana - 1
                    elif choice == "DEFEND":
                        if looper:
                            try:
                                chain = int(input("How many times do you wish to chain your action? "))
                            except ValueError:
                                chain = 1
                            if chain > mana:
                                chain = mana
                        for i in range(chain):
                            blockrng = 0
                            uplim = 1 + playerdefendboost
                            if uplim < 0:
                                blockrng == 0
                            else:
                                blockrng = random.randint(-1,uplim)
                            if blockrng == 0:
                                print("Block Failed...")
                            elif blockrng > 0:
                                playerblock = playerblock + 1
                                print("Successful defend!")
                                print("Total block: " + str(playerblock))
                            mana = mana - 1
                    elif choice == "INFLICT":
                        #boost luck
                        print("Inflict Chance")
                        #3% chance to be invincible one turn
                        print("Inflict Protect")
                
                        #Relics detailed at very top
                        if poisonkit == True:
                            print("Inflict Poison")
                        if salamanderblood == True:
                            print("Inflict Transfusion")
                        if mirror == True:
                            print("Inflict Reflection")
                        if sufferingnettle == True:
                            print("Inflict Suffering")
                        if cursedcoin == True:
                            print("Inflict Gamble")
                        inflict_type = input("What inflict would you like to use? ")
                        inflict_type = inflict_type.upper()
                    
                        #items will add more inflicts
                
                
                        if inflict_type == "CHANCE":
                            print("Luck increased!")
                            playerluck = playerluck + 2
                        elif inflict_type == "PROTECT":
                            uplim = 99 + playerluck
                            if uplim < 0:
                                protect = True
                            else:
                                protect = random.randint(0,uplim)
                            if protect < 96:
                                print("Protect Failed...")
                                protect = False
                        elif inflict_type == "POISON" and poisonkit:
                            which = 1
        
                            if which == "1" and ahp > 0:
                                print("You poison the " + label1 + ".")
                                apoison = apoison + 3
                            else:
                                print("Invalid Input")
                        elif inflict_type == "TRANSFUSION" and salamanderblood:
                            health = health + 8
                            if health > healthmax:
                                health = healthmax
                            print("You focus and heal 8 health points.")
                        elif inflict_type == "REFLECTION" and mirror == True:
                            uplim = 1 + playerluck
                            refrng = 0
                            if uplim < 1:
                                refrng = 0
                            else:
                                refrng = random.randint(0,uplim)
                            if refrng == 0:
                                print("Reflection Failed...")
                            else:
                                playerreflect = True
                                print("Reflection Successful!")
                        elif inflict_type == "SUFFERING" and sufferingnettle:
                            suffer_rng = 0
                            uplim = 99 + playerluck
                            if uplim < 0:
                                suffer_rng = 0
                            else: suffer_rng = random.randint(1,uplim)
                            which = 1
                            #enemy 1
                            if which == "1":
                                if suffer_rng < 85:
                                    print("Ambush Failed...")
                                else:
                                    asuffer = asuffer + 3
                                    print("Ambush succeeded, " + label1 + " is now neutralized")
                            else:
                                inflict_type = ""
                        elif inflict_type == "GAMBLE" and cursedcoin:
                            gamble = random.randint(0,1)
                            which = 1
                            #enemy 1
                            if which == "1":
                                if gamble == 1:
                                    print("Curse Backfired...")
                                    playerluck = playerluck - 2
                                else:
                                    aluck = aluck - 2
                                    print(label1 + " was cursed successfully!")
                            else:
                                inflict_type = ""

                        
                        if inflict_type == "CHANCE" or inflict_type == "PROTECT" or (inflict_type == "GAMBLE" and cursedcoin) or (inflict_type == "POISON" and poisonkit) or (inflict_type == "TRANSFUSION" and salamanderblood) or (inflict_type == "SUFFERING" and sufferingnettle) or (inflict_type == "REFLECTION" and mirror):
                            mana = mana - 1
                        else:
                            print("Invalid Input")
                if ahp < 1 or health < 1:
                    break
            print('''
            
            
            ''')
            if aintent == 1:
                lowlim = 20 + apunchboost
                uplim = 25 + apunchboost
                burst = random.randint(lowlim,uplim)
                if asuffer > 0:
                    burst = 1
                if wrath:
                    burst = burst * 3
                if overclock:
                    burst = burst * 2
                health = health - burst
                print("The Core Glows And You Get Shot")
                print("You take " + str(burst) + " damage.")
                if overclock:
                    print("Overclock wears off...")
                    overclock = False
            elif aintent == 2:
                ablock = ablock + 3
                print("The Core Sets Up A Barrier")
            elif aintent == 3:
                overclock = True
                print("THE SENTRY OVERCLOCKS!!")
            elif aintent == 4:
                ahp = ahp + 50
                if ahp > 185:
                    ahp = 200
                apunchboost = apunchboost + random.randint(6,11)
                print("The Core Charges!")
                print("The Core's Stats Rise!")
        if ahp < 1 and health > 0:
            print("")
            print("YOU WON! GOOD JOB!")
            print("")
            diff_select()
            exo()
        else:
            print("")
            print("YOU LOST! BETTER LUCK NEXT TIME!")
            print("")
            diff_select()
    elif a == 17:
        playervoid = True
        enrage = False
        minions = 0
        accuracy = 100
        print("You enter the boss door...")
        print("M O D E L   M O U L D")
        label1 = "MODEL MOULD"
        print('''
        
        
        
        ''')
        ahp = 300
        print("The light is dim...")
        if playersafe:
            print("You negate the effects of the boss room!")
            playervoid = False
        else:
            print("Your confidence wavers...")
        print("")
        while ahp > 0 and health > 0:
            if asuffer > 0:
             asuffer = asuffer - 1
            #the player's actions
            
            if enrage:
                label1 =  "ENRAGED MOULD"
            
            if ahp > 0:
                print("")
                print(label1 + " hp: " + str(ahp))
                print("")
            
            aintent = random.randint(1,4)
            
            aintent_label = "do something, but it is unclear"
            if enrage:
                aintent_label = "do something very bad.."
            print(label1 + " intends to " + aintent_label + ".")
            
            
            ''':
            Slash:
                flat 25 + boost
            Cloak:
                permanent accuracy decrease, maybe 5%
            Cast:
            Do something that lowers accuracy temporarily by 10%, when you miss, decrease the temp by 10%
            Charge:
                buff
                atk + 6
            '''
        
        
            mana = 3
            if wrath:
                mana = 2
            if blindbattery == True:
                mana = mana * 2
        
            while mana > 0 and health > 0 and ahp > 0:
                print('''
            
            
            
                ''')
                health = health - 3
                print("Spirit: " + str(mana))
                print("")
                print("Health: " + str(health) + "/" + str(healthmax))
                print("")
                print("Block: " + str(playerblock))
                choice = input("Do you wish to attack, defend, buff, or inflict? ")
                choice = choice.upper()
                chain = 1
            
                if choice == "ATTACK":
                    if looper:
                        try:
                            chain = int(input("How many times do you wish to chain your action? "))
                        except ValueError:
                            chain = 1
                        if chain > mana:
                            chain = mana
                    for i in range(chain):
                        which = 1
                        miniondeb = minions * 5
                        accuracy = accuracy - miniondeb
                        if which == 1 and ahp > 0:
                            print("You attack the " + label1 + ".")
                            accuracycheck = random.randint(1,100)
                            if accuracycheck > accuracy:
                                print("You Missed!")
                                mana = mana - 1
                                if minions > 0:
                                    minions = minions - 1
                                    accuracy = accuracy + 5
                                    print("You cut down a mould mimic!")
                            else:
                                if ablock > 0:
                                    print("You hit the " + label1 + "'s block!")
                                    ablock = ablock - 1
                                    mana = mana - 1
                                else:
                                    attack = random.randint(7,11) + playerpunchboost - weak
                                    if wrath:
                                        attack = attack * 3
                                    if attack < 1:
                                        attack = 0
                                    ahp = ahp - attack
                                    mana = mana - 1
                                    print("You dealt " + str(attack) + " damage!")
                                    if ahp < 1:
                                        print("BOSS KILLED.")
                                        break
                                    else:
                                        print(label1 + " hp: " + str(ahp))
                        else:
                            print("invalid input.")
                elif choice == "BUFF":
                    if looper:
                        try:
                            chain = int(input("How many times do you wish to chain your action? "))
                        except ValueError:
                            chain = 1
                        if chain > mana:
                            chain = mana
                    for i in range(chain):
                        if mana == 1 and playervoid:
                            print("You don't have enough spirit to buff yourself...")
                            break
                        else:
                            boost_type = random.randint(1,2)
                            if boost_type == 1:
                                print("Attack Boost!")
                                boostrng = 0
                                uplim = 3 + playerluck
                                if uplim < 0:
                                    boostrng = 0
                                else:
                                    boostrng = random.randint(1,uplim)
                                playerpunchboost = playerpunchboost + boostrng
                                print("Attack boosted by " + str(boostrng) + ", with a total boost of " + str(playerpunchboost) + ".")
                            elif boost_type == 2:
                                print("Defend boost!")
                                boostrng = 0
                                uplim = 4 + playerluck
                                if uplim < 0:
                                    boostrng = 0
                                else:
                                    boostrng = random.randint(1,uplim)
                                playerdefendboost = playerdefendboost + boostrng
                                print("Defend boosted by " + str(boostrng) + ", with a total boost of " + str(playerdefendboost) + ".")
                            mana = mana - 1
                elif choice == "DEFEND":
                    if looper:
                        try:
                            chain = int(input("How many times do you wish to chain your action? "))
                        except ValueError:
                            chain = 1
                        if chain > mana:
                            chain = mana
                    for i in range(chain):
                        blockrng = 0
                        uplim = 1 + playerdefendboost
                        if uplim < 0:
                            blockrng == 0
                        else:
                            blockrng = random.randint(-1,uplim)
                        if blockrng == 0:
                            print("Block Failed...")
                        elif blockrng > 0:
                            playerblock = playerblock + 1
                            print("Successful defend!")
                            print("Total block: " + str(playerblock))
                        mana = mana - 1
                elif choice == "INFLICT":
                    if mana == 1 and playervoid:
                        print("You don't have enough spirit to inflict anything...")
                    else:
                        #boost luck
                        print("Inflict Chance")
                        #3% chance to be invincible one turn
                        print("Inflict Protect")
                
                        #Relics detailed at very top
                        if poisonkit == True:
                            print("Inflict Poison")
                        if salamanderblood == True:
                            print("Inflict Transfusion")
                        if mirror == True:
                            print("Inflict Reflection")
                        if sufferingnettle == True:
                            print("Inflict Suffering")
                        if cursedcoin == True:
                            print("Inflict Gamble")
                        inflict_type = input("What inflict would you like to use? ")
                        inflict_type = inflict_type.upper()
                    
                        #items will add more inflicts
                
                
                        if inflict_type == "CHANCE":
                            print("Luck increased!")
                            playerluck = playerluck + 2
                        elif inflict_type == "PROTECT":
                            uplim = 99 + playerluck
                            if uplim < 0:
                                protect = True
                            else:
                                protect = random.randint(0,uplim)
                            if protect < 96:
                                print("Protect Failed...")
                                protect = False
                        elif inflict_type == "POISON" and poisonkit:
                            which = 1
        
                            if which == "1" and ahp > 0:
                                print("You poison the " + label1 + ".")
                                apoison = apoison + 3
                            else:
                                print("Invalid Input")
                        elif inflict_type == "TRANSFUSION" and salamanderblood:
                            health = health + 8
                            if health > healthmax:
                                health = healthmax
                            print("You focus and heal 8 health points.")
                        elif inflict_type == "REFLECTION" and mirror:
                            uplim = 1 + playerluck
                            refrng = 0
                            if uplim < 1:
                                refrng = 0
                            else:
                                refrng = random.randint(0,uplim)
                            if refrng == 0:
                                print("Reflection Failed...")
                            else:
                                playerreflect = True
                                print("Reflection Successful!")
                        elif inflict_type == "SUFFERING" and sufferingnettle:
                            suffer_rng = 0
                            uplim = 99 + playerluck
                            if uplim < 0:
                                suffer_rng = 0
                            else: suffer_rng = random.randint(1,uplim)
                            which = 1
                            #enemy 1
                            if which == "1":
                                if suffer_rng < 85:
                                    print("Ambush Failed...")
                                else:
                                    asuffer = asuffer + 3
                                    print("Ambush succeeded, " + label1 + " is now neutralized")
                            else:
                                inflict_type = ""
                        elif inflict_type == "GAMBLE" and cursedcoin:
                            gamble = random.randint(0,1)
                            which = 1
                            #enemy 1
                            if which == "1":
                                if gamble == 1:
                                    print("Curse Backfired...")
                                    playerluck = playerluck - 2
                                else:
                                    aluck = aluck - 2
                                    print(label1 + " was cursed successfully!")
                            else:
                                inflict_type = ""

                        
                        if inflict_type == "CHANCE" or inflict_type == "PROTECT" or (inflict_type == "GAMBLE" and cursedcoin) or (inflict_type == "POISON" and poisonkit) or (inflict_type == "TRANSFUSION" and salamanderblood) or (inflict_type == "SUFFERING" and sufferingnettle) or (inflict_type == "REFLECTION" and mirror):
                            mana = mana - 2
                        else:
                            print("Invalid Input")
                if ahp < 1 or health < 1:
                    break
            print('''
            
            
            ''')
            if aintent == 1:
                slash = 25 + apunchboost
                if asuffer > 0:
                    slash = 1
                if enrage:
                    slash = slash * 2
                if wrath:
                    slash = slash * 3
                health = health - slash
                print("The Mould Slices You")
                print("You take " + str(slash) + " damage.")
            elif aintent == 2:
                ablock = ablock + 3
                print("The Mould Blends Into The Darkness...")
                print("accuracy decreased")
                accuracy = accuracy - 5
            elif aintent == 3:
                print("The Mould Makes a Model!")
                print("You can't tell which one is the mould or the model...")
                minions = minions + 1
            elif aintent == 4:
                apunchboost = apunchboost + 6
                print("The Mould Sharpens Its Hands!")
                print("The Mould's Stats Rise!")
        if ahp < 1 and health > 0:
            print("")
            print("YOU WON! GOOD JOB!")
            print("")
            diff_select()
            exo()
        else:
            print("")
            print("YOU LOST! BETTER LUCK NEXT TIME!")
            print("")
            diff_select()
            
def elite():
    import random
    a = random.randint(1,3)
    b = 0
    c = 0
    
    
    if a == 3:
        label1 = "Sentry"
        label2 = "Sentry"
        label3 = "Sentry"
        b = 3
        c = 3
    elif a == 1:
        label1 = "High Drob"
    elif a == 2:
        label1 = "Model"
    one = True
    two = False
    three = False
    if a == 3:
        two = True
        three = True
    global health
    global healthmax
    global gold
    global poisonkit
    global salamanderblood
    global mirror
    global wrath
    global sufferingnettle
    global soulsafe
    global blindbattery
    global cursedcoin
    global looper
    
    ahp = 0
    ablock = 0
    apunchboost = 0
    adefendboost = 0
    abuff = 0
    astatus = 0
    aluck = 0
    apoison = 0
    asuffer = 0
    aintent = 0
    
    bhp = 0
    bblock = 0
    bpunchboost = 0
    bdefendboost = 0
    bbuff = 0
    bstatus = 0
    bluck = 0
    bpoison = 0
    bsuffer = 0
    bintent = 0
    
    chp = 0
    cblock = 0
    cpunchboost = 0
    cdefendboost = 0
    cbuff = 0
    cstatus = 0
    cluck = 0
    cpoison = 0
    csuffer = 0
    cintent = 0
    
    playerblock = 0
    playerpunchboost = 0
    playerdefendboost = 0
    playerluck = 0
    playerreflect = False
    protect = 0
    weak = 0
    
    global playersafe
    playersafe = False
    if soulsafe:
        playersafe = True
    if a == 1:
        ahp = 200
        while ahp > 0 and health > 0:
            print("")
            print(label1 + " hp: " + str(ahp))
            print("")
            import random
            aintent = random.randint(1,2)
            if aintent == 1:
                aintent_label = "Crush"
            elif aintent == 2:
                aintent_label = "Boost"
            if blindbattery:
                print("You cannot determine the enemy's intentions.")
            else:
                print(label1 + " intends to " + aintent_label + ".")
                
            mana = 3
            if wrath:
                mana = 2
            if blindbattery == True:
                mana = mana * 2
        
            while mana > 0 and health > 0 and ahp > 0:
                print('''
            
            
            
                ''')
                print("Spirit: " + str(mana))
                print("")
                print("Health: " + str(health) + "/" + str(healthmax))
                print("")
                print("Block: " + str(playerblock))
                choice = input("Do you wish to attack, defend, buff, or inflict? ")
                choice = choice.upper()
            
            
                if choice == "ATTACK":
                    which = 1
                    chain = 1
                    if looper:
                        try:
                            chain = int(input("How many times do you wish to chain your action? "))
                        except ValueError:
                            chain = 1
                        if chain > mana:
                            chain = mana
                    for i in range(chain):
                        if which == 1 and ahp > 0:
                            print("You attack the " + label1 + ".")
                            if ablock > 0:
                                print("You hit the " + label1 + "'s block!")
                                ablock = ablock - 1
                                mana = mana - 1
                            else:
                                attack = random.randint(7,11) + playerpunchboost - weak
                                if wrath:
                                    attack = attack * 3
                                if attack < 1:
                                    attack = 0
                                ahp = ahp - attack
                                mana = mana - 1
                                print("You dealt " + str(attack) + " damage!")
                                if ahp < 1:
                                    print(label1 + " killed.")
                                    break
                                else:
                                    print(label1 + " hp: " + str(ahp))
                        
                       
                        else:
                            print("invalid input.")
                elif choice == "BUFF":
                    chain = 1
                    if looper:
                        try:
                            chain = int(input("How many times do you wish to chain your action? "))
                        except ValueError:
                            chain = 1
                        if chain > mana:
                            chain = mana
                    for i in range(chain):
                        boost_type = random.randint(1,2)
                        if boost_type == 1:
                            print("Attack Boost!")
                            boostrng = 0
                            uplim = 3 + playerluck
                            if uplim < 0:
                                boostrng = 0
                            else:
                                boostrng = random.randint(1,uplim)
                            playerpunchboost = playerpunchboost + boostrng
                            print("Attack boosted by " + str(boostrng) + ", with a total boost of " + str(playerpunchboost) + ".")
                        elif boost_type == 2:
                            print("Defend boost!")
                            boostrng = 0
                            uplim = 4 + playerluck
                            if uplim < 0:
                                boostrng = 0
                            else:
                                boostrng = random.randint(1,uplim)
                            playerdefendboost = playerdefendboost + boostrng
                            print("Defend boosted by " + str(boostrng) + ", with a total boost of " + str(playerdefendboost) + ".")
                        mana = mana - 1
                elif choice == "DEFEND":
                    chain = 1
                    if looper:
                        try:
                            chain = int(input("How many times do you wish to chain your action? "))
                        except ValueError:
                            chain = 1
                        if chain > mana:
                            chain = mana
                    for i in range(chain):
                        blockrng = 0
                        uplim = 1 + playerdefendboost
                        if uplim < 0:
                            blockrng == 0
                        else:
                            blockrng = random.randint(-1,uplim)
                        if blockrng == 0:
                            print("Block Failed...")
                        elif blockrng > 0:
                            playerblock = playerblock + 1
                            print("Successful defend!")
                            print("Total block: " + str(playerblock))
                        mana = mana - 1
                elif choice == "INFLICT":
                    #boost luck
                    print("Inflict Chance")
                    #3% chance to be invincible one turn
                    print("Inflict Protect")
                
                    #Relics detailed at very top
                    if poisonkit == True:
                        print("Inflict Poison")
                    if salamanderblood == True:
                        print("Inflict Transfusion")
                    if mirror == True:
                        print("Inflict Reflection")
                    if sufferingnettle == True:
                        print("Inflict Suffering")
                    if cursedcoin == True:
                        print("Inflict Gamble")
                    inflict_type = input("What inflict would you like to use? ")
                    inflict_type = inflict_type.upper()
                    
                    #items will add more inflicts
                
                
                    if inflict_type == "CHANCE":
                        print("Luck increased!")
                        playerluck = playerluck + 2
                    elif inflict_type == "PROTECT":
                        uplim = 99 + playerluck
                        if uplim < 0:
                            protect = True
                        else:
                            protect = random.randint(0,uplim)
                        if protect < 96:
                            print("Protect Failed...")
                            protect = False
                    elif inflict_type == "POISON" and poisonkit:
                        which = 1
        
                        if which == "1" and ahp > 0:
                            print("You poison the " + label1 + ".")
                            apoison = apoison + 3
                        else:
                            print("Invalid Input")
                    elif inflict_type == "TRANSFUSION" and salamanderblood:
                        health = health + 8
                        if health > healthmax:
                            health = healthmax
                        print("You focus and heal 8 health points.")
                    elif inflict_type == "REFLECTION" and mirror == True:
                        uplim = 1 + playerluck
                        refrng = 0
                        if uplim < 1:
                            refrng = 0
                        else:
                            refrng = random.randint(0,uplim)
                        if refrng == 0:
                            print("Reflection Failed...")
                        else:
                            playerreflect = True
                            print("Reflection Successful!")
                    elif inflict_type == "SUFFERING" and sufferingnettle:
                        suffer_rng = 0
                        uplim = 99 + playerluck
                        if uplim < 0:
                            suffer_rng = 0
                        else: suffer_rng = random.randint(1,uplim)
                        which = 1
                        #enemy 1
                        if which == "1":
                            if suffer_rng < 85:
                                print("Ambush Failed...")
                            else:
                                asuffer = asuffer + 3
                                print("Ambush succeeded, " + label1 + " is now neutralized")
                        else:
                            inflict_type = ""
                    elif inflict_type == "GAMBLE" and cursedcoin:
                        gamble = random.randint(0,1)
                        which = 1
                        #enemy 1
                        if which == "1":
                            if gamble == 1:
                                print("Curse Backfired...")
                                playerluck = playerluck - 2
                            else:
                                aluck = aluck - 2
                                print(label1 + " was cursed successfully!")
                        else:
                            inflict_type = ""

                        
                    if inflict_type == "CHANCE" or inflict_type == "PROTECT" or (inflict_type == "GAMBLE" and cursedcoin) or (inflict_type == "POISON" and poisonkit) or (inflict_type == "TRANSFUSION" and salamanderblood) or (inflict_type == "SUFFERING" and sufferingnettle) or (inflict_type == "REFLECTION" and mirror):
                        mana = mana - 1
                    else:
                        print("Invalid Input")
            if ahp < 1 or health < 1:
                break
            print('''
            
            
            ''')
            
            if ahp > 0:
                if aintent == 1:
                    attack = random.randint(18,30) + apunchboost
                    if playerblock > 1:
                        print("Blocked the attack!")
                        playerblock = playerblock - 2
                    elif playerblock == 1:
                        print("The High Drob Pierces Your Shield!")
                        playerblock = playerblock - 2
                        health = health - attack
                        print("You have been hit for " + str(attack) + ".")
                    else:
                        health = health - attack
                        print("You have been hit for " + str(attack) + ".")
                else:
                    random = random.randint(6,8)
                    apunchboost = apunchboost + random
                    print(label1 +" has boosted its attack by " + str(random) + ".")
        
    elif a == 2:
        ahp = 170
        puncture = False
        while ahp > 0 and health > 0:
            print("")
            print(label1 + " hp: " + str(ahp))
            print("")
    
        
            aintent = random.randint(1,2)
            if aintent == 1:
                aintent_label = "Slash"
            elif aintent == 2:
                aintent_label = "Puncture"
            if blindbattery:
                print("You cannot determine the enemy's intentions.")
            else:
                print(label1 + " intends to " + aintent_label + ".")
                
            mana = 3
            if wrath:
                mana = 2
            if blindbattery == True:
                mana = mana * 2
        
            while mana > 0 and health > 0 and ahp > 0:
                print('''
            
            
            
                ''')
                print("Spirit: " + str(mana))
                print("")
                if puncture:
                    health = health - 7
                    print("You bled from the puncture")
                    print("")
                print("Health: " + str(health) + "/" + str(healthmax))
                print("")
                print("Block: " + str(playerblock))
                choice = input("Do you wish to attack, defend, buff, or inflict? ")
                choice = choice.upper()
            
            
                if choice == "ATTACK":
                    chain = 1
                    if looper:
                        try:
                            chain = int(input("How many times do you wish to chain your action? "))
                        except ValueError:
                            chain = 1
                        if chain > mana:
                            chain = mana
                    for i in range(chain):
                        which = 1
                        #enemy 1
                        if which == 1 and ahp > 0:
                            print("You attack the " + label1 + ".")
                            if ablock > 0:
                                print("You hit the " + label1 + "'s block!")
                                ablock = ablock - 1
                                mana = mana - 1
                            else:
                                attack = random.randint(7,11) + playerpunchboost - weak
                                if wrath:
                                    attack = attack * 3
                                if attack < 1:
                                    attack = 0
                                ahp = ahp - attack
                                mana = mana - 1
                                print("You dealt " + str(attack) + " damage!")
                                if ahp < 1:
                                    print("You killed the" + label1)
                                    break
                                else:
                                    print(label1 + " hp: " + str(ahp))
                            
                        
                        else:
                            print("invalid input.")
                elif choice == "BUFF":
                    chain = 1
                    if looper:
                        try:
                            chain = int(input("How many times do you wish to chain your action? "))
                        except ValueError:
                            chain = 1
                        if chain > mana:
                            chain = mana
                    for i in range(chain):
                        boost_type = random.randint(1,2)
                        if boost_type == 1:
                            print("Attack Boost!")
                            boostrng = 0
                            uplim = 3 + playerluck
                            if uplim < 0:
                                boostrng = 0
                            else:
                                boostrng = random.randint(1,uplim)
                            playerpunchboost = playerpunchboost + boostrng
                            print("Attack boosted by " + str(boostrng) + ", with a total boost of " + str(playerpunchboost) + ".")
                        elif boost_type == 2:
                            print("Defend boost!")
                            boostrng = 0
                            uplim = 4 + playerluck
                            if uplim < 0:
                                boostrng = 0
                            else:
                                boostrng = random.randint(1,uplim)
                            playerdefendboost = playerdefendboost + boostrng
                            print("Defend boosted by " + str(boostrng) + ", with a total boost of " + str(playerdefendboost) + ".")
                        mana = mana - 1
                elif choice == "DEFEND":
                    chain = 1
                    if looper:
                        try:
                            chain = int(input("How many times do you wish to chain your action? "))
                        except ValueError:
                            chain = 1
                        if chain > mana:
                            chain = mana
                    for i in range(chain):
                        blockrng = 0
                        uplim = 1 + playerdefendboost
                        if uplim < 0:
                            blockrng == 0
                        else:
                            blockrng = random.randint(-1,uplim)
                        if blockrng == 0:
                            print("Block Failed...")
                        elif blockrng > 0:
                            playerblock = playerblock + 1
                            print("Successful defend!")
                            print("Total block: " + str(playerblock))
                        mana = mana - 1
                elif choice == "INFLICT":
                    #boost luck
                    print("Inflict Chance")
                    #3% chance to be invincible one turn
                    print("Inflict Protect")
                
                    #Relics detailed at very top
                    if poisonkit == True:
                        print("Inflict Poison")
                    if salamanderblood == True:
                        print("Inflict Transfusion")
                    if mirror == True:
                        print("Inflict Reflection")
                    if sufferingnettle == True:
                        print("Inflict Suffering")
                    if cursedcoin == True:
                        print("Inflict Gamble")
                    inflict_type = input("What inflict would you like to use? ")
                    inflict_type = inflict_type.upper()
                    
                    #items will add more inflicts
                
                
                    if inflict_type == "CHANCE":
                        print("Luck increased!")
                        playerluck = playerluck + 2
                    elif inflict_type == "PROTECT":
                        uplim = 99 + playerluck
                        if uplim < 0:
                            protect = True
                        else:
                            protect = random.randint(0,uplim)
                        if protect < 96:
                            print("Protect Failed...")
                            protect = False
                    elif inflict_type == "POISON" and poisonkit:
                        which = 1
        
                        if which == "1" and ahp > 0:
                            print("You poison the " + label1 + ".")
                            apoison = apoison + 3
                        else:
                            print("Invalid Input")
                    elif inflict_type == "TRANSFUSION" and salamanderblood:
                        health = health + 8
                        if health > healthmax:
                            health = healthmax
                        if puncture:
                            puncture = False
                            print("Healed the puncture!")
                        print("You focus and heal 8 health points.")
                    elif inflict_type == "REFLECTION" and mirror == True:
                        uplim = 1 + playerluck
                        refrng = 0
                        if uplim < 1:
                            refrng = 0
                        else:
                            refrng = random.randint(0,uplim)
                        if refrng == 0:
                            print("Reflection Failed...")
                        else:
                            playerreflect = True
                            print("Reflection Successful!")
                    elif inflict_type == "SUFFERING" and sufferingnettle:
                        suffer_rng = 0
                        uplim = 99 + playerluck
                        if uplim < 0:
                            suffer_rng = 0
                        else: suffer_rng = random.randint(1,uplim)
                        which = 1
                        #enemy 1
                        if which == "1":
                            if suffer_rng < 85:
                                print("Ambush Failed...")
                            else:
                                asuffer = asuffer + 3
                                print("Ambush succeeded, " + label1 + " is now neutralized")
                        else:
                            inflict_type = ""
                    elif inflict_type == "GAMBLE" and cursedcoin:
                        gamble = random.randint(0,1)
                        which = 1
                        #enemy 1
                        if which == "1":
                            if gamble == 1:
                                print("Curse Backfired...")
                                playerluck = playerluck - 2
                            else:
                                aluck = aluck - 2
                                print(label1 + " was cursed successfully!")
                        else:
                            inflict_type = ""

                        
                    if inflict_type == "CHANCE" or inflict_type == "PROTECT" or (inflict_type == "GAMBLE" and cursedcoin) or (inflict_type == "POISON" and poisonkit) or (inflict_type == "TRANSFUSION" and salamanderblood) or (inflict_type == "SUFFERING" and sufferingnettle) or (inflict_type == "REFLECTION" and mirror):
                        mana = mana - 1
                    else:
                        print("Invalid Input")
            if ahp < 1 or health < 1:
                break
            print('''
            
            
            ''')
            if ahp > 0:
                if aintent == 1:
                    attack = 16 + apunchboost
                    if playerblock > 0:
                        print(label1 + "bypasses your shield!")
                        health = health - attack
                    else:
                        health = health - attack
                    print("You have been hit for " + str(attack) + ".")
                else:
                    if playersafe:
                        playersafe = False
                        puncture = False
                        print("Inflict Negated.")
                    else:
                        puncture = True
                        print(label1 +" has pierced you.")
                    
    elif a == 3:
        
        aintent = 1
        bintent = 2
        cintent = 1
        ahp = 90
        bhp = 90
        chp = 90
        
        enemystringtext = "In front of you, there is a " + label1 + " 1"
        if two > 0:
            enemystringtext = enemystringtext + " and a " + label2 + " 2"
        
        if three > 0:
            enemystringtext = enemystringtext + " along with a " + label3 + " 3"
        
        enemystringtext = enemystringtext + "."
        print(enemystringtext)
        
        
        while (ahp > 0 or bhp > 0 or chp > 0) and health > 0:
        
            if protect == True:
                protect = False
        
            if playerreflect == True:
                playerreflect = False
        
            asuffer = asuffer - 1
            bsuffer = bsuffer - 1
            csuffer = csuffer - 1
            
            ahp = ahp - apoison
            if apoison > 0:
                apoison = apoison - 1
            bhp = bhp - bpoison
            if bpoison > 0:
                bpoison = bpoison - 1
            chp = chp - cpoison
            if cpoison > 0:
                cpoison = cpoison - 1
        
            if ahp > 0:
                print("")
                print(label1 + " 1 hp: " + str(ahp))
                print("")
            if bhp > 0:
                print(label2 + " 2 hp: " + str(bhp))
                print("")
            if chp > 0:
                print(label3 + " 3 hp: " + str(chp))
                print("")
        
            
            #puts the intent into words
            #is a while loop because i wanted to be able to hide it in the code
            while True:
        
                aintent_label = ""
                bintent_label = ""
                c_intent_label = ""
        
                if aintent == 2:
                    aintent = 1
                    aintent_label = "attack"
                elif aintent == 1:
                    aintent_label = "buff"
                if bintent == 2:
                    bintent = 1
                    bintent_label = "attack"
                elif bintent == 1:
                    bintent = 2
                    bintent_label = "buff"
                if cintent == 2:
                    cintent = 1
                    cintent_label = "attack"
                elif cintent == 1:
                    cintent = 2
                    cintent_label = "buff"
                break
        
        
            if ahp > 0 and blindbattery != True:
                print(label1 + " 1 will " + aintent_label + ".")
                print("")
            if bhp > 0 and blindbattery != True:
                print(label2 + " 2 will " + bintent_label + ".")
                print("")
            if chp > 0 and blindbattery != True:
                print(label3 + " 3 will " + cintent_label + ".")
                print("")
            if blindbattery:
                print("You cannot determine the enemy's intentions.")
            
        
        
            #the player's actions
            
            mana = 3
            if wrath:
                mana = 2
            if blindbattery == True:
                mana = mana * 2
        
            while mana > 0 and health > 0 and (ahp > 0 or bhp > 0 or chp > 0):
                print('''
                
                
                
                ''')
                print("Spirit: " + str(mana))
                print("")
                print("Health: " + str(health) + "/" + str(healthmax))
                print("")
                print("Block: " + str(playerblock))
                choice = input("Do you wish to attack, defend, buff, or inflict? ")
                choice = choice.upper()
                
                
                if choice == "ATTACK":
                    which = input("Do you wish to attack enemy 1, 2, or 3? ")
                    print("")
                    chain = 1
                    if looper:
                        try:
                            chain = int(input("How many times do you wish to chain your action? "))
                        except ValueError:
                            chain = 1
                        if chain > mana:
                            chain = mana
                    for i in range(chain):
                        #enemy 1
                        if which == "1" and ahp > 0:
                            print("You attack the " + label1 + ".")
                            if ablock > 0:
                                print("You hit the " + label1 + "'s block!")
                                ablock = ablock - 1
                                mana = mana - 1
                            else:
                                attack = random.randint(7,11) + playerpunchboost - weak
                                if wrath:
                                    attack = attack * 3
                                if attack < 1:
                                    attack = 0
                                ahp = ahp - attack
                                mana = mana - 1
                                print("You dealt " + str(attack) + " damage!")
                                if ahp < 1:
                                    print("You've killed the " + label1 + "!")
                                    break
                                else:
                                    print(label1 + " 1 hp: " + str(ahp))
                            
                           
                        elif which == "1" and ahp < 1:
                            if one > 0:
                                print("That enemy is dead")
                            else:
                                print("invalid input.")
                                
                                
                        #enemy 2     
                        elif which == "2" and bhp > 0:
                            print("You attack the " + label2 + ".")
                            if bblock > 0:
                                print("You hit the " + label2 + "'s block!")
                                bblock = bblock - 1
                                mana = mana - 1
                            else:
                                attack = random.randint(7,11) + playerpunchboost - weak
                                if wrath:
                                    attack = attack * 3
                                if attack < 1:
                                    attack = 0
                                bhp = bhp - attack
                                mana = mana - 1
                                print("You dealt " + str(attack) + " damage!")
                                if bhp < 1:
                                    print("You've killed the " + label2 + "!")
                                    break
                                else:
                                    print(label2 + " 1 hp: " + str(bhp))
                                    
                        elif which == "2" and bhp < 1:
                            if two > 0:
                                print("That enemy is dead")
                            else:
                                print("invalid input.")
                                
                        #enemy 3     
                        elif which == "3" and chp > 0:
                            print("You attack the " + label3 + ".")
                            if cblock > 0:
                                print("You hit the " + label3 + "'s block!")
                                cblock = cblock - 1
                                mana = mana - 1
                            else:
                                attack = random.randint(7,11) + playerpunchboost - weak
                                if wrath:
                                    attack = attack * 3
                                if attack < 1:
                                    attack = 0
                                chp = chp - attack
                                mana = mana - 1
                                print("You dealt " + str(attack) + " damage!")
                                if chp < 1:
                                    print("You've killed the " + label3 + "!")
                                    break
                                else:
                                    print(label3 + " 1 hp: " + str(chp))
                                
                        elif which == "3" and chp < 1:
                            if three > 0:
                                print("That enemy is dead")
                            else:
                                print("invalid input.")
                                
                        else:
                            print("Invalid Input.")
                elif choice == "BUFF":
                    chain = 1
                    if looper:
                        try:
                            chain = int(input("How many times do you wish to chain your action? "))
                        except ValueError:
                            chain = 1
                        if chain > mana:
                            chain = mana
                    for i in range(chain):
                        boost_type = random.randint(1,2)
                        if boost_type == 1:
                            print("Attack Boost!")
                            boostrng = 0
                            uplim = 4 + playerluck
                            if uplim < 0:
                                boostrng = 0
                            else:
                                boostrng = random.randint(1,uplim)
                            playerpunchboost = playerpunchboost + boostrng
                            print("Attack boosted by " + str(boostrng) + ", with a total boost of " + str(playerpunchboost) + ".")
                        elif boost_type == 2:
                            print("Defend boost!")
                            boostrng = 0
                            uplim = 4 + playerluck
                            if uplim < 0:
                                boostrng = 0
                            else:
                                boostrng = random.randint(1,uplim)
                            playerdefendboost = playerdefendboost + boostrng
                            print("Defend boosted by " + str(boostrng) + ", with a total boost of " + str(playerdefendboost) + ".")
                        mana = mana - 1
                elif choice == "DEFEND":
                    chain = 1
                    if looper:
                        try:
                            chain = int(input("How many times do you wish to chain your action? "))
                        except ValueError:
                            chain = 1
                        if chain > mana:
                            chain = mana
                    for i in range(chain):
                        blockrng = 0
                        uplim = 1 + playerdefendboost
                        if uplim < 0:
                            blockrng == 0
                        else:
                            blockrng = random.randint(-1,uplim)
                        if blockrng == 0:
                            print("Block Failed...")
                        elif blockrng > 0:
                            playerblock = playerblock + 1
                            print("Successful defend!")
                            print("Total block: " + str(playerblock))
                        mana = mana - 1
                elif choice == "INFLICT":
                    #boost luck
                    print("Inflict Chance")
                    #3% chance to be invincible one turn
                    print("Inflict Protect")
                    
                    #Relics detailed at very top
                    if poisonkit == True:
                        print("Inflict Poison")
                    if salamanderblood == True:
                        print("Inflict Transfusion")
                    if mirror == True:
                        print("Inflict Reflection")
                    if sufferingnettle == True:
                        print("Inflict Suffering")
                    if cursedcoin == True:
                        print("Inflict Gamble")
                    inflict_type = input("What inflict would you like to use? ")
                    inflict_type = inflict_type.upper()
                    
                    #items will add more inflicts
                    
                    
                    if inflict_type == "CHANCE":
                        print("Luck increased!")
                        playerluck = playerluck + 2
                    elif inflict_type == "PROTECT":
                        uplim = 99 + playerluck
                        if uplim < 0:
                            protect = True
                        else:
                            protect = random.randint(0,uplim)
                        if protect < 96:
                            print("Protect Failed...")
                            protect = False
                    elif inflict_type == "POISON" and poisonkit:
                        which = input("Do you wish to poison enemy 1, 2, or 3? ")
            
                        if which == "1" and ahp > 0:
                            print("You poison the " + label1 + ".")
                            apoison = apoison + 3
                        elif which == "1" and ahp < 1:
                            if one > 0:
                                print("That enemy is dead")
                            else:
                                print("invalid input.")
                            #enemy 2
                        elif which == "2" and bhp > 0:
                            print("You poison the " + label2 + ".")
                            bpoison = bpoison + 3
                        elif which == "2" and bhp < 1:
                            if two > 0:
                                print("That enemy is dead")
                            else:
                                print("invalid input.")
                        #enemy 3
                        elif which == "3" and chp > 0:
                            print("You poison the " + label3 + ".")
                            cpoison = cpoison + 3
                        elif which == "3" and chp < 1:
                            if three > 0:
                                print("That enemy is dead")
                            else:
                                print("invalid input.")
                        else:
                            mana = mana + 1
                    elif inflict_type == "TRANSFUSION" and salamanderblood:
                        health = health + 8
                        if health > healthmax:
                            health = healthmax
                        print("You focus and heal 8 health points.")
                    elif inflict_type == "REFLECTION" and mirror:
                        uplim = 1 + playerluck
                        refrng = 0
                        if uplim < 1:
                            refrng = 0
                        else:
                            refrng = random.randint(0,uplim)
                        if refrng == 0:
                            print("Reflection Failed...")
                        else:
                            playerreflect = True
                            print("Reflection Successful!")
                    elif inflict_type == "SUFFERING" and sufferingnettle:
                        suffer_rng = 0
                        uplim = 99 + playerluck
                        if uplim < 0:
                            suffer_rng = 0
                        else: suffer_rng = random.randint(1,uplim)
                        which = input("Which enemy do you want to suffer? ")
                        #enemy 1
                        if which == "1":
                            if suffer_rng < 85:
                                print("Ambush Failed...")
                            else:
                                asuffer = asuffer + 3
                                print("Ambush succeeded, " + label1 + " is now neutralized")
                        elif which == "1" and ahp < 1:
                            if one > 0:
                                print("That enemy is dead")
                            else:
                                print("Invalid input.")
                                inflict_type = ""
                        #enemy 2
                        elif which == "2":
                            if suffer_rng < 85:
                                print("Ambush Failed...")
                            else:
                                bsuffer = bsuffer + 3
                                print("Ambush succeeded, " + label2 + " is now neutralized")
                        elif which == "2" and bhp < 1:
                            if two > 0:
                                print("That enemy is dead")
                            else:
                                print("Invalid input.")
                                inflict_type = ""
                        #enemy 1
                        if which == "3":
                            if suffer_rng < 85:
                                print("Ambush Failed...")
                            else:
                                csuffer = csuffer + 3
                                print("Ambush succeeded, " + label3 + " is now neutralized")
                        elif which == "3" and chp < 1:
                            if three > 0:
                                print("That enemy is dead")
                            else:
                                print("invalid input.")
                                inflict_type = ""
                        else:
                            print("Invalid Input")
                            inflict_type = ""
                    elif inflict_type == "GAMBLE" and cursedcoin:
                        gamble = random.randint(0,1)
                        which = input("Which enemy do you want to curse? ")
                        #enemy 1
                        if which == "1":
                            if gamble == 1:
                                print("Curse Backfired...")
                                playerluck = playerluck - 2
                            else:
                                aluck = aluck - 2
                                print(label1 + " was cursed successfully!")
                        elif which == "1" and ahp < 1:
                            if one > 0:
                                print("That enemy is dead")
                            else:
                                print("invalid input.")
                                inflict_type = ""
                        #enemy 2
                        if which == "2":
                            if gamble == 1:
                                print("Curse Backfired...")
                                playerluck = playerluck - 2
                            else:
                                bluck = bluck - 2
                                print(label2 + " was cursed successfully!")
                        elif which == "2" and bhp < 1:
                            if two > 0:
                                print("That enemy is dead")
                            else:
                                print("invalid input.")
                                inflict_type = ""
                        #enemy 3
                        if which == "3":
                            if gamble == 1:
                                print("Curse Backfired...")
                                playerluck = playerluck - 2
                            else:
                                cluck = cluck - 2
                                print(label3 + " was cursed successfully!")
                        elif which == "3" and chp < 1:
                            if three > 0:
                                print("That enemy is dead")
                            else:
                                print("invalid input.")
                                inflict_type = ""
                            
                    if inflict_type == "CHANCE" or inflict_type == "PROTECT" or (inflict_type == "GAMBLE" and cursedcoin) or (inflict_type == "POISON" and poisonkit) or (inflict_type == "TRANSFUSION" and salamanderblood) or (inflict_type == "SUFFERING" and sufferingnettle) or (inflict_type == "REFLECTION" and mirror):
                        mana = mana - 1
                    else:
                        print("Invalid Input")
            if (ahp < 1 and bhp < 1 and chp < 1) or health < 1:
                break
            
            if ahp > 0:
                if aintent == 1:
                    attack = 14 + apunchboost
                    if playerblock > 1:
                        print("Attack Blocked!")
                        playerblock = playerblock - 1
                    else:
                        health = health - attack
                        print(label1 + " hit you for " + str(attack) + ".")
                elif aintent == 2:
                    apunchboost = apunchboost + 2
                    bpunchboost = bpunchboost + 2
                    cpunchboost = cpunchboost + 2
                    print(label1 + " boosted every Sentry's attacks!")
            if bhp > 0:
                if bintent == 1:
                    attack = 14 + bpunchboost
                    if playerblock > 1:
                        print("Attack Blocked!")
                        playerblock = playerblock - 1
                    else:
                        health = health - attack
                        print(label2 + " hit you for " + str(attack) + ".")
                elif bintent == 2:
                    apunchboost = apunchboost + 2
                    bpunchboost = bpunchboost + 2
                    cpunchboost = cpunchboost + 2
                    print(label2 + " boosted every Sentry's attacks!")
            if chp > 0:
                if cintent == 1:
                    attack = 14 + cpunchboost
                    if playerblock > 1:
                        print("Attack Blocked!")
                        playerblock = playerblock - 1
                    else:
                        health = health - attack
                        print(label3 + " hit you for " + str(attack) + ".")
                elif cintent == 2:
                    apunchboost = apunchboost + 2
                    bpunchboost = bpunchboost + 2
                    cpunchboost = cpunchboost + 2
                    print(label3 + " boosted every Sentry's attacks!")
    
    if health < 1:
        print("Game Over.")
        diff_select()
        exo()
    else:
        global gold
        infinite_money_generator = random.randint(18,32)
        if b != 0:
            infinite_money_generator = infinite_money_generator + random.randint(18,32)
        if c != 0:
            infinite_money_generator = infinite_money_generator + random.randint(18,32)
        infinite_money_generator = infinite_money_generator * 3
        gold = gold + infinite_money_generator
        print("You got " + str(infinite_money_generator) + " gold.") 
        print("You now have " + str(gold) + " gold.")
        if salamanderblood and health != healthmax:
            health = health + 4
            if health > healthmax:
                health = healthmax
            print("You healed 4 health points.")

def fight(one,two):
    import random
    a = 0
    b = 0
    c = 0
    
    three = 0
    
    if two > 0:
        three = random.randint(0,1)
    
    if one > 0:
        a = random.randint(1,10)
    if two > 0:
        b = random.randint(1,10)
    if three > 0:
        c = random.randint(1,10)
        
    global poisonkit
    global salamanderblood
    global mirror
    global wrath
    global sufferingnettle
    global soulsafe
    global blindbattery
    global cursedcoin
    
    
    
    #below is the code that determines what enemy the entity is, and assigns
    #it the appropriate name
    
    label1 = ""
    label2 = ""
    label3 = ""
    
    if a == 1 or a == 2 or a == 3:
        label1 = "Grub"
    elif a == 4 or a == 5:
        label1 = "Slime Ball"
    elif a == 6 or a == 7:
        label1 = "Slime Globe"
    elif a == 8 or a == 9 or a == 10:
        label1 = "Drob"
    elif a == 11 or a == 12:
        label1 = "Sentry"
    elif a == 13:
        label1 = "Drob Elite"
    elif a == 14:
        label1 = "Model"
    elif a == 15:
        label1 = "SUPER SLIME"
    elif a == 16:
        label1 = "SENTRY CORE"
    elif a == 17:
        label1 = "MODEL MOULD"
    
    if b == 1 or b == 2 or b == 3:
        label2 = "Grub"
    elif b == 4 or b == 5:
        label2 = "Slime Ball"
    elif b == 6 or b == 7:
        label2 = "Slime Globe"
    elif b == 8 or b == 9 or b == 10:
        label2 = "Drob"
    elif b == 11 or b == 12:
        label2 = "Sentry"
        
    if c == 1 or c == 2 or c == 3:
        label3 = "Grub"
    elif c == 4 or c == 5:
        label3 = "Slime Ball"
    elif c == 6 or c == 7:
        label3 = "Slime Globe"
    elif c == 8 or c == 9 or c == 10:
        label3 = "Drob"
    elif c == 11 or c == 12:
        label3 = "Sentry"
    
    #introductory text
    
    enemystringtext = "In front of you, there is a " + label1 + " 1"
    if two > 0:
        enemystringtext = enemystringtext + " and a " + label2 + " 2"
        
    if three > 0:
        enemystringtext = enemystringtext + " along with a " + label3 + " 3"
        
    enemystringtext = enemystringtext + "."
    print(enemystringtext)
    
    #sets up the variables for the player that are used in the combat
    
    playerblock = 0
    playerpunchboost = 0
    playerdefendboost = 0
    playerluck = 0
    playerreflect = False
    protect = 0
    weak = 0
    
    global playersafe
    playersafe = False
    if soulsafe:
        playersafe = True
    
    #determines the enemy's health, and sets up the variables used in the fight
    
    ahp = 0
    bhp = 0
    chp = 0
    
    adefend = 0
    bdefend = 0
    cdefend = 0
    
    ablock = 0
    bblock = 0
    cblock = 0
    
    apunch = 0
    bpunch = 0
    cpunch = 0
    
    astatus = 0
    bstatus = 0
    cstatus = 0
    
    abuff = 0
    bbuff = 0
    cbuff = 0
    
    apunchboost = 0
    bpunchboost = 0
    cpunchboost = 0
    
    adefendboost = 0
    bdefendboost = 0
    cdefendboost = 0
    
    aluck = 0
    bluck = 0
    cluck = 0
    
    apoison = 0
    bpoison = 0
    cpoison = 0
    
    asuffer = 0
    bsuffer = 0
    csuffer = 0
    
    ahp = random.randint(12,20)
    if two > 0:
        bhp = random.randint(12,20)
    else:
        bhp = 0
    if three > 0:
        chp = random.randint(12,20)
    else:
        chp = 0
    
    if a == 6 or a == 7:
        ahp = ahp * 2
    if b == 6 or b == 7:
        bhp = bhp * 2
    if c == 6 or c == 7:
        chp = chp * 2
    
    global health
    global healthmax
    
    
    
    #the loop of the fight itself
    
    while (ahp > 0 or bhp > 0 or chp > 0) and health > 0:
        
        if protect == True:
            protect = False
        
        if playerreflect == True:
            playerreflect = False
        
        asuffer = asuffer - 1
        bsuffer = bsuffer - 1
        csuffer = csuffer - 1
        
        ahp = ahp - apoison
        if apoison > 0:
            apoison = apoison - 1
        bhp = bhp - bpoison
        if bpoison > 0:
            bpoison = bpoison - 1
        chp = chp - cpoison
        if cpoison > 0:
            cpoison = cpoison - 1
        
        if ahp > 0:
            print("")
            print(label1 + " 1 hp: " + str(ahp))
            print("")
        if bhp > 0:
            print(label2 + " 2 hp: " + str(bhp))
            print("")
        if chp > 0:
            print(label3 + " 3 hp: " + str(chp))
            print("")
        
        #intent determines whether the enemy will status, buff, defend, or attack  
        #0: no intent
        #1: attack
        #2: defend
        #3: status (inflict)
        #4: buff
        
        aintent = 0
        bintent = 0
        cintent = 0
        
        if ahp > 0:
            aintent = random.randint(1,4)
        if bhp > 0:
            bintent = random.randint(3,4)
        if chp > 0:
            cintent = random.randint(1,2)
            
        #puts the intent into words
        #is a while loop because i wanted to be able to hide it in the code
        while True:
        
            aintent_label = ""
            bintent_label = ""
            c_intent_label = ""
        
            if aintent == 1:
                aintent_label = "attack"
            elif aintent == 2:
                aintent_label = "defend"
            elif aintent == 3:
                aintent_label = "inflict"
            elif aintent == 4:
                aintent_label = "buff"
            
            if bintent == 1:
                bintent_label = "attack"
            elif bintent == 2:
                bintent_label = "defend"
            elif bintent == 3:
                bintent_label = "inflict"
            elif bintent == 4:
                bintent_label = "buff"
            
            if cintent == 1:
                cintent_label = "attack"
            elif cintent == 2:
                cintent_label = "defend"
            elif cintent == 3:
                cintent_label = "inflict"
            elif cintent == 4:
                cintent_label = "buff"
            break
        
        
        if ahp > 0 and blindbattery != True:
            print(label1 + " 1 will " + aintent_label + ".")
            print("")
        if bhp > 0 and blindbattery != True:
            print(label2 + " 2 will " + bintent_label + ".")
            print("")
        if chp > 0 and blindbattery != True:
            print(label3 + " 3 will " + cintent_label + ".")
            print("")
        if blindbattery:
            print("You cannot determine the enemy's intentions.")
            
        
        
        #the player's actions
        
        mana = 3
        if wrath:
            mana = 2
        if blindbattery == True:
            mana = mana * 2
        
        while mana > 0 and health > 0 and (ahp > 0 or bhp > 0 or chp > 0):
            print('''
            
            
            
            ''')
            print("Spirit: " + str(mana))
            print("")
            print("Health: " + str(health) + "/" + str(healthmax))
            print("")
            print("Block: " + str(playerblock))
            choice = input("Do you wish to attack, defend, buff, or inflict? ")
            choice = choice.upper()
            
            
            if choice == "ATTACK":
                which = input("Do you wish to attack enemy 1, 2, or 3? ")
                print("")
                #enemy 1
                chain = 1
                if looper:
                    try:
                        chain = int(input("How many times do you wish to chain your action? "))
                    except ValueError:
                        chain = 1
                    if chain > mana:
                        chain = mana
                for i in range(chain):
                    if which == "1" and ahp > 0:
                        print("You attack the " + label1 + ".")
                        if ablock > 0:
                            print("You hit the " + label1 + "'s block!")
                            ablock = ablock - 1
                            mana = mana - 1
                        else:
                            attack = random.randint(7,11) + playerpunchboost - weak
                            if wrath:
                                attack = attack * 3
                            if attack < 1:
                                attack = 0
                            ahp = ahp - attack
                            mana = mana - 1
                            print("You dealt " + str(attack) + " damage!")
                            if ahp < 1:
                                print("You've killed the " + label1 + "!")
                                break
                            else:
                                print(label1 + " 1 hp: " + str(ahp))
                            
                           
                    elif which == "1" and ahp < 1:
                        if one > 0:
                            print("That enemy is dead")
                        else:
                            print("invalid input.")
                            
                            
                    #enemy 2     
                    elif which == "2" and bhp > 0:
                        print("You attack the " + label2 + ".")
                        if bblock > 0:
                            print("You hit the " + label2 + "'s block!")
                            bblock = bblock - 1
                            mana = mana - 1
                        else:
                            attack = random.randint(7,11) + playerpunchboost - weak
                            if wrath:
                                attack = attack * 3
                            if attack < 1:
                                attack = 0
                            bhp = bhp - attack
                            mana = mana - 1
                            print("You dealt " + str(attack) + " damage!")
                            if bhp < 1:
                                print("You've killed the " + label2 + "!")
                                break
                            else:
                                print(label2 + " 1 hp: " + str(bhp))
                                
                    elif which == "2" and bhp < 1:
                        if two > 0:
                            print("That enemy is dead")
                        else:
                            print("invalid input.")
                            
                    #enemy 3     
                    elif which == "3" and chp > 0:
                        print("You attack the " + label3 + ".")
                        if cblock > 0:
                            print("You hit the " + label3 + "'s block!")
                            cblock = cblock - 1
                            mana = mana - 1
                        else:
                            attack = random.randint(7,11) + playerpunchboost - weak
                            if wrath:
                                attack = attack * 3
                            if attack < 1:
                                attack = 0
                            chp = chp - attack
                            mana = mana - 1
                            print("You dealt " + str(attack) + " damage!")
                            if chp < 1:
                                print("You've killed the " + label3 + "!")
                                break
                            else:
                                print(label3 + " 1 hp: " + str(chp))
                            
                    elif which == "3" and chp < 1:
                        if three > 0:
                            print("That enemy is dead")
                        else:
                            print("invalid input.")
                            
                    else:
                        print("Invalid Input.")
            elif choice == "BUFF":
                chain = 1
                if looper:
                    try:
                        chain = int(input("How many times do you wish to chain your action? "))
                    except ValueError:
                        chain = 1
                    if chain > mana:
                        chain = mana
                for i in range(chain):
                    boost_type = random.randint(1,2)
                    if boost_type == 1:
                        print("Attack Boost!")
                        boostrng = 0
                        uplim = 4 + playerluck
                        if uplim < 0:
                            boostrng = 0
                        else:
                            boostrng = random.randint(1,uplim)
                        playerpunchboost = playerpunchboost + boostrng
                        print("Attack boosted by " + str(boostrng) + ", with a total boost of " + str(playerpunchboost) + ".")
                    elif boost_type == 2:
                        print("Defend boost!")
                        boostrng = 0
                        uplim = 4 + playerluck
                        if uplim < 0:
                            boostrng = 0
                        else:
                            boostrng = random.randint(1,uplim)
                        playerdefendboost = playerdefendboost + boostrng
                        print("Defend boosted by " + str(boostrng) + ", with a total boost of " + str(playerdefendboost) + ".")
                    mana = mana - 1
            elif choice == "DEFEND":
                
                blockrng = 0
                uplim = 1 + playerdefendboost
                chain = 1
                if looper:
                    try:
                        chain = int(input("How many times do you wish to chain your action? "))
                    except ValueError:
                        chain = 1
                    if chain > mana:
                        chain = mana
                for i in range(chain):
                    if uplim < 0:
                        blockrng == 0
                    else:
                        blockrng = random.randint(-1,uplim)
                    if blockrng == 0:
                        print("Block Failed...")
                    elif blockrng > 0:
                        playerblock = playerblock + 1
                        print("Successful defend!")
                        print("Total block: " + str(playerblock))
                    mana = mana - 1
            elif choice == "INFLICT":
                #boost luck
                print("Inflict Chance")
                #3% chance to be invincible one turn
                print("Inflict Protect")
                
                #Relics detailed at very top
                if poisonkit == True:
                    print("Inflict Poison")
                if salamanderblood == True:
                    print("Inflict Transfusion")
                if mirror == True:
                    print("Inflict Reflection")
                if sufferingnettle == True:
                    print("Inflict Suffering")
                if cursedcoin == True:
                    print("Inflict Gamble")
                inflict_type = input("What inflict would you like to use? ")
                inflict_type = inflict_type.upper()
                
                #items will add more inflicts
                
                
                if inflict_type == "CHANCE":
                    print("Luck increased!")
                    playerluck = playerluck + 2
                elif inflict_type == "PROTECT":
                    uplim = 99 + playerluck
                    if uplim < 0:
                        protect = True
                    else:
                        protect = random.randint(0,uplim)
                    if protect < 96:
                        print("Protect Failed...")
                        protect = False
                elif inflict_type == "POISON" and poisonkit:
                    which = input("Do you wish to poison enemy 1, 2, or 3? ")
        
                    if which == "1" and ahp > 0:
                        print("You poison the " + label1 + ".")
                        apoison = apoison + 3
                    elif which == "1" and ahp < 1:
                        if one > 0:
                            print("That enemy is dead")
                        else:
                            print("invalid input.")
                    #enemy 2
                    elif which == "2" and bhp > 0:
                        print("You poison the " + label2 + ".")
                        bpoison = bpoison + 3
                    elif which == "2" and bhp < 1:
                        if two > 0:
                            print("That enemy is dead")
                        else:
                            print("invalid input.")
                    #enemy 3
                    elif which == "3" and chp > 0:
                        print("You poison the " + label3 + ".")
                        cpoison = cpoison + 3
                    elif which == "3" and chp < 1:
                        if three > 0:
                            print("That enemy is dead")
                        else:
                            print("invalid input.")
                    else:
                        mana = mana + 1
                elif inflict_type == "TRANSFUSION" and salamanderblood:
                    health = health + 8
                    if health > healthmax:
                        health = healthmax
                    print("You focus and heal 8 health points.")
                elif inflict_type == "REFLECTION" and mirror:
                    uplim = 1 + playerluck
                    refrng = 0
                    if uplim < 1:
                        refrng = 0
                    else:
                        refrng = random.randint(0,uplim)
                    if refrng == 0:
                        print("Reflection Failed...")
                    else:
                        playerreflect = True
                        print("Reflection Successful!")
                elif inflict_type == "SUFFERING" and sufferingnettle:
                    suffer_rng = 0
                    uplim = 99 + playerluck
                    if uplim < 0:
                        suffer_rng = 0
                    else: suffer_rng = random.randint(1,uplim)
                    which = input("Which enemy do you want to suffer? ")
                    #enemy 1
                    if which == "1":
                        if suffer_rng < 85:
                            print("Ambush Failed...")
                        else:
                            asuffer = asuffer + 3
                            print("Ambush succeeded, " + label1 + " is now neutralized")
                    elif which == "1" and ahp < 1:
                        if one > 0:
                            print("That enemy is dead")
                        else:
                            print("Invalid input.")
                            inflict_type = ""
                    #enemy 2
                    elif which == "2":
                        if suffer_rng < 85:
                            print("Ambush Failed...")
                        else:
                            bsuffer = bsuffer + 3
                            print("Ambush succeeded, " + label2 + " is now neutralized")
                    elif which == "2" and bhp < 1:
                        if two > 0:
                            print("That enemy is dead")
                        else:
                            print("Invalid input.")
                            inflict_type = ""
                    #enemy 1
                    if which == "3":
                        if suffer_rng < 85:
                            print("Ambush Failed...")
                        else:
                            csuffer = csuffer + 3
                            print("Ambush succeeded, " + label3 + " is now neutralized")
                    elif which == "3" and chp < 1:
                        if three > 0:
                            print("That enemy is dead")
                        else:
                            print("invalid input.")
                            inflict_type = ""
                    else:
                        print("Invalid Input")
                        inflict_type = ""
                elif inflict_type == "GAMBLE" and cursedcoin:
                    gamble = random.randint(0,1)
                    which = input("Which enemy do you want to curse? ")
                    #enemy 1
                    if which == "1":
                        if gamble == 1:
                            print("Curse Backfired...")
                            playerluck = playerluck - 2
                        else:
                            aluck = aluck - 2
                            print(label1 + " was cursed successfully!")
                    elif which == "1" and ahp < 1:
                        if one > 0:
                            print("That enemy is dead")
                        else:
                            print("invalid input.")
                            inflict_type = ""
                    #enemy 2
                    if which == "2":
                        if gamble == 1:
                            print("Curse Backfired...")
                            playerluck = playerluck - 2
                        else:
                            bluck = bluck - 2
                            print(label2 + " was cursed successfully!")
                    elif which == "2" and bhp < 1:
                        if two > 0:
                            print("That enemy is dead")
                        else:
                            print("invalid input.")
                            inflict_type = ""
                    #enemy 3
                    if which == "3":
                        if gamble == 1:
                            print("Curse Backfired...")
                            playerluck = playerluck - 2
                        else:
                            cluck = cluck - 2
                            print(label3 + " was cursed successfully!")
                    elif which == "3" and chp < 1:
                        if three > 0:
                            print("That enemy is dead")
                        else:
                            print("invalid input.")
                            inflict_type = ""
                        
                if inflict_type == "CHANCE" or inflict_type == "PROTECT" or (inflict_type == "GAMBLE" and cursedcoin) or (inflict_type == "POISON" and poisonkit) or (inflict_type == "TRANSFUSION" and salamanderblood) or (inflict_type == "SUFFERING" and sufferingnettle) or (inflict_type == "REFLECTION" and mirror):
                    mana = mana - 1
                else:
                    print("Invalid Input")
        if (ahp < 1 and bhp < 1 and chp < 1) or health < 1:
            break
        #enemy's actions
        #1A 2D 3I 4B
        if aintent == 1 and ahp > 0:
            uplim = 19 + aluck
            if uplim < 1:
                apunch = 0
            else:
                apunch = random.randint(8,uplim) + apunchboost
                if a == 8 or a == 9 or a == 10:
                    apunch = apunch * 2
            if asuffer > 0:
                apunch = 1
            if wrath:
                apunch = apunch * 3
            if playerblock > 0:
                playerblock = playerblock - 1
                print("Blocked " + label1 + "'s Attack!")
            elif protect > 0:
                print("Protected yourself from " + label1 + "'s Attack!")
            else:
                health = health - apunch
                print(label1 + " has hit you for " + str(apunch) + ".")
        elif aintent == 2 and ahp > 0:
            enemy = random.randint(1,3)
            if enemy == 1:
                adefend = adefend + 1 + adefendboost
                print(label1 + " has blocked itself.")
            elif enemy == 2:
                bdefend = bdefend + 1 + bdefendboost
                print(label1 + " has blocked" + label2 + ".")
            else:
                cdefend = cdefend + 1 + cdefendboost
                print(label1 + " has blocked " + label3 + ".")
        elif aintent == 3 and ahp > 0:
            if playersafe:
                print("Inflict Negated.")
                playersafe = False
            else:
                weak = random.randint(2,5)
                print(label1 + " has weakened you!")
        elif aintent == 4 and ahp > 0:
            buff = random.randint(1,2)
            bufftype = random.randint(1,2)
            if buff == 1:
                if bufftype == 1:
                    boost = random.randint(2,3)
                    apunchboost = apunchboost + boost
                    print(label1 + " had its attack boosted by " + str(boost) + ".")
                else:
                    boost = random.randint(2,3)
                    adefendboost = adefendboost + boost
                    print(label1 + " had its defense boosted by " + str(boost) + ".")
            else:
                if bufftype == 1:
                    boost = random.randint(2,3)
                    cpunchboost = cpunchboost + boost
                    print(label3 + " had its attack boosted by " + str(boost) + ".")
                else:
                    boost = random.randint(2,3)
                    cdefendboost = cdefendboost + boost
                    print(label3 + " had its defense boosted by " + str(boost) + ".")
        if bintent == 1 and bhp > 0:
            uplim = 19 + bluck
            if uplim < 1:
                bpunch = 0
            else:
                bpunch = random.randint(8,uplim) + bpunchboost
                if b == 8 or b == 9 or b == 10:
                    bpunch = bpunch * 2
            if bsuffer > 0:
                bpunch = 1
            if wrath:
                bpunch = bpunch * 3
            if playerblock > 0:
                playerblock = playerblock - 1
                print("Blocked " + label2 + "'s Attack!")
            elif protect > 0:
                print("Protected yourself from " + label2 + "'s Attack!")
            else:
                health = health - bpunch
                print(label2 + " has hit you for " + str(bpunch) + ".")
        elif bintent == 2 and bhp > 0:
            enemy = random.randint(1,3)
            if enemy == 1:
                bdefend = bdefend + 1 + bdefendboost
                print(label2 + " has blocked itself.")
            elif enemy == 2:
                adefend = adefend + 1 + adefendboost
                print(label2 + " has blocked" + label1 + ".")
            else:
                cdefend = cdefend + 1 + cdefendboost
                print(label2 + " has blocked " + label3 + ".")
        elif bintent == 3 and bhp > 0:
            if playersafe:
                print("Inflict Negated.")
                playersafe = False
            else:
                weak = random.randint(2,5)
                print(label2 + " has weakened you!")
        elif bintent == 4 and bhp > 0:
            buff = random.randint(1,2)
            bufftype = random.randint(1,2)
            if buff == 1:
                if bufftype == 1:
                    boost = random.randint(2,3)
                    apunchboost = apunchboost + boost
                    print(label1 + " had its attack boosted by " + str(boost) + ".")
                else:
                    boost = random.randint(2,3)
                    adefendboost = adefendboost + boost
                    print(label1 + " had its defense boosted by " + str(boost) + ".")
            else:
                if bufftype == 1:
                    boost = random.randint(2,3)
                    cpunchboost = cpunchboost + boost
                    print(label3 + " had its attack boosted by " + str(boost) + ".")
                else:
                    boost = random.randint(2,3)
                    cdefendboost = cdefendboost + boost
                    print(label3 + " had its defense boosted by " + str(boost) + ".")
        if cintent == 1 and chp > 0:
            uplim = 19 + cluck
            if uplim < 1:
                cpunch = 0
            else:
                cpunch = random.randint(8,uplim) + cpunchboost
                if c == 8 or c == 9 or c == 10:
                    cpunch = cpunch * 2
            if csuffer > 0:
                cpunch = 1
            if wrath:
                cpunch = cpunch * 3
            if playerblock > 0:
                playerblock = playerblock - 1
                print("Blocked " + label3 + "'s Attack!")
            elif protect > 0:
                print("Protected yourself from " + label3 + "'s Attack!")
            else:
                health = health - cpunch
                print(label3 + " has hit you for " + str(cpunch) + ".")
        elif cintent == 2 and chp > 0:
            enemy = random.randint(1,3)
            if enemy == 1:
                cdefend = cdefend + 1 + cdefendboost
                print(label3 + " has blocked itself.")
            elif enemy == 2:
                bdefend = bdefend + 1 + bdefendboost
                print(label3 + " has blocked" + label2 + ".")
            else:
                adefend = adefend + 1 + adefendboost
                print(label3 + " has blocked " + label1 + ".")
        elif cintent == 3 and chp > 0:
            if playersafe:
                print("Inflict Negated.")
                playersafe = False
            else:
                weak = random.randint(2,5)
                print(label3 + " has weakened you!")
        elif cintent == 4 and chp > 0:
            buff = random.randint(1,2)
            bufftype = random.randint(1,2)
            if buff == 1:
                if bufftype == 1:
                    boost = random.randint(2,3)
                    apunchboost = apunchboost + boost
                    print(label1 + " had its attack boosted by " + str(boost) + ".")
                else:
                    boost = random.randint(2,3)
                    adefendboost = adefendboost + boost
                    print(label1 + " had its defense boosted by " + str(boost) + ".")
            else:
                if bufftype == 1:
                    boost = random.randint(2,3)
                    cpunchboost = cpunchboost + boost
                    print(label3 + " had its attack boosted by " + str(boost) + ".")
                else:
                    boost = random.randint(2,3)
                    cdefendboost = cdefendboost + boost
                    print(label3 + " had its defense boosted by " + str(boost) + ".")
                
        
        
    #determines whether you've lost or won, and rewards you accordingly
    
    if health < 1:
        print("Game Over.")
        diff_select()
        exo()
    else:
        global gold
        infinite_money_generator = random.randint(18,32)
        if b != 0:
            infinite_money_generator = infinite_money_generator + random.randint(18,32)
        if c != 0:
            infinite_money_generator = infinite_money_generator + random.randint(18,32)
        if difficulty == 4 or difficulty == 5:
            infinite_money_generator = random.randint(15,25)
        gold = gold + infinite_money_generator
        print("You got " + str(infinite_money_generator) + " gold.") 
        print("You now have " + str(gold) + " gold.")
        if salamanderblood and health != healthmax:
            health = health + 4
            if health > healthmax:
                health = healthmax
            print("You healed 4 health points.")

def exo():
    import random
    global difficulty
    global health
    global healthmax
    global gold
    
    global poisonkit
    global salamanderblood
    global mirror
    global wrath
    global sufferingnettle
    global soulsafe
    global blindbattery
    global cursedcoin
    
    poisonkit = False
    salamanderblood = False
    mirror = False
    wrath = False
    sufferingnettle = False
    soulsafe = False
    blindbattery = False
    cursedcoin = False
    
    
    allrelicscheat = False
    if difficulty == 5:
        allrelicscheat = True
    if allrelicscheat:
        poisonkit = True
        salamanderblood = True
        mirror = True
        wrath = True
        sufferingnettle = True
        soulsafe = True
        blindbattery = True
        cursedcoin = True
    #initialization ^^^
    
    if difficulty == 1:
        spaces_away_from_boss = 8
        #setup ^^^
        while spaces_away_from_boss > 0:
            spaces_away_from_boss = spaces_away_from_boss - 1
            #  vvv  "enemy random number generator"
            erng = random.randint(0,1)
            elitechance = random.randint(1,6)
            shopchance = random.randint(1,8)
            if shopchance == 8:
                shop()
            else:
                if elitechance != 6:
                    fight(1,erng)
                else:
                    elite()
        boss()
            
            
            
        
    elif difficulty == 2:
        health = health - 12
        gold = gold - 23
        spaces_away_from_boss = 10
        #setup ^^^
        while spaces_away_from_boss > 0:
            spaces_away_from_boss = spaces_away_from_boss - 1
            elitechance = random.randint(1,4)
            shopchance = random.randint(1,8)
            if shopchance == 8:
                shop()
            else:
                if elitechance != 4:
                    fight(1,1)
                else:
                    elite()
        boss()
        
        
        
    elif difficulty == 3:
        health = health - 30
        healthmax = healthmax - 20
        gold = gold - 80
        spaces_away_from_boss = 13
        #setup ^^^
        
        while spaces_away_from_boss > 0:
            spaces_away_from_boss = spaces_away_from_boss - 1
            elitechance = random.randint(1,3)
            shopchance = random.randint(1,8)
            if shopchance == 8:
                shop()
            else:
                if elitechance != 3:
                    fight(1,1)
                else:
                    elite()
        boss()
            
    elif difficulty == 4:
        health = health - 50
        healthmax = healthmax - 35
        gold = 0
        spaces_away_from_boss = 16
        wrath = True
        
        while spaces_away_from_boss > 0:
            spaces_away_from_boss = spaces_away_from_boss - 1
            elitechance = random.randint(1,2)
            shopchance = random.randint(1,8)
            if shopchance == 8:
                shop()
            else:
                if elitechance != 2:
                    fight(1,1)
                else:
                    elite()
    elif difficulty == 5:
        health = health - 12
        gold = gold - 23
        spaces_away_from_boss = 10
        #setup ^^^
        while spaces_away_from_boss > 0:
            spaces_away_from_boss = spaces_away_from_boss - 1
            elitechance = random.randint(1,4)
            shopchance = random.randint(1,8)
            if shopchance == 8:
                shop()
            else:
                if elitechance != 4:
                    fight(1,1)
                else:
                    elite()
        boss()    


print("Hello, Mr. Developer Here, More commonly Known as 'Tristan' or 'Palest'.")
print("I'm making this an ACTUAL game in Gamemaker Studio 2, so if you have any feedback, feel free to tell me!")
print("Enjoy the game!")
print('''



''')
diff_select()
exo()
