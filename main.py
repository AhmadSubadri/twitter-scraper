from twitter_scraper_abad import get_tweets

data = []
error = 0
for t in get_tweets('objek', pages=1):
    data.append(t)
    if (t['status'] != 'ok'):
        error += 1
    
print('tweet found: ', len(data))
print('error: ', error)

for i, t in enumerate(data):
    print(t['tweet']['text'], '\n')