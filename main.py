from random import randint
from time import sleep
from bcolors import bcolors


'''
Welcome to the Lotto Machine.
This was proudly coded in Python 3.8
The purpose of this program is to make a fun / free way of gambling.
This program works stricly based off of random intergers, there is no luck involved in this.
Coded with VSC (Visual Studio Code) (A great coding IDE)
'''
'''
A couple of issues that I had while making this project is finding a way to print symbols (which I still couldnt fix)but other than that, I didnt have any issues
'''

#################################################################
#                                                               #
#                                                               #
#                 __author__ = Matthew Klein                    #
#                       __Version__ = 1.0                       #
#                           NOTICE:                             #
#        THE BCOLORS IS REQUIRED TO BE IN THE SAME FOLDER       #
#                        AS THE PROGRAM!!                       #
#                                                               #
#                                                               #
#################################################################







#Iteration 1
#################################################
#                                               #
#       Prompt user for starting credits        #
#                                               #
#################################################
welcome_scrn = '#################################################\n#                                               #\n#          Welcome to the LottoMachine!         #\n#                                               #\n#################################################'
info_scrn = '#################################################\n#                                               #\n#                LottoMachine v1                #\n#                                               #\n#################################################'
credits = '0'
clrscrn = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'

def crdtamt():
    global credits
    print(clrscrn)
    print(welcome_scrn)
    credits = input('\nHow many credits would you like to start off with?\n\n')
#Checking if args are legal (According to the rules set.)
    if credits.isdecimal():
        if int(credits) == 0:
            print('\nreally?\n')
            sleep(3)
            print(clrscrn)
            crdtamt()
        if int(credits) > 500:
            print('\nTo not have any unfair advantages or to make it too easy on yourself, please choose a number within 50 - 500.\n')
            sleep(3)
            print(clrscrn)
            crdtamt()
        if int(credits) < 50:
            print('\nThat is not enough credits to start off with. Please choose a number within 50 - 500.\n')
            sleep(3)
            print(clrscrn)
            crdtamt()
        if int(credits) >= 50 and int(credits) <= 500:
            sleep(3)
            multiplieramt()
        #next process.
        #Down to Iteration 4 due to discontined iterations (below)
    else:
        print('\nPlease use numbers.\n')
        sleep(3)
        print(clrscrn)
        crdtamt()


#################################################
#                                               #
#                  Iteration 2                  #
#          How many slots do they want?         #
#                                               #
#################################################

# Discontinued (Only 3 slots available) #

costperslot = 5
slots = '3'

'''

def slotamt():
    global slots
    print(clrscrn)
    print(info_scrn)
    slots = input('\nHow many slots would you like to play?\n\n')
    if slots.isdecimal():
        if int(slots) == 0:
            print('\nreally?\n')
            sleep(3)
            slotamt()
        if int(slots) > 5:
            print('\nThat is too many slots. Please choose a number between 3 and 5.\n')
            sleep(3)
            slotamt()
        if int(slots) < 3:
            print('\nThat is not enough slots to play. Please choose a number between 3 and 5.\n')
            sleep(3)
            slotamt()
        if int(slots) >= 3 and int(slots) <= 5:
            sleep(3)
            betamt()
            #next stage
    else:
        print('Please use numbers.')
        sleep(3)
        slotamt()

'''

#################################################
#                                               #
#                  Iteration 3                  #
#             How much ya wanna bet?            #
#                                               #
#################################################


# DISCONTUNED #

'''

betamount = '10'

def betamt():
    global betamount
    print(clrscrn)
    print(info_scrn)
    print('\nHow much would you like to bet on this spin? Default: 10. Cannot go below 10.\nYour current balance is', int(credits) - costperslot * int(slots), '.\n')
    betamount = input()

    if betamount.isdecimal():
        if int(betamount) > int(credits) - costperslot * int(slots):
            print('\nYou dont have enough money to bet on that amount.\n')
            sleep(3)
            betamt()
        if int(betamount) < 10:
            print('You cannot bet below 10.')
            sleep(3)
            betamt()
        if int(betamount) <= int(credits) - costperslot * int(slots):
            #goto next section.
            multiplieramt()
    else:
        print('Please use numbers.')
        sleep(3)
        betamt()

'''

#################################################
#                                               #
#                  Iteration 4                  #
#                Any multipliers?               #
#                                               #
#################################################

multiplierconf = ''
multiplier = '1'
multiplier_determine = 1

