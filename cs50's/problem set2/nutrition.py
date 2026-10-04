def main():
    my_fruits = {
        "mango" : 130,
        "apple" : 120,
        "orange" : 150
    }

    item = input("Item: ").lower()
    for key, value in my_fruits.items():
        if item == key:
            print(f"Calories: {value}")


if __name__ == "__main__":
        main()