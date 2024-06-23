def get_starting_number():
    number=input("How many bottles of beer on the wall?")
    true=True
    if number.isdigit():
        number=int(number)
        if number>=1:
            return int(number)
    else:
        while true:
            number=input("How many bottles of beer on the wall?")
            if number.isdigit():
                number=int(number)
                if number>=1:
                    true=False


def sing(number):

    for a in range(number-1):
        if number-1==1:
            bottle='bottle'
        else:
            bottle='bottles'

        print(f'{number} bottles of beer on the wall, {number} bottles of beer.\nTake one down, pass it around, {number-1} {bottle} of beer on the wall.\n')
        number-=1

    print('1 bottle of beer on the wall, 1 bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!')



