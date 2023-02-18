import queue
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


# Define the queue with the maximum size
link_queue = queue.Queue(maxsize=1000)

# Define a function to extract the markup from a URL
session = requests.Session()


def extract_markup(url):
    '''Function to extract markup from a URL'''
    try:
        response = session.get(url)
        return response.text
    except:
        return None

# Define a producer function to read URLs from a file and extract the markup
def producer():
    '''Function to read URLs from file to extract markup'''
    with open('urls.txt', 'r') as f:
        urls = f.readlines()
    with ThreadPoolExecutor(max_workers=10) as executor:
        for markup in executor.map(extract_markup, urls):
            if markup:
                link_queue.put(markup)
                

# Define a consumer function to parse the HTML and extract hyperlinks
def consumer():
    '''Function to parse HTML and extract hyperlinks'''
    while True:
        try:
            markup = link_queue.get(timeout=1)
            soup = BeautifulSoup(markup, 'lxml')
            links = [link.get('href') for link in soup.find_all('a')]
            with open('output.txt', 'a') as f:
                f.write(f'{links}\n')
            link_queue.task_done()
        except queue.Empty:
            break

# Define a function to run the producer and consumer concurrently
def run():
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer)
        executor.submit(consumer)
    link_queue.join()

if __name__ == '__main__':
    run()
