def main():
    statement = input("Greetings: ").lower().lstrip()
    if statement.startswith("hello"):
        print("$0")
    elif statement.startswith("h"):
        print("$20")
    else:
        print("$100")

main()