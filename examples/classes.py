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

    def filter_dataframe(self, cols):
        self.group_by_obj.columns = cols
        self.data_frame = self.data_frame[~self.data_frame['car_id'].isin(self.group_by_obj[self.group_by_obj['count']>1]['car_id'].unique())]
        self.data_frame = self.data_frame[self.data_frame['days']>0]
        # print self.data_frame

    def group_by(self, cols):
        self.group_by_obj = self.data_frame.groupby(cols).size().reset_index()
        cols.append('count')
        self.filter_dataframe(cols=cols)

    def derived_features(self):
        lamdbafunc = lambda x: pd.Series([(x['days'] - x['date_interval']) / x['date_interval'],
                            (x['mileage'] - x['mileage_interval']) / x['mileage_interval'],
                            x['mileage'] / x['days']])
        self.data_frame[['days_normalise', 'mileage_normalise', 'avg_run_per_day']] = self.data_frame.apply(lamdbafunc, axis = 1)
        # x = self.data_frame.apply(lamdbafunc, axis = 1)


        # self.data_frame['days_normalise']= (self.data_frame['days'] - self.data_frame['date_interval']) / self.data_frame['date_interval']
        # self.data_frame['mileage_normalise']= (self.data_frame['mileage'] - self.data_frame['mileage_interval']) / self.data_frame['mileage_interval']
        # self.data_frame['avg_run_per_day']= self.data_frame['mileage'] / self.data_frame['days']


if __name__ == '__main__':
    try:
        data_analysis = customer_segmentation()
        data_analysis.read_csv('customer.csv')
        group_by_cols = ['car_id','service_type']
        data_analysis.group_by(group_by_cols)
        data_analysis.derived_features()
        print "hello world"
        # print data_analysis.group_by_obj
    except Exception() as err:
        print  err
