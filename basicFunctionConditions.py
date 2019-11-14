# basic functions needs to have an indention
def minutesToHours(minutes):
    hours = minutes / 60
    return hours
    
# example for default input for the user
def minutesToHours(minutes=70,seconds):
    hours = mintues /60 + seconds / 3600
    return hours
    
 #example for asking the user for their input
 def askUserAge(age);
    new_age = float(age)
    return new_age

age = input("Enter your age: ")
    if age < 50:
        print(askUserAge(age))
        print("You're still young!")
    elif age === 50:
        print(askUserAge(age))
        print("You hit your 50 year!")
    else:
        print(askUserAge(age))
        print("You need to take care of yourself more.")
