from tornado import web, ioloop, httpserver, iostream
import mimetypes
import os
import asyncio
import time
import io
import sys


class FileHandler(web.RequestHandler):

    async def get(self):

        print("PID {} : getting file".format(os.getpid()))

        abs_path = os.path.abspath(self.get_argument('path'))

        if not os.access(abs_path, os.R_OK):
            raise web.HTTPError(
                status_code=404, reason="File Not Found or File Access Denied")

        file_size = os.path.getsize(abs_path)
        content_type, _ = mimetypes.guess_type(abs_path)

        if not content_type:
            self.set_header('Content-Type', "application/octet-stream")
        else:
            self.set_header('Content-Type', content_type)

        self.add_header('Content-Disposition',
                        "attachment; filename={}".format(os.path.basename(abs_path)))
        self.add_header('Content-Length', file_size)

        chunk_size = 1024 * 1024 * 2

        with open(abs_path, "rb") as fp:

            while True:
                chunk = fp.read(chunk_size)

                if not chunk:
                    break

                try:
                    self.write(chunk)
                    await self.flush()

                except iostream.StreamClosedError:
                    break

                finally:
                    del chunk

                    # Used for metering/limiting request bandwidth or forced context switching for fast networks
                    await asyncio.sleep(0.0000000001)

        print("PID {} : sent file {}".format(
            os.getpid(), os.path.basename(abs_path)))


def make_app():
    app = web.Application([

        (r"/files", FileHandler)

    ], autoreload=False, debug=False)
    return app


def main():

    try:
        port = int(sys.argv[1])
    except:
        print("Error: Port not provided!")
        sys.exit(2)

    # Fix for windows python 3.8 --> use the tornado supported selector event loop instead of theproactor event loop on windows
    if sys.version_info >= (3, 8) and sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    app = make_app()
    server = httpserver.HTTPServer(app)
    server.bind(port)
    server.start(0)  # forks one process per cpu
    print("FileServer PID {0}: Listening on port {1}".format(
        os.getpid(), port))
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
