import os
import unittest

class TestProducerConsumer(unittest.TestCase):
    
    def setUp(self):
        # create a test file with some URLs
        with open('test_urls.txt', 'w') as f:
            f.write('http://example.com/\n')
            f.write('https://bdwumah.dev/\n')
        
    def tearDown(self):
        # remove the test file and output file
        os.remove('test_urls.txt')
        os.remove('test_output.txt')
    
    def test_producer_consumer(self):
        # run the producer and consumer functions
        from extractor import run
        
        with open('test_output.txt', 'w') as f:
            f.write('')
        
        run('test_urls.txt', 'test_output.txt')
        
        # check that the output file was created and has the expected content
        with open('test_output.txt', 'r') as f:
            output = f.read()
            self.assertIn('https://www.iana.org/domains/example', output)


# run on terminal: python -m unittest test.py
