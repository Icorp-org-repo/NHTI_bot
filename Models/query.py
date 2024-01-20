AND = 'and'
OR = 'or'


class Q:

    def __init__(self, exp_type=AND, **kwargs):
        '''
        Параметр в основном для опретора Where
        :param exp_type: Условный сепаратор
        :param kwargs: Параметры
        '''
        self.separator = exp_type
        self._params = kwargs

    # TODO: добавить add или extend
    def extend(self, **kwargs):
        self._params = self._params | kwargs

    def __str__(self):
        kv_pairs = [f'{k} = {v}' for k, v in self._params.items()]
        return f' {self.separator} '.join(kv_pairs)

    def __bool__(self):
        return bool(self._params)


class BaseExp:
    name = None

    def add(self, *args, **kwargs):
        '''
        Добавляет параметры для оператора
        :param args: параметры
        :param kwargs: параметры оператора
        :return: None
        '''
        raise NotImplementedError()

    def definition(self):
        '''
        Формирует оператора с его параметрами
        '''
        return self.name + '\n\t' + self.line() + '\n'

    def line(self) -> str:
        '''
        Возвращает параметры оператора
        :return: Строка состоящая из параметров
        '''
        raise NotImplementedError()

    def __bool__(self):
        '''
        Если параметров нет то возвращает False
        :return:
        '''
        raise NotImplementedError()


class Select(BaseExp):

    name = 'SELECT'

    def __init__(self):
        self._params = []

    def add(self, *args, **kwargs):
        self._params.extend(args)

    def line(self):
        separator = ','
        return separator.join(self._params)

    def __bool__(self):
        return bool(self._params)


class From(BaseExp):

    name = 'FROM'

    def __init__(self):
        self._params = []

    def add(self, *args, **kwargs):
        self._params.extend(args)

    def line(self):
        separator = ','
        return separator.join(self._params)

    def __bool__(self):
        return bool(self._params)


class Where(BaseExp):

    name = 'WHERE'

    def __init__(self, exp_type=AND, **kwargs):
        self._q = Q(exp_type=exp_type, **kwargs)

    def add(self, **kwargs):
        self._q.extend(**kwargs)

    def line(self):
        return str(self._q)

    def __bool__(self):
        return bool(self._q)


class Query:
    def __init__(self, exp_type=AND):
        self._data = {'select': Select(), 'from': From(), 'where': Where(exp_type)}

    def SELECT(self, *args):
        self._data['select'].add(*args)
        return self

    def FROM(self, *args):
        self._data['from'].add(*args)
        return self

    def WHERE(self, **kwargs):
        self._data['where'].add(**kwargs)
        return self

    def _line(self, key):
        separator = ','
        return separator.join(self._data[key])

    def _lines(self):
        for key, value in self._data.items():
            yield value.definition()

    def __str__(self):
        return ''.join(self._lines())


if __name__ == '__main__':
    q = Query()
    q.SELECT('age', 'all').FROM('abs').FROM('Asdf').WHERE(a=1).WHERE(b='dfsad')
    print(q)