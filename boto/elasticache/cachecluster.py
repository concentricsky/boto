from boto.elasticache.cachenode import CacheNode
from boto.resultset import ResultSet

class CacheCluster(object):

    def __init__(self, connection=None, id=None):
        self.connection = connection
        self.id = id
        self.nodes = None

    def __repr__(self):
        return 'CacheCluster:%s' % self.id

    def startElement(self, name, attrs, connection):
        if name == 'CacheNodes':
            self.nodes = ResultSet([('CacheNode', CacheNode)])
            return self.nodes
        return None

    def endElement(self, name, value, connection):
        if name == 'CacheClusterId':
            self.id = value
        elif name == 'CacheClusterStatus':
            self.status = value
        elif name == 'CacheClusterCreateTime':
            self.create_time = value
        elif name == 'Engine':
            self.engine = value
        elif name == 'EngineVersion':
            self.engine_version = value
        elif name == 'PreferredAvailabilityZone':
            self.preferred_availability_zone = value
        elif name == 'CacheNodeType':
            self.node_type = value
        elif name == 'PreferredMaintenanceWindow':
            self.preferred_maintenance_window = value
        elif name == 'NumCacheNodes':
            self.num_cache_nodes = value
        elif name == 'Address':
            self.address = value
        elif name == 'Port':
            self.port = value
        else:
            setattr(self, name, value)
