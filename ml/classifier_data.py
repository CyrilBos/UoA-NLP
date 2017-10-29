class ClassifierData:
    """
    Class that holds the data used by the Classifier.
    """
    __data = []
    __target = []
    __target_names = []

    def __init__(self, data, target, target_names):
        self.__data = data
        self.__target = target
        self.__target_names = target_names

    @property
    def data(self):
        return self.__data

    @property
    def target(self):
        return self.__target

    @property
    def target_names(self):
        return self.__target_names

    @data.setter
    def data(self, value):
        self._data = value

    @target_names.setter
    def target_names(self, value):
        self._target_names = value