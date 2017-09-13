# PlantAPI
**CRUD REST API for plants. You can add a plants to the database. Plants are added with the botanical name like so, "Genus species". **

All of the end points (except for register and auth) require JWT token authentication in the header: {"Authorization" : JWT}
Examples of http body and headers are underneath the description of the endpoint.
End points are as follows: 

POST /register : allows a user to register with a username and password

  headers: Content-Type: application/json
  {
  "username": "testacc",
  "password": "testpw"
  }

POST /auth : this endpoint will allow a registered user to authenticate and get a web token.

  headers: Content-Type: application/json
  {
  "username": "testacc",
  "password": "testpw"
  }

GET /plants : returns a JSON of all of the plants in the database.
  
  
GET /plant/<name> : retrieves a plant from the database by its name.

  headers: Autorization: JWT {{jwt_token}}

POST /plant/<name> : creates a plant in the database. use JSON format, must include "price", "genus_id", and "quantity".

  headers: Autorization: JWT {{jwt_token}}, Content-Type: application/json
  {
  "price": 15.99,
  "quantity": 10,
  "genus_id": "Chamaedorea"
  }  

PUT /plant/<name> : creates a plant if it doesn't exist, otherwise updates the plant with new values.

  headers: Autorization: JWT {{jwt_token}}, Content-Type: application/json
  {
  "price": 10.99,
  "quantity": 5,
  "genus_id": "Chamaedorea"
  }

DEL /plant/<name> : deletes a plant by its name.

GET /genus/<name> : retreives a list of plants under a specific genus in the database.

POST /genus/<name> : creates a genus in the database.
  
DEL /genus/<name> : deletes a genus by its name. Can cause problems with floating entries in the plants table. Must delete plants 
                    that are still attatched to the deleted genus in order to make proper table connections.
                    
GET /genera : retreieves a list of all genera and plants in the database linked to the genus.


