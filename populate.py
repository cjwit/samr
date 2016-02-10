from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random, datetime
from random import randint
from samr_db_setup import Base, Bio, Event, Bibliography, Project, Resource
 
engine = create_engine('sqlite:///samr.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

first_names = ["John", "Stacy", "Bill", "Samra", "Fiona", "Carl", "Taylor", "Stephen", "Muhammed", "Fatima", "Amina"]
last_names = ["Smith", "Jones", "Arrazak", "Assalam", "Miller", "Meuller", "Michaelson", "Saladin", "Farrouk"]
interests = ["Sufism", "Islam", "Maqams", "Politics", "Piety", "Sacred", "Anthropology", "Economics", "Rhtyhm", "Oud", "Egypt", "Morocco", "Gulf States", "Iran", "Indonesia", "Performance", "Ritual", "Coptic music", "Activism", "Arab Spring"]
domains = ["gmail.com", "hotmail.com", "aol.com", "yahoo.com", "fakeschool.edu", "sillyplace.edu"]

affiliations = ["Oxfordhouse", "Carnegie Schoolfront", "Skippers University", "Skylight College", "Pragmatics Polytechnic", "NYC Universityland", "LaLa U", "The LLT", "Ohio A&M", "Texas University", "Schoemaker U"]

def randomName():
	first = (randint(1, len(first_names))) - 1
	last = (randint(1, len(last_names))) - 1
	return first_names[first] + " " + last_names[last]

def randomInterests():
	num = randint(1, 4)
	current_interests = []
	for number in range(num):
		intrest_num = (randint(1, len(interests))) - 1
		current_interests.append(interests[intrest_num])
	interest_string = ""
	for interest in current_interests:
		interest_string += interest + " "
	return interest_string.replace(" ", ", ")[0:-2]

def randomEmail(name):
	email = name.replace(" ", ".").lower()
	domain_num = (randint(1, len(domains))) - 1
	domain = domains[domain_num]
	email += "@" + domain
	return email

# events
event_titles = ["Concert", "Symposium", "Workshop", "Performance", "Research group", "Meeting", "Conference"]
locations = ["London", "NYC", "Seattle", "Santa Barbara", "Tallahassee", "Scandanavia", "Los Angeles", "Chicago"]
descriptions = ["Meet important people", "Research activities are grand", "You'll wish you had stayed at home"]

def randomDate():
	today = datetime.date.today()
	from_today = randint(-365, 365)
	event_date = today + datetime.timedelta(days = from_today)
	return event_date

# projects
project_titles = ["Website", "Database", "Concert series", "Symposium"]
project_descriptions = ["Meet important people", "Research activities are grand", "You'll wish you had stayed at home"]

# bibliographies

# items
item_titles = ["Article 1", "Article 2", "Article 3", "Article 4", "Book 1", "Book 2", "Book 3", "Book 4"]

# populate database

for bio in range(30):
	name = randomName()
	new_bio = Bio(name = name, 
		website = "http://www."+ domains[randint(0, len(domains) - 1)],
		interests = randomInterests(), 
		email = randomEmail(name), 
		affiliation = affiliations[randint(0, len(affiliations) - 1)]
		)
	session.add(new_bio)
	session.commit()

for event in range(15):
	new_event = Event(title = event_titles[randint(0, len(event_titles) - 1)], 
		location = locations[randint(0, len(locations) - 1)],
		description = descriptions[randint(0, len(descriptions) - 1)], 
		start_date = randomDate(),
		host_name = randomName(),
		contact = randomEmail(randomName())
	)
	session.add(new_event)
	session.commit()

for project in range(10):
	new_project = Project(title = project_titles[randint(0, len(project_titles) - 1)], 
		description = project_descriptions[randint(0, len(project_descriptions) - 1)], 
		owner_id = randint(1, 30))
	session.add(new_project)
	session.commit()

for bib in range(10):
	title = interests[randint(0, len(interests) - 1)]
	description = "Bibliography on the topic of " + title
	new_bib = Bibliography(title = title, 
		description = description)
	session.add(new_bib)
	session.commit()

for item in range(50):
	title = item_titles[randint(0, len(item_titles) - 1)]
	new_resource = Resource(title = title, 
		description = "Interesting writing on the topic of " + title, 
		info = "Published somehwere, hope you can find it", 
		website = "http://www.google.com/" + interests[randint(0, len(interests) - 1)], 
		bibliography_id = randint(1, 11))
	session.add(new_resource)
	session.commit
	