# Python-File-Server
A RESTful file server app for servicing download requests concurrently


Usage:

1. Activate virtualenv: /env/bin/activate
2. Run `python threaded_server.py <port>` for multi-threaded file reads or `python async_server.py <port>` for asynchronous network i/o only
3. Use an http client, cURL or web browser to fetch files from server's file-system with a GET request


Examples:

`cURL http://<ip>:<port>/files -G -d 'path=/home/user/Desktop/file.tar' -o file.tar`

`http://<ip>:<port>/files?path=/home/user/Desktop/file.tar`
