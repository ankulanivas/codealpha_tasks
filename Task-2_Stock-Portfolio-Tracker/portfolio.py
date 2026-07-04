stock=input("Enter the stock name : ").upper()
quantity=int(input("Enter the quantity : "))
stock_prices={
    "AAPL":180,
    "TSLA":250,
    "GOOGLE":150,
    "MSFT":200
}
if stock in stock_prices:
    total_investment=stock_prices[stock]*quantity
    print(total_investment)

    with open("total.txt","w") as f:
        f.write(str(f"Stock Name : {stock}\nQuantity : {quantity}\nPrice : {stock_prices[stock]}$\nTotal_investment : {total_investment}$"))
  
    print("Data saved Successfully....")     
else:
    print("Stock Not Found")    