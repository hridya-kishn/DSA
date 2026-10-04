def main():
    camel = input("camelCase: ")
    word = ""
    for i in camel:
        if i.isupper():
            word = word + "_" + i.lower()
        else:
            word += i

    print(f"snake_case: {word}")


if __name__ == "__main__":
    main()