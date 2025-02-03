import unittest
from scheduler.fcfs import schedule_processes

class TestFCFSScheduler(unittest.TestCase):
    def test_fcfs(self):
        processes = [
            {'id': 1, 'arrival': 0, 'burst': 4, 'priority': 1},
            {'id': 2, 'arrival': 1, 'burst': 3, 'priority': 2},
        ]
        schedule = schedule_processes(processes)
        self.assertEqual(schedule[0]['start'], 0)
        self.assertEqual(schedule[0]['finish'], 4)
        self.assertEqual(schedule[1]['start'], 4)
        self.assertEqual(schedule[1]['finish'], 7)

if _name_ == '_main_':
    unittest.main()
