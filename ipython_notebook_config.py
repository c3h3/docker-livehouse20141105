
c = get_config()

headers = {'X-Frame-Options': 'ALLOWALL'}

c.NotebookApp.allow_origin = '*'
c.NotebookApp.allow_credentials = True

c.NotebookApp.webapp_settings = {'headers': headers}

import os
password = os.environ.get("PASSWORD", "ipynb")

from IPython.lib import passwd
password = passwd(password)

c.NotebookApp.password = unicode(password)

