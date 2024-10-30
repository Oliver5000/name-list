name = ["Oliver", "Anjali", "Dillara", "Nick","Alex"]
print("Press 1 to add a name")
print("Press 2 to edit a name")
print("Press 3 to remove a name")
print("Press 4 to see all names")
print("Press 5 to exit")
choice = int(input("Write here:"))
if choice == 1:
    n = input("What name would you like to add?")
    name.append(n)
    print(name)