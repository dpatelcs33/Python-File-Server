import tornado.web as web
import tornado.ioloop as ioloop
import tornado.httpserver as httpserver
import mimetypes
import os
#import asyncio


class FileHandler(web.RequestHandler):

    def get(self):

        # TODO : handle get requests Asynchronously

        abs_path = os.path.abspath(self.get_argument('path'))
        print(abs_path)

        if not os.access(abs_path, os.R_OK):
            raise web.HTTPError(status_code=404, reason="File Not Found or Access Denied")
    
        content_type, _ = mimetypes.guess_type(abs_path)
        print(content_type)
        self.add_header('Content-Type', content_type)

        with open(abs_path) as fp:
            self.write(fp.read())        

def main():
    # TODO: production --> debug off
    app = web.Application([

        (r"/files", FileHandler)

    ], debug=True)

    http_server = httpserver.HTTPServer(app)
    http_server.listen(8080)
    print("Listening on port 8080")
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
