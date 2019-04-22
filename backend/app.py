from flask import Flask,json
import requests

app = Flask(__name__)

#routing to call  the specific url with integer id like "http://localhost:8006/api/pokemon/25"
@app.route('/api/pokemon/<id>')
def index(id):
 if ((int(id) >= 1) and( int(id)<= 151)):
  
     #initialising empty dict to store values of pokemon
     data={}
     data['pokemon']={}
     
     #storing the value of key 'id' in dict by extracting from route requested
     data['pokemon']['id']= int(id)
     
     #calling RESTFUL API by dynamically generating URL and converting the data into json format for easy access
     response = requests.get('https://pokeapi.co/api/v2/pokemon/{0}'.format(id)).json()
     
     #retrieving required values from json data stored in 'response' variable to store into pokemon dict
     data['pokemon']['name']=response['species']['name']
     data['pokemon']['sprite'] = response['sprites']['front_default']
     
     #json.dumps converts dict into string format and returns
     return json.dumps(data)
 else:
      return '<h1>The requested id is not valid. Please enter an id in between 1 and 151</h1>'  ,404
      
#To handle the case when id requested is not int i.e "api/pokenmon/unknown"
@app.errorhandler(ValueError)
def not_integer(error=None):
 return '<h1>The id provided must be of type int</h1>',500

# Error handling message when any other url with localhost:8006 is used
@app.errorhandler(404)
def file_not_found(error= None):
    return '<h1>The entered URL is not valid. Please enter a valid one.</h1>',404      


if __name__ == '__main__':
    app.run(host='localhost', port=8006, debug=True)
