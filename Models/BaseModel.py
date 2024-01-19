

class Model():
    def __init__(self):
        self.SQL_request = ''
        self.table_name: str = 'test'

    def _crate_conditions(self, kwargs):
        def get_v(v: str|int|float):
            return f'\"{v}\"' if v.isdigit() else f'\"{v}\"'
        return ' AND '.join([f'{k}={get_v(v)}' for k, v in kwargs])

    def get(self, **kwargs):
        '''Select '''
        print(f'''Select * \n FROM {self.table_name} WHERE {' AND '.join([f"{k}={v}" for k,v in kwargs.items()])}''')

    def get_all(self, **kwargs):
        print(kwargs)

    def set(self, **kwargs):
        print(kwargs)


if __name__ == "__main__":
    m = Model()
    m.get(a='6')
