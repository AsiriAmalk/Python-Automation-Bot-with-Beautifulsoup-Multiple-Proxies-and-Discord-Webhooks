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

from brettwerk_bot.webhook import run_app_by_search

# Change The web-hook url with your own
webhook_url = "Your Discord webhook Url"
# Here is how to create a discord webhook
# https://medium.com/@asiriamalk/how-to-create-discord-webhook-and-test-using-postman-926a1f846aaf
# Change the item url
target_url = "https://www.brettwerk.com/detail/index/sArticle/2730/number/BV2078-002"

# Search Term
"""
This is the keyword that you need to use in search option in the brettwerk site and the results will be from the listed 
searches

In default it is Nike and change it according to your references
"""

# Filter Tag
"""
If you need to filer that keyword includes, "Flip Flop" set filter_tag = "Flip Flop"
In default filter is vision , So filter_tag = "Vision"
"""

"""
The notifications will be the searched Nike shoes with specific keyword include Vision
"""

search_term = "Nike"
filter_tag = "Vision"

if __name__ == "__main__":
    print("Bot Started...")
    run_app_by_search(webhook_url,
                      search_term=search_term,
                      filter_tag=filter_tag)
    print("Bot Stopped")
