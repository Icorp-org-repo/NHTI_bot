
class Meta(type):

    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.clas_attrs.items():
            self.__dict__[key] == value

    def __init__(cls, name, bases, attrs):
        cls.clas_attrs = attrs
        cls.__init__ = Meta.create_local_attrs()
