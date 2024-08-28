def convert(current,to,amount,rates) :
    amount = float(amount)
    if (current == to) : return amount
    if current != "USD" :
        amount = amount / rates[current]
    return amount * rates[to]
    
rates = {
        "EUR": 0.93,    
        "USD": 1.00,  
        "PKR": 280.00,  
        "INR": 82.00,    
        "Yen": 145.00   
}

print("Currency Options: ")
for currency in rates :
    print(f"- {currency}")

current = input("Enter the currency you currently have: ")
amount = input("Enter amount in your possession: ")
to = input("Enter the currency you want to convert to: ")

print("Converted to ", to, "with amount: ",convert(current,to,amount,rates))
