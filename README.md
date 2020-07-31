# Twitter Scraper

Twitter's API is annoying to work with, and has lots of limitations —
luckily their frontend (JavaScript) has it's own API, which I reverse–engineered.
No API rate limits. No restrictions. Extremely fast.

# Usage

    from twitter_scraper_abad import get_tweets

    for tweet in get_tweets('fadlizon', pages=1):
         print(tweet['text'])

It appears you can ask for up to 25 pages of tweets reliably (~486 tweets) because it only could retrieve tweet in **last 7 days**.

---

# Installation

    $ git clone https://github.com/AhmadSubadri/twitter-scraper.git

Only Python 3.6+ is supported

# Example

How to use it? Check `main.py` file for example or `main.ipynb` if you are using jupyter notebook

# LICENSE

MIT
