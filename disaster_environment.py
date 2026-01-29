import random
import time
from datetime import datetime

class DisasterEnvironment:
    def __init__(self):
        self.damage_level = 0      # 0-100 (severity)
        self.temperature = 25.0    # Celsius
        self.flood_level = 0       # meters
        self.event_history = []    # Log of disasters

    def simulate_time_step(self):
        """Simulate passage of time: possible random events."""
        # Random chance of disaster every step
        event = None
        if random.random() < 0.15:  # ~15% chance per step
            event_type = random.choice(["earthquake", "flood", "fire"])
            if event_type == "earthquake":
                increase = random.randint(20, 50)
                self.damage_level = min(100, self.damage_level + increase)
                event = f"Earthquake! Damage +{increase} → {self.damage_level}"
            elif event_type == "flood":
                increase = random.uniform(0.5, 2.0)
                self.flood_level += increase
                event = f"Flood rising! Level +{increase:.1f}m → {self.flood_level:.1f}m"
            elif event_type == "fire":
                increase = random.randint(10, 30)
                self.damage_level = min(100, self.damage_level + increase)
                self.temperature += random.uniform(5, 15)
                event = f"Fire outbreak! Damage +{increase}, Temp +{self.temperature-25:.1f}°C"

        if event:
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.event_history.append(f"[{timestamp}] {event}")
            print(f"EVENT: {event}")  # Immediate log

        # Natural decay/recovery (small random changes)
        self.damage_level = max(0, self.damage_level - random.uniform(0.5, 2.0))
        self.temperature = max(20, self.temperature - random.uniform(0.1, 0.5))

    def get_percept(self):
        """What the agent 'senses' right now."""
        return {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "damage_level": round(self.damage_level, 1),
            "temperature": round(self.temperature, 1),
            "flood_level": round(self.flood_level, 1),
            "recent_events": self.event_history[-3:] if self.event_history else ["No events yet"]
        }