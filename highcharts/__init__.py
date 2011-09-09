import encoders
import options
from common import *
from config_sections import *


class Chart(DictBacked):
    '''
    The base config for a highcharts chart.

    See http://www.highcharts.com/ref/ for available options.
    '''
    available_options = options.CHART
    defaults = {
        "series": [],
        "chart": ChartConfig,
        "title": TitleConfig,
        "subtitle": SubtitleConfig,
        "legend": LegendConfig,
        "tooltip": TooltipConfig,
        "xAxis": XAxisConfig,
        "yAxis": YAxisConfig
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

    def __init__(self, data=None, **kwargs):
        super(Point, self).__init__(**kwargs)
        if data == None:
            return
        if isinstance(data, (list, tuple)) and len(data) == 2:
            self.x = data[0]
            self.y = data[1]
        else:
            self.y = data
