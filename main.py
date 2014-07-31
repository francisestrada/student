
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Student(ndb.Model):
    student_number=ndb.StringProperty(indexed=False)
    first_name=ndb.StringProperty(indexed=False)
    last_name=ndb.StringProperty(indexed=False)
    email=ndb.StringProperty(indexed=False)
    contact_number=ndb.StringProperty(indexed=False)
    course=ndb.StringProperty(indexed=False)

class SuccessPageHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('successDent.html')
        self.response.write(template.render())

class StudentNewHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('studentNew.html')
        self.response.write(template.render())

    def post(self):
        student = Student() 
        student.student_number = self.request.get('student_number')
        student.first_name= self.request.get('first_name')
        student.last_name = self.request.get('last_name')
        student.email = self.request.get('email')
        studentphone_number = self.request.get('phone_number')
        student.course = self.request.get('course')
        student.put()
        self.redirect('/success')

class StudentDescriptionHandler(webapp2.RequestHandler):
    def get(self, student_id):
                student_all=Student.query().fetch()
                student_id = int(student_id)
                template_values={
                        'id': student_id,
                        'student_all': student_all
                }
                template = JINJA_ENVIRONMENT.get_template('studentView.html')
                self.response.write(template.render(template_values))
 
class StudentListHandler(webapp2.RequestHandler):
    def get(self):
                student_all=Student.query().fetch()
                template_values={
                        'student_all': student_all
                }
 
                template = JINJA_ENVIRONMENT.get_template('studentList.html')
                self.response.write(template.render(template_values))
        

app = webapp2.WSGIApplication([
    ('/student/new', StudentNewHandler),
    ('/success', SuccessPageHandler),
    ('/student/list', StudentListHandler),
    ('/student/view/(\d+)', StudentDescriptionHandler)
], debug=True)
