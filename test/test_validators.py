from unittest import TestCase, main as unittest_main

from bettertutors_sql_models.custom_fields import EmailField


class TestSqlFields(TestCase):
    def test_email(self):
        ef = EmailField()
        self.assertRaises(AssertionError, lambda: ef.coerce('foobar.com'))
        self.assertTrue(ef.coerce('foo@bar.com'))


if __name__ == '__main__':
    unittest_main()
