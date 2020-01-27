from unittest import TestCase, main
from os import path

from ..api import v1 as figlib_api

class TestJsonCfg(TestCase):

    def __init__(self, methodName=None):
        TestCase.__init__(self, methodName="test_all")
        self.data_dir = path.join(path.dirname(__file__), "data")

    
    def test_all(self):
        self.test_simple()

    def test_simple(self):
        json_fp = path.join(self.data_dir, "simple_json.json")
        config = figlib_api.load_json_config(json_fp)

        self.assertEqual(config.name, "project")
        self.assertEqual(config.number, 10)


if __name__ == "__main__":
    main()
