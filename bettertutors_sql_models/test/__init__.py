from unittest import TestCase, main as unittest_main
from re import compile, match

from bettertutors_sql_models import __version__


class TestSqlModelsPackage(TestCase):
    has_three_nums = compile('\d{1,3}\.\d{1,3}\.\d{1,3}\w*')

    def test_setup_dots(self):
        """ Not a full semver check, just checking if it starts like num.num.num """
        self.assertTrue(match(self.has_three_nums, __version__), "Not in semver format")


if __name__ == '__main__':
    unittest_main()
