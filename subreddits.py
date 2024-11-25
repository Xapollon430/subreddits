import webbrowser
import time

# List of subreddit names you want to visit.
subreddit_names = ['reactjs', 'webdev', 'swift', "node", "programming", "cscareerquestions", "gmu", "csmajors",
                   "tressless", "short", "smalldickproblems", "stoicism", "pornfree", "seduction", "dating_advice", "decidingtobebetter", "personalfinance",
                   "omad", "1500isplenty", "selfimprovement", "productivity", "PurplePillDebate", "loseit", "teslalounge", "minoxbeards"]

# Loop through each subreddit.
for subreddit_name in subreddit_names:
    # Construct the URL for the subreddit and add '/top/?t=week' to filter by top past week.
    subreddit_url = f'https://www.reddit.com/r/{subreddit_name}/top/?t=week'

    # Open the subreddit URL in your default web browser.
    webbrowser.open(subreddit_url, new=0, autoraise=True)

    # Sleep for a few seconds to allow the page to load (you can adjust the sleep duration).
