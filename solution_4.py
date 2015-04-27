# 4. Which article is in more categories? Python (programming language) or R (programming language)? 

import requests

article_list = ["Python (programming language)", "R (programming language)"]
 
for article in article_list:
    # Get the list of categories
    parameters = {'action' : 'query',
                  'titles' : article,
                  'prop' : 'categories',
                  'format' : 'json',
                  'continue' :  ''}

    # reset the counter to zero once per article
    counter = 0
    
    # run a "while True" loop
    while True:
        wp_call = requests.get('https://en.wikipedia.org/w/api.php', params=parameters)
        response = wp_call.json()

        for page_id in response["query"]["pages"].keys():
            for category in response["query"]["pages"][page_id]['categories']:
                counter = counter + 1

        if 'continue' in response:
            parameters.update(response['continue'])
        else:
            break

    output_line = "%s: %s categories" % (article, counter)
    print(output_line)
