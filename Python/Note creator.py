print("Enter note name")
a = input()
print("You can write your notes now!")
note = input()


try:
    with open(f"{a}", "x") as file:

        file.write(f"{note}\n")


except FileExistsError:
    print("File already exist.")