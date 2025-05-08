from flask import Flask
import redis
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

r = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    r.set('message', 'Hello from Redis!')
    redis_message = r.get('message').decode('utf-8')

    app.logger.info('Main page accessed')

    return f'Flask is working! Redis says: {redis_message}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
