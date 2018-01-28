
from config import key_prefix
from component import Component

class Bundle(object):

    __version_major = 1
    __version_minor = 0

    __sysname_key = key_prefix + 'SYSTEMNAME'
    __components_key = key_prefix + 'COMPONENTS'
    __sysvariants_key = key_prefix + 'SYSTEMVARIANTS'

    def __init__(self, datastore):
        self._systemname = str(datastore.getVar(self.__sysname_key))
        if len(self._sysname) is 0:
            raise Exception('No system name specified.')

        self._sysvariants = str(datastore.getVar(self.__sysvariants_key))
        if len(self._sysvariants) is 0:
            raise Exception('No system variants specified.')

        components = str(datastore.getVar(self.__components_key)).split()
        if len(components) is 0:
            raise Exception('No components have been specified for the bundle.')
        
        self._components = []
        for component in components:
            if len(component) is 0:
                continue

            self._components.append(Component(datastore, component))

