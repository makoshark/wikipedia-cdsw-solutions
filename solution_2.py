# 2. Print out the revision ids and edit summaries (i.e., comment) of each revision for the article on Python.

import requests

# parameter version which makes a little more sense
parameters = {'action' : 'query',
              'prop' : 'revisions',
              'titles' : 'Python (programming language)',
              'rvlimit' : 100,
              # changed this line to add ids|comment
              'rvprop' : "ids|comment",
              'format' : 'json',
              'continue' : ''}

# run a "while True" loop
while True:
    wp_call = requests.get('https://en.wikipedia.org/w/api.php', params=parameters)
    response = wp_call.json()
    
    for page_id in response["query"]["pages"].keys():
        revisions = response["query"]["pages"][page_id]["revisions"]
        
        for rev in revisions:
            # changed this line to add revid and comment
            print(str(rev["revid"]) + "\t" + rev["comment"])

    if 'continue' in response:
        parameters.update(response['continue'])
    else:
        break
            
