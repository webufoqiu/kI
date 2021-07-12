import pickle
some_list = [i for i in range(100)]

with open('some_file','wb') as f:
    pickle.dump(some_list,f)



with open('some_file','rb') as g:
    object = pickle.load(g)

print(object)