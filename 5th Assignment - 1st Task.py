
try:
    dictionary={'Arya':98,'Aryaman':92,'Alice':45,'Akash':33}

    name=input("Enter the student's name:")
    marks=dictionary[name]
    print(f"{name}'s marks:{marks}")
except KeyError:
   print("student not found")