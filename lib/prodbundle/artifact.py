
from config import key_prefix

class Artifact(object):

    __version_major = 1
    __version_minor = 0

    __artifact_prefix = key_prefix + 'ARTIFACT_'

    __name_flag = 'name'
    __type_flag = 'type'
    __format_flag = 'format'
    __downgrade_flag = 'downgrade'
    __versiontype_flag = 'version.type'
    __checksumtype_flag = 'checksum.type'

    __formats = ('bin', 'hex')
    __types = ('firmware', 'diskimage')
    __checksum_types = ('crc32', 'sha256')
    __version_types = ('indexed', 'dotted', 'dotted-date')
    __downgrade_values = ('yes', 'no')

    def __init__(self, datastore, name):
        self._name = str(name)


