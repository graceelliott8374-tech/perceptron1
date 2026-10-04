# Tyger Perceptron

A Python perceptron built from scratch to predict whether my cat, Tyger, will come when called. The model learns from observed outcomes and saves its weights and bias between sessions.

## How It Works

The program asks five yes/no questions:

- Are you holding treats?
- Is Tyger asleep?
- Is Tyger nearby?
- Is Tyger already eating?
- Does Tyger recognize the person calling?

Answers become numeric inputs: `1` for yes and `0` for no.

The perceptron multiplies each input by its weight, adds the bias, and makes a prediction:

- `1`: Tyger will come.
- `0`: Tyger will not come.

After calling Tyger, the user records whether he approached within 30 seconds. The program compares this outcome with its prediction and updates the weights and bias when it makes a mistake.

## Learning Rule

The weights and bias start at zero for a new model. The learning rate is `0.1`.

```text
error = actual outcome - prediction

weight = weight + learning rate × error × input
bias = bias + learning rate × error
```

Updated weights and bias are saved to `tyger_model.json` after each observation and loaded when the program starts again.

## Getting Started

### Requirements

- Python 3
- No external packages required

### Run the Program

From the project folder:

```bash
python perceptron.py
```

Answer the questions, observe Tyger's response, and record the actual outcome. Choose whether to record another observation or exit.

If `tyger_model.json` does not exist, the program initializes a new model.

## Files

| File               | Purpose                                                       |
| ------------------ | ------------------------------------------------------------- |
| `perceptron.py`    | Input collection, prediction, learning, and model persistence |
| `tyger_model.json` | Saved weights and bias                                        |

Run the program from the project folder so it reads and writes the expected model file.

## What I Practiced

- Functions and return values
- Input validation
- Loops and conditionals
- Lists and indexing
- Perceptron prediction and training
- Reading and writing JSON files
- Learning from prediction errors

## Limitations

This is an educational project, and its accuracy has not been established. Cat behavior varies, and a single perceptron can only learn a linear decision boundary.

The JSON file stores the model's current parameters; it does not store individual observations.
