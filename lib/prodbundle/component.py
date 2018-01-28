
from config import key_prefix
from artifact import Artifact

class Component(object):

    __version_major = 1
    __version_minor = 0

    __artifacts_prefix = key_prefix + 'ARTIFACTS_'
    __connection_prefix = key_prefix + 'CONNECTION_'

    def __init__(self, datastore, name):
        self._name = str(name)

        connection_key = self.__connection_prefix + self._name
        self._connection = str(datastore.getVar(connection_key))
        if len(self._connection) is 0:
            raise Exception('No connection specified for component %s' % (self.name))

        artifacts_key = self.__artifacts_prefix + self._name
        artifacts = str(datastore.getVar(artifacts_key)).split()
        if len(artifacts) is 0:
            raise Exception('No artifacts specified for component %s' % (self._name))

        self._artifacts = []
        for artifact in artifacts:
            if len(artifact) is 0:
                continue

            self._artifacts.append(Artifact(datastore, artifact))

