# curl http://127.0.0.1:8080/files -G -d 'path=/home/waldo/Desktop'

#TODO : test asynchronous requests -- (pycurl, tornado test modules, requests package)

from tornado import testing, httpclient
import time
import unittest
import server

class TestFileServer(testing.AsyncHTTPTestCase):
    
    def __init__(self, *args, **kwargs):
        testing.AsyncHTTPTestCase.__init__(self, *args, **kwargs)
        self.server = server.main()
    
    def get_app(self):
        return self.server._app

    def test_bad_path(self):
        pass
    
    def test_bad_query(self):
        pass
    
    def test_small_seq_downloads(self):
        pass
    
    def test_large_seq_downloads(self):
        pass
    
    @testing.gen_test
    def test_small_async_downloads(self):
        request_obj = httpclient.HTTPRequest(url= 'http://127.0.0.1:8080/files?test_files/10MB-file.tar', method = "GET")
        self.server.start()
        start = time.time()
        resp1, resp2 = yield [
            self.http_client.fetch(request_obj),
            self.http_client.fetch('http://127.0.0.1:8080/files?test_files/10MB-file.tar'),
        ]
        diff = time.time() - start
        print("Execution time: ", diff)

    @testing.gen_test
    def test_large_async_downloads(self):
        
        start = time.time()
        resp1, resp2 = yield [
            self.http_client.fetch('http://127.0.0.1:8080/files?test_files/1000MB-file.tar'),
            self.http_client.fetch('http://127.0.0.1:8080/files?test_files/1000MB-file.tar'),
        ]
        diff = time.time() - start

        with open("resp1.tar" , "wb") as r1, open("resp2.tar", "wb") as r2:
            r1.write(resp1.content)
            r2.write(resp2.content)
        
        self.assertTrue(diff, diff)


if __name__ == "__main__":
    #testing.main(argv=['first-arg-is-ignored'], exit=False, verbosity = 2)
    testing.main(verbosity = 2)