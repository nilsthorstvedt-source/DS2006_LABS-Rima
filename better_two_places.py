

visited_places = {
    "city": "",
    "country": "",
    "year": "",
}

my_visited_places = []

for i in range(0, 2):
    # make a copy of the dictionary template:
    places = visited_places.copy()

    places["city"] = input("enter city name: ")
    places["country"] = input("enter country name: ")

    my_visited_places.append(places)

print(my_visited_places)


# output task 10:
# enter city name: aleppo
# enter country name: syria
# enter the year: 2025
# enter city name: paris
# enter country name: france
# enter the year: 2023
# [{'city': 'aleppo', 'country': 'syria', 'year': '2025'}, {'city': 'paris', 'country': 'france', 'year': '2023'}]
