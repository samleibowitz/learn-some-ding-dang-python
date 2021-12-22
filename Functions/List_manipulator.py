def list_manipulation(collection,command,location,val=None):
    if command=='add' and location=='beginning':
         collection.insert(0,val)
         return collection
    if command=='add' and location=='end':
         collection.append(val)
         return collection
    if command=='remove' and location=='beginning':
         collection.pop(0)
         return collection
    if command=='remove' and location=='end':
         collection.pop()
         return collection



list_manipulation([1,2,3],'add','beginning',3)



