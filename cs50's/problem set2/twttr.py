def main():
    string = input("Input: ")
    new_string = ""
    for i in string:
        if i not in "AEIOUaeiou":
            new_string += i

    print(new_string)


if __name__ == "__main__":
    main()