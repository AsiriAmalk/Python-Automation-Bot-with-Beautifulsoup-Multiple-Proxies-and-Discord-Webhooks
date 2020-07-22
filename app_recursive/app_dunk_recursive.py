__author__ = "Asiri Amal"
__copyright__ = "Copyright 2020, Brettwerk Discord Bot Project"
__version__ = "1.0.1"
__maintainer__ = "Rob Knight"
__email__ = "asiri.15@cse.mrt.ac.lk"
__status__ = "Production"


import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from brettwerk_bot.webhook import run_app_dunk_recurrent

webhook_url = "https://discordapp.com/api/webhooks/729952839379582997/tVvW77hGEAo1HrKegS2mWzlOXdCiqe2994w7i762NZnHD_iZPenHlq-gAI6NXE61SCpR"

# Sleep Seconds
"""
Use desired time gap you need in default it runs 1 min, 
"""
sleep_seconds = 60

if __name__ == "__main__":
    run_app_dunk_recurrent(webhook_url,
                           target_url='https://www.brettwerk.com/search?sSearch=dunk',
                           search_term="Dunk",
                           filter_tag="dunk ",
                           sleep_seconds=sleep_seconds,
                           first_loop=True,
                           url_set=set(), )
