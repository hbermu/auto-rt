# Auto-rt

Basic auto-retwee application using Python and Tweepy 

To run this sample code, you'll need to install the following python libraries:

- Tweepy 3.2.0: [https://github.com/tweepy/tweepy](https://github.com/tweepy/tweepy) 

## Run in Docker
---
Need build and run:  
docker build -t auto-rt .  
docker run -d --name delegacion-rt auto-rt:latest

If you want to change configuration without build:  
docker run -d --name delegacion-rt -v "pathTo_twitter.conf:/usr/src/app/twitter.conf" auto-rt:latest

Repo in https://hub.docker.com/r/hbermu/auto-rt/


## Getting Started
---
Create a [Twitter App](https://apps.twitter.com/).

Specify your Twitter App keys and tokens in a new config file named twitter.conf  
There is a sample config file named twitter.conf.sample:

```
[apikey]
key = your_api_key
secret = your_api_secret

[token]
token = your_access_token
secret = your_access_secret

[accounts]
accounts = @test,@test2,...

```

Install dependencies:

```
pip install tweepy==3.2.0
```

Run the python script in the project directory:

```
python2.7 auto-rt.py
```

Notes
-----


[The Twitter Rules](https://support.twitter.com/articles/18311-the-twitter-rules)<br/>
[Automation Rules & Best Practices](https://support.twitter.com/articles/76915)<br/>
[API Rate Limiting](https://dev.twitter.com/rest/public/rate-limits)
