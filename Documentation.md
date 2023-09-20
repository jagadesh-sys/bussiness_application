##  FastAPI Business API
## This is a simple RESTful API built with FastAPI for managing information about businesses. It allows you to perform basic CRUD (Create, Read, Update, Delete) operations on business entities.

##  Business Model
    The API uses a Business model defined using Pydantic to represent business entities. Each business has the following attributes:
    
    name (str): The name of the business.
    address (str): The address of the business.
    owner_name (str): The name of the owner of the business.
    employee_size (int): The size of the employee workforce at the business.

##  Endpoints
##  1. Create a Business
    HTTP Method: POST
    Endpoint: /businesses
    Request Body: JSON data representing a Business object.
    Description: This endpoint allows you to create a new business by providing its details in the request body. It returns the created business as a response.
##  2. Get All Businesses
HTTP Method: GET
Endpoint: /businesses
Description: This endpoint retrieves a list of all businesses currently stored in the API. It returns a JSON array containing information about each business.
3. Update a Business
HTTP Method: PUT
Endpoint: /businesses/{business_id}
Path Parameter: business_id (int) - The unique identifier of the business to update.
Request Body: JSON data representing a Business object.
Description: This endpoint allows you to update the details of a specific business identified by its business_id. It returns the updated business as a response.
4. Delete a Business
HTTP Method: DELETE
Endpoint: /businesses/{business_id}
Path Parameter: business_id (int) - The unique identifier of the business to delete.
Description: This endpoint allows you to delete a specific business identified by its business_id. It returns a simple message indicating that the business has been deleted.
5. Search for Businesses by Name
HTTP Method: GET
Endpoint: /businesses/search
Query Parameter: name (str) - The name of the business to search for.
Description: This endpoint allows you to search for businesses by their names, performing a case-insensitive search. It returns a JSON array containing matching businesses.
Sample Data
The API includes sample data for three businesses: SoftBank, Apple, and Microsoft. You can use these businesses as examples or add more businesses to the businesses list in the code.

Running the API
To run the API, you can uncomment the line uvicorn.run(app) at the end of the code. This will start the FastAPI application, and you can access the API at the specified endpoints.

Please note that this code is a basic example and does not include error handling, data persistence, or authentication. In a production application, you would typically implement these features to make the API more robust and secure.