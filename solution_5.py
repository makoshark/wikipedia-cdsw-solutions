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

user_list = ['Peterl', 'Hfastedge']

counter_peterl = 0
counter_hfastedge = 0

# run a "while True" loop
while True:
    wp_call = requests.get('https://en.wikipedia.org/w/api.php', params=parameters)
    response = wp_call.json()
    
    for page_id in response["query"]["pages"].keys():
        revisions = response["query"]["pages"][page_id]["revisions"]
        
        for rev in revisions:
            if rev['user'] == "Peterl":
                counter_peterl = counter_peterl + 1
            if rev['user'] == "Hfastedge":
                counter_hfastedge = counter_hfastedge + 1

    if 'continue' in response:
        parameters.update(response['continue'])
    else:
        break
            

print("Peterl made %s edits" % counter_peterl)
print("Hfastedge made %s edits" % counter_hfastedge)
