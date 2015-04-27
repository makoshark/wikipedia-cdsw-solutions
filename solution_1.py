# 1. Save the revision metadata printed in wikipedia1-2.py to a file called "wikipedia_revisions.tsv".


import requests

# raw string:
# ?action=query&prop=revisions&titles=Python_(programming_language)&rvlimit=500&rvprop=timestamp|user&format=json')

# parameter version which makes a little more sense
parameters = {'action' : 'query',
              'prop' : 'revisions',
              'titles' : 'Python (programming language)',
              'rvlimit' : 500,
              'rvprop' : "timestamp|user",
              'format' : 'json',
              'continue' : ''}

output_file = open("wikipedia_revisions.tsv", 'w')

# run a "while True" loop
while True:
    wp_call = requests.get('https://en.wikipedia.org/w/api.php', params=parameters)
    response = wp_call.json()
    
    for page_id in response["query"]["pages"].keys():
        page_title = response["query"]["pages"][page_id]["title"]
        revisions = response["query"]["pages"][page_id]["revisions"]

        for rev in revisions:
            print(page_title + "\t" + rev["user"] + "\t" + rev["timestamp"], file=output_file)

    if 'continue' in response:
        parameters.update(response['continue'])
    else:
        break
            

output_file.close()
