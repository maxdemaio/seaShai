# Parse all the menu data

appetizers = """<h3>Appetizers</h3>
            E1 Sushi Appetizer Assorted slices of raw fish on seasoned rice (4pcs) 9.00
            E2 Sashimi Appetizer Assorted slices of raw fish (9 pcs) 13.00
            E3 Seaweed Salad Seaweed and cucumbers in a vinegar sauce 5.00
            E4 Sunomono Assorted slices of raw fish and seaweed in a vinegar sauce 10.00
            E5 Kani-Su Crabstick rolled inside cucumbers 7.00
            E6 Tako-Su Octopus in a vinegar sauce 9.00
            E7 Ebi-Su Shrimp in a vinegar sauce 9.00
            E8 Tuna-Su Tuna rolled inside cucumber 10.00
            E9 Tuna Tataki Grilled Tuna w/ Ponzu Sauce 13.00
            E10 Tuna Tartar Fresh tuna green onion and radish w/ Ponzu Sauce 13.00
            E11 Salmon Tartar Fresh salmon, avocado, and onion w/ avocado sauce 9.00
        <h3>Entrees</h3>
            E12 Sushi Assorted slices of raw fish on seasoned rice 
            Regular 21.00
            Deluxe 25.00
            E13 Sashimi Assorted slices of raw fish 
            Regular 23.00
            Deluxe 29.00
            E14 Moriawase Combination of sushi and sashimi w/ California Roll 24.00
            E15 Chirashi Sushi Seasoned rice topped w/ assorted raw fish 20.00
            E16 Tekka-Don Seasoned rice topped w/ tuna 20.00
            E17 Una-Don Seasoned rice topped w/ eel 20.00
            E18 Makimono Combination 
            California,Tekka, Kappa - Regular 14.00
            new Sea Shai, California, Tekka, Kappa - Deluxe 23.00
            E19 Hae-Dup Bob Assorted slices of raw fish and vegetables with a dynamite sauce 18.00
        <h3>Special Combinations</h3>
            New Sea Shai Boat Assortment of Sashimi, Sushi, &new Sea Shai Roll
            F1 5pcs Sushi, 6pcs Sashimi, &new Sea Shai Roll Small 29.00
            F2 8pcs Sushi, 9pcs Sashimi, new Sea Shai Roll & Calif. Roll Medium 39.00
            F3 10pcs Sushi, 12pcs Sashimi, 3 rolls & new Sea Shai Roll Large 65.00
            F4 12pcs Sushi, 18pcs Sashimi, 4 rolls & new Sea Shai Roll King 85.00
            New Sea Shai Combination Assortment of Sushi and Maki
            F5 5pcs Sushi, new Sea Shai Roll, & California Roll Small 29.00
            F6 8pcs Sushi, newSea Shai Roll, Calif., Tekka, &Kappa Rolls Medium 39.00
            F7 10pcs Sushi,new Sea Shai Roll, Calif., Tekka, Kappa, Futomaki, & Sake w/Cucumber Rolls Large 65.00
            F8 12pcs Sushi, new Sea Shai Rolls & 8 rolls Queen 85.00 
    </div>
"""
## Preliminary lists
# Overarching app list, empty list for menu items
appList = appetizers.split("\n")
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
