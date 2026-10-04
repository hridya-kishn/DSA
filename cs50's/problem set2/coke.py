def main():
    amount_due = 50
    print("Amount_due: 50")
    while(True):
        insert_coin = int(input("Insert Coin: "))
        if insert_coin in [25, 10, 5]:
            amount_due = amount_due - insert_coin
            if amount_due > 0:
                print(f"Amount Due: {amount_due}")
        else:
            print(f"Amount Due: {amount_due}")
        if amount_due == 0:
            print(f"Change Owed: {amount_due}")
            break
        elif amount_due < 0:
            # amount_due = -1 * amount_due
            print(f"Change Owed: {abs(amount_due)}")
            break
        

if __name__ == "__main__":
    main()