print("Welcome To Emmett's Cereal Emporium")
import csv
#What I want from the CSV
def newCerealDict(data):
    return {
        "Name": data[0],
        "Calories": data[3],
        "Protien": data[4],
        "Fat": data[5],
        "Sugars": data[9]
    }
#Stores csv information I want
cereals = []

file_ref = open("cereal.csv", "r")
for line in file_ref:
    line = line.strip()
    line_data = line.split(";")
    cereals.append(newCerealDict(line_data))
file_ref.close()
count = 0
Favourites = []

def main():

    print(f'''
    Please Select an Option:
    1. Display All Cereals
    2. Display Healthy Cereals
    3. Display High Protien Cereals
    4. Add item to list of Favourites
    5. Remove Item from list    
    6. Print Favourites list
    To close press any other key
    ''')
    selection = int(input("Selection: "))
    if selection == 1:
        for i in range(len(cereals)):
            print(cereals[i])
        main()
    if selection == 2:
        for i in cereals:
            if count > 0:
                Calories = int(i["Calories"])
                Sugars =  int(i['Sugars'])
                if (Calories < 100) and (Sugars < 7):
                    print(i["Name"])
            count += 1
        main()
    if selection == 3:
        for i in cereals:
            if count > 0:
                Protien = int(i["Protien"])
                if (Protien >= 6):
                    print(i["Name"])
            count += 1
        main()
    if selection == 4:
        user_input = input("Please enter a Name to add to your list of Favourites: ")
        Favourites.append(user_input)
        print(f'{user_input} has been added to favourites' )
        main()
    if selection == 5:
        user_input = input("Please enter a Name to remove from your list of Favourites: ")
        Favourites.remove(user_input)
        print(f'{user_input} has been added to favourites' )
        main()
    if selection == 6:
        print(Favourites)
        main()
    else:
        return 0
main()