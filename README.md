# DAE-Technical

## Getting Started

```extractor.py```: This is the main Python module containing the implementation of the producer and consumer functions.

- *fetch_html(url)*: This function takes a URL as input and fetches the HTML content of the web page at that URL using the requests library. If the request is successful, it returns the HTML content as a string. If the request fails, it prints an error message and returns None.

- *extract_links(html)*: This function takes an HTML string as input and uses the BeautifulSoup library to parse the HTML and extract all the hyperlinks (i.e., anchor tags with href attributes). It returns a list of URLs.

- *producer(urls)*: This function takes a file path as input and reads URLs from the file. It then submits a task to a thread pool to fetch the HTML content for each URL using the fetch_html function. If the request is successful, it adds the HTML content to a queue called link_queue.

- *consumer(output)*: This function takes a file path as input and repeatedly reads items from the link_queue. If an item is a string (i.e., HTML content), it extracts the hyperlinks using the extract_links function and writes them to a file specified by the output argument. If an item is None, it signals that there are no more items in the queue and exits the loop.

- *run(urls, output)*: This function takes two file paths as input: one for the input file containing URLs and one for the output file where the extracted hyperlinks will be written. It creates a process pool with two processes and submits the producer and consumer functions to the pool. It then waits for both functions to complete using the result method of the Future object returned by the submit method.

```unittest_extract_links.py```: This test uses the @patch decorator to mock the requests.get function and simulate a response. The content attribute of the response is set to some HTML content that includes a link. The extract_links method is called with this HTML content, and the test verifies that the method returns the correct link. This test does not rely on loading any files from disk, and it simulates a real-world scenario where the HTML content is obtained from a website.

```urls.txt```: This is a text file containing a list of URLs to be processed by the producer function. Each URL should be on a separate line.

```output.txt```: This is the output file that will be created by the consumer function. It will contain a list of URLs and their associated hyperlinks.

Make sure that all these files are located in the same directory. The producer_consumer.py and test_producer_consumer.py files should both import the queue module, which is part of the standard library and should be available by default.

Clone the repository
```git clone https://github.com/Ben74x/DAE-Technical.git```


## Usage
To use this extractor, you'll need to provide a list of URLs to process. You can do this by modifying the URLs in urls.txt. Once you've added your URLs to the urls.txt file, you can run the program by opening a terminal or command prompt in the same directory as the script, and running the following command:

```python extractor.py```

The extractor will then start fetching the markup from each URL and extracting hyperlinks from the markup. The output will be written to a file called output.txt, which will contain the original URL and a list of all the hyperlinks found on the page.

## Customization
The code includes several parameters that you can customize to suit your needs. These parameters are defined at the top of the *extractor.py* file, and include:

**link_queue**: The maximum size of the queue that holds the markup for processing.

**threadpoolexecutor**: Pool of threads to fetch markups in producer and extract hyperlinks in consumer. It is also specified in the *run* function.


## Testing
The project includes a set of unit tests to verify that the program is working correctly. You can run the test by opening a terminal or command prompt in the same directory as the script, and running the following command:

```python -m unittest test.py```

The tests will then be run, and any errors or failures will be reported to the console.
