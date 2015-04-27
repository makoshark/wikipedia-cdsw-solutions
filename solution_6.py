# 6. How would you use the API to find out how many revisions/edits the user "Benjamin Mako Hill" has made to Wikipedia?

# I found documentation here: https://www.mediawiki.org/wiki/API:Users

import requests

# parameter version which makes a little more sense
parameters = {'action' : 'query',
              'list' : 'users',
              'ususers' : 'Benjamin Mako Hill',
              'usprop' : 'editcount',
              'format' : 'json' }

wp_call = requests.get('https://en.wikipedia.org/w/api.php', params=parameters)
response = wp_call.json()

print(response['query']['users'][0]['editcount'])
