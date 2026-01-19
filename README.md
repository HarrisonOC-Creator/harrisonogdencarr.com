# This file contains the WSGI configuration required to serve up your
# web application at http://harrisonogdencarr.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Django project

import os
import sys

project_home = '/home/harrisonogdencarr/www_harrisonogdencarr_com'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
/var/www/www_harrisonogdencarr_com_wsgi.py
