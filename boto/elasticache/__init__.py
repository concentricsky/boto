
from boto.connection import AWSQueryConnection
from boto.regioninfo import RegionInfo
from boto.elasticache.cachecluster import CacheCluster


class ElasticacheConnection(AWSQueryConnection):

    DefaultRegionName = 'us-east-1'
    DefaultRegionEndpoint = 'elasticache.us-east-1.amazonaws.com'
    APIVersion = '2011-07-15'

    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None,
                 is_secure=True, port=None, proxy=None, proxy_port=None,
                 proxy_user=None, proxy_pass=None, debug=0,
                 https_connection_factory=None, region=None, path='/'):
        if not region:
            region = RegionInfo(self, self.DefaultRegionName,
                                   self.DefaultRegionEndpoint)
        self.region = region
        AWSQueryConnection.__init__(self, aws_access_key_id, aws_secret_access_key,
                                    is_secure, port, proxy, proxy_port, proxy_user,
                                    proxy_pass, self.region.endpoint, debug,
                                    https_connection_factory, path)

    def _required_auth_capability(self):
        return ['ec2']


    def get_all_clusters(self, cluster_id=None, max_records=None, marker=None):
        params = {
            'ShowCacheNodeInfo': 'true',
        }
        if cluster_id:
            params['CacheClusterId'] = cluster_id
        if max_records:
            params['MaxRecords'] = max_records
        if marker:
            params['Marker'] = marker
        return self.get_list('DescribeCacheClusters', params, [('CacheCluster', CacheCluster)])

    def create_cache_cluster(self, id, node_type, num_cache_nodes, engine='memcached',
                             port=None,preferred_availability_zone=None,
                             security_groups=None, engine_version=None,
                             auto_minor_version_upgrade=True):
        params = {
            'CacheClusterId': id,
            'CacheNodeType': node_type,
            'NumCacheNodes': num_cache_nodes,
            'Engine': engine,
        }
        if port:
            params['port'] = port
        if preferred_availability_zone:
            params['PreferredAvailabilityZone'] = preferred_availability_zone
        if security_groups:
            self.build_list_params(params, security_groups, 'CacheSecurityGroups.member')
        if engine_version:
            params['EngineVersion'] = engine_version
        if auto_minor_version_upgrade is False:
            params['AutoMinorVersionUpgrade'] = 'false'

        return self.get_object('CreateCacheCluster', params, CacheCluster)






