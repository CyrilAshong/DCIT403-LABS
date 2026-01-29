import asyncio
import spade
from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour
from disaster_environment import DisasterEnvironment  # Import from above

class SensorAgent(Agent):
    class MonitorBehaviour(PeriodicBehaviour):
        async def on_start(self):
            print("SensorAgent started monitoring...")
            self.env = DisasterEnvironment()  

        async def run(self):
            # Simulate time passing
            self.env.simulate_time_step()

            # Perceive current state
            percept = self.env.get_percept()

            # Log the percept 
            print(f"[{percept['timestamp']}] Percept:")
            print(f"  Damage: {percept['damage_level']}%")
            print(f"  Temp: {percept['temperature']}°C")
            print(f"  Flood: {percept['flood_level']}m")
            if percept['recent_events']:
                print("  Recent events:")
                for ev in percept['recent_events']:
                    print(f"    - {ev}")
            print("-" * 40)

            # Save to file for deliverable
            with open("event_logs.txt", "a") as f:
                f.write(f"[{percept['timestamp']}] Damage: {percept['damage_level']}%, Temp: {percept['temperature']}°C, Flood: {percept['flood_level']}m\n")
                for ev in percept['recent_events']:
                    f.write(f"  Event: {ev}\n")

    async def setup(self):
        print(f"SensorAgent {self.jid} online.")
        behav = self.MonitorBehaviour(period=5)  # Sense every 5 seconds
        self.add_behaviour(behav)

async def main():
    agent = SensorAgent("sensoragent@localhost", "secret123")
    await agent.start(auto_register=True)

    print("SensorAgent running... Press Ctrl+C to stop.")
    await asyncio.sleep(120)  # Run for 2 minutes 

    await agent.stop()
    print("SensorAgent stopped.")

if __name__ == "__main__":
    spade.run(main())