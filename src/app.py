from operations import addition, division, multiply, substract

print("Berechne zwei Zahlen: ")
print("(A)ddition")
print("(S)ubstraktion")
print("(M)ultiplikation")
print("(D)ivision\n")

# Declaration
is_answer_correct = False

users_guess = ""
result = 0

operation = input("Operation: ")
while not(operation == "A".lower() or operation == "M".lower() or operation == "S".lower() or operation == "D".lower()):
    print("Die Operation wird nicht unterstützt!")
    print("Wähle eine andere Operation aus.")
    operation = input("Operation: ")

number_one = input("Zahl 1: ")
number_two = input("Zahl 2: ")

while not is_answer_correct:
    users_guess = input("Deine Antwort: ")

    if users_guess == "e":
        print("Ich beende das Spiel!")
        break

    if operation == "A".lower():
        result = addition(number_one, number_two)
    elif operation == "M".lower():
        result = multiply(number_one, number_two)
    elif operation == "S".lower():
        result = substract(number_one, number_two)
    elif operation == "D".lower():
        result = division(number_one, number_two)

    if result == int(users_guess):
        print(f"Du hast Recht! Das Ergebnis ist {users_guess}.")
        is_answer_correct = True
    else:
        print(f"Das Ergebnis ist nicht {users_guess}.")
        print("Probiere es doch gleich noch einmal!")
        continue
