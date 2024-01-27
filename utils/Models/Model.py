from collections import OrderedDict
from .manager import Manager


class Field:
    def __init__(self,
                 default,
                 primary_key:bool=False,
                 unique:bool=False,
                 not_null:bool=True,
                 ):
        pass


class IntegerField(Field):
    __fildtype__ = 'integer'


class SerialField(Field):
    __fildtype__ = 'serial'


class SmallSerialField(Field):
    __fildtype__ = 'smallserial'



class CharField(Field):
    pass


class ModelMeta(type):
    def __new__(mcs, class_name, parents, attributes: dict):
        # print(f"Create class {class_name}")
        fields = OrderedDict()
        for k, v in attributes.items():
            if isinstance(v, Field):
                fields[k] = v
                # Заглушка
                attributes[k] = None
        c = super(ModelMeta, mcs).__new__(mcs, class_name, parents, attributes)
        # Название таблицы
        setattr(c, '_model_name', attributes['__qualname__'].lower())
        setattr(c, '_original_filter', fields)
        setattr(c, 'objects', Manager(c))
        return c


class Model(metaclass=ModelMeta):
    id = IntegerField()

    def __repr__(self):
        return f'<{self._model_name}: {self.id}>'
    pass



class City(Model):
    name = CharField()
    population = IntegerField()


if __name__ == '__main__':
    pass
