import json
from google.cloud import firestore
import pprint


def get_filtered_user(request):

    request_json = request.get_json()
    if request.args and 'name' in request.args:
        request_name = request.args.get('name')
    elif request_json and 'name' in request_json:
        request_name = request_json['name']
    else:
        request_name = ''

    db = firestore.Client()

    query = db.collection('user').where('name', '==', request_name)
    docs = query.get()
    users_list = []
    for doc in docs:
        users_list.append(doc.to_dict())
    return_json = json.dumps({"users": users_list}, ensure_ascii=False)

    return return_json


if __name__ == "__main__":
    query = {}
    request = {}
    request = {"name": "Alice"}
    obj = DevRequest(query=query, params=request,method='POST')
    r = get_user(obj)
    pprint.pprint(r)
