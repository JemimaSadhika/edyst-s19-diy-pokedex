from flask import Flask,json
import requests

app = Flask(__name__)

#routing to call  the specific url is http://localhost:8006/api/pokemon/id where id range 1 to 151
@app.route('/api/pokemon/<int:id>')
def specificIdData(id):
    #list to hold retrieved file data
    loadedFileData = []

    #checking and retrieves data for id in between 1 and 151
    if (id >= 1) and  (id<=151):
    	#dict to hold json data
	    data = {}
		#opening and retrieving all data in the file
	    with open('pokemondetails.json') as fileData: 
		    loadedFileData = json.load(fileData)
			#extracting specific id information from the list
		    data['pokemon'] = loadedFileData[id-1] 
		    #converts the dictionary into string format while returning data as dict cannot be directly displayed
		    return json.dumps(data)

    #when id is not in specific range error is displayed with 404 status code		   
    else:
      return '<h1>The requested id is not valid. Please enter an id in between 1 and 151</h1>'  ,404
      


# Error handling message when any other url with localhost:8006 is used or id is not of type integer
@app.errorhandler(404)
def file_not_found(error= None):
   return '<h1>The entered URL is not valid. Please enter a valid one.</h1>',404      


if __name__ == '__main__':
    app.run(host='localhost', port=8006, debug=True)

    
