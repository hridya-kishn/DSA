def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # check the lenght
    if len(s) < 2 or len(s) > 6:
        return False
    # n = len(s)
    # checks digit in between 
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == 0:
                return False
            if not s[i:].isdigit():
                    return False
            break
    # checks symbols other than numbers and alphabets
    if not s.isalnum():
        return False
    # checks if the 1st 2 are alphabets
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    return True

if __name__ == "__main__":
    main()
