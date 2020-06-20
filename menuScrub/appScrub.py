# Parse all the menu data

appetizers = """<h3>Grilled</h3>
            A1 Yakitori (Chicken) 6.00
            A3 Negimaki (Beef w/scallion) 6.00
            A4 Hamachi Kama (Yellowtail) 12.00
            A5 Sake Kama (Salmon) 8.00
        <h3>Dumplings</h3>
            A6 Vegetable Gyoza 4.50
            A7 Pork Gyoza 5.00
            A8 Shrimp Shumai 5.00
            A9 Beef Mandoo (Korean) 5.00
        <h3>Tempura</h3>
            A10 Shrimp Tempura 9.00
            A11 Chicken Tempura 7.00
            A12 Vegetable Tempura 6.00
            A13 Seafood Tempura 12.00
        <h3>Deep Fried</h3>
            B1 Fried Calamari 8.00
            B2 Age Tofu 5.00
            B3 Spring Rolls 4.50
            B4 Soft Shell Crab 10.00
        <h3>Korean Pancakes</h3>
            B5 Pa-Jun (Scallion) 8.00
            B6 Gochoo Pa-Jun (Korean Pepper) 9.00
            B7 Seafood Pa-Jun 13.00
        <h3>Salads</h3>
            C1 Japanese Garden Salad 4.00
            C2 Tofu Salad 6.00
            C3 Orange & Avocado Salad 7.00
            C4 Maguro (Tuna) Salad 12.00
            C5 Avocado Crunchy Salad 7.00
            C6 Seaweed Salad 5.00
        <h3>Soups</h3>
            C7 Miso Soup 2.00
            C8 Egg Drop Soup 3.00
            C9 Dak-gae-Jang (Chicken) 8.00
            C10 Yook-gae-Jang (Beef) 9.00
            C11 Man-Doo Kook 8.00
        <h3>Side Orders</h3>
            D1 White Rice 2.00
            D2 Fried Rice (small/large) 3.50/6.50
            D3 Oshinko 3.00
            D4 Kimchee 2.50
            D5 Steamed Vegetables 5.00
            D6 Ohitash (Spinach) 5.00
            D7 Edamame 4.00
    </div>
"""
## Preliminary lists
# Overarching app list, empty list for menu items
appList = appetizers.split("\n")
menuItems = []

## Final lists
# Item numbers, items, headers, prices
itemNumbers = []
finalMenuItems = []
headers = []
prices = []

# Get all the items for appetizers
for x in appList:
    if "<h3>" in x:
        headers.append(x.strip()[4:-5])
    else:
        menuItems.append(x.strip())

# Split each string up on spaces and assign accordingly
for item in menuItems:
    splitString = item.split(" ")
    # print(splitString)
    itemNumbers.append(splitString[0])
    prices.append(splitString[-1])
    finalMenuItems.append(" ".join(splitString[1:-1]))

print(finalMenuItems)
print()
print(headers)
print()
print(prices)
print()

# Wrap headers in description header tag
for header in headers:
    print("<div class='card-header'>" + "<span><strong>" +
          header + "</strong></span>" + "</div>")

print() 

# Wrap menu items in description data tag
for x in range(0, len(finalMenuItems)):
    print("<li class='list-group-item list-group-item-action'>" + finalMenuItems[x] + " <span class='price float-right'>" + "$" + prices[x] + "</span>" + "</li>")
