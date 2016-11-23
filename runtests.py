#!./.env/bin/python

import unittest

from unittests.test_server_response import ServerResponseTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ServerResponseTest())
    return suite


if __name__ == "__main__":
    unittest.main()
