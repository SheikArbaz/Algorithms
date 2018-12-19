import collections
dict1 = {'b':21,'a':31}
dict2 = {'c':1,'d':2}

ch_map = collections.ChainMap(dict1, dict2)

print(list(ch_map.keys()))

#If we change the order the dictionaries while clubbing them in the above example we see that the position of the elements get interchanged as if they are in a continuous chain.
#This again shows the behaviour of Maps as stacks. 

#If there are duplicate keys, then only the value from the first key is preserved. 
