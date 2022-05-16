travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited, times_visited, cities_visited):
  add_new = True
  while add_new:
      for log in travel_log:
          country_visited = input("What country did you visit?\n")
          times_visited = int(input("How many times have you visited this country?\n"))
          cities_visited = input("What cities did you visit?\n")
  
          new_country = {}
          new_country["country"] = country_visited
          new_country["visits"] = times_visited
          new_country["cities"] = cities_visited
          travel_log.append(new_country)
          if add_new == True:
            user_response = input("Do you want to add a new entry?\n").lower()
            if user_response == "no":
              add_new = False
              print("Thank you and goodbye.")
              break


#🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("country_visited", "times_visited", "cities_visited")              
print(travel_log)



