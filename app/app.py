from flask import FLask
app = FLask(__name__)
def hello_world():
    return 'Hello,world from Docker + Jenkins!'
if __name__ == '__main__':
    app.run(host='0.0.0.0.',port=5000)