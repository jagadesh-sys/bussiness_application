import requests

# @pytest.mark.parametrize("name, address, owner_name, employee_size", [
#     ("Google", "1600 Amphitheatre Parkway, Mountain View, CA 94043", "Sundar Pichai", 155000),
#     ("Amazon", "410 Terry Ave N, Seattle, WA 98109", "Jeff Bezos", 1600000),
#     ("Apple", "1 Infinite Loop, Cupertino, CA 95014", "Tim Cook", 154000),
# ])
def test_create_business(name, address, owner_name, employee_size):
    response = requests.post("http://localhost:8000/businesses", json={
        "name": name,
        "address": address,
        "owner_name": owner_name,
        "employee_size": employee_size,
    })
    assert response.status_code == 200
    assert response.json()["name"] == name
    assert response.json()["address"] == address
    assert response.json()["owner_name"] == owner_name
    assert response.json()["employee_size"] == employee_size


def test_update_business():
    response = requests.put("http://localhost:8000/businesses/2", json={
        "name": "Google",
        "address": "1600 Amphitheatre Parkway, Mountain View, CA 94043",
        "owner_name": "Sundar Pichai",
        "employee_size": 156000
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Google"
    assert response.json()["address"] == "1600 Amphitheatre Parkway, Mountain View, CA 94043"
    assert response.json()["owner_name"] == "Sundar Pichai"
    assert response.json()["employee_size"] == 156000


def test_delete_business():
    response = requests.delete("http://localhost:8000/businesses/1")
    assert response.status_code == 200


def test_search_businesses():
    response = requests.get("http://localhost:8000/businesses/search?name=Apple")
    assert response.status_code == 200
    assert response.json()[0]["name"] == "Apple", "data not available"
    return "Passed"


def test_invalid_request_body():
    response = requests.post("http://localhost:8000/businesses", json={
        "name": "Google",
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Missing required field: address"

def test_unsupported_method():
    response = requests.get("http://localhost:8000/businesses/1")
    assert response.status_code == 405
    assert response.json()["detail"] == "Method Not Allowed"

if __name__ == "__main__":

    # print(test_create_business("Google", "1600 Amphitheatre Parkway, Mountain View, CA 94043", "Sundar Pichai", 155000))
    print(test_search_businesses())
    # print(test_update_business())
    # print(test_delete_business())
    # print(test_invalid_request_body())
    # print(test_unsupported_method())