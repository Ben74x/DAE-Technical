import asyncio
import unittest
from extractor import producer
import tracemalloc

tracemalloc.start()

class TestProducer(unittest.TestCase):

    async def test_producer(self):
        urls = "urls.txt"
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(producer(urls))
        loop.run_until_complete(future)
        self.assertIsNotNone(future.result())
        loop.close()
        await asyncio.sleep(5)

tracemalloc.stop()
if __name__ == '__main__':
    asyncio.run(unittest.main())
