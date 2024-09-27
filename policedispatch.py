# police_dispatch_system.py

class DispatchRecord:
    def __init__(self, dispatch_id, description):
        self.dispatch_id = dispatch_id
        self.description = description
        self.response_times = []

    def add_response_time(self, time):
        self.response_times.append(time)

    def average_response_time(self):
        if not self.response_times:
            return 0
        return sum(self.response_times) / len(self.response_times)

class DispatchManager:
    def __init__(self):
        self.dispatches = {}

    def create_dispatch(self, dispatch_id, description):
        if dispatch_id in self.dispatches:
            raise ValueError(f"Dispatch ID {dispatch_id} already exists.")
        self.dispatches[dispatch_id] = DispatchRecord(dispatch_id, description)

    def read_dispatch(self, dispatch_id):
        return self.dispatches.get(dispatch_id)

    def update_dispatch(self, dispatch_id, new_description):
        if dispatch_id not in self.dispatches:
            raise ValueError(f"Dispatch ID {dispatch_id} does not exist.")
        self.dispatches[dispatch_id].description = new_description

    def delete_dispatch(self, dispatch_id):
        if dispatch_id not in self.dispatches:
            raise ValueError(f"Dispatch ID {dispatch_id} does not exist.")
        del self.dispatches[dispatch_id]

class ResponseTimeTracker:
    def __init__(self):
        self.response_times = []

    def add_response_time(self, time):
        self.response_times.append(time)

    def average_response_time(self):
        if not self.response_times:
            return 0
        return sum(self.response_times) / len(self.response_times)

# Unit Tests

import unittest

class TestPoliceDispatchSystem(unittest.TestCase):
    def test_dispatch_creation(self):
        dm = DispatchManager()
        dm.create_dispatch(101, "Robbery in progress")
        self.assertIn(101, dm.dispatches)

    def test_dispatch_read(self):
        dm = DispatchManager()
        dm.create_dispatch(102, "Assault in progress")
        dispatch = dm.read_dispatch(102)
        self.assertEqual(dispatch.description, "Assault in progress")

    def test_dispatch_update(self):
        dm = DispatchManager()
        dm.create_dispatch(103, "Theft in progress")
        dm.update_dispatch(103, "Theft in progress - Suspect apprehended")
        self.assertEqual(dm.read_dispatch(103).description, "Theft in progress - Suspect apprehended")

    def test_dispatch_delete(self):
        dm = DispatchManager()
        dm.create_dispatch(104, "Fraud report")
        dm.delete_dispatch(104)
        self.assertNotIn(104, dm.dispatches)

    def test_response_time(self):
        rt = ResponseTimeTracker()
        rt.add_response_time(300)
        rt.add_response_time(450)
        self.assertEqual(rt.average_response_time(), 375)

if __name__ == '__main__':
    unittest.main()
