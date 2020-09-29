# curl http://127.0.0.1:8080/files -G -d 'path=/home/waldo/Desktop'

#TODO : test asynchronous requests -- (pycurl, tornado test modules, requests package)

import tornado.testing
import tornado.httpclient
import time

class TestFileServer(tornado.testing.AsyncHTTPTestCase):
    
    def test_bad_path:
        NotImplemented
    
    def test_bad_query:
        NotImplemented
    
    def test_small_seq_downloads:
        NotImplemented
    
    def test_large_seq_downloads:
        NotImplemented
    
    @tornado.testing.gen_test
    def test_small_async_downloads:
        start = time.time()
        resp1, resp2 = yield [
            self.http_client.fetch(),
            self.http_client.fetch(self.get_url('/async')),
        ]
        diff = time.time() - start
    
    @tornado.testing.gen_test
    def test_large_async_downloads:
        start = time.time()
        resp1, resp2 = yield [
            self.http_client.fetch(),
            self.http_client.fetch(self.get_url('/async')),
        ]
        diff = time.time() - start


if __name__ == "__main__":
    tornado.testing.main(verbosity = 2)