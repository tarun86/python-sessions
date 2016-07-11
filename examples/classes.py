'''
Importing modules for the class
'''
import pandas as pd
import numpy as np
from jenks import jenks

'''
This is the samples for the python classes
'''

class customer_segmentation():
    '''
    Definition: Customer segmentation for the FREE type of process
    based on days or mileage pattern
    '''

    def read_csv(self, name):
        '''
        :param name: name of the file
        :return: set the data in data_frame attribute
        '''
        try:
            self.data_frame = pd.read_csv(name)
        except IOError as err:
            print "IOError : {}".format(err)

    def __init__(self):
        '''
        :return:
        '''

    def group_by(self, cols):
        self.group_by_obj = self.data_frame.groupby(cols)


if __name__ == '__main__':
    try:
        data_analysis = customer_segmentation()
        data_analysis.read_csv('customer.csv')
        print data_analysis.data_frame.head()
        group_by_cols = ['car_id','service_type']
        data_analysis.group_by(group_by_cols)
        print data_analysis.group_by_obj.

    except:
        print  "something went wrong"