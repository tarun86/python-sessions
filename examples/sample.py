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
    

#Strings Are Immutable .This means that once you have created a string, you cannot change it. Although this might seem like a bad thing, it really isn't. We will see why this is not a limitation in the various programs that we see later on



string_operations()
