# Python-File-Server (Tornado)
A RESTful, Asynchronous file server application for servicing download requests Concurrently(Multi-Threading) and/or in Parallel(Multi-Processing).

*Currently only supporting `GET` requests with pause/resume functionality

## Dependencies:  

> python 3.8 / pip3 --> **Using included virtualenv "env" can lead to problems. Use at your own risk**
>
> **Setting up a new python 3.8 virtualenv and then using `pip install -r requirements.txt` is highly recommended**
> 
> Linux (Testing):   
> loadimpact/k6 (example scripts included) --> https://k6.io/  
> har-to-k6 --> browser session convertion for testing  
> node.js 14.x --> for har-to-k6  
> cURL

## Usage:

1. Setup a fresh virtualenv using python 3.8  

2. Activate environment  

3. Use the provided requirements.txt --> `pip install -r requirements.txt` to get the needed dependencies  

4. Run  
`python threaded_server.py <port>` for multi-threaded file i/o  
or  
`python async_server.py <port>` for asynchronous network i/o only  
or  
`python multi_process_threaded_server.py <port>` for multi-processed, multi-threaded file and network i/o  
or  
`python multi_process_async_server.py <port>` for multi-processed, async network i/o only  

5. Use an http client, cURL or web browser to fetch files from server's file-system with a GET request


## Examples:

`cURL http://<ip>:<port>/files -G -d 'path=/home/user/Desktop/file.tar' -o file.tar`

`http://<ip>:<port>/files?path=/home/user/Desktop/file.tar`

## -----Contributions are Welcome-----

**Some takeaways and guidelines from developer's perspective (as of 10/07/2020):**

- Multithreaded would be useful for fast drives like SSDs and scales up very well. Apps benefit from non-blocking calls in that the server can take and serve more requests (with the benefit of in-memory buffers) but HDD needles still need to travel to the different sectors physically to retrieve files/chunks sequentially. I/O bound tasks, in general, are better handled with threads. Threads in this case are contained in a single-process with callbacks to the IOLoop in the main thread. Main thread uses the IOLoop to peform context switching between threads.

- Multiprocessing can dramatically impact runime delays like python bookkeeping, garbage collection overhead, buffering, callbacks, IOLoop latency, building responses etc.

- Download pause/resume functionality can backfire if client code is not setup correctly to timeout/disconnect upon a long pause duration. However, the benefits of pause/resume feature with very large file downloads from user side outweighs this and there might be a way to resolve it with some thought on server side.

- Some buffering and chunk size modification might be required for optimal performance based on system and environment as well as the test results.

- Python, Tornado and OS level buffers are difficult to manage from beginning to end. Tornado specifically doesn't allow for kernel level file transfer to non-blocking sockets like nginx, apache. For example, os.sendfile doesn't work with async calls as it doesn't support callbacks natively and therefore, the entire file has to be written out to the network socket at once. User address space (app instance memory space) file buffers copy data from kernel buffers and this can add significant overhead. To mitigate this, user-space buffering was turned off when opening file and the posix_fadvise (suggestion/information to kernel on app's use of file) was set to optimize caching priority in kernel-layer buffer (SUPPORTED FOR UNIX ONLY)

- Different user space caching techniques could be used like mmap, bytearray, etc. all with costs/benefits of their own and need to be efficiently controlled within app for multi-threaded and multi-processing to take full advantage.

**Some interesting features for future consideration:**  

- load balancing setup
- byte-serving files in a specific range
- granular initialization of multiprocessing forks depending on # of concurrent requests
- streaming content
- Database/remote file system integration
- user authentication/authorization
- file permissions
- compressed streams.
