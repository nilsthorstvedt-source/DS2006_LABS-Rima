

visited_places = {
    "city": "",
    "country": "",
    "dates": [],
}

my_visited_places = []

for i in range(0, 2):
    # make a copy of the dictionary template:
    places = visited_places.copy()

    places["city"] = input("enter city name: ")
    places["country"] = input("enter country name: ")
    times = input("how many times have you visited?")
    for j in range(0, int(times)):
        year = input(f"enter the year of the {j+1} time you went there: ")
        places["dates"].append(year)

    my_visited_places.append(places)

print(my_visited_places)

# output task 11:
# enter city name: aleppo
# enter country name: syria
# how many times have you visited?2
# enter the year of the 1 time you went there: 2003
# enter the year of the 2 time you went there: 2025
# enter city name: istanbul
# enter country name: turkey
# how many times have you visited?3
# enter the year of the 1 time you went there: 2016
# enter the year of the 2 time you went there: 2024
# enter the year of the 3 time you went there: 2025
# [{'city': 'aleppo', 'country': 'syria', 'dates': ['2003', '2025', '2016', '2024', '2025']}, {'city': 'istanbul', 'country': 'turkey', 'dates': ['2003', '2025', '2016', '2024', '2025']}]
