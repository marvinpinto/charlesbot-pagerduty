import asynctest
from asynctest.mock import patch


class TestPagerduty(asynctest.TestCase):

    def setUp(self):
        patcher1 = patch('charlesbot_pagerduty.pagerduty.Pagerduty.load_config')  # NOQA
        self.addCleanup(patcher1.stop)
        self.mock_load_config = patcher1.start()

        from charlesbot_pagerduty.pagerduty import Pagerduty
        test_plug = Pagerduty()  # NOQA

    def tearDown(self):
        pass

    @asynctest.ignore_loop
    def test_something(self):
        pass
