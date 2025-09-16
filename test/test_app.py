import unittest
from app import App

class TestCodeLineCounter(unittest.TestCase):

    def test_single_java_file(self):
        counter = App()
        stats = counter.count_file_lines('test/sample_files/test_data1.java')

        assert stats.blank == 3
        assert stats.comments == 3
        assert stats.code == 6
        assert stats.total == 12
    
    def test_single_python_file(self):
        counter = App()
        stats = counter.count_file_lines('test/sample_files/test_data2.py')

        assert stats.blank == 5
        assert stats.comments == 3
        assert stats.code == 4
        assert stats.total == 12
    
    def test_single_python_file(self):
        counter = App()
        stats = counter.count_file_lines('test/sample_files/test_data2.py')

        assert stats.blank == 5
        assert stats.comments == 3
        assert stats.code == 4
        assert stats.total == 12
    
    def test_single_javascript_file(self):
        counter = App()
        stats = counter.count_file_lines('test/sample_files/test_data1.js')
        
        assert stats is None
    
    def test_directory_files(self):
        counter = App()
        stats = counter.count_directory_file_lines('test/sample_files')

        assert len(stats) == 5
        assert stats['test/sample_files/test_data3.py'].blank == 3
        assert stats['test/sample_files/test_data3.py'].comments == 2
        assert stats['test/sample_files/test_data3.py'].code == 4
        assert stats['test/sample_files/test_data3.py'].total == 9

if __name__ == "__main__":
    unittest.main()