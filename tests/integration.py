import unittest
import top_spotify_track
from unittest import TestCase

class TestIntegration(TestCase):
    def setUp(self):
        top_spotify_track.app.testing = True
        self.app = top_spotify_track.app.test_client()

    def test_default_page(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)

    def test_no_artist(self):
        response = self.app.post('/find', data=dict(artist=None))
        self.assertEqual(404, response.status_code)

    def test_bad_artist(self):
        response = self.app.post('/find', data=dict(artist="awdawd"))
        self.assertEqual(404, response.status_code)
        
    def test_adele(self):
        response = self.app.post('/find', data=dict(artist="Adele"))
        self.assertEqual(200, response.status_code)

    def test_track_id(self):
        # This top track probably isn't moving anytime soon, but it
        # could be a potential test concern
        response = self.app.post('/find', data=dict(artist="Journey"))
        self.assertEqual(200, response.status_code)
        response_data = response.data.decode("utf-8")
        self.assertTrue("4bHsxqR3GMrXTxEPLuK5ue" in response_data)

#    def test_send_sms(self):
        #sid = top_spotify_track.send_sms_with_top_justin_bieber_track()
        #self.assertTrue(sid.startswith('SM'))

if __name__ == "__main__":
    unittest.main()
