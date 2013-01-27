import cherrypy
from cherrypy.lib.cptools import accept
from models import Photoblog
from lib import conf
from lib.tools import find_acceptable_within

class Resource(object):
    def handle_GET(self, obj_id):
        best = accept(['application/xml', 'application/atom+xml',
                        'text/json', 'text/x-json',
                        'application/json'])
                        
                        
