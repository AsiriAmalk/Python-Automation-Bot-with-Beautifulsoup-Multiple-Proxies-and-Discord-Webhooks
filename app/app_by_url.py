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

from brettwerk_bot.webhook import run_app_by_url

# Change The web-hook url with your own
webhook_url = "Your Discord webhook Url"
# Here is how to create a discord webhook
# https://medium.com/@asiriamalk/how-to-create-discord-webhook-and-test-using-postman-926a1f846aaf
# Change the item url
target_url = "https://www.brettwerk.com/detail/index/sArticle/2730/number/BV2078-002"

# Filter Tag
"""
If you need to filer that keyword includes, "Flip Flop" set filter_tag = "Flip Flop"
In default no filter have been applyied, So filter_tag = " "
"""
filter_tag = " "

if __name__ == "__main__":
    print("Bot Started...")
    run_app_by_url(webhook_url,
                   target_url=target_url,
                   filter_tag=filter_tag)
    print("Bot Stopped")
