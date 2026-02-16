import os
import json
from datetime import datetime

class ApplicationTracker:
    def __init__(self, storage_file="applications.json"):
        self.storage_file = storage_file
        # This identifies the name of this specific script
        self.filename = os.path.basename(__file__)
        
    def save_application(self, company, position, status="Applied"):
        """Saves a new application entry with a timestamp and file reference."""
        data = self.load_all()
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "company": company,
            "position": position,
            "status": status,
            "recorded_by": self.filename
        }
        data.append(entry)
        
        with open(self.storage_file, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"✔️ Entry added via {self.filename}")

    def load_all(self):
        """Loads all entries from the JSON database."""
        if not os.path.exists(self.storage_file):
            return []
        with open(self.storage_file, 'r') as f:
            return json.load(f)

# --- Execution Block ---
if __name__ == "__main__":
    tracker = ApplicationTracker()
    
    print(f"--- Application Tracker Logic Active ({tracker.filename}) ---")
    
    # Example usage:
    tracker.save_application("Cyberdyne Systems", "AI Developer", "Pending")
    
    # Display the current list
    apps = tracker.load_all()
    print(f"\nTotal Applications tracked: {len(apps)}")
    for app in apps:
        print(f"[{app['date']}] {app['company']} - {app['position']} ({app['status']})")
