import json

def ask_yes_no(question):
    while True:
        answer = input(f"{question} (yes/no): ").strip().lower()

        if answer == 'yes':
            return 1
        elif answer == 'no':
            return 0
        else:
            print("Please enter yes or no")

try:
    with open("tyger_model.json", "r") as file:
        model = json.load(file)

    weights = model["weights"]
    bias = model["bias"]

except FileNotFoundError:
    weights = [0.0, 0.0, 0.0, 0.0, 0.0]
    bias = 0.0
learning_rate = 0.1

def predict(inputs, weights, bias):
    score = bias

    for i in range(len(inputs)):
        score += inputs[i] * weights[i]
    return 1 if score > 0 else 0
while True:
    treats = ask_yes_no("Are you holding treats?")
    asleep = ask_yes_no("Is Tyger asleep?")
    nearby = ask_yes_no("Is Tyger nearby?")
    eating = ask_yes_no("Is Tyger already eating?")
    recognize = ask_yes_no("Does Tyger recognize the person calling?")

    inputs = [treats, asleep, nearby, eating, recognize]
    print(f"Inputs: {inputs}")
    prediction = predict(inputs, weights, bias)
    print(f"Prediction: {prediction}")

    actual = ask_yes_no("Did Tyger come within 30 seconds after he was called?")
    error = actual - prediction

    print(f"Prediction error: {error}")

    for i in range(len(inputs)):
        weights[i] += learning_rate * error * inputs[i]

    bias += learning_rate * error

    print(f"Updated weights: {weights}")
    print(f"Updated bias: {bias}")
    with open("tyger_model.json", "w") as file:
        json.dump({"weights": weights, "bias": bias}, file, indent=4)

    again = ask_yes_no("Would you like to record another observation?")
    if again == 0:
        break