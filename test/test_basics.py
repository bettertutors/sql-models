from unittest import TestCase, main as unittest_main

from bettertutors_sql_models.base import db
from bettertutors_sql_models.models.Signup import Signup
from bettertutors_sql_models.utils import row_to_dict
from mocks import users


class TestSqlModels(TestCase):
    @classmethod
    def setUpClass(cls):
        db.connect()
        db.create_tables([Signup], safe=True)

    @classmethod
    def tearDownClass(cls):
        db.drop_tables([Signup], safe=True)
        db.close()

    users = users

    def test_create_read(self):
        for user in self.users:
            # Create user
            Signup.create(**user).save()

            # Ensure user exists (with correct fields and values)
            row_d = row_to_dict(Signup.select().where(Signup.email == user['email']).execute().next())
            user['registered_on'] = row_d['registered_on']
            self.assertEqual(row_d, user)


if __name__ == '__main__':
    unittest_main()
