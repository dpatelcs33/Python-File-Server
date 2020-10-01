from tornado import web, ioloop, httpserver, iostream
import mimetypes
import os
import asyncio


class FileHandler(web.RequestHandler):

    async def get(self):

        # TODO : non-blocking file reads

        abs_path = os.path.abspath(self.get_argument('path'))
        
        #print(abs_path)

        if not os.access(abs_path, os.R_OK):
            raise web.HTTPError(status_code=404, reason="File Not Found or File Access Denied")
    
        file_size = os.path.getsize(abs_path)
        content_type, _ = mimetypes.guess_type(abs_path)

        if not content_type:
            self.set_header('Content-Type', "application/octet-stream")
            
        #print(content_type)

        self.add_header('Content-Disposition', "attachment; filename={}".format(os.path.basename(abs_path)))
        self.set_header('Content-Type', content_type)
        self.add_header('Content-Length', file_size)
        buff_size = 1024 * 1024 * 1

        with open(abs_path, "rb") as fp:

            while True:

                chunk = fp.read(buff_size)        
                
                if not chunk:
                    break

                try:
                    self.write(chunk)
                    await self.flush()

                except iostream.StreamClosedError:
                    break

                finally:
                    del chunk
                    await asyncio.sleep(0)


def main():

    # TODO: production --> debug off , autoreload = off
    app = web.Application([

        (r"/files", FileHandler)

    ], autoreload = True, debug = True)

    http_server = httpserver.HTTPServer(app)
    http_server.listen(8080)
    print("Listening on port 8080")
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
