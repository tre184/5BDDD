import crud, schema, pytest
from pydantic import ValidationError

def test_crud1():
    '''
    Test de fonction crud
    :return:
    '''
    u1 = crud.get_user_by_id(99)
    assert u1.id == 99
    assert u1.name == 'goudot-99'


def test_crud2():
    '''
    Test 2
    :return:
    '''
    m = schema.Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '20'])
    print(repr(m))
    assert m.dimensions[1] == 20

    external_data = {
        'id': 123,
        'signup_ts': '2019-06-01 12:22',
        'email': 'test@gmail.com',
        'tastes': {
            'wine': 9,
            b'cheese': 7,
            'cabbage': '1',
        },
    }

    user = schema.User(**external_data)
    print('user', user)
    print(user.model_dump())
    assert user.id == 123

    external_data2 = {
        'id': 123,
        'signup_ts': '2019-06-01 12:22',
        'email': 'test..t@gmail.com',
    }

    with pytest.raises(ValidationError) as excinfo :
        user2 = schema.User(**external_data2)
