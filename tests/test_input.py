import get_input
import unittest

class Test_get_input(unittest.TestCase):

#Test Username get_input
    def test_username_corrrect(self):
        self.assertTrue(get_input.get_username("name"))
    
    def test_username_empty(self):
        self.assertFalse(get_input.get_username(""))

    def test_username_number(self):
        self.assertFalse(get_input.get_username(1234))

    def test_username_contain_number(self):
        self.assertFalse(get_input.get_username("name123"))

    def test_contains_charector(self):
        self.assertFalse(get_input.get_username("??\/"))

#Test Date get_get_input in the format DD/MM/YYYY

    def test_date_correct(self):
        self.assertTrue(get_input.get_date("12/03/2021"))

    def test_date_no_input(self):
        self.assertFalse(get_input.get_date(""))

    def test_date_date_passed1(self):
        self.assertFalse(get_input.get_date("12/12/2019"))

    def test_date_date_passed2(self):
        self.assertFalse(get_input.get_date("08/08/2010"))

    def test_date_date_and_latters(self):
        self.assertFalse(get_input.get_date("jk/h/20f"))

#Test time input
    def test_correct_time(self):
        self.assertTrue(get_input.get_time("15:30", "01/01/2021"))

    def test_time_incorect_format(self):
        self.assertFalse(get_input.get_time("15 -30", "01/01/2021"))

    def test_time_incorrect_hours(self):
        self.assertFalse(get_input.get_time("25:30","01/01/2021"))

    def test_timeincorrect_min(self):
        self.assertFalse(get_input.get_time("15:60","01/01/2019"))

    def test_not_separated(self):
        self.assertFalse(get_input.get_time("1530","01/01/2021"))

    def test_blank(self):
        self.assertFalse(get_input.get_time("","01/01/2021"))

    def test_time_not_complete(self):
        self.assertFalse(get_input.get_time("15","01/01/2021"))