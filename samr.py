from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from samr_db_setup import Base, Bio, Event, Project, Bibliography, Resource
from datetime import datetime, date
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
	today = datetime.date.today()
	upcoming = session.query(Event).filter(Event.start_date >= today).order_by(Event.start_date)
	past = session.query(Event).filter(Event.start_date < today).order_by(Event.start_date.desc())
	return render_template('events.html', upcoming = upcoming, past = past)

@app.route('/events/add/', methods=['GET', 'POST'])
def addEvent():
	if request.method == "POST":
		date_string = request.form['start_date']
		split = date_string.split('/')
		month = int(split[0])
		day = int(split[1])
		year = int(split[2])
		new_date = date(year, month, day)
		new_event = Event(title = request.form['title'], 
			location = request.form['location'], 
			description = request.form['description'],
			host_id = request.form['host_id'],
			start_date = new_date
			)
		session.add(new_event)
		session.commit()
		flash("Event added")
		return redirect(url_for('events'))
	else:
		return render_template('addevent.html')

@app.route('/events/<int:event_id>/edit/', methods=['GET', 'POST'])
def editEvent(event_id):
	if request.method == "POST":
		event = session.query(Event).filter_by(id = event_id).one()
		date_string = request.form['start_date']
		split = date_string.split('/')
		month = int(split[0])
		day = int(split[1])
		year = int(split[2])
		new_date = date(year, month, day)
		event.title = request.form['title']
		event.location = request.form['location']
		event.description = request.form['description']
		event.host_id = request.form['host_id']
		event.start_date = new_date
		session.commit()
		flash("Event updated")
		return redirect(url_for('events'))
	else:
		event = session.query(Event).filter_by(id = event_id).one()
		date_info = event.start_date.split('-')
		start_date = date_info[1] + '/' + date_info[2] + '/' + date_info[0]
		return render_template('editevent.html', event = event, start_date = start_date)

@app.route('/events/<int:event_id>/delete/', methods=['GET', 'POST'])
def deleteEvent(event_id):
	if request.method == "POST":
		event = session.query(Event).filter_by(id = event_id).one()
		session.delete(event)
		session.commit()
		flash("Event deleted")
		return redirect(url_for('events'))
	else:
		event = session.query(Event).filter_by(id = event_id).one()
		date_info = event.start_date.split('-')
		start_date = date_info[1] + '/' + date_info[2] + '/' + date_info[0]
		return render_template('deleteevent.html', event = event, start_date = start_date)

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