# DAE-Technical

## Getting Started

```extractor.py```: This is the main Python module containing the implementation of the producer and consumer functions.

- *fetch_html(url)*: This function takes a URL as input and fetches the HTML content of the web page at that URL using the requests library. If the request is successful, it returns the HTML content as a string. If the request fails, it prints an error message and returns None.

- *extract_links(html)*: This function takes an HTML string as input and uses the BeautifulSoup library to parse the HTML and extract all the hyperlinks (i.e., anchor tags with href attributes). It returns a list of URLs.

- *producer(urls)*: This function takes a file path as input and reads URLs from the file. It then submits a task to a thread pool to fetch the HTML content for each URL using the fetch_html function. If the request is successful, it adds the HTML content to a queue called link_queue.

- *consumer(output)*: This function takes a file path as input and repeatedly reads items from the link_queue. If an item is a string (i.e., HTML content), it extracts the hyperlinks using the extract_links function and writes them to a file specified by the output argument. If an item is None, it signals that there are no more items in the queue and exits the loop.

- *run(urls, output)*: This function takes two file paths as input: one for the input file containing URLs and one for the output file where the extracted hyperlinks will be written. It creates a process pool with two processes and submits the producer and consumer functions to the pool. It then waits for both functions to complete using the result method of the Future object returned by the submit method.

```unittest_extract_links.py```: This test uses the @patch decorator to mock the requests.get function and simulate a response. The content attribute of the response is set to some HTML content that includes a link. The extract_links method is called with this HTML content, and the test verifies that the method returns the correct link. This test does not rely on loading any files from disk, and it simulates a real-world scenario where the HTML content is obtained from a website.

```unittest_producer.py```: This test checks that the producer function runs without errors when given a valid input file of URLs. It does this by setting the input file to a test file, creating an event loop and an asyncio.Future object to hold the result of running the producer function, running the producer function using asyncio.ensure_future, waiting for the future to complete using loop.run_until_complete, and then checking that the result of the future is not None. This test assumes that the consumer function is working correctly and that the URLs in the input file are valid.

```unittest_consumer.py```: This test checks if the consumer function extracts hyperlinks and writes them to a file correctly. It also uses producer function to create the file with URLs first, which is a good way to test consumer function. Overall, the test covers the main functionality of consumer function and it's a good way to ensure that it works correctly.

```urls.txt```: This is a text file containing a list of URLs to be processed by the producer function. Each URL should be on a separate line.

```output.txt```: This is the output file that will be created by the consumer function. It will contain a list of URLs and their associated hyperlinks.



Clone the repository
```git clone https://github.com/Ben74x/DAE-Technical.git```


## Usage
To use this extractor, you'll need to provide a list of URLs to process. You can do this by modifying the URLs in urls.txt. Once you've added your URLs to the urls.txt file, you can run the program by opening a terminal or command prompt in the same directory as the script, and running the following command:

```python extractor.py```

The extractor will then start fetching the markup from each URL and extracting hyperlinks from the markup. The output will be written to a file called output.txt, which will contain the original URL and a list of all the hyperlinks found on the page.



## Testing
The project includes a set of unit tests to verify that the program is working correctly. You can run the test by opening a terminal or command prompt in the same directory as the script, and running the following command:

```python -m unittest unittest_extract_links.py```
```python -m unittest unittest_producer.py```
```python -m unittest unittest_consumer.py```

The tests will then be run, and any errors or failures will be reported to the console.
