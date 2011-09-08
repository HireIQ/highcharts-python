import encoders
import options


class HighchartError(Exception):
    '''Base class for errors in the highchart package.'''


class DictBacked(object):
    '''
    A class that stores it's attributes in a dictionary
    and json encodes to the value of that dictionary.
    '''
    defaults = {}
    available_options = []

    def __init__(self, **kwargs):
        self.options = {}

        for key, value in self.defaults.items():
            # If it is a ConfigSection, we instantiate it.
            if hasattr(value, '__bases__') and ConfigSection in value.__bases__:
                value = value()
            self.options[key] = value

        for key, value in kwargs.items():
            if key in self.available_options:
                self.options[key] = value
            else:
                raise AttributeError('Invalid option %s' % key)

    def __setattr__(self, attr, val):
        if attr in self.available_options:
            if val == None:
                del self.options[attr]
            else:
                self.options[attr] = val
        else:
            super(DictBacked, self).__setattr__(attr, val)

    def __getattr__(self, attr):
        if attr in self.available_options:
            return self.__dict__['options'].get(attr, None)
        else:
            raise AttributeError

    def as_json(self):
        return self.options


class ConfigSection(DictBacked):
    '''Just a marker to specifiy that an object in a defaults list should be instantiated.'''


class ChartConfig(ConfigSection):
    '''
    The 'chart' section of a Highcharts config.

    See http://www.highcharts.com/ref/#chart for available options.
    '''
    available_options = options.CHART_CONFIG


class Chart(DictBacked):
    '''
    The base config for a highcharts chart.

    See http://www.highcharts.com/ref/ for available options.
    '''
    available_options = options.CHART
    defaults = {
        "series": [],
        "chart": ChartConfig
    }

    def add_series(self, series):
        self.series.append(series)

    def __str__(self):
        return encoders.dump_json(self)


class Point(DictBacked):
    '''
    A specific data point in a series.

    Points can be defined as Point objects, numbers, or (x, y) pairs of numbers.
    See http://www.highcharts.com/ref/#point for available options.
    '''
    available_options = options.POINT


class Series(DictBacked):
    '''
    The base class for any series type.

    See http://www.highcharts.com/ref/#plotOptions-series for available options.
    '''
    def __init__(self, **kwargs):
        self.defaults = {
            "type": self.series_type
        }
        self.available_options += options.SERIES
        super(Series, self).__init__(**kwargs)


class Line(Series):
    '''
    A line chart series.

    See http://www.highcharts.com/ref/#plotOptions-line for available options.
    '''
    series_type = 'line'
    available_options = options.LINE