def multiplieramt():
    global multiplierconf
    global multiplier
    global credits
    print(clrscrn)
    print(info_scrn)
    credits = int(credits) - 15
    if int(credits) < 15:
        print('Game Over! You dont have enough Credits to spin again. :(')
        exit()
    if int(credits) - costperslot * int(slots) >= 25:
        print('\nWould you like to purchase a multiplier spin?\nThis will cost an extra 25 credits.\nYou currently have', int(credits), 'credits.')
    multiplierconf = input()
    if 'yes' in multiplierconf.lower():
        credits = int(credits) - 25
        multiplier_determine = randint(1,100)
        if multiplier_determine <= 50:
            multiplier = 1
        elif multiplier_determine <= 51 and multiplier_determine <= 75:
            multiplier = 2
        elif multiplier_determine <= 76 and multiplier_determine <= 85:
            multiplier = 3
        elif multiplier_determine <= 86 and multiplier_determine <= 90:
            multiplier = 4
        elif multiplier_determine <= 91 and multiplier_determine <= 95:
            multiplier = 5
        elif multiplier_determine <= 96 and multiplier_determine <= 100:
            multiplier = 6
    else:
        pass
    print('\n\nYour current multiplier is', multiplier, '\n')
    sleep(3)
    spinslots3()

#################################################
#                                               #
#                  Iteration 5                  #
#              Spin, Those, Slots!              #
#                                               #
#################################################

slot1 = ''
slot2 = ''
slot3 = ''

'''
text image should look like this

###################################
#          |          |           #
#          |          |           #   
#    🔔    #    🔔    #    🔔    #
#          |          |           #
#          |          |           #
###################################
'''

'''

UNSUPPORTED SYMBOLS IN CODE, PLEASE REFERENCE KEY INSTEAD.

'''

'''

3. WATERMELON
4. LEMON
5. GRAPES
6. DIAMOND / GEMSTONE
8. BAR

'''

credsowed = '0'
slot1_1 = '0'
slot2_1 = '0'
slot3_1 = '0'

def spinslots3():
    global slot1
    global slot2
    global slot3
    global slot1_1
    global slot2_1
    global slot3_1
    global credsowed
    print(clrscrn)
    print(info_scrn)
    slot1 = randint(1,8)
    if int(slot1) == 1:
        slot1 = '\N{CHERRIES}'
        slot1_1 = '1'
    elif int(slot1) == 2:
        slot1 = '\N{BELL}'
        slot1_1 = '2'
    elif int(slot1) == 3:
        slot1 = '\N{WATERMELON}'
        slot1_1 = '3'
    elif int(slot1) == 4:
        slot1 = '\N{LEMON}'
        slot1_1 = '4'
    elif int(slot1) == 5:
        slot1 = '\N{GRAPES}'
        slot1_1 = '5'
    elif int(slot1) == 6:
        slot1 = '\N{GEM STONE}'
        slot1_1 = '6'
    elif int(slot1) == 7:
        slot1 = '7'
        slot1_1 = '7'
    elif int(slot1) == 8:
        slot1_1 = '8'
        slot1 = 'BAR'
    slot2 = randint(1,8)
    if int(slot2) == 1:
        slot2 = '\N{CHERRIES}'
        slot2_1 = '1'
    elif int(slot2) == 2:
        slot2 = '\N{BELL}'
        slot2_1 = '2'
    elif int(slot2) == 3:
        slot2 = '\N{WATERMELON}'
        slot2_1 = '3'
    elif int(slot2) == 4:
        slot2 = '\N{LEMON}'
        slot2_1 = '4'
    elif int(slot2) == 5:
        slot2 = '\N{GRAPES}'
        slot2_1 = '5'
    elif int(slot2) == 6:
        slot2 = '\N{GEM STONE}'
        slot2_1 = '6'
    elif int(slot2) == 7:
        slot2_1 = '7'
        slot2 = '7'
    elif int(slot2) == 8:
        slot2_1 = '8'
        slot2 = 'BAR'
    slot3 = randint(1,8)
    if int(slot3) == 1:
        slot3_1 = '1'
        slot3 = '\N{CHERRIES}'
    elif int(slot3) == 2:
        slot3_1 = '2'
        slot3 = '\N{BELL}'
    elif int(slot3) == 3:
        slot3_1 = '3'
        slot3 = '\N{WATERMELON}'
    elif int(slot3) == 4:
        slot3_1 = '4'
        slot3 = '\N{LEMON}'
    elif int(slot3) == 5:
        slot3_1 = '5'
        slot3 = '\N{GRAPES}'
    elif int(slot3) == 6:
        slot3_1 = '6'
        slot3 = '\N{GEM STONE}'
    elif int(slot3) == 7:
        slot3_1 = '7'
        slot3 = '7'
    elif int(slot3) == 8:
        slot3_1 = '8'
        slot3 = 'BAR'
    print('Spin')
    sleep(1)
    print('Those')
    sleep(1)
    print('Slots!')
    sleep(2)
    print('###################################')
    print('#          |          |           #')
    print('#          |          |           #')
    print('#   ',slot1,end='')
    sleep(1)
    print('   #   ',slot2,end='')
    sleep(1)
    print('  #    ',slot3,end='')
    sleep(1)
    print('     #')
    print('#          |          |           #')
    print('#          |          |           #')
    print('###################################')
    winnings()

