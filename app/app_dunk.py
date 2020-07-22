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

from brettwerk_bot.webhook import run_app_dunk

# Change The web-hook url with your own
webhook_url = "https://discordapp.com/api/webhooks/729952839379582997/tVvW77hGEAo1HrKegS2mWzlOXdCiqe2994w7i762NZnHD_iZPenHlq-gAI6NXE61SCpR"


if __name__ == "__main__":
    print("Bot Started...")
    run_app_dunk(webhook_url,
                 target_url='https://www.brettwerk.com/search?sSearch=dunk',
                 search_term="Dunk",
                 filter_tag="dunk ")
    print("Bot Stopped")
