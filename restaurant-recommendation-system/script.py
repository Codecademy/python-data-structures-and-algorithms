from data import *
from welcome import *
from linkedlist import LinkedList

print_welcome()


# Write code to insert food types into a data structure (LinkedList) here. The data is in data.py
def insert_food_types():
    food_type_list = LinkedList()
    for food_type in types:
        food_type_list.insert_beginning(food_type)
    return food_type_list


# Write code to insert restaurant data into a data structure (LinkedList of LinkedLists) here. The data is in data.py
def insert_restaurant_data():
    restaurant_data_list = LinkedList()
    for food_type in types:
        restaurant_sublist = LinkedList()
        for restaurant in restaurant_data:
            if restaurant[0] == food_type:
                restaurant_sublist.insert_beginning(restaurant)
        restaurant_data_list.insert_beginning(restaurant_sublist)
    return restaurant_data_list


my_food_list = insert_food_types()
my_restaurant_list = insert_restaurant_data()


selected_food_type = ""

# Write code for user interaction here
while len(selected_food_type) == 0:
    user_input = str(input(
        "\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if "
        "it's here.\n")).lower()

    # Search for user_input in food types data structure here
    matching_types = []
    type_list_head = my_food_list.get_head_node()
    while type_list_head is not None:
        if str(type_list_head.get_value()).startswith(user_input):
            matching_types.append(type_list_head.get_value())
        type_list_head = type_list_head.get_next_node()

    # print list of matching food types
    for food in matching_types:
        print(food)

    # Check if only one type of restaurant was found, ask user if they would like to select this type
    if len(matching_types) == 1:
        select_type = str(input(
            "\nThe only matching type for the specified input is " + matching_types[0] + ". \nDo you want to look at " +
            matching_types[0] + " restaurants? Enter y for yes and n for no\n")).lower()

        # After finding food type write code for retrieving restaurant data here
        if select_type == 'y':
            selected_food_type = matching_types[0]
            print("Selected Food Type: " + selected_food_type)
            restaurant_list_head = my_restaurant_list.get_head_node()
            while restaurant_list_head.get_next_node() is not None:
                sublist_head = restaurant_list_head.get_value().get_head_node()
                if sublist_head.get_value()[0] == selected_food_type:
                    while sublist_head.get_next_node() is not None:
                        print("--------------------------")
                        print("Name: " + sublist_head.get_value()[1])
                        print("Price: " + sublist_head.get_value()[2] + "/5")
                        print("Rating: " + sublist_head.get_value()[3] + "/5")
                        print("Address: " + sublist_head.get_value()[4])
                        print("--------------------------\n")
                        sublist_head = sublist_head.get_next_node()
                restaurant_list_head = restaurant_list_head.get_next_node()

            # Ask user if they would like to search for other types of restaurants
            repeat_loop = str(input("\nDo you want to find other restaurants? Enter y for yes and n for no.\n")).lower()
            if repeat_loop == 'y':
                selected_food_type = ""
