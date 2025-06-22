import unittest
import os
import sys

def run_all_tests():
    src_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
    sys.path.insert(0, src_dir)
    
    # wszystkie pliki testowe w katalogu
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir='test', pattern='test_*.py')
    
    # testy z wyjściem szczegółowym
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)
    
    # kod zakończenia (0 jeśli wszystkie testy przeszły, 1 jeśli nie)
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    # katalog projektu do ścieżki 
    project_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, project_dir)
    
    # wszystkie testy
    exit_code = run_all_tests()
    sys.exit(exit_code)
