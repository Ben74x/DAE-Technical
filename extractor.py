import queue
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor



# Define the queue with the maximum size
link_queue = queue.Queue(maxsize=1000)


def fetch_html(url):
    '''Function to fetch the HTML from a URL'''
    try:
        response = requests.get(url)
        return response.text
    
    # Returning possible error messages instead of None.
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Oops: Something Else",err)

def extract_links(html):
    '''Function to extract hyperlinks from HTML'''
    if html is None:
        return []
    soup = BeautifulSoup(html, 'lxml')

    # Considering 'a' tags with only 'href' attributes
    links = [link.get('href') for link in soup.find_all('a') if link.has_attr('href')]
    return links


# Define producer function to read URLs from file and extract markup
def producer(urls):
    '''Function to read URLs from file and extract markup'''
    with open(urls, 'r') as f:
        urls = f.readlines()
    with ThreadPoolExecutor(max_workers=10) as executor:
        for markup in executor.map(fetch_html, urls):
            if markup:
                link_queue.put(markup)
    # Signal the consumer that there are no more links to process
    link_queue.put(None)
                

# Define a consumer function to parse the HTML and extract hyperlinks
def consumer(output):
    '''Function to parse HTML and extract hyperlinks'''
    with open(output, 'a') as f:
        while True:
            markup = link_queue.get()
            if markup is None:
                # There are no more links to process
                break
            links = extract_links(markup)
            f.write(f'{links}\n')
            link_queue.task_done()

# Define a function to run the producer and consumer concurrently
def run(urls, output):
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer(urls))
        executor.submit(consumer(output))
    link_queue.join()

if __name__ == '__main__':
    run('urls.txt', 'output.txt')



# run on terminal: python extractor.py