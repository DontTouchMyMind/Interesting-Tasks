categories = [
    {
        "title": "Food",
        "subcategories": [
            {"title": "Bread"},
            {
                "title": "Meat",
                "subcategories": [
                    {"title": "Pork",
                     "subcategories":[
                         {"title": "White Pork"},
                         {"title": "Red Pork"}
                     ]
                     },
                    {"title": "Beef"},
                ],
            },
            {"title": "Cheese"},
        ],
    },
    {"title": "Drinks"},
]


def get_formatted_list(categories: list, counter: int = 0):
    for category in categories:
        print(f'{counter * "-"}{category.get("title")}')

        if category.get("subcategories"):
            counter += 1
            get_formatted_list(category.get("subcategories"), counter)
            counter -= 1


if __name__ == '__main__':
    get_formatted_list(categories)
