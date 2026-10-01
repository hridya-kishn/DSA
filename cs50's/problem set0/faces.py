def convert():
    result = input()
    if ":)" in result:
        result = result.replace(":)", "🙂")
    elif ":(" in result:
        result = result.replace(":(", "🙁")
    print(result)


if __name__ == "__main__":
    convert()