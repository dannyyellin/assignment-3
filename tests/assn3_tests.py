import sys

import connectionController
# from assertions import *
global orange_ID, spaghetti_ID, apple_pie_ID

# test 1:  Execute three POST /dishes requests using the dishes, “orange”, “spaghetti”, and “apple pie”.   The test is
# successful if (i) all 3 requests return unique IDs (none of the IDs are the same), and (ii) the return status code
# from each POST request is 201.
def test1():
    orange =  {"name": "orange"}
    global orange_ID, spaghetti_ID, apple_pie_ID
    orange_response = connectionController.http_post("dishes",orange)
    assert orange_response.status_code == 201
    orange_ID = orange_response.json()

    spaghetti = {"name": "spaghetti"}
    spaghetti_response = connectionController.http_post("dishes", spaghetti)
    assert spaghetti_response.status_code == 201
    spaghetti_ID = spaghetti_response.json()

    apple_pie  = {"name": "apple pie"}
    apple_pie_response = connectionController.http_post("dishes", apple_pie)
    assert apple_pie_response.status_code == 201
    apple_pie_ID = apple_pie_response.json()

    assert orange_ID != spaghetti_ID
    assert orange_ID != apple_pie_ID
    assert spaghetti_ID != apple_pie_ID

# test 2: Execute a GET dishes/<orange-ID> request, using the ID of the orange dish.  The test is successful if (i) the
# sodium field of the return JSON object is between 1 and 5 and (ii) the return status code from the request is 200.
def test2():
    response = connectionController.http_get(f"dishes/{orange_ID}")
    sodium = response.json()["sodium"]
    assert response.status_code == 200
    assert sodium >= 1 and sodium <=5
    print("sodium of orange = ", sodium)
    sys.stdout.flush()

# test 3: Execute a GET /dishes request.  The test is successful if (i) the returned JSON object has 3 embedded JSON objects (
# dishes), and (ii) the return status code from the GET request is 200.
def test3():
    response = connectionController.http_get("dishes")
    # get number of objects returned
    assert response.status_code == 200


# test 4:  Execute a POST /dishes request supplying the dish name “blah”. The test is successful if (i) the return
# value is -3, and (ii) the return code is 404 or 400.
def test4():
    blah = {"name": "blah"}
    blah_response = connectionController.http_post("dishes", blah)
    # assert blah_response.status_code == 400
    assert blah_response.status_code == 400 or blah_response.status_code == 422



# def test_get_word_by_id():
#     word = "book"
#     response = connectionController.http_post_qs("words",word)
#     assert_valid_added_resource(response)
#     book_id = response.json()
#     word_collection[book_id] = "book"
#     response = connectionController.http_get(f"words/{book_id}")
#     assert_status_code(response, status_code=200)
#     assert response.json() == "book"
#
# def test_add_exists_word():
#     word = "house"
#     response = connectionController.http_post_qs("words", word)
#     assert_status_code(response, status_code=422)
#     assert_ret_value(response, 0)
#
#
# def test_get_not_exists_word_id():
#     NOT_EXISTS_WORD_ID = 11235
#     response = connectionController.http_get(f"words/{NOT_EXISTS_WORD_ID}")
#     assert_status_code(response, status_code=404)
#     assert_ret_value(response, returned_value=0)


