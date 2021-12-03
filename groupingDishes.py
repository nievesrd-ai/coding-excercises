def groupingDishes(dishes):
    # a nested loop, outer loop is dish. Inner loop parses the dish name
    # as ingredients are iterated, the ingredient will be used to access a
    # hash table, which will be populated with the dish name
    temp = {}
    output = []
    temp_row = []
    lengths = {}
    for dish in dishes:
        current_dish = dish[0]
        for j in range(1, len(dish)):
            if dish[j] not in temp.keys():
                temp[dish[j]] = []
            temp[dish[j]].append(current_dish)

    for sorted_key in sorted(temp):
        if lengths[sorted_key] > 1:
            temp_row.append(sorted_key)
            temp_row = temp_row + sorted(temp[sorted_key])
            output.append(temp_row)
            temp_row = []
    return output

dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

print(groupingDishes(dishes))