#############################################
#                                           #
#               Iteration 5.5               #
#                 Winnings                  #
#                                           #
#############################################

winreason = ''

def winnings():
    global slot1_1
    global slot2_1
    global slot3_1
    global winreason
    global credsowed
    global multiplier
    # cherries #

    #one cherry

    if int(slot1_1) == 1 and int(slot2_1) > 1 and int(slot3_1) > 1:
        winreason = 'Cherries in slot 1\n'
        credsowed = int(credsowed) + 10 * int(multiplier)

    #double cherries

    if int(slot1_1) == 1 and int(slot2_1) == 1 and int(slot3_1) > 1:
        winreason = 'Double Cherries in slots 1 and 2\n'
        credsowed = int(credsowed) + 20 * int(multiplier)
    elif int(slot1_1) == 1 and int(slot3_1) == 1 and int(slot2_1) > 1:
        winreason = 'Double Cherries in slots 1 and 2\n'
        credsowed = int(credsowed) + 20 * int(multiplier)
    elif int(slot2_1) == 1 and int(slot3_1) == 1 and int(slot1_1) > 1:
         winreason = 'Double Cherries in slots 1 and 2\n'
         credsowed = int(credsowed) + 20 * int(multiplier)

    #all cherries

    if int(slot1_1) == 1 and int(slot2_1) == 1 and int(slot3_1) == 1:
        winreason = 'BIG WIN! Cherries in all 3 slots\n'
        credsowed = int(credsowed) + 70 * int(multiplier)

    # bells #

    #double bells
    
    if int(slot1_1) == 2 and int(slot2_1) == 2 and int(slot3_1) > 2 or int(slot1_1) == 2 and int(slot2_1) == 2 and int(slot3_1) < 2:
        winreason = 'bells in two slots\n'
        credsowed = int(credsowed) + 50 * int(multiplier)
    elif int(slot1_1) == 2 and int(slot3_1) == 2 and int(slot2_1) > 2 or int(slot1_1) == 2 and int(slot3_1) == 2 and int(slot2_1) < 2:
        winreason = 'bells in two slots\n'
        credsowed = int(credsowed) + 50 * int(multiplier)
    elif int(slot2_1) == 2 and int(slot3_1) == 2 and int(slot1_1) > 2 or int(slot2_1) == 2 and int(slot3_1) == 2 and int(slot1_1) < 2:
        winreason = 'bells in two slots\n'
        credsowed = int(credsowed) + 50 * int(multiplier)

    #all bells

    if int(slot1_1) == 2 and int(slot2_1) == 2 and int(slot3_1) == 2:
        winreason = 'BIG WIN! All slots have bells!'
        credsowed = int(credsowed) + 150 * int(multiplier)

    # watermelons #

    #Double watermelons

    if int(slot1_1) == 3 and int(slot2_1) == 3 and int(slot3_1) > 3 or int(slot1_1) == 3 and int(slot2_1) == 3 and int(slot3_1) < 3:
        winreason = 'Watermelons in two slots\n'
        credsowed = int(credsowed) + 100 * int(multiplier)
    elif int(slot1_1) == 3 and int(slot3_1) == 3 and int(slot2_1) > 3 or int(slot1_1) == 3 and int(slot3_1) == 3 and int(slot2_1) < 3:
        winreason = 'Watermelons in two slots\n'
        credsowed = int(credsowed) + 100 * int(multiplier)
    elif int(slot2_1) == 3 and int(slot3_1) == 3 and int(slot1_1) > 3 or int(slot2_1) == 3 and int(slot3_1) == 3 and int(slot1_1) < 3:
        winreason = 'Watermelons in two slots\n'
        credsowed = int(credsowed) + 100 * int(multiplier)

    #all watermelons

    if int(slot1_1) == 3 and int(slot2_1) == 3 and int(slot3_1) == 3:
        winreason = 'BIG WIN! All slots have watermelons!'
        credsowed = int(credsowed) + 250 * int(multiplier)

    # Lemons #

    #double Lemons

    if int(slot1_1) == 4 and int(slot2_1) == 4 and int(slot3_1) > 4 or int(slot1_1) == 4 and int(slot2_1) == 4 and int(slot3_1) < 4:
        winreason = 'Lemons in two slots\n'
        credsowed = int(credsowed) + 150 * int(multiplier)
    elif int(slot1_1) == 4 and int(slot3_1) == 4 and int(slot2_1) > 4 or int(slot1_1) == 4 and int(slot3_1) == 4 and int(slot2_1) < 4:
        winreason = 'Lemons in two slots\n'
        credsowed = int(credsowed) + 150 * int(multiplier)
    elif int(slot2_1) == 4 and int(slot3_1) == 4 and int(slot1_1) > 4 or int(slot2_1) == 4 and int(slot3_1) == 4 and int(slot1_1) < 4:
        winreason = 'Lemons in two slots\n'
        credsowed = int(credsowed) + 150 * int(multiplier)
    
    #all Lemons

    if int(slot1_1) == 4 and int(slot2_1) == 4 and int(slot3_1) == 4:
        winreason = 'BIG WIN! All slots have lemons!'
        credsowed = int(credsowed) + 350 * int(multiplier)
    
    # Grapes #

    # Double Grapes #

    if int(slot1_1) == 5 and int(slot2_1) == 5 and int(slot3_1) > 5 or int(slot1_1) == 5 and int(slot2_1) == 5 and int(slot3_1) < 5:
        winreason = 'Grapes in two slots\n'
        credsowed = int(credsowed) + 200 * int(multiplier)
    elif int(slot1_1) == 5 and int(slot3_1) == 5 and int(slot2_1) > 5 or int(slot1_1) == 5 and int(slot3_1) == 5 and int(slot2_1) < 5:
        winreason = 'Grapes in two slots\n'
        credsowed = int(credsowed) + 200 * int(multiplier)
    elif int(slot2_1) == 5 and int(slot3_1) == 5 and int(slot1_1) > 5 or int(slot2_1) == 5 and int(slot3_1) == 5 and int(slot1_1) < 5:
        winreason = 'Grapes in two slots\n'
        credsowed = int(credsowed) + 200 * int(multiplier)

    # All Grapes #

    if int(slot1_1) == 5 and int(slot2_1) == 5 and int(slot3_1) == 5:
        winreason = 'BIG WIN! All slots have lemons!'
        credsowed = int(credsowed) + 450 * int(multiplier)

    # Diamonds #

    # Double diamonds #

    if int(slot1_1) == 6 and int(slot2_1) == 6 and int(slot3_1) > 6 or int(slot1_1) == 6 and int(slot2_1) == 6 and int(slot3_1) < 6:
        winreason = 'Diamonds in two slots\n'
        credsowed = int(credsowed) + 300 * int(multiplier)
    elif int(slot1_1) == 6 and int(slot3_1) == 6 and int(slot2_1) > 6 or int(slot1_1) == 6 and int(slot3_1) == 6 and int(slot2_1) < 6:
        winreason = 'Diamonds in two slots\n'
        credsowed = int(credsowed) + 300 * int(multiplier)
    elif int(slot2_1) == 6 and int(slot3_1) == 6 and int(slot1_1) > 6 or int(slot2_1) == 6 and int(slot3_1) == 6 and int(slot1_1) < 6:
        winreason = 'Diamonds in two slots\n'
        credsowed = int(credsowed) + 300 * int(multiplier)

    # All Diamonds #

    if int(slot1_1) == 6 and int(slot2_1) == 6 and int(slot3_1) == 6:
        winreason = 'BIG WIN! All slots have diamonds!'
        credsowed = int(credsowed) + 600 * int(multiplier)

    # Sevens #

    # Must have all 3 sevens to with this prize. #

    if int(slot1_1) == 7 and int(slot2_1) == 7 and int(slot3_1) == 7:
        winreason = 'Mini Jackpot!! All slots have sevens!!'
        credsowed = int(credsowed) + 1000 * int(multiplier)

    # Bar #

    # Must have all 3 BARs to win this prize. #

    if int(slot1_1) == 8 and int(slot2_1) == 8 and int(slot3_1) == 8:
        winreason = 'MEGA JACKPOT!!! ALL SLOTS HAVE BARS!!!'
        credsowed = int(credsowed) + 2500 * int(multiplier)
    
    transactions()
    #next section
    


    

from tqdm import tqdm


#############################################
#                                           #
#                Iteration 6                #
#                Transactions               #
#                                           #
#############################################

playagain_conf = ''

def transactions():
    global credsowed
    global credits
    global winreason
    print(clrscrn)
    print(winreason)
    print('Your current balance is', credits, '. You won', credsowed)
    sleep(3)
    credits = int(credits) + int(credsowed)
    loop = tqdm(total = int(credsowed), position=0, leave=False)
    while int(credsowed) > 1:
        for k in range(int(credsowed)):
            loop.set_description('Processing...\r'.format(k))
            loop.update(1)
            credsowed = int(credsowed) - 1
        loop.close()
    print('\nWould you like to play again?\n')
    playagain_conf = input()
    if 'yes' in playagain_conf.lower():
        winreason = ''
        multiplieramt()
    else:
        exit()


#start the program
crdtamt()
