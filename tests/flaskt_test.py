"""tests."""
import flaskt
import unittest


class FlasktTestCase(unittest.TestCase):
    """Unittest class."""

    def setUp(self):
        """Setting up app.test_client()."""
        flaskt.app.config['TESTING'] = True
        self.app = flaskt.app.test_client()

    def test_index_view(self):
        """Test GET index view."""
        r = self.app.get('/')
        assert r.data == 'index'

    def test_hooker_get(self):
        """Test GET /hooker."""
        r = self.app.get('/hook')
        assert r.data == 'OK'


if __name__ == '__main__':
    unittest.main()
