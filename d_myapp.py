from flask import Flask, render_template, Markup
import tweepy


app = Flask(__name__)
"""
@app.route('/')
def foo(name='Dennis')
	return render_template('d_myapp.html', to=name)
"""


@app.route('/')

def foo2():
	
	
	auth = tweepy.OAuthHandler('2UNx8WnQE85eFjTOT6a9rri3P', 'EXihRlowpD2CC002wJNS3GVAxBejGAGLsC7HrRxgpg3x1EButM')
	auth.set_access_token('321359097-EkhoEOXfkEJRUch4fqzp7Nnmgc4SJcpAImKpmSou', 'g6Clf0q4BfMZemgr0jKcpjNLWMtPaw71pYXTAb5ZowJY3')
	
	api = tweepy.API(auth)
	
	public_tweets = api.home_timeline()
	tweet_list= ""
	
	for tweet in public_tweets:
    		tweet_list += Markup("<br>") + tweet_list + tweet.text + Markup("</br>")
		

	

	

	return render_template('d_myapp.html', to=tweet_list)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

