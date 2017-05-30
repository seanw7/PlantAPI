# PlantAPI
CRUD REST API for plants. You can create plants with attatched genera names. 

All of the end points require JWT token authentication in the header: {"Authorization" : JWT}

End points are as follows:

POST /register : allows a user to register with a username and password

POST /auth : this endpoint will allow a registered user to authenticate and get a web token.

GET /plants : returns a JSON of all of the plants in the database.

GET /plant/<name> : retrieves a plant from the database by its name.

POST /plant/<name> : creates a plant in the database. use JSON format, must include "price", "genus_id", and "quantity".

PUT /plant/<name> : creates a plant if it doesn't exist, otherwise updates the plant with new values.

DEL /plant/<name> : deletes a plant by its name.

GET /genus/<name> : retreives a list of plants under a specific genus in the database.

POST /genus/<name> : creates a genus in the database.

DEL /genus/<name> : deletes a genus by its name.

GET /genera : retreieves a list of all genera and plants in the database linked to the genus.
