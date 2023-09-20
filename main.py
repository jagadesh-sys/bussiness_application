from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class Business(BaseModel):
    name: str
    address: str
    owner_name: str
    employee_size: int


app = FastAPI()


@app.post("/businesses")
def create_business(business: Business):
    #Create a new business
    businesses.append(business)
    return businesses


@app.get("/businesses")
def get_businesses():
    #Get all businesses
    return [business for business in businesses]


@app.put("/businesses/{business_id}")
def update_business(business_id: int, business: Business):
    #Update a business
    businesses[business_id] = business
    return business


@app.delete("/businesses/{business_id}")
def delete_business(business_name: int):
    #Delete a business
    business_name
    businesses.pop(business_name)
    businesses = list(filter(lambda i: i['name'] != business_name, businesses))
    return "Business deleted"


@app.get("/businesses/search")
def search_businesses(name: str):
    #Search for businesses by name
    return [business for business in businesses if business.name.lower() == name.lower()]


if __name__ == "__main__":
    businesses = [
        Business(name="SoftBank", address="100 California Street, San Francisco, CA 94111", owner_name="Masayoshi Son", employee_size=50000),
        Business(name="Apple", address="1 Infinite Loop, Cupertino, CA 95014", owner_name="Tim Cook", employee_size=154000),
        Business(name="Microsoft", address="One Microsoft Way, Redmond, WA 98052", owner_name="Satya Nadella", employee_size=181000),
        ]
    uvicorn.run(app)

