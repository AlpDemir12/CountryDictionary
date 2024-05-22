import time
# Create an empty dictionary
countryDB = {
    "china":"beijing",
    "switzerland":"geneva",
    "turkey":"ankara"
}

while True:
    time.sleep(2)
    print("Option 1: Add \n Option 2: Remove \n Option 3: Get capital \n Option 4: Display all capitals \n Option 5: Display all countries \n Option 6: Display the whole dictionary")
    options = int(input("Please enter the number of the option you chose: "))
    if options == 1:
        country = input("What country would you like to add? ").upper()
        capital = input("What should the capital of this country be? ").upper()
        countryDB[country] = capital
        print(countryDB)
    elif options == 2:
        delcountry = input("Which country would you like to remove? ").upper()
        del countryDB[delcountry]
        print(countryDB)
    elif options == 3:
        d = input("Which country would you like to get the capital of? ").upper()
        #print(countryDB[choice])
        print(countryDB.get(d))
    elif options == 4:
        print(countryDB.values())
    elif options == 5:
        print(countryDB.keys())
    elif options == 6:
        print(countryDB)