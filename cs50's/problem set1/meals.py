def main():
    time = input("Enter the time: ")
    new_time = convert(time)
    if new_time >= 7.00 and new_time <= 8.00: 
            print("breakfast time")
    elif new_time >= 12.00 and new_time <= 13.00:
            print("lunch time")
    elif new_time >= 18.00 and new_time <= 19.00:
            print("dinner time")


def convert(time):
    hr, min = time.split(":")
    new_time = float(hr) + float(min) / 60
    return new_time


if __name__ == "__main__":
    main()