"""
Testing for us11
Author: yzhou
"""
import os
import unittest
from ssw555Prj_Hogwarts import Repository
from us11 import us11_no_bigamy


class MyTestCase(unittest.TestCase):
    def test_us11(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(us11_no_bigamy(test), [('ERROR', 'INDIVIDUAL', 'US11', (180, 189), '@I3@', 'Husband:<@I3@> has one more spouse.'),
                                            ('ERROR', 'INDIVIDUAL', 'US11', (189, 180), '@I3@', 'Husband:<@I3@> has one more spouse.'),
                                            ('ERROR', 'INDIVIDUAL', 'US11', (415, 421), '@I_W_US17_1@', 'Husband:<@I_W_US17_1@> has one more spouse.'),
                                            ('ERROR', 'INDIVIDUAL', 'US11', (421, 415), '@I_W_US17_1@', 'Husband:<@I_W_US17_1@> has one more spouse.')])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
