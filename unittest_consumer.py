import asyncio
import unittest
from extractor import consumer, producer


class TestConsumer(unittest.TestCase):
    async def test_consumer(self):
        urls = 'urls.txt'
        loop = asyncio.get_event_loop()
        file_path = 'output.txt'
        loop.run_until_complete(producer(urls))
        loop.run_until_complete(consumer(file_path))
        with open(file_path, 'r') as f:
            contents = f.read()
        self.assertTrue('https://www.python.org/psf/' in contents)
