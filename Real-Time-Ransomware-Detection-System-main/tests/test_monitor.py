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
from app.monitor import RansomwareMonitor

class TestRansomwareMonitor(unittest.TestCase):
    def test_on_created(self):
        monitor = RansomwareMonitor(["/dummy/path"])
        monitor.on_created(type('test', (object,), {'src_path': '/dummy/path/new_file.txt'}))
        self.assertTrue(True)  # Add assertions as needed

if __name__ == '__main__':
    unittest.main()
