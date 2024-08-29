from google.cloud import firestore
from ..userrepository import UserRepository

class FirestoreUserRepository(UserRepository):
    def __init__(self):
        self.db = firestore.Client()

    def get_user(self, id):
        doc_ref = self.db.collection('users').document(id)
        doc = doc_ref.get()
        if doc.exists:
            return User(doc.id, doc.to_dict()['name'], doc.to_dict()['email'])
        else:
            return None
