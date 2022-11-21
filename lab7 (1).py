import random
import time

n = random.randint(1, 99)
userinput = []

print("Please enter a number between 1 and 100")

i = 0
while True:
  try:
    userinput = input("Enter a number between 1 and 100.\n")
    if userinput.isdigit():
      userinput = int(userinput)
    else:
      raise ValueError()
    if 1 <= userinput <= 100:
      break

  except ValueError():
    print("Must be a value between 1 and 100.")
if userinput == n:
  print("You guessed correct")
else:
  print(f"The correct value was {n}")

list_dictionaries = [{
  "name": "Marie",
  "lastname": "Fraser",
  "job title": "Questar Lecturer",
  "email": "mfraser@albany.edu"
}, {
  'name': 'Martha',
  'lastname': 'Avila',
  'job title': 'Informatics Lecturer',
  'email': 'mavilamaravila@albany.edu'
}, {
  "name": 'Gary',
  "lastname": 'Ackerman',
  "job title": "Associate Professor and Associate Dean",
  "email": "gackerman@albany.edu"
}]
for faculty in list_dictionaries:
  print(faculty)

import time

US_state_cap = {
  'Alabama': 'Montgomery',
  'Alaska': 'Juneau',
  'Arizona': 'Phoenix',
  'Arkansas': 'Little Rock',
  'California': 'Sacramento',
  'Colorado': 'Denver',
  'Connecticut': 'Hartford',
  'Delaware': 'Dover',
  'Florida': 'Tallahassee',
  'Georgia': 'Atlanta',
  'Hawaii': 'Honolulu',
  'Idaho': 'Boise',
  'Illinios': 'Springfield',
  'Indiana': 'Indianapolis',
  'Iowa': 'Des Monies',
  'Kansas': 'Topeka',
  'Kentucky': 'Frankfort',
  'Louisiana': 'Baton Rouge',
  'Maine': 'Augusta',
  'Maryland': 'Annapolis',
  'Massachusetts': 'Boston',
  'Michigan': 'Lansing',
  'Minnesota': 'St. Paul',
  'Mississippi': 'Jackson',
  'Missouri': 'Jefferson City',
  'Montana': 'Helena',
  'Nebraska': 'Lincoln',
  'Neveda': 'Carson City',
  'New Hampshire': 'Concord',
  'New Jersey': 'Trenton',
  'New Mexico': 'Santa Fe',
  'New York': 'Albany',
  'North Carolina': 'Raleigh',
  'North Dakota': 'Bismarck',
  'Ohio': 'Columbus',
  'Oklahoma': 'Oklahoma City',
  'Oregon': 'Salem',
  'Pennsylvania': 'Harrisburg',
  'Rhode Island': 'Providence',
  'South Carolina': 'Columbia',
  'South Dakoda': 'Pierre',
  'Tennessee': 'Nashville',
  'Texas': 'Austin',
  'Utah': 'Salt Lake City',
  'Vermont': 'Montpelier',
  'Virginia': 'Richmond',
  'Washington': 'Olympia',
  'West Virginia': 'Charleston',
  'Wisconsin': 'Madison',
  'Wyoming': 'Cheyenne'
}

for key, value in US_state_cap.items():
  print(f"The city of {value} is the capital of {key}.")
  time.sleep(2)
for key, value in US_state_cap.items():
  print(f"{key} state", end="\n")
  print(f"{value} city", end="\n")
  time.sleep(2)