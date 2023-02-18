# DAE-Technical

## Getting Started

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