import time
def calculate():
    percent = eval(input("Enter the percent you want to calculate: "))
    percentNum = eval(input("Enter the number you want a percentage of: "))
    result = (percent) * (percentNum)

    print (result)

    answer = input("Do you want to do another?\ny/n: ")

    if answer == 'y':
        calculate()
    elif answer == 'yes':
        calculate()
    elif answer == 'Y':
        calculate()
    elif answer == 'Yes':
        calculate()
    elif answer == 'n':
        print("Thanks for testing out the percentage calculator!")
        time.sleep(0.5)
        quit()
    else:
        print("Please check your choice and try again... ")
        quit()
calculate()
  
