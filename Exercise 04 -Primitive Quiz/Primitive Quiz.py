#Dictionary of the European countries and their capitals
info = {

    "France" : "Paris",
    "Germany" : "Berlin",
    "Italy" : "Rome",
    "Sweden" : "Stockholm",
    "Spain" : "Madrid",
    "Denmark" : "Copenhagen",
    "Portugal" : "Lisbon",
    "Ireland" : "Dublin",
    "Poland" : "Warsaw",
    "Hungary" : "Budapest"
}

marks = 0
#Asking the questions 
for country, capital in info.items():
    answer = input(f"What is the capital of {country}? ")
    if answer.strip().lower() == capital.lower():
        print("The answer you entered is correct!")
        marks += 1
    else:
        print(f"Wrong! The correct answer is {capital}.")
print(f"\nYou got {marks} out of {len(info)} correct!")