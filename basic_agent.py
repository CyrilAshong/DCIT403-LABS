import asyncio
import spade
from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour

class HelloAgent(Agent):
    class SayHelloBehaviour(PeriodicBehaviour):
        async def run(self):
            print(f"Hello from {self.agent.jid}! (periodic message every 4 seconds)")

    async def setup(self):
        print(f"Agent {self.jid} starting up...")
        self.add_behaviour(self.SayHelloBehaviour(period=4))  

async def main():
    # local username + password
    agent = HelloAgent("helloagent@localhost", "mypassword123")

    # Start the agent 
    await agent.start(auto_register=True)

    print("Agent is now connected and running. Waiting...")

    # Keep alive for 40 seconds to see several messages
    await asyncio.sleep(40)

    
    await agent.stop()
    print("Agent stopped.")

if __name__ == "__main__":
    spade.run(main())  