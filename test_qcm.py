import unittest
from question import Question
from qcm import QCM

class TestQCM(unittest.TestCase):
    def test_check_reponse_correct(self):
        q = Question("1 + 1", ["2", "3", "4"], "2")
        user_reponse = "2"
        self.assertTrue(q.check_reponse(user_reponse))

    def test_check_reponse_incorrect(self):
        q = Question("1 + 1", ["2", "3", "4"], "2")
        user_reponse = "3"
        self.assertFalse(q.check_reponse(user_reponse))

if __name__ == '__main__':
    unittest.main()
