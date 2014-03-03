from HashTable import HashTable
import collections
import logging

h = HashTable() 

def open_file(file):
    with open(file) as f:
        for w in f.read().split():
            h.add_to_table(w, 1)                   
    return h.hashtable

print open_file("random.txt")
print h.add_to_table("the", 10)
print h.get_value("the")


#Performance test functions -> Speed

def time(word):
    import time
    start = time.clock()
    h.get_value(word)
    return time.clock() - start
    
'''
#Non-collision lookup times ------> 

print time("the")
# --> 1.79999999972e-05 
print time("a")
# --> 4.99999999803e-06
print time("Muses")
# --> 0.002769
print time("Epilogue")
# --> 3.09999999999e-05
print time("Ship")
# --> 8.00000000112e-06
print time("James")
# --> 0.000803999999999
print time("Business")
# --> 9.99999999962e-06

#collided words lookup times ------>  
  
print time('Advice!')
# --> 0.001278
print time('Hussy')
# --> 0.003567
print time('Free-hearted')
# --> 0.004656
print time('Fly')
# --> 0.002304
print time('following')
# --> 0.000443000000001
print time('nought')
# --> 1.19999999981e-05
print time('Noble')
# --> 0.000702

'''
