import os
import urllib
import datetime

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2
import logging


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Student(ndb.Model):

    PatientName = ndb.StringProperty(indexed=False)
    ConsultationDate = ndb.StringProperty(indexed=False)
    Doctor = ndb.StringProperty(indexed=False)
    Nurse = ndb.StringProperty(indexed=False)
    Concern = ndb.StringProperty(indexed=False)
    CourseName = ndb.StringProperty(indexed=False)
    Year = ndb.StringProperty(indexed=False)
    ContactNum = ndb.StringProperty(indexed=False)    
    Section = ndb.StringProperty(indexed=False)

class Faculty(ndb.Model):

    PatientName = ndb.StringProperty(indexed=False)
    ConsultationDate = ndb.StringProperty(indexed=False)
    Doctor = ndb.StringProperty(indexed=False)
    Nurse = ndb.StringProperty(indexed=False)
    Concern = ndb.StringProperty(indexed=False)
    Department = ndb.StringProperty(indexed=False)
    Age = ndb.StringProperty(indexed=False)
    ContactNum = ndb.StringProperty(indexed=False)          

class Home(webapp2.RequestHandler):
    def get(self):
        # Checks for active Google account session
 
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Sign In'
    
        template_values = {
            'url': url,
            'user': users.get_current_user(),
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('Homepage.html')
        self.response.write(template.render(template_values))

class About(webapp2.RequestHandler):
    def get(self):

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Sign In'
    
        template_values = {
            'url': url,
            'user': users.get_current_user(),
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('About.html')
        self.response.write(template.render(template_values))        

class Contact(webapp2.RequestHandler):
    def get(self):

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Sign In'
    
        template_values = {
            'url': url,
            'user': users.get_current_user(),
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('Contact.html')
        self.response.write(template.render(template_values)) 

class PatientLog(webapp2.RequestHandler):
    def get(self):

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Sign In'
    
        template_values = {
            'url': url,
            'user': users.get_current_user(),
            'url_linktext': url_linktext,
        }
        
        template = JINJA_ENVIRONMENT.get_template('Patientlog.html')
        self.response.write(template.render(template_values)) 

class StudentNewRecord(webapp2.RequestHandler):
    def get(self):

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Sign In'
    
        template_values = {
            'url': url,
            'user': users.get_current_user(),
            'url_linktext': url_linktext,
        }
        
        template = JINJA_ENVIRONMENT.get_template('StudentNew.html')
        self.response.write(template.render(template_values))

    def post(self):

    	student = Student()
        student.PatientName = self.request.get('PatientName')
        student.ConsultationDate = self.request.get('ConsultationDate')
        student.ContactNum = self.request.get('ContactNum')
        student.CourseName = self.request.get('CourseName')
        student.Year = self.request.get('Year')
        student.Section = self.request.get('Section') 
        student.Concern = self.request.get('Concern')
        student.Doctor = self.request.get('Doctor')
        student.Nurse = self.request.get('Nurse')               
        student.put()
        self.redirect('/studentnew')

class StudentList(webapp2.RequestHandler):
    def get(self):

        student = Student.query().fetch();

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Sign In'
  
        template_values = {
            'url': url,
            'user': users.get_current_user(),
            'url_linktext': url_linktext,            
        	'student': student,            
        } 

        template = JINJA_ENVIRONMENT.get_template('StudentList.html')
        self.response.write(template.render(template_values))

class StudentView(webapp2.RequestHandler):
    def get(self, thesid):

        student = Student.query().fetch();
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)

        else:
            url = users.create_login_url(self.request.uri)

        template_values = {
        'student': student,
        'id'    : int(thesid)
        }

        template = JINJA_ENVIRONMENT.get_template('StudentView.html')
        self.response.write(template.render(template_values))        

class FacultyNewRecord(webapp2.RequestHandler):
    def get(self):

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Sign In'
    
        template_values = {
            'url': url,
            'user': users.get_current_user(),
            'url_linktext': url_linktext,
        }
        
        template = JINJA_ENVIRONMENT.get_template('FacultyNew.html')
        self.response.write(template.render(template_values))

    def post(self):

    	faculty = Faculty()
        faculty.PatientName = self.request.get('PatientName')
        faculty.ConsultationDate = self.request.get('ConsultationDate')
        faculty.ContactNum = self.request.get('ContactNum')
        faculty.Department = self.request.get('Department')
        faculty.Age = self.request.get('Age') 
        faculty.Concern = self.request.get('Concern')
        faculty.Doctor = self.request.get('Doctor')
        faculty.Nurse = self.request.get('Nurse')               
        faculty.put()
        self.redirect('/facultynew')

class FacultyList(webapp2.RequestHandler):
    def get(self):

        faculty = Faculty.query().fetch();

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Sign In'
  
        template_values = {
            'url': url,
            'user': users.get_current_user(),
            'url_linktext': url_linktext,            
        	'faculty': faculty,            
        } 

        template = JINJA_ENVIRONMENT.get_template('FacultyList.html')
        self.response.write(template.render(template_values))

class FacultyView(webapp2.RequestHandler):
    def get(self, thesid):

        faculty = Faculty.query().fetch();
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)

        else:
            url = users.create_login_url(self.request.uri)

        template_values = {
        'faculty': faculty,
        'id'    : int(thesid)
        }

        template = JINJA_ENVIRONMENT.get_template('FacultyView.html')
        self.response.write(template.render(template_values))

			 
application = webapp2.WSGIApplication([
	#Homeurls
    ('/', Home),
    ('/about', About),    
    ('/contact', Contact),
    ('/patientlogs', PatientLog),
    #Studentrecords
    ('/studentnew', StudentNewRecord),
    ('/studentlist',StudentList),
    ('/studentview/(\d+)',StudentView),
    #Facultyrecords
    ('/facultynew', FacultyNewRecord),
    ('/facultylist',FacultyList),
    ('/facultyview/(\d+)',FacultyView),        
], debug=True)