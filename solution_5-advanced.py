# 5. Find out how many revisions to the article on "Python
# (programming language)" were made by user "Peterl"? How about
# "Hfastedge"?

import requests

# parameter version which makes a little more sense
parameters = {'action' : 'query',
              'prop' : 'revisions',
              'titles' : 'Python (programming language)',
              'rvlimit' : 500,
              'rvprop' : "ids|user",
              'format' : 'json',
              'continue' : ''}

user_counts = {}

# run a "while True" loop
while True:
    wp_call = requests.get('https://en.wikipedia.org/w/api.php', params=parameters)
    response = wp_call.json()
    
    for page_id in response["query"]["pages"].keys():
        revisions = response["query"]["pages"][page_id]["revisions"]
        
        for rev in revisions:
            current_user = rev['user']
            
            if current_user in user_counts:
                user_counts[current_user] = user_counts[current_user] + 1
            else:
                user_counts[current_user] = 1

    if 'continue' in response:
        parameters.update(response['continue'])
    else:
        break
            

# now that we've built up the dictionary, lets print it out
for editor in user_counts.keys():
    print("%s made %s edits" % (editor, user_counts[editor]))

