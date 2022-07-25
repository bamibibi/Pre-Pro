'''1 star'''
def main():
    '''hi'''
    money = int(input())
    water = int(input())
    ans = money-water
    snack_1 = int(input())
    snack_2 = int(input())
    snack_3 = int(input())
    if ans%3 == 0:
        snack_1 = snack_1*10
    elif ans%3 == 1:
        snack_1 = snack_1*15
    elif ans%3 == 2:
        snack_1 = snack_1*20
    total_1 = ans-snack_1
    if total_1%3 == 0:
        snack_2 = snack_2*12
    elif total_1%3 == 1:
        snack_2 = snack_2*15
    elif total_1%3 == 2:
        snack_2 = snack_2*18
    total_2 = total_1-snack_2
    if total_2%3 == 0:
        snack_3 = snack_3*5
    elif total_2%3 == 1:
        snack_3 = snack_3*7
    elif total_2%3 == 2:
        snack_3 = snack_3*9
    yay = money-water-snack_1-snack_2-snack_3
    if yay >= 0:
        print("Now you have "+str(yay)+" left.")
        print("Here's your order!")
        print("Water: "+ str(water)+" baht")
        print("Snack number 1: "+str(snack_1)+" baht")
        print("Snack number 2: "+str(snack_2)+" baht")
        print("Snack number 3: "+str(snack_3)+" baht")
    elif yay < 0:
        print("Now you have "+str(money)+" left.")
        print("You don't have enough money!")
main()

