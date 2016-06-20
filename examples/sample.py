import pandas

### Strings & Python ###
def string_operations():
###Triple Quotes###
    print '''Hello world, 
    How are you doing,
    Good Bye'''
###Double Quotes###
    print "Hello World"
###Single Quotes###
    print 'Hello World'
    name='Tarun'
    age=30
    print 'My name is {0} and I am {1} years old'.format(name, age)
    print 'My name is {name} and I am {age} years old'.format(name=name, age=age)
    
string_operations()
