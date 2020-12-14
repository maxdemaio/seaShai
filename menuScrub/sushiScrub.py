# Parse all the menu data

entrees = """<h3>Entrees</h3>
            E12 Sushi Assorted slices of raw fish on seasoned rice Regular 21.00
            E13 Sashimi Assorted slices of raw fish Regular 23.00
            E14 Moriawase Combination of sushi and sashimi w/ California Roll 24.00
            E15 Chirashi Sushi Seasoned rice topped w/ assorted raw fish 20.00
            E16 Tekka-Don Seasoned rice topped w/ tuna 20.00
            E17 Una-Don Seasoned rice topped w/ eel 20.00
            E18 Makimono Combination California,Tekka, Kappa - Regular 14.00
            E19 Hae-Dup Bob Assorted slices of raw fish and vegetables with a dynamite sauce 18.00
"""

## Preliminary lists
# Overarching app list, empty list for menu items
appList = entrees.split("\n")
menuItems = []

## Final lists
# Item numbers, sushiContents, items, headers, prices
itemNumbers = []
sushiContents = []
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
    # Try and get numbers after 'Dr'
    try:
        itemNumbers.append(splitString[0] + splitString[1])
    except:
        itemNumbers.append(splitString[0])
    
    prices.append(splitString[-1])
    finalMenuItem = " ".join(splitString[1:-1])
    # To put the contents of sushi in grey, grab contents
    detailSep = finalMenuItem.split("-")
    finalMenuItems.append(detailSep[0])
    try:
        sushiContents.append("(" + detailSep[1].strip() + ")")
    except:
        sushiContents.append("")

print()
print(sushiContents)
print()
print(itemNumbers)
print()
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
    print("<li class='list-group-item list-group-item-action'>" +
          "<span class='itemNum'>" + itemNumbers[x] + ": </span>" + finalMenuItems[x] + 
          "<span class='text-muted'>" + sushiContents[x] + "</span>" +
          " <span class='price float-right'>" + "$" + prices[x] + "</span>" + "</li>")
