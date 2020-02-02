import json
from google.cloud import firestore
import pprint


def get_user(request):
    db = firestore.Client()

    docs = db.collection('user').get()
    users_list = []
    for doc in docs:
        users_list.append(doc.to_dict())
    return_json = json.dumps({"users": users_list}, ensure_ascii=False)

    return return_json


if __name__ == "__main__":
    request = {}
    r = get_user(request)
    pprint.pprint(r)
