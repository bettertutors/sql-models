from unittest import TestCase, main as unittest_main

from bettertutors_sql_models import db
from bettertutors_sql_models.User import User


row_to_dict = lambda row: {key: getattr(row, key) for key in row._meta.fields.keys()}


class TestSqlModels(TestCase):
    @classmethod
    def setUpClass(cls):
        db.connect()
        db.create_tables([User])

    @classmethod
    def tearDownClass(cls):
        db.drop_tables([User])
        db.close()

    users = (
        {'email': u'foo@bar.com', 'institute': u'UNSW', 'role': u'tutor'},
        {'email': u'foobar@car.com', 'institute': u'Sydney', 'role': u'tutor'}
    )

    def test_create_read(self):
        for user in self.users:
            # Create user
            User.create(**user).save()

            # Ensure user exists (with correct fields and values)
            row_d = row_to_dict(User.select().where(User.email == user['email']).execute().next())
            user['registered_on'] = row_d['registered_on']
            self.assertEqual(row_d, user)


if __name__ == '__main__':
    unittest_main()
