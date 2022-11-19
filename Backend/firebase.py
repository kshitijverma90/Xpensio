import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd 
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db=firestore.client()
# for i in range(2,10):
#     db.collection("email1").document("transaction"+str(i)).set({"Date":"12/11/22","To":"Dunzo"+str(i),"Amount":1200+i})
def solve():
    date=[]
    amount=[]
    category=[]
    to=[]
    docs=db.collection('email1').get()
    for doc in docs:
        d=list(doc.to_dict().values())
        date.append(d[1])
        amount.append(d[2])
        to.append(d[0])
    
    dict= {'Date': date, 'amount': amount,'TO':to}    
    return dict    
# df = pd.DataFrame(dict) 
# df.to_csv('dataset.csv')


