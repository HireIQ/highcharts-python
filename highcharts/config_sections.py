'''Config sections for a chart.'''
import options
from common import *


class ChartConfig(ConfigSection):
    '''
    The 'chart' section of a Highcharts config.

    See http://www.highcharts.com/ref/#chart for available options.
    '''
    available_options = options.CHART_CONFIG


class TitleConfig(ConfigSection):
    '''
    The 'title' section of a Highcharts config.

    See http://www.highcharts.com/ref/#title for available options.
    '''
    available_options = options.TITLE_CONFIG


class SubtitleConfig(ConfigSection):
    '''
    The 'subtitle' section of a Highcharts config.

    See http://www.highcharts.com/ref/#title for available options.
    '''
    available_options = options.SUBTITLE_CONFIG


class LegendConfig(ConfigSection):
    '''
    The 'legend' section of a Highcharts config.

    See http://www.highcharts.com/ref/#legend for available options.
    '''
    available_options = options.LEGEND_CONFIG


class TooltipConfig(ConfigSection):
    '''
    The 'tooltip' section of a Highcharts config.

    See http://www.highcharts.com/ref/#tooltip for available options.
    '''
    available_options = options.TOOLTIP_CONFIG


class XAxisConfig(ConfigSection):
    '''
    The 'xAxis' section of a Highcharts config.

    See http://www.highcharts.com/ref/#xAxis for available options.
    '''
    available_options = options.X_AXIS_CONFIG


class YAxisConfig(ConfigSection):
    '''
    The 'yAxis' section of a Highcharts config.

    See http://www.highcharts.com/ref/#yAxis for available options.
    '''
    available_options = options.Y_AXIS_CONFIG
