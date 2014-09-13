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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('blog.html')
        self.response.write(template.render())
		
class Movie (webapp2.RequestHandler):
	def get(self, id): 
		movie = int(id) 
		value = {'movie-id': movie}
		template1 = JINJA_ENVIRONMENT.get_template('templates/view.html')
		self.response.write(template1.render(value))
			 
application = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/view/(.*)',Movie),
], debug=True)