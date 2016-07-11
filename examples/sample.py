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

############FORMAT############

    print 'My name is {0} and I am {1} years old'.format(name, age)
    print 'My name is {name} and I am {age} years old'.format(name=name, age=age)
    print 'My name is {} and I am {} years old'.format(name, age)
# decimal (.) precision of 3 for float '0.333'
    print('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
    print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
    print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

############FORMAT############

###########RAW STRING###########
    print(r'I\'m good \n How are you')
    print(R'I\'m good \n How are you')


"""
Note for Object Oriented Programming users:
    Python is strongly object-oriented in the sense that everything is an object
    including numbers, strings and functions.
"""
if __name__=='__main__':
    string_operations()
