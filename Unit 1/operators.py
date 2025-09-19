from numpy import number


print('Good Morning')

def goodMorningMsg():
    username = input("what is your name?")
    print('good morning, '+ username )

goodMorningMsg()

def compoundInterest():
    investAmount = 100
    investAmount *= .05
    moneyGained = investAmount
    print(moneyGained)

compoundInterest()

def totalCost(itemName, itemPrice):
    tax = 0.5
    totalTax = itemPrice * tax
    totalPrice = totalTax + itemPrice
    print(totalPrice)

totalCost('arctic Coat', 100.00)

"Arctic coat total is $275.00"
"Snow boots total is $165.00"
"Goggles total is $110.00"

print(int(number) + 30 )


data = [1,2,3,4,32,4344]


harddrive =