import unittest
from core.utils import pos_tag
from backend import create_app

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_post_tag(self):
        text = "amazon co. can pusblish government related factories and microsoft doesn't now how to cope with facebook and bill gates is old but elon musk is young"

        result = pos_tag(text)

        assert len(result) > 0
