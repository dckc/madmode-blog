
# coding: utf-8

# ## Organizing Downloads: Google Chrome
# 
# My `Downloads` folder doesn't connect the files back to
# where they came from. But... ah! [Chrome data][1] has the info.
# 
# 
# Other download patterns:
# 
#  - dev-ebooks
#  - chord charts
#  - research papers
#    - zotero metadata
# 
# 
# [1]: https://www.foxtonforensics.com/browser-history-examiner/chrome-data
# 

# In[1]:


import pandas as pd
import sqlalchemy as sqla
dict(pandas=pd.__version__, sqlalchemy=sqla.__version__)


# [Finding my profile][2] ... `chrome://version/`...
# 
# ```
# Profile Path	/home/connolly/.config/google-chrome/Default
# ```
# 
# The `History` db there is locked,
# and I couldn't get a [read-only connection][3] to work,
# so I made a copy in `~/Desktop`:
# 
# [2]: https://www.howtogeek.com/255653/how-to-find-your-chrome-profile-folder-on-windows-mac-and-linux/
# [3]: https://github.com/pudo/dataset/issues/136

# In[2]:


import sqlite3

def _home():
    from pathlib import Path
    from os import environ
    return Path(environ['HOME'])

profile = _home() / '.config' / 'google-chrome' / 'Default'
desktop = _home() / 'Desktop'
history = sqla.create_engine('sqlite:///%s?mode=%s' % (profile / 'History', 'ro'))

history = lambda: sqlite3.connect('%s' % (desktop / 'History',))
history = sqla.create_engine('sqlite:///' , creator=history)

pd.read_sql('select 1', history)


# In[3]:


pd.read_sql('''
SELECT *
from sqlite_master
WHERE type='table'
ORDER BY name
''', history)


# In[4]:


pd.read_sql('''
select *
from downloads
limit 10
''', history, index_col='id')


# Interesting... what's that `downloads_url_chains` table? A search turns up [chrome_history.py][4], part of [GRR Rapid Response][GRR]: remote live forensics for incident response.
# 
# [4]: https://github.com/google/grr/blob/master/grr/parsers/chrome_history.py
# [GRR]: https://github.com/google/grr

# In[5]:


pd.read_sql('''
SELECT downloads.start_time, downloads_url_chains.url,
                       downloads.target_path, downloads.received_bytes,
                       downloads.total_bytes
                       FROM downloads, downloads_url_chains
                       WHERE downloads.id = downloads_url_chains.id
                       ORDER BY downloads.start_time DESC
''', history)

