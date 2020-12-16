from flask import Flask, render_template, jsonify, request
import pusher
import json


app = Flask(__name__)

pusher_client = pusher.Pusher(
  app_id='1106312',
  key='d1aacd6ddbe4dae09f34',
  secret='cd9aece6afcff03ea515',
  cluster='ap2',
  ssl=True
)

@app.route('/')
def index():
   return render_template('index.html', name = 'Sylvia')

@app.route('/paint',methods=['POST', 'GET'])
def paint():
   print(request.data)
   data = json.loads(request.data)
   pusher_client.trigger('painting', 'draw', data)
   


if __name__ == '__main__':
   app.run(debug = True)