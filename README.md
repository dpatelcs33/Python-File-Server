# Python-File-Server
A RESTful file server app for servicing download requests concurrently

Dependencies:  
>python 3.7+ / pip --> use included virtualenv
>
>Linux (Testing):   
>loadimpact/k6 (example scripts included) --> https://k6.io/  
>har-to-k6 --> browser session convertion for testing  
>node.js 14.x --> for har-to-k6  
>cURL

Usage:

1. Activate virtualenv: /env/bin/activate

2. Run  
`python threaded_server.py <port>` for multi-threaded file reads  
or  
`python async_server.py <port>` for asynchronous network i/o only  
or  
`python multi_process_threaded_server.py <port>` for multi-processed and multi-threaded server  
or  
`python multi_process_async_server.py <port>` for multi-processed async network i/o only  

3. Use an http client, cURL or web browser to fetch files from server's file-system with a GET request


Examples:

`cURL http://<ip>:<port>/files -G -d 'path=/home/user/Desktop/file.tar' -o file.tar`

`http://<ip>:<port>/files?path=/home/user/Desktop/file.tar`
