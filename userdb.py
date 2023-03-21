import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def enroll(db):
    #tempid = int(input('enter an id to create an entry:'))
    name = input('enter a name:')
    data = {'name':name,'tempid':tempid}
    db.collection('users ').add(data)

def delete_entry(db):
    id = int(input('enter an id to delete an entry:'))
    docs = db.collection('users ').where('tempid','==',id).get()
    for doc in docs:
        docid= doc.id
        print(docid)
        db.collection('users ').document(docid).delete()
def get_empname(db,empid):
    #id = int(input('enter a temp id:'))
    doc= db.collection(u'users ').where(u'tempid',u'==',empid).get()#returns list of dictionaries
    result=doc[0].to_dict()
    #print(result['name'])
    return result['name']
def get_rfid(db,rid):
    docs=db.collection(u'users ').where(u'rfid',u'==',rid).get()
    for doc in docs:
        if doc.exists:
            result=doc.to_dict()
            return  result['name']
        else:
            return False
def readdb(db):
    docs = db.collection('users ').stream()
    for doc in docs:
        print(doc.to_dict())
# Use a service account.
def initializeDB(path):
    cred = credentials.Certificate(path)
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db


# while True:
#     print('--------------------------------------------------------------')
#     print("1.search \t 2.enroll \t 3.delete \t 4.read db \t 5.exit")
#     choice = int(input('enter ur choice:'))
#     if choice==1:
#         search(db)
#     elif choice==2:
#         enroll(db)
#     elif choice==3:
#         delete_entry(db)
#     elif choice==4:
#         readdb(db)
#     elif choice == 5:
#         break
