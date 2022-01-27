# version : 1.0.0

import os
from tinydb import TinyDB, Query
from core.settings import SETTINGS

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))


class Table(TinyDB):
    """ This class simplify using of TinyBD
    remember that using 'insert()' return database_index
    """

    def __init__(self, table_name, *args, **kwargs):
        """Initialize TinyBD with special parametrer
            but can be overrided

            @table_name : string"""

        if not table_name.endswith('.json'):
            # Extension of data file is not
            table_name = '{0}.json'.format(table_name)

        self._name = table_name
        table_path = os.path.join(PROJECT_PATH, SETTINGS.NETWORK_PATH, SETTINGS.NETWORK, self._name)
        # Setting not configured arguments
        kwargs['path'] = table_path
        kwargs['sort_keys'] = kwargs['sort_keys'] if 'sort_keys' in kwargs else True
        kwargs['indent'] = kwargs['indent'] if 'indent' in kwargs else 4
        kwargs['separators'] = kwargs['separators'] if 'separators' in kwargs else (',', ': ')
        kwargs['encoding'] = kwargs['encoding'] if 'encoding' in kwargs else 'utf-8'
        kwargs['ensure_ascii'] = kwargs['ensure_ascii'] if 'ensure_ascii' in kwargs else False

        super().__init__(*args, **kwargs)

    def get_table_name(self):
        """Return the test_network filename"""

        return self._name

    @staticmethod
    def get_fields(datas, fields_name: list):
        """ Returns the list of the elements of a field
            @test_network : data List
            @fields_name : list<str> : names of the columns to get"""

        if len(fields_name) < 2:
            # Only one row is asking
            return [r[fields_name[0]] for r in datas]

        # Two or more rows are asking
        result = list()
        for row in datas:
            filtred_data = tuple()
            for label in fields_name:
                filtred_data += (row[label],)
            result.append(filtred_data)
        return result
