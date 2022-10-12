from weather import *

myfile = "weather.dat"

mychoice = 0
while(True):
    print("      *** TUFFY TITAN WEATHER LOGGER MAIN MENU")
    print()
    print("1. Set data FileName")
    print("2. Add Weather Data")
    print("3. Print Daily Report")
    print("4. Print Historical Data")
    print("9. Exit the Program")
    print()

    mychoice = input("Enter menu choice: ")
    print()

    if(mychoice == '1'):
        myfile = input("Enter Data Filename: ")
        weather = read_data(myfile)
    elif mychoice == '2':
        dt = input("Enter date: ")
        tm = input("Enter time: ")
        t = int(input("Enter Temperature: "))
        h = int(input("Enter Humidity: "))
        r = float(input("Enter the Rainfall: "))
        weather[dt+tm] = {'t':t, 'h':h, 'r':r}
        write_data(weather, myfile)
        print()
    elif mychoice == '3':
        d = input("Enter date: ")
        display = report_daily(weather, d)
        print(display)
    elif mychoice == '4':
        display = report_historical(weather)
        print(display)
    elif mychoice == '9':
        break


