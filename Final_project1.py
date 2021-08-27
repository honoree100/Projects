wine_selection={"Verejo":[["mexican", "american", "world" ],["savory"] ,["tacos", "steak", "chicken"]],\
     "Agiorgitiko":[["indian", "chinese", "world"],["spicy", "savory"],["steak","rice","tomato_sauce"]], \
         "tokaji":[["french", "italian", "world"],["savory"],["cheese", "salad"]]\
             }

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
    counter = 0
    wine_to_drink =wine_selected[0]

    for i in wine_selected:
        curr_frequency = wine_selected.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            wine_to_drink = i
 
    print("For you meal, I would strongly recommend to pair it with a nice glass of "+ wine_to_drink.upper())


wine_to_drink("world","savory","salad")


# def most_frequent(List):
#     counter = 0
#     num = List[0]
     
#     for i in List:
#         curr_frequency = List.count(i)
#         if(curr_frequency> counter):
#             counter = curr_frequency
#             num = i
 
#     return num
 
# List = [23, 5, 2, 2, 1, 3]
# print(most_frequent(List))






    
