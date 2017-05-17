class Model:

    def __init__(self, mag_bundle, config_name):
        self.mag_bundle = mag_bundle
        self.config_name = config_name
        self.__mag_path = ''

    def get_mag(self):
        return self.__mag_path+self.mag_bundle

    def __str__(self):
        return self.config_name
