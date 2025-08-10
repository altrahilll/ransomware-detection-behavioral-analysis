"""
Ransomware Detection using Behavioral Analysis
Author: Rahil Khan
Description:
 Personal project exploring behavioral ransomware detection
 using dynamic anaylsis and machine learning.
Date: 2025
"""

"""
Ransomware Detection using Behavioral Analysis
Author: Rahil Khan
Description:
    Personal project exploring behavioral ransomware detection
    using dynamic analysis and machine learning.
Date: 2025
"""

import unittest
import os
from app.detector import RansomwareDetector

class TestRansomwareDetector(unittest.TestCase):
    def setUp(self):
        self.detector = RansomwareDetector()

    def test_detect_changes(self):
        test_file = "test.txt"
        with open(test_file, "w") as f:
            f.write("Initial content")
        self.assertFalse(self.detector.detect_changes(test_file))
        with open(test_file, "w") as f:
            f.write("Changed content")
        self.assertTrue(self.detector.detect_changes(test_file))
        os.remove(test_file)

if __name__ == '__main__':
    unittest.main()
