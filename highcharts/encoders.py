import datetime, time
try:
    import simplejson as json
except ImportError:
    import json


class ObjectEncoder(json.JSONEncoder):
    '''
    Encode any object with the method as_json on it.
    '''
    def default(self, obj):
        if hasattr(obj, 'as_json'):
            return obj.as_json()
        elif isinstance(obj, (datetime.date, datetime.datetime)):
            return time.mktime(obj.timetuple()) * 1000
        else:
            return super(ObjectEncoder, self).default(obj)


def dump_json(chart):
    '''Dumps a chart to json'''
    return json.dumps(chart, cls=ObjectEncoder)
