# LAB 1: Environment and Agent Platform Setup Report

- **Student:** Cyril Ashong.
- **ID:** 11253767.
- **Date:** 29 January 2025.  


# LAB 1: Summary of Setup 
 
- Created a new GitHub repository and launched Codespace.  
- Verified Python and installed SPADE via `pip install spade`.  
- Started the embedded XMPP server with `spade run`.  
- No manual user registration needed — used `auto_register=True`.  
- Implemented and run a basic periodic HelloAgent that prints messages every 3 seconds.  

**Issues Encountered**  
- None major. Initial SPADE install was required (not pre-installed).  
- Kept `spade run` in a separate terminal to maintain server connection.  

**Conclusion**  
The environment is fully configured. A basic SPADE agent deploys successfully using the built-in XMPP server. Ready for multi-agent extensions.


# LAB 2: Percepts Explanation

The SensorAgent perceives the simulated disaster environment every 5 seconds via a PeriodicBehaviour.

Percepts include:
- timestamp: Current time of sensing.
- damage_level (%): Structural damage from events (0–100).
- temperature (°C): Rising during fires.
- flood_level (m): Water accumulation.
- recent_events: List of last disasters (e.g., "Earthquake! Damage +35 → 45").

These percepts represent the agent's sensory input, enabling future decision-making (e.g., alert if damage > 70%). Events are generated randomly to mimic real unpredictability.