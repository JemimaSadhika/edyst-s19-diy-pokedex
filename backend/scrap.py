import json,requests

#function to collect data of all 151 pokemons
def scrappingToCollectData():
 id=1
 #list holds data of all pokemons in dict
 pokemonDetailsList=[]
 #loop to iterate through id values from 1 to 151

 while id <= venv151:
    data={}
    #storing required values in json format into dict
    data['id'] = id
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{0}'.format(id)).json()
    data['name']= response['species']['name']
    data['sprite'] =  response['sprites']['front_default']
    #adding that dict value into a list
    pokemonDetailsList.append(data)
    id=id+1

#writing the list of pokemon data into a file
 f= open("pokemondetails.json","w+") 
 json.dump(pokemonDetailsList,f) 
 f.close()

if __name__ == "__main__":
    scrappingToCollectData()


