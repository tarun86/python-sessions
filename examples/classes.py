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

    def dataframe_preprocessing(self, cols):
        self.group_by_obj.columns = cols
        self.data_frame = self.data_frame[~self.data_frame['car_id'].isin(self.group_by_obj[self.group_by_obj['count']>1]['car_id'].unique())]
        self.data_frame = self.data_frame.ix[self.data_frame.days > 0]
        self.data_frame = self.data_frame.ix[self.data_frame.mileage > 0]
        # print self.data_frame

    def group_by(self, cols):
        self.group_by_obj = self.data_frame.groupby(cols).size().reset_index()
        cols.append('count')
        self.dataframe_preprocessing(cols=cols)

    def derived_features(self):
        lamdbafunc = lambda x: pd.Series([(x['days'] - x['date_interval']) / x['date_interval'],
                            (x['mileage'] - x['mileage_interval']) / x['mileage_interval'],
                            x['mileage'] / x['days']])
        self.data_frame[['days_normalise', 'mileage_normalise', 'avg_run_per_day']] = self.data_frame.apply(lamdbafunc, axis = 1)
        # x = self.data_frame.apply(lamdbafunc, axis = 1)
        # self.data_frame['days_normalise']= (self.data_frame['days'] - self.data_frame['date_interval']) / self.data_frame['date_interval']
        # self.data_frame['mileage_normalise']= (self.data_frame['mileage'] - self.data_frame['mileage_interval']) / self.data_frame['mileage_interval']
        # self.data_frame['avg_run_per_day']= self.data_frame['mileage'] / self.data_frame['days']

    def get_typeof_service(self, service):
        return self.data_frame [self.data_frame['service_type'] == service]
        # customer_fr2 = self.data_frame.ix[self.data_frame['service_type']=='FR2',:]

    def quantile_filtering(self, obj, low = 0.025, high = 0.975, keys = ['days', 'mileage']):
        print "SHape of the object : {}".format(obj.shape)
        for key in keys:
            obj = obj[obj[key] > obj[key].quantile(low)]
            obj = obj[obj[key] < obj[key].quantile(high)]
        print "SHape of the object : {}".format(obj.shape)

    def set_typeof_service(self, service, index="car_id"):
        if(service == "FR1"):
            self.customer_fr1 = self.get_typeof_service(service)
            self.customer_fr1 = self.customer_fr1.set_index(index)

        if(service == "FR2"):
            self.customer_fr2 = self.get_typeof_service(service)
            self.customer_fr2 = self.customer_fr2.set_index(index)

        if(service == "FR3"):
            self.customer_fr3 = self.get_typeof_service(service)
            self.customer_fr3 = self.customer_f3.set_index(index)
def main():
    try:
        data_analysis = customer_segmentation()
        data_analysis.read_csv('customer.csv')
        group_by_cols = ['car_id','service_type']
        data_analysis.group_by(group_by_cols)
        data_analysis.derived_features()
        data_analysis.set_typeof_service('FR1')
        data_analysis.set_typeof_service('FR2')
        data_analysis.quantile_filtering(data_analysis.customer_fr1)
        print "hello world"
        return data_analysis
        # print data_analysis.group_by_obj
    except Exception() as err:
        print  err

if __name__ == '__main__':
    main()
    # try:
    #     data_analysis = customer_segmentation()
    #     data_analysis.read_csv('customer.csv')
    #     group_by_cols = ['car_id','service_type']
    #     data_analysis.group_by(group_by_cols)
    #     data_analysis.derived_features()
    #     print "hello world"
    #     # print data_analysis.group_by_obj
    # except Exception() as err:
    #     print  err
