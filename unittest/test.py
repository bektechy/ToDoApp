import app
import unittest


def check_username_with_specific_id(id):
    user = app.User(id)
    user.name = f'user{id}'
    return user.__str__()


def check_id():
    user = app.User(9)
    return user.get_id()


class UnitTesting(unittest.TestCase):
    def testing_username(self):
        self.assertEqual(check_username_with_specific_id(17), "user17")

    def testing_if_id_is_none(self):
        self.assertIsNone(check_id())

if __name__ == '__main__':
    unittest.main()
