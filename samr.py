from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from samr_db_setup import Base, Bio, Event, Project, Bibliography, Resource
import datetime

app = Flask(__name__)

engine = create_engine('sqlite:///samr.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/home/')
def home():
	today = datetime.date.today()
	events = session.query(Event).filter(Event.start_date > today).order_by(Event.start_date)
	projects = session.query(Project).order_by(Project.title)
	return render_template('home.html', events = events, projects = projects)

# View, add, edit, and delete events
@app.route('/events/')
def events():
	return "Events home page"

@app.route('/events/<int:event_id>/')
def viewEvent(event_id):
	return "View info for event number " + str(event_id)

@app.route('/events/add/')
def addEvent():
	return "Page to add an event"

@app.route('/events/<int:event_id>/edit/')
def editEvent(event_id):
	return "Edit or delete event number " + str(event_id)

# View, add, edit, and delete biographies
@app.route('/bios/')
def bios():
	return "Bio home page"

@app.route('/bios/<int:bio_id>/')
def viewBio(bio_id):
	return "View info for bio number " + str(bio_id)

@app.route('/bios/add/')
def addBio():
	return "Page to add an bio"

@app.route('/bios/<int:bio_id>/edit/')
def editBio(bio_id):
	return "Edit or delete bio number " + str(bio_id)

# View, add, edit, and delete projects/webpages
@app.route('/projects/')
def projects():
	return "Projects home page"

@app.route('/projects/<int:project_id>/')
def viewProject(project_id):
	return "View info for project number " + str(project_id)

@app.route('/projects/add/')
def addProject():
	return "Page to add a project"

@app.route('/projects/<int:project_id>/edit/')
def editProject(project_id):
	return "Edit or delete project number " + str(project_id)

# View, add, edit, and delete bibliographies
@app.route('/bib/')
def bibliographies():
	return "Bibliographies home page"

@app.route('/bib/<int:bib_id>/')
def viewBib(bib_id):
	return "View info for bibliography number " + str(bib_id)

@app.route('/bib/add/')
def addBib():
	return "Page to add a bibliography"

@app.route('/bib/<int:bib_id>/edit/')
def editBib(bib_id):
	return "Edit or delete bibliography number " + str(bib_id)

# View, add, edit, and delete bibliography resources
@app.route('/bib/item/add/')
def addResource():
	return "Page to add an item to a bibliography"

@app.route('/bib/item/<int:item_id>/')
def viewResource(item_id):
	return "Page to view info on item number " + str(item_id)

@app.route('/bib/item/<int:item_id>/edit/')
def editResource(item_id):
	return "Edit or delete item number " + str(item_id)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)