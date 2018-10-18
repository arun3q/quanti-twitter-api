# quanti-twitter-api
To Develop a Restful webservice which should be able to analyze twitter content for given
twitter handle.



### http://ip:port/twitter/follower?twitterhandle={input}
```This GET request will take a twitter handle (i.e., netflix) and return the response in JSON format
with total number of followers for the given twitter handle.
```

### http://ip:port/twitter/following?twitterhandle={input}
```This GET request will take a twitter handle (i.e., netflix) and return the response
in JSON format with total number of twitter account the given twitter handle is following.
```

### http://ip:port/twitter/toptweets?twitterhandle={input}
```
This GET request will take a twitter handle (i.e., netflix) and return the response
in JSON format with top 10 tweets of the given twitter handle.
```

### Prerequisites

```
You will need to install dependencies given in requirements.txt file.
```
```
1. First create a virtual environment
    virtualenv djangoenv -p python3

2. activate the virtual environment
    source djangoenv/bin/activate            linux os
```
```
2. Then install the modules in requirements.txt
pip install -r requirements.txt
```

After that you can simply run using ```python manage.py runserver```. This will start your django rest api on your localhost.

```
You can run ``` python manage.py populate_data ``` to populate the database with data from twitter but for that you will have
make changes into the populate_data.py file and use twitter API keys.
```


### This app is up and running on https://quant-twitter-api.herokuapp.com
