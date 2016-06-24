#Here comes an array with Strings, Integers, Floats and Characters
friends = ['John','Beth','Gary','Saul', 123, 123.45, 'A']
for i, name in enumerate(friends):
    print ("Position {itr} is {name}".format(itr=i, name=name))