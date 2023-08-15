#messin around naughts and crosses game
#Project start date: Weihnachten '22


#Idea: make a dictionary holding description of place and its respective index in the matrix
#or even simpler just its index in a list
#each turn output the possible choices remaining, once user input has been entered check off from list


spaces = [
            "1. Top Left",
            "2. Top Middle",
            "3. Top Right",
            "4. Middle Left",
            "5. Middle Middle",
            "6. Middle Right",
            "7. Bottom Left",
            "8. Bottom Middle",
            "9. Bottom Right"
            ]



def print_spaces(space):
    print("%s" %(space))
    

def user_input(available):
    while True:
        print("------------------------------------------------------------")
        value = input("Choose a slot by choosing corresponding number as per list above:     ")
        print("------------------------------------------------------------")
        try:
            #convert to an integer and check if valid
            value = int(value)
            #ensures value is part of list of remaining options
            if value in available:
                print("value is integer, '%d' is accepted"%value)
                break
            else:
                print("value '%d' is not available or out of range, choose again" %value)
            

        except ValueError:
                print("Value entered '%s' has not been accepted, try again"%value)
    return value

def amend_spaces(spaces, value):
    print("You have chosen %s" %spaces[(value-1)])
    return spaces

def check_win(array):
    win_indicator = 0

    #wins across horizontal rows
    if array[0] == array[1] and array[1] == array[2]:
        win_indicator = 1
    if array[3] == array[4] and array[4] == array[5]:
        win_indicator = 1
    if array[6] == array[7] and array[7] == array[8]:
        win_indicator = 1

    #wins across vertical columns
    if array[0] == array[3] and array[3] == array[6]:
        win_indicator = 1
    if array[1] == array[4] and array[4] == array[7]:
        win_indicator = 1
    if array[2] == array[5] and array[5] == array[8]:
        win_indicator = 1

    #wins diagonal across
    if array[0] == array[4] and array[4] == array[8]:
        win_indicator = 1
    if array[6] == array[4] and array[4] == array[2]:
        win_indicator = 1
        
    return win_indicator

def print_array(array):
    print("------------------------------------------------------------")
    print("%s %s %s" %(array[0],array[1],array[2]))
    print("%s %s %s" %(array[3],array[4],array[5]))
    print("%s %s %s" %(array[6],array[7],array[8]))
    print("------------------------------------------------------------")

results = list(map(print_spaces, spaces))

#array to hold values
array = ["1","2","3","4","5","6","7","8","9"]
print_array(array)

#list to keep track of spaces that have been filled such that user cannot chose space again
available = [1,2,3,4,5,6,7,8,9]

while True:
    
    #check for win
    win = check_win(array)
    if win == 1:
        print("We have a winner! Congratulations Player 2")
        break

    #check for no winner, by checking if available spots list is empty
    if not available:
        print("No winner this time")
        break
        
    
    #player 1 to make a move
    print("Player 1:")
    value = user_input(available)
    available.remove(value)
    spaces = amend_spaces(spaces, value)
    array[(value-1)] = "X"
    print_array(array)

    #check for win
    win = check_win(array)
    if win == 1:
        print("We have a winner! Congratulations Player 1")
        break

    #check for no winner, by checking if available spots list is empty
    if not available:
        print("No winner this time")
        break

    #player 2 to make a move
    print("Player 2:")
    value = user_input(available)
    available.remove(value)
    spaces = amend_spaces(spaces, value)
    array[(value-1)] = "O"
    print_array(array)





