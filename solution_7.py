# 7. Can you build a list of all of the articles edited by "Benjamin
# Mako Hill"? What is the article with the longest title that user
# Benjamin Mako Hill has edited?

# Step 1: Searching around on Google, I found this documentation which
# seemed like the right way to answer this question:
# https://www.mediawiki.org/wiki/API:Usercontribs

import requests

edited_pages = []

# parameter version which makes a little more sense
parameters = {'action' : 'query',
              'list' : 'usercontribs',
              'ucuser' : 'Benjamin Mako Hill',
              'uclimit' : 500,
              'ucprop' : 'title',
              'format' : 'json',
              'continue' : ''}

while True:
    wp_call = requests.get('https://en.wikipedia.org/w/api.php', params=parameters)
    response = wp_call.json()

    contribs = response['query']['usercontribs']
    
    for contrib in contribs:
        if contrib['title'] not in edited_pages:
            edited_pages.append(contrib['title'])

    # keep looping if we need to continue
    if 'continue' in response:
        parameters.update(response['continue'])
    else:
        break

# print out the list of pages
counter = 0
for page in edited_pages:
    counter = counter + 1
    print(page)

print("TOTAL PAGES: %s" % counter)
