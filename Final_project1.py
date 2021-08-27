wine_selection={"Verejo":[["mexican", "american", "world" ],["savory"] ,["tacos", "steak", "chicken"]], "Agiorgitiko":[["indian", "chinese", "world"],["spicy", "savory"],["steak","rice","tomato_sauce"]], "tokaji":[["french", "italian", "world"],["savory"],["cheese", "salad"]]}

def wine_to_drink(cusine,taste, meal):
    verejo_total_count=0
    Agiorgitiko_total_count=0
    tokaji_total_count=0
    # print(wine_selection.values())
    # print(wine_selection.keys())
    wine_selected=[]

    for wine, choices in wine_selection.items():
        for tastes in choices:
            if taste in tastes:
                wine_selected.append(wine)
        for cusines in choices:
            if cusine in cusines:
                wine_selected.append(wine)
        for meals in choices:
            if meal in meals:
                wine_selected.append(wine)
    
    print(wine_selected)
    wine_to_drink=[]
    counter = 0
    num =wine_selected[0]

    for i in wine_to_drink:
        curr_frequency = wine_to_drink.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    print(num)


wine_to_drink("american","savory","steak")











    
