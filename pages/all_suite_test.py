import unittest

from unittest.loader import makeSuite

from test_cases.fill_in_a_form import TestFillInaForm

from pages import Leg_dropdown, Add_a_player_form, Contact_button, Sign_out_from_the_system, Clear_form
from test_cases import login_to_the_system

from test_cases.framework import Test


class Clear_form:
   pass


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(Leg_dropdown)
   test_suite.addTest(login_to_the_system)
   test_suite.addTest(Add_a_player_form)
   test_suite.addTest(Contact_button)
   test_suite.addTest(Sign_out_from_the_system)
   test_suite.addTest(Clear_form)
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())