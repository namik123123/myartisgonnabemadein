def theart(name, year):
    print(f"this arts name is {name} and its gonna be made in {year}")



name = input("enter the name of the art: ")
year = input("enter when the art is gonna relase: ")

if not name and not year:
    print("you have to enter the name and the year of the art")
elif not name:
    print("you have to enter the name of the art")
elif not year:
    print("you have to enter the year of the art")
else:
    theart(name, year)
