
import tornado.web
import tornado.ioloop
# from mimetypes import guess_type
# import os.path
# import asyncio


class FileHandler(tornado.web.RequestHandler):

    def get(self):

        # TODO : handle get requests

        pass


def main():
	
	app = tornado.web.Application([

	    #TODO: setup calls to requesthandler

    ])

    #TODO: server

    app.listen(8080)
    print("Listening on port 8080")
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
	main()

