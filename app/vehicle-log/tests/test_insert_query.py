import datetime
import pytest
from vehicle.insert_query import insert_query

@pytest.mark.parametrize('input_list, expected', [
    (['test', 'test', '', datetime.datetime(2020, 9, 13, 11, 22, 1)], 'INSERT INTO USER (start,finish,memo,create_at) VALUES (\'test\', \'test\', \'\', \'2020-09-13 11:22:01.000000\')'),
    (['A', 'B', 'point', datetime.datetime(2020, 9, 13, 11, 22, 1)], 'INSERT INTO USER (start,finish,memo,create_at) VALUES (\'A\', \'B\', \'point\', \'2020-09-13 11:22:01.000000\')'),
    (['aaa', 'bbb', None, datetime.datetime(2020, 9, 13, 11, 22, 1)], 'INSERT INTO USER (start,finish,memo,create_at) VALUES (\'aaa\', \'bbb\', None, \'2020-09-13 11:22:01.000000\')')
])
def test_insert_query(input_list, expected):
    query = insert_query(*input_list)
    print(query)
    assert query == expected