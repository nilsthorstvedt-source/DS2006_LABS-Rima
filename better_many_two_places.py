
import copy


visited_places = {
    "city": "",
    "country": "",
    "dates": [],
}

my_visited_places = []

for i in range(0, 2):
    # make a deep copy of the dictionary template:
    places = copy.deepcopy(visited_places)

    places["city"] = input("enter city name: ")
    places["country"] = input("enter country name: ")
    times = input("how many times have you visited?")

    for j in range(0, int(times)):
        year = input(f"enter the year of the {j+1} time you went there: ")
        places["dates"].append(year)

    my_visited_places.append(places)

print(my_visited_places)


# output task 12:
# enter city name: stockholm
# enter country name: sweden
# how many times have you visited?3
# enter the year of the 1 time you went there: 2016
# enter the year of the 2 time you went there: 2020
# enter the year of the 3 time you went there: 2025
# enter city name: vienna
# enter country name: austria
# how many times have you visited?1
# enter the year of the 1 time you went there: 2023
# [{'city': 'stockholm', 'country': 'sweden', 'dates': ['2016', '2020', '2025']}, {'city': 'vienna', 'country': 'austria', 'dates': ['2023']}]
