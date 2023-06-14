import sys

import connectionController
# from assertions import *

def test1():
    orange =  {"name": "orange"}
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


# def test_insert_word1():
#     word = "house"
#     response = connectionController.http_post_qs("words",word)
#     print("response.text =")
#     print(response.text)
#     print("response.json() =")
#     print(response.json())
#     print("response.status_code =")
#     print(str(response.status_code))
#     sys.stdout.flush()
#     assert_valid_added_resource(response)
#     word_collection[response.json()] = "house"
#
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


