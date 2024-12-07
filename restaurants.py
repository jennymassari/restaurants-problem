    # visitors_dict = {}
    # access each restaunt value 
    # for key, visitors in visits.items():
    # create a counter for each visitor,
        # for visitor in visitors:
    # starting with 0 and increasing by one each time the visitor apears in a restaurant
            # visitors_dict[visitor] = visitors_dict.get(0)
    # variable to hold visitor that appears the most
    # conditional to compare number of  visits and substitute for new vistor if hold a bigger value
    #  return the variable with hold visitor that appears the most

def most_varied_visitor(visits):
    name = ""
    counter = 0
    counter_dict = {}

    for restaurant, visitors in visits.items():
        for visitor in visitors:
            if visitor not in counter_dict:
                counter_dict[visitor] = 1
            else:
                counter_dict[visitor] = counter_dict.get(restaurant, 1) + 1
    # print(counter_dict)

    for key, value in counter_dict.items():
        if value > counter:
            counter = value
            name = key      
    
    return name

        

print(most_varied_visitor({
    "Spicy City" : ["Eliza"],
    "La Especial Norte" : ["Eliza"],
    "Sushi Kashiba": ["Xinting"],
}))

print(most_varied_visitor({
    "Spicy City" : ["Auberon", "Elora"],
    "La Especial Norte": ["Elora", "Auberon", "Rowan"],
    "Sushi Kashiba": ["Xinting", "Aisha", "Xinting"],
    "Lyon's Grocery": ["Auberon", "Xinting", "Sam", "Xinting"],
    "Applebee's": ["Sam", "Eliza"],
}))
visits_1 = {
    "Spicy City" : ["Eliza"],
    "La Especial Norte" : ["Eliza"],
    "Sushi Kashiba": ["Xinting"],
}
assert most_varied_visitor(visits_1) == "Eliza"

visits_2 = {
    "Spicy City" : ["Auberon", "Elora"],
    "La Especial Norte": ["Elora", "Auberon", "Rowan"],
    "Sushi Kashiba": ["Xinting", "Aisha", "Xinting"],
    "Lyon's Grocery": ["Auberon", "Xinting", "Sam", "Xinting"],
    "Applebee's": ["Sam", "Eliza"],
}
assert most_varied_visitor(visits_2) == "Auberon"

visits_3 = {
    "Spicy City" : ["Elora", "Elora", "Elora"],
}
assert most_varied_visitor(visits_3) == "Elora"
print("All tests passed! If time remains, discuss time/space complexity")