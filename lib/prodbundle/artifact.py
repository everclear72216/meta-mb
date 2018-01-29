import os
import shutil

from prodbundle.config import key_prefix

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
        
        artifact_key = self.__artifact_prefix + self._name
        self._artifact = datastore.getVar(artifact_key) or ''
        if len(self._artifact) is 0:
            raise Exception('The artifact is undefined')

        flags = datastore.getVarFlags(artifact_key) or {}
        flag_keys = flags.keys()
        
        if self.__name_flag not in flag_keys or len(flags[self.__name_flag]) is 0:
            raise Exception('The name of the artifact is undefined: %s' % (str(flags)))
        self._filename = flags[self.__name_flag]

        if self.__type_flag not in flag_keys or len(flags[self.__type_flag]) is 0:
            raise Exception('The type of the artifact is undefined.')
        self._type = flags[self.__type_flag]

        if self.__format_flag not in flag_keys or len(flags[self.__format_flag]) is 0:
            raise Exception('The format of the artifact is undefined.')
        self._format = flags[self.__format_flag]

        if self.__downgrade_flag not in flag_keys or len(flags[self.__downgrade_flag]) is 0:
            raise Exception('The downgrade clearance of the artifact is undefined.')
        self._downgrade = flags[self.__downgrade_flag]

        if self.__versiontype_flag not in flag_keys or len(flags[self.__versiontype_flag]) is 0:
            raise Exception('The version type of the artifact is undefined.')
        self._versiontype = flags[self.__versiontype_flag]

        if self.__checksumtype_flag not in flag_keys or len(flags[self.__checksumtype_flag]) is 0:
            raise Exception('The checksum type of the artifact is undefined.')
        self._checksumtype = flags[self.__checksumtype_flag]

    def register_dependencies(self, datastore):
        if self._type == 'diskimage':
            datastore.appendVarFlag('do_unpack', 'depends', ' ' + self._artifact + ':do_image_complete')
        else:
            datastore.appendVarFlag('do_unpack', 'depends', ' ' + self._artifact + ':do_deploy')

    def populate_bundle(self, datastore, bundledir):
        if self._type == 'diskimage':
            machine = datastore.getVar('MACHINE') or ""
            if len(machine) is 0:
                raise Exception('MACHINE is undefined')
            
            imgsource = '%s-%s.%s' % (self._artifact, machine, 'ext4') 
            bundlepath = '%s/%s' % (bundledir, self._filename)
            shutil.copy(datastore.expand('${DEPLOY_DIR_IMAGE}/%s' % (imgsource)), bundlepath) 
            if not os.path.exists(bundlepath):
                raise Exception('Failed to copy image')
        else:
            raise Exception('Artifact is no image') 
