from tinydb import TinyDB, Query

db=TinyDB('db.json')
todo= Query()
#db.insert({'todo': 'Learn Flask', 'status': 'started', 'priority': 'high'})

#returns everything in your database, array
#create
#read 
#update
#delete
# data=db.all()
# data= db.update({'todo':"make more money"}, doc_ids=[1])
# print(data)
# data1=db.update({'todo':"go to store"}, doc_ids=[9])

data= db.get(todo.priority== "high")
print(data)
# for todo in data:
#     print(todo)