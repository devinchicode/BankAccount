from accounts import chikimoto, ishimoto

"""
    operations you can implement:
    1. deposit
    2. withdraw
    3. transfer_money
    4. show_account
    example for each operation wrote below.
"""
print(chikimoto.deposit(5000))
print("-----------------------")
print(chikimoto.withdraw(5000))
print("-----------------------")
print(ishimoto.show_account())
print(chikimoto.transfer_money(ishimoto, 5000))
print(ishimoto.show_account())
print("-----------------------")
print(chikimoto.show_account())
