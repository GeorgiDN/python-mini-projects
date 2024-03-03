from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


def take_integer_input(nutrient):
    while True:
        try:
            current_nutrient = int(input(f"{nutrient}: "))
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")

    return current_nutrient


CALORIE_GOAL_LIMIT = 3000  # kcal
PROTEIN_GOAL = 180  # grams
FAT_GOAL = 80  # grams
CARBS_GOAL = 300  # grams

today = []

@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fats: int
    carbs: int


done = False


while True:
    if done:
        break

    print("(1) - Add a new food\n"
          "(2) - Visualise the progress\n"
          "(q) - Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Adding a new food!")
        name = input("Name: ")
        calories = take_integer_input("Calories")
        protein = take_integer_input("Protein")
        fats = take_integer_input("Fats")
        carbs = take_integer_input("Carbs")
        food = Food(name, calories, protein, fats, carbs)
        today.append(food)
        print(f"The food: '{food.name}' is successfully added!")

    elif choice == "2":
        calories_sum = sum(food.calories for food in today)
        protein_sum = sum(food.protein for food in today)
        fats_sum = sum(food.fats for food in today)
        carbs_sum = sum(food.carbs for food in today)

        fig, axs = plt.subplots(2, 2)
        axs[0, 0].pie([protein_sum, fats_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"], autopct=lambda p: f'{p * sum([protein_sum, fats_sum, carbs_sum]) / 100:.0f}')
        axs[0, 0].set_title("Macronutrients Distribution")
        axs[0, 1].bar([0, 1, 2], [protein_sum, fats_sum, carbs_sum], width=0.4)
        axs[0, 1].bar([0.5, 1.5, 2.5], [PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL], width=0.4)
        axs[0, 1].set_title("Macronutrients progress")
        axs[1, 0].pie([calories_sum, CALORIE_GOAL_LIMIT - calories_sum], labels=["Calories", "Remaining"], autopct=lambda p: f'{p * sum([calories_sum, CALORIE_GOAL_LIMIT - calories_sum]) / 100:.0f}')
        axs[1, 0].set_title("Calories Goal Progress")
        axs[1, 1].plot(list(range(len(today))), np.cumsum([food.calories for food in today]), label="Calories Eaten")
        axs[1, 1].plot(list(range(len(today))), [CALORIE_GOAL_LIMIT] * len(today), label="Calorie Goal")
        axs[1, 1].legend()
        axs[1, 1].set_title("Calories Goal Over Time")

        fig.tight_layout()
        plt.show()

    elif choice == "q":
        done = True
    else:
        print("Invalid choice")
