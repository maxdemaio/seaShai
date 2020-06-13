# Parse all the menu data

appetizers = """<h3>Fresh</h3>
            Dr 1 Maguro - Tuna 6.00
            Dr 2 Hamachi - Yellow Tail 6.00
            Dr 3 Sake - Salmon 5.00
            Dr 4 Hirame - Fluke 5.00
            Dr 5 Toro - Tuna Belly M/P
            Dr 6 Amaebi - Sweet Shrimp 6.00
            Dr 7 Tai - Red Snapper 4.50
            Dr 8 Hocky Gai - Surf Clam 5.50
            Dr 9 Saba - Mackerel 4.50
            Dr 10 Suzuki - Sea Bass 4.50
            Dr 11 Ika - Squid 4.50
            Dr 12 Hotate - Scallop 6.50
            Dr 13 Shiro Maguro - White Tuna 5.50
        <h3>Smoked/Cooked</h3>
            Dr 14 Sake - Smoked Salmon 6.00
            Dr 15 Tako - Octopus 6.00
            Dr 16 Kani Kama - Crab Stick 4.00
            Dr 17 Ebi - Shrimp 5.00
            Dr 18 Unagi - Eel 5.00
            Dr 19 Tamago - Egg 4.00
        <h3>Roe</h3>
            Dr 20 Ikura - Salmon Roe 7.00
            Dr 21 Tobiko - Flying Fish Roe 5.50
            Dr 22 Uni - Sea Urchin 8.00
            Dr 23 Uzura - Quail Egg 2.00
        <h3>Vegetable Maki (8 pcs/order)</h3>
            Dr 24 Kappa - Cucumber 4.00
            Dr 25 Oshinko - Pickled Radish 4.00
            Dr 26 Yamagobo - Pickled Gobo Root4.00
            Dr 27 Avocado - Avocado 4.00
            Dr 28 Kampyo - Squash 4.00
            Dr 29 Mushroom - Mushroom 4.00
            Dr 30 Spinach - Spinach 4.00
            Dr 31 Sakura - Avo,cuc,carrot 5.00
        <h3>Inside Maki (seaweed on outside)</h3>
            Dr 32 Tekka - Tuna Roll 5.00
            Dr 33 Sake - Salmon 5.00
            Dr 34 Tobiko - Maki Flying Fish Roe 6.00
            Dr 35 Futomaki - Vegetable only 6.00 w/egg ,crab stick 7.00
        <h3>Inside Out Maki (rice on outside)</h3>
            Dr 36 California - crab,avo,fish roe cuc 5.00
            Dr 37 Boston - salmon crab,mayo,cuc, 5.50
            Dr 38 Manhattan - smoked salmon,avo 6.50
            Dr 39 Mexican - shr temp, cuc, hotsauce 6.00
            Dr 40 Negihamachi - yellowtail,scallions 8.00
            Dr 41 Unagi w/avo - eel w/avo 6.00
            Dr 42 Unagi w/cuc - eel w/cuc 6.00
            Dr 43 Spicy Tekka - tuna w/cuc 7.00
            Dr 44 Spicy Hotate - scallop, hot sauce 8.00
            Dr 45 New Sea Shai - 5 different fish w/crab, avo 11.00
            Dr 46 Sake Kawa - salmon skin, cuc 6.00
            Dr 47 Shrimp w/cucumber 6.00
            Dr 48 Soft Shell Crab Roll 8.00
            Dr 49 Philadelphia - smoked salmon w/ cream cheese 6.50
            Dr 50 Indiana - flying fish roe crabstick, avocado, w/mayo 6.00
        <h3>Special Rolls</h3>
            Dr51 Hamachi Jalapeno 8.00 
            Dr52 Spicy Crunch 12.00
            Dr53 Dragon Roll -- Shrimp tempura & eel , avocado on top 14.00
            Dr54 Dynamite Roll -- grilled tako, crab, tobiko , scallions 8.00
            Dr55 Crunchy Munchy -- Crab, cucumber, tempura flake w/ mayo sauce 8.00
            Dr56 Philly Dream Roll -- shrimp tempura, cream cheese, tobiko w/ eel sauce 9.00
            Dr57 360 Philadelphia -- cream cheese, asparagus topped w/ tuna and deep fried 11.00
            Dr58 Rainbow -- assortment of fish w/ crab, avo, cuc 16.00
            Dr59Spider Roll -- Jumbo soft shell crab, cuc, & flying fish roe 15.00
            Dr60 Caterpillar Roll -- layers of avocado w/ eel & cucumber 10.00
            Dr61 Crazy Dragon -- Shrimp Tempura, cucumber, and avo, spicy tuna on top w/ spicy mayo 15.00
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
    print("<dt>" + header + "</dt>")

print()

# Wrap menu items in description data tag
for x in range(0, len(finalMenuItems)):
    print("<dd>" + finalMenuItems[x] +
          " | <span class='price'>" + prices[x] + "</span>" + "</dd>")
