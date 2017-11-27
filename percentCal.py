import time
def calculate():
    percent = eval(input("\nEnter the percent you want to calculate.\n\nPercent must be in decimal form!: "))
    percentNum = eval(input("\nEnter the number you want a percentage of: "))
    result = (percent) * (percentNum)

    print (percent,"percent of", percentNum, "is", result)

    answer = input("\nDo you want to do another?\ny/n: ")

    if answer == 'y':
        calculate()
    elif answer == 'yes':
        calculate()
    elif answer == 'Y':
        calculate()
    elif answer == 'Yes':
        calculate()
    elif answer == 'n':
        print("\nThanks for testing out the percentage calculator!")
        time.sleep(0.5)
        quit()
    else:
        print("\nPlease check your choice and try again... ")
        quit()
calculate()
