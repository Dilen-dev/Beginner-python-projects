import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value ={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):#------we loop through every row
        symbol = columns[0][line]#------the symbol we want to check is whatever symbol in the first column of the current row
        for column in columns:#------Since we now know what symbol we want we now loop through every symbol column an check for that symbol
            symbol_to_check = column[line]
            if symbol != symbol_to_check:#------We check if the symbols are not the same, if not we break out and check the next line, if we get to the end of the for loop without breaking it means the symbols are the same and the user won
                break
        else:
            winnings += values[symbol] * bet#------the winnings calculated here are for one line
            winning_lines.appeend(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = [] #------We define our columns list
    for _ in range(cols):#------We generate a column for every single column we have(meaning if we have 3 columns we have to run the block below 3 times)
        column = [] #------we say columns equals empty list
        current_symbols = all_symbols[:]#------The [:] creates a copy of a list
        for _ in range(rows):#------We loop through the number of rows we have to generate which is the number of rows in our slot machine
            value = random.choice(all_symbols)#------A random value is picked from the all symbols list
            current_symbols.remove(value)#------We remove the value from the list so we dont pick it again
            column.append(value)#------We add the value to the column

        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):#------we loop through every single row we have
        for i, column in enumerate(columns):#------for every single row we loop through every single column(enumerate gives the index as well as the item as we loop through)
            if i != len(columns) -1:#------for every column we print the current row we are on
                print(column[row], end =" | ") #------This process essentially flips our columns from being horizontal to be vertical
            else:
                print(column[row], end =" ")
        print()

def deposit():
    while True: #------This is used because we are gonna keep asking the user till they give a valid amount
        amount = input("How much would like to deposit? $")
        if amount.isdigit():#------It checks if the input is a number if  yes it will return True
           amount = int(amount)#------we convert the amount to after we have checked if its a digit
           if amount > 0:
               break
           else:
               print("Amount must be above 0.")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines():
    while True: #------This is used because we are gonna keep asking the user till they give a valid amount
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():#------It checks if the input is a number if  yes it will return True
           lines = int(lines)#------we convert the lines to after we have checked if its a digit(beacuse input is always treated as a string)
           if  1<= lines <= MAX_LINES:
               break
           else:
               print("Enter valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True: #------This is used because we are gonna keep asking the user till they give a valid amount
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():#------It checks if the input is a number if  yes it will return True
           amount = int(amount)#------we convert the amount to after we have checked if its a digit
           if MIN_BET <=amount <= MAX_BET:
               break
           else:
               print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You can not bet that amount, your current balance is: ${balance}")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin(q to quit)").lower()
        
        if answer == "q":
            break
        balance += game(balance)
    print(f"You keft with ${balance}")
main()