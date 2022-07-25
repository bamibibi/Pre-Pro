'''1 star'''
def main():
    '''hi'''
    grade_1 = float(input())
    if grade_1 < 1:
        print("I'm so sad.")
    elif grade_1 < 2:
        grade_2 = 4-grade_1
        print("%.2f" %grade_2)
    else:
        print("I'm so happy.")
main()
