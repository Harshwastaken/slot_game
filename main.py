
import random
MAX_LINE = 3
MAX_BET =100
MIN_BET=1

ROWS = 3
COL=3

weel = {"A":1,"B":2,"C":3,"D":4}

bet_multiplier={"A":5,"B":4,"C":3,"D":2}



def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def dect_to_list(**kwargs):
    l1 =[]
    for key,value in kwargs.items():
        for _ in range(value):
            l1.append(key)      
    return l1
    
    

def get_slots():
    
    weel_list = dect_to_list(**weel)
    
    column =[]
    for _ in range(COL):
        c1=[]
        for _ in range(MAX_LINE):
            i=random.choice(weel_list)
            weel_list.remove(i)
            c1.append(i)
        
        column.append(c1)

    return(column)    
    
def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()
    
    
    
    
    
    
def deposit():
    while True:
        amount = input("enter your deposit amount $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("enter a amount gratewr then 0")
        else:
            print("enter a valid amount")
    return amount  

def number_of_lines():
    while True:
        line = input(f"enter line number you want to bet on (1-{MAX_LINE})")
        if line.isdigit():
            line=int(line)
            if line>0 and line <=MAX_LINE:
                break
            else:
                print("line cant be 0 OR more then ",MAX_LINE)
        else:
            print("enter a valid line")
    return line  
    
def get_bet():
    while True:
        amount = input("enter your bet amount $")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <=amount <=MAX_BET:
                break
            else:
                print(f"bet must be in range ${MAX_BET} - ${MIN_BET}")
        else:
            print("enter a valid amount")
    return amount
    
def spin(balance):
    lines = number_of_lines()
    while True:
        bet = get_bet()
        t_bet = bet*lines
        if t_bet <= balance:
            break 
        else:
            print(f"you dont have enough abnce to place this bet . your current balance is ${balance}")
            
    print(f"you are betting ${bet} on {lines}lines \n total bet = {t_bet}")

    slots = get_slots()
    print_slot(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, bet_multiplier)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - t_bet                  

def main1():
    
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
    
main1()    