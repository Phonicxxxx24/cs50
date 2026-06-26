# amount due :, for loop if user enters 25,10,5
acc_coins = [5,10,25]
da = 50
cost = 50
print(f"Amount due: {da}")
i_coin = 0

while da > 0:
    i = int(input("Insert coin: "))
    if (i in acc_coins):
        da = da - i
        print(f"amount due: {da}")
        

    else:
        print("coin not accepted")
print(f"Amount owed: {abs(da)}")
    