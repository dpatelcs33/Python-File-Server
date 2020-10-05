# Python-File-Server
A RESTful file server application for servicing download requests concurrently(multi threading) and/or in parrelel(multi processing).

Currently only supporting `GET` requests with pause/resume functionality.

Dependencies:  

>python 3.8 / pip3 --> **Using included virtualenv "env" can lead to problems. Use at your own risk**
>
>**Setting up a new python 3.8 virtualenv and then using `pip install -r requirements.txt` is highly recommended**
>
>Linux (Testing):   
>loadimpact/k6 (example scripts included) --> https://k6.io/  
>har-to-k6 --> browser session convertion for testing  
>node.js 14.x --> for har-to-k6  
>cURL

Usage:

1. Setup a fresh virtualenv using python 3.8  

2. Activate environment  

3. Use the provided requirements.txt --> `pip install -r requirements.txt` to get the needed dependencies  

4. Run  
`python threaded_server.py <port>` for multi-threaded file reads  
or  
`python async_server.py <port>` for asynchronous network i/o only  
or  
`python multi_process_threaded_server.py <port>` for multi-processed and multi-threaded server  
or  
`python multi_process_async_server.py <port>` for multi-processed async network i/o only  

5. Use an http client, cURL or web browser to fetch files from server's file-system with a GET request


Examples:

`cURL http://<ip>:<port>/files -G -d 'path=/home/user/Desktop/file.tar' -o file.tar`

`http://<ip>:<port>/files?path=/home/user/Desktop/file.tar`
