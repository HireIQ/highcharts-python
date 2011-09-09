'''
The different types of series that can be charted.
'''
import options
from common import *


class Series(DictBacked):
    '''
    The base class for any series type.

    See http://www.highcharts.com/ref/#plotOptions-series for available options.
    '''
    def __init__(self, data=[], **kwargs):
        self.defaults = {
            "type": self.series_type
        }
        self.available_options += options.SERIES
        super(Series, self).__init__(**kwargs)
        self.data = data


class LineSeries(Series):
    '''
    A line chart series.

    See http://www.highcharts.com/ref/#plotOptions-line for available options.
    '''
    series_type = 'line'
    available_options = ['step']


class PieSeries(Series):
    '''
    A pie chart series.

    See http://www.highcharts.com/ref/#plotOptions-pie for available options.
    '''
    series_type = 'pie'
    available_options = ['size', 'slicedOffset', 'center']
