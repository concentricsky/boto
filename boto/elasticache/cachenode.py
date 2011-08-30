
class CacheNode(object):
    def __init__(self, connection=None):
        self.connection = connection
        self._in_endpoint = False

    def __repr__(self):
        return 'CacheNode:%s' % self.id

    def startElement(self, name, attrs, connection):
        if name == 'Endpoint':
            self._in_endpoint = True
        return None

    def endElement(self, name, value, connection):
        if name == 'CacheNodeId':
            self.id = value
        elif name == 'CacheNodeCreateTime':
            self.create_time = value
        elif name == 'CacheNodeStatus':
            self.status = value
        elif name == 'ParameterGroupStatus':
            self.parameter_group_status = value
        elif name == 'Address':
            if self._in_endpoint:
                self._address = value
        elif name == 'Port':
            if self._in_endpoint:
                self._port = int(value)
        elif name == 'Endpoint':
            self.endpoint = (self._address, self._port)
            self._in_endpoint = False
        else:
            setattr(self, name, value)

