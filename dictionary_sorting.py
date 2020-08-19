from collections import OrderedDict

dict = {'avi':10,'ranjan':9,'pri':15,'yash':2,'bunny':32}

#sorting by keys
d = OrderedDict(sorted(dict.items()))
print(d)
#OrderedDict([('avi', 10), ('bunny', 32), ('pri', 15), ('ranjan', 9), ('yash', 2)])

#sorting by values
print(sorted(dict.items(),key = lambda x:(x[1],x[0])))

#[('yash', 2), ('ranjan', 9), ('avi', 10), ('pri', 15), ('bunny', 32)]
