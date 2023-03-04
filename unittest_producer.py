import asyncio
import unittest
from extractor import producer
import tracemalloc

tracemalloc.start()

class TestProducer(unittest.TestCase):

    async def test_producer(self):
        urls = "test_urls.txt"
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(producer(urls))
        loop.run_until_complete(future)
        loop.close()
        await asyncio.sleep(5)


if __name__ == '__main__':
    asyncio.run(unittest.main())
