#Dictonery
from __dic__ import data

print("""
        .........................   .................
        :::::::::::::::::::::::::   :::::::::::::::::
        ....    .......     .....   ....       ::::::
        ....    .......     .....   ....         ::::
        ....    .......     .....   ....          :::
        ....    .......     .....   ....          :::
        ....                .....   ....          :::
        ....                .....   ....          :::
        ....                .....   ....         ::::
        ....                .....   ....       ::::::
        ::::                :::::   :::::::::::::::::
        """)

print("\t\tWelcome To Master's Dictonery")

while(1):
    take = input("\nEnter the word here : ")

    crt = open("input_check.txt", "w")
    crt.write(take)
    crt.close()

    opn = open("input_check.txt", "r")
    rd = opn.read()
    opn.close()

    if("8888" in rd):
        for items in data:
            print(items , " - ", data[items])
    elif ("0000" in rd):
        exit()
    elif (take in data):
        print(f"\n Meaning : {data[take]}")
    elif (take not in data):
        print("Meaning not found.")
        while(1):
            ad = (input("Type 'add' to add the word in dictonery or 'continue' to go forward : "))
            if (ad == "add" or ad  == "Add"):
                add_word = input("Enter the Word : ")
                add_meaning = input("\nEnter the meaning : ")
                opn = open("__dic__.py","a")
                rd = opn.write(f'data["{add_word}"] = "{add_meaning}"\n')
                opn.close()
                print("Word is added to the dictonery. \nThe Changes will take place after the restart of Program.")
            elif (ad == "continue" or ad == "Continue"):
                print("Sorry for not giving your answer.")
                break
    continue

