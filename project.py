import sys
from random import choice
from termcolor import colored


class Fridge:
    def __init__(self):
        self.inventory = {}
        self.recipes = {}
        self.command = None

    def get_name(self, my_string):
        while True:
            user_input_string = input(colored(my_string, "cyan")).strip().upper()
            if not user_input_string == "":
                if user_input_string.replace(" ", "").replace("(", "").replace(")", "").isalpha():
                    break
                else:
                    print(colored("You can only input letters.", "red"))
            else:
                print(colored("Please enter a valid name.", "red"))
        return user_input_string

    def get_number(self, my_string):
        while True:
            user_input_number = (input(colored(my_string, "cyan")).strip().upper()).replace(",", ".")
            if not user_input_number == "":
                if user_input_number.replace("+", "").replace("-", "").replace(".", "").isnumeric() or user_input_number == "C":
                    break
                else:
                    print(colored("You can only input numbers.", "red"))
            else:
                print(colored("Please enter a valid number.", "red"))
        return user_input_number

    def get(self):
        """
        prompts the user for a command
        exits program if user enters "E"
        prompts the user again in case of an invalid input
        """

        while True:
            get_command = "\nWhat would you like to do? \n(C)hoose a recipe / (A)dd a recipe / (D)elete a recipe / (U)pdate inventory / (R)equest a suggestion / (E)xit program\n"
            command = self.get_name(get_command)

            match command:
                case "C":
                    self.choose_recipe()
                case "A":
                    self.add_recipe()
                case "D":
                    self.delete_recipe()
                case "U":
                    self.update_inventory()
                case "R":
                    self.request_suggestion()
                case "E":
                    sys.exit(colored("You quit the program.\n", "red"))
                case _:
                    print(colored("Invalid input", "red"))

    def choose_recipe(self):
        """
        lists the ingredients the user has to buy for a chosen recipe
        navigates back if user enters "C"
        warns the user if the book is empty
        prompts the user again in case of an invalid input
        """

        recipe_list = list(self.recipes.keys())
        if len(recipe_list):
            recipe_str = ", ".join(recipe_list).lower()
            while True:
                get_rec_string = f"\nWhich recipe do you want to make? Enter 'C' to cancel.\n{recipe_str}\n\n"
                recipe_to_make = self.get_name(get_rec_string)

                if recipe_to_make in recipe_list:
                    if not recipe_to_make == "C":
                        need_to_have = self.recipes[recipe_to_make]

                        already_have = {}
                        for ing_name in need_to_have:
                            if ing_name in self.inventory:
                                already_have[ing_name] = self.inventory[ing_name]

                        need_to_buy = {}
                        for ing_name in need_to_have:
                            if ing_name in already_have:
                                if need_to_have[ing_name] - already_have[ing_name] > 0:
                                    need_to_buy[ing_name] = (
                                        need_to_have[ing_name] - already_have[ing_name]
                                    )
                            else:
                                need_to_buy[ing_name] = need_to_have[ing_name]
                        if len(need_to_buy):
                            print(
                                colored(
                                    f"\nYou need to buy the following ingredients for {recipe_to_make.lower()}:",
                                    "yellow",
                                )
                            )
                            for k in need_to_buy:
                                print(f"{k}: {need_to_buy[k]}")
                        else:
                            print(
                                colored(
                                    f"\nYou already have everything for {recipe_to_make.lower()}.",
                                    "yellow",
                                )
                            )

                        break
                elif recipe_to_make == "C":
                    break
                else:
                    print(colored("There's no such recipe in your book.\n", "red"))
        else:
            print(colored("There are no recipes in your book right now.", "red"))

    def add_recipe(self):
        """
        user can add a new recipe to the book
        1) prompts the user for the name of the recipe
        2) prompts the user for the name and amount of ingredients
        submits recipe if the user enters "S"
        prompts the user again in case of an invalid input
        """

        while True:
            get_new_rec_string = (
                "\nWhat's the name of the new recipe? Enter 'C' to cancel.\n"
            )
            name_of_new_recipe = self.get_name(get_new_rec_string)
            if name_of_new_recipe == "C":
                break
            elif name_of_new_recipe not in self.recipes:
                dict_of_ingredients = {}
                print(
                    colored(
                        "\nEnter the ingredients for the recipe. Enter 'S' to submit the recipe.",
                        "cyan",
                    )
                )
                while True:
                    ingredient_of_new_recipe = self.get_name("Ingredient: ").lower()

                    if ingredient_of_new_recipe.upper() == "S":
                        self.recipes[name_of_new_recipe] = dict_of_ingredients
                        print(
                            colored(
                                f"Added {name_of_new_recipe.lower()} to your book.",
                                "yellow",
                            )
                        )
                        return True
                    else:
                        if not ingredient_of_new_recipe.upper() == "C":
                            if ingredient_of_new_recipe not in dict_of_ingredients:
                                while True:
                                    amount_of_ingredient = self.get_number("Amount: ")
                                    if not amount_of_ingredient.upper() == "C":
                                        dict_of_ingredients[
                                            ingredient_of_new_recipe
                                        ] = float(amount_of_ingredient)
                                        print()
                                        break
                                    else:
                                        return True
                            else:
                                print(colored("Already added to recipe.", "red"))
                        else:
                            return True
            else:
                print(colored("Recipe is already in your book.", "red"))

    def delete_recipe(self):
        """
        removes one recipe from the user's book
        navigates back if user enters "C"
        warns the user if the book is already empty
        prompts the user again in case of an invalid input
        """

        recipe_list = list(self.recipes.keys())
        if len(recipe_list):
            recipe_str = ", ".join(recipe_list).lower()
            while True:
                rec_to_del_string = f"\nWhich recipe do you want to delete from your book? Enter 'C' to cancel.\n{recipe_str}\n\n"
                name_of_recipe = self.get_name(rec_to_del_string)
                if name_of_recipe in recipe_list:
                    if not name_of_recipe == "C":
                        del self.recipes[name_of_recipe]
                        print(
                            colored(
                                f"Deleted {name_of_recipe.lower()} from your book.",
                                "yellow",
                            )
                        )
                        break
                elif name_of_recipe == "C":
                    break
                else:
                    print(colored("There's no such recipe in your book.\n", "red"))
        else:
            print(colored("There are no recipes in your book right now.", "red"))

    def update_inventory(self):
        """
        user can deposit and withdraw to/from the inventory
        prints the current inventory before every entry
        if amount = 0, item is deleted from the inventory
        if user wants to withdraw more than what's available, an error message is printed
        prompts the user again in case of an invalid input
        """

        print(
            colored(
                "You can change your inventory by entering the name and amount of ingredients you want to change. Enter 'C' to cancel.",
                "cyan",
            )
        )
        while True:
            print(colored("\nCurrent inventory:", "green"))
            for element in sorted(self.inventory.items()):
                print(f"{element[0]} - {element[1]}")
            ch_ingred = self.get_name("\nIngredient: ").lower()
            if not ch_ingred.isnumeric():
                if ch_ingred.upper() == "C":
                    break
                else:
                    while True:
                        ch_amount = self.get_number("Amount: ")
                        if ch_amount.upper() == "C":
                            return True
                        if ch_ingred not in self.inventory:
                            if not ch_amount.startswith("-"):
                                self.inventory[ch_ingred] = float(ch_amount)
                            else:
                                print(
                                    colored(
                                        "\nYou can't withdraw more than what's available.",
                                        "red",
                                    )
                                )
                        else:
                            if self.inventory[ch_ingred] + float(ch_amount) >= 0:
                                self.inventory[ch_ingred] = self.inventory[
                                    ch_ingred
                                ] + float(ch_amount)
                            else:
                                print(
                                    colored(
                                        "\nYou can't withdraw more than what's available.",
                                        "red",
                                    )
                                )
                            if self.inventory[ch_ingred] == 0:
                                del self.inventory[ch_ingred]
                        break

    def request_suggestion(self):
        """
        done
        prints the name and required ingredients of a random recipe from the user's book that the user can make from the current inventory
        """

        if len(self.recipes):
            can_be_made = []
            for recipe in self.recipes:
                result_list = []
                for ingredient in self.recipes[recipe]:
                    if (
                        ingredient in self.inventory
                        and self.recipes[recipe][ingredient]
                        <= self.inventory[ingredient]
                    ):
                        result_list.append("1")
                    else:
                        break
                if set(result_list) == {"1"}:
                    can_be_made.append(recipe)
            if len(can_be_made):
                sug_rec = choice(can_be_made)
                ingredients = self.recipes[sug_rec]
                print(
                    colored(
                        f"\nYou can make the following dish based on your current inventory: {sug_rec.lower()}\nRequired ingredients:",
                        "yellow",
                    )
                )
                for k in ingredients:
                    print(f"{k}: {ingredients[k]}")
            else:
                print(
                    colored(
                        "You can't make any of your recipes based on your current inventory.",
                        "red",
                    )
                )
        else:
            print(colored("There are no recipes in your book right now.\n", "red"))


def main():
    fridge = Fridge()
    starter_recipes = {
        "GOULASH": {"pork": 1, "potatoes": 2, "paprika": 1},
        "SCHNITZEL": {"chicken": 1, "potatoes": 1, "flour": 1},
        "HAM AND EGGS": {"ham": 1, "eggs": 1},
    }

    starter_inventory = {
        "carrot": 2,
        "butter": 3,
        "flour": 1,
        "sugar": 2,
        "potatoes": 1,
        "eggs": 1,
        "chicken": 1,
        "onions": 4,
        "ham": 1,
    }

    fridge.recipes = starter_recipes
    fridge.inventory = starter_inventory

    fridge.get()


if __name__ == "__main__":
    main()
