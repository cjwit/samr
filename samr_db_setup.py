import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Bio(Base):
	__tablename__ = 'bio'
	name = Column(String(80), nullable = False)
	affiliation = Column(String(250), nullable = True)
	interests = Column(String(250), nullable = True)
	email = Column(String(250), nullable = True)
	website = Column(String(250), nullable = True)
	id = Column(Integer, primary_key = True)
	projects = relationship("Project", cascade="all, delete-orphan")

class Event(Base):
	__tablename__ = 'event'
	title = Column(String(80), nullable = False)
	location = Column(String(250), nullable = False)
	description = Column(String(250), nullable = True)
	start_date = Column(String(10), nullable = False)
	id = Column(Integer, primary_key = True)
	host_name = Column(String(80), nullable = True)
	contact = Column(String(80), nullable = True)

class Project(Base):
	__tablename__ = 'project'
	title = Column(String(80), nullable = False)
	description = Column(String(250), nullable = True)
	id = Column(Integer, primary_key = True)
	owner_id = Column(Integer, ForeignKey('bio.id'))
	owner = relationship(Bio)

class Bibliography(Base):
	__tablename__ = 'bibliography'
	title = Column(String(80), nullable = False)
	description = Column(String(250), nullable = True)
	id = Column(Integer, primary_key = True)
	resources = relationship("Resource", cascade="all, delete-orphan")

class Resource(Base):
	__tablename__ = 'resource'
	title = Column(String(80), nullable = False)
	description = Column(String(250), nullable = True)
	info = Column(String(250), nullable = True)
	website = Column(String(250), nullable = True)
	id = Column(Integer, primary_key = True)
	bibliography_id = Column(Integer, ForeignKey('bibliography.id'))
	bibliography = relationship(Bibliography)

engine = create_engine('postgres://bstjlxdcqblgkv:QnqPK3x9hkRD49k67g_HT4oZDK@ec2-54-225-215-233.compute-1.amazonaws.com:5432/d9u6nclt064q0a')

Base.metadata.create_all(engine)