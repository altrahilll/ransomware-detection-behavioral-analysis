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
from app.alert import AlertSystem

class TestAlertSystem(unittest.TestCase):
    def test_send_alert(self):
        alert_system = AlertSystem(["test@example.com"])
        try:
            alert_system.send_alert("This is a test alert")
            self.assertTrue(True)  # If no exceptions, the test passes
        except Exception as e:
            self.fail(f"Alert sending failed with error: {e}")

if __name__ == '__main__':
    unittest.main()
