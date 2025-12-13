from flask import Flask
from redis import Redis

app = Flask(__name__)
# Connect to the container named 'redis'
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    # Increment the counter in the database
    count = redis.incr('hits')
    return f'<h1>Hello Docker!</h1> <p>This page has been viewed {count} times.</p>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)