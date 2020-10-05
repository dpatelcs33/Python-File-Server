from tornado import web, ioloop, iostream
import mimetypes
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor
import aiofiles


class FileHandler(web.RequestHandler):

    async def get(self):

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

        async with aiofiles.open(abs_path, "rb", buffering=0, loop=ioloop.IOLoop.current(), executor=self.application.thread_executor) as fp:

            # No buffering in address space and inform kernel to buffer aggressively for given file
            if os.name == "posix":

                os.posix_fadvise(fp.fileno(), 0, file_size,
                                 os.POSIX_FADV_WILLNEED)

            while True:

                chunk = await fp.read(chunk_size)

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
                    await asyncio.sleep(0.000000001)


def main():

    # TODO: production --> debug off , autoreload = off
    app = web.Application([

        (r"/files", FileHandler)

    ], autoreload=True, debug=True)

    app.thread_executor = ThreadPoolExecutor()

    app.listen(8080)
    print("FileServer(Threaded File Reads): Listening on port 8080")

    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()