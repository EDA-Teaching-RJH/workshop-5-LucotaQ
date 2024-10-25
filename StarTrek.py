import random 
# Constants 
MISSION_TYPES = ["Exploration", "Diplomacy", "Combat", "Rescue", "Scientific Research"] 
# Ship systems, resources, and crew 
ship = { 
		"systems": { 
		"shields": 100, 
		"weapons": 100, 
		"engines": 100, 
		"sensors": 100 
		}, 
		"resources": { 
			"energy": 1000, 
			"torpedoes": 10 
		}, 
		"crew": { 
			"Picard": "Command", 
			"Riker": "Command", 
			"Data": "Operations", 
			"Worf": "Operations", 
			"La Forge": "Operations", 
			"Crusher": "Sciences", 
			"Troi": "Sciences" 
		} 
	} 

def main(): 
	print("Welcome to the Star Trek: TNG Mission Simulator!") 
	score = 0 
	turns = 0 

	while True: 
		display_status() 
		action = get_user_action() 

	if action == "1": 
		score += run_mission() 
	elif action == "2": 
		repair_system() 
	elif action == "3": 
		add_crew_member() 
	elif action == "4": 
		print(f"Simulation ended. Final score: {score}") 
		break 
	else: 
		print("Invalid action. Please try again.") 
		
	turns += 1 
	handle_random_event() 

	if turns % 3 == 0: 
		replenish_resources() 

def display_status(): 
	ship_power_supply = randint(1 , 100)

def get_user_action(): 
	useraction = input("What would you like to do Commander" + name)
	return useraction

def run_mission(): 
	mission_type = random.choice(MISSION_TYPES) 
	print(f"\nNew mission: {mission_type}") 
Exploration: # next line
	

def repair_system(): 

	outerforcefield = (randint(1, 100))
	if outerforcefield == >=25:
		print ("FORCEFIELD INTEGRITY CRITICAL! TEND TO IMMDEIATELY!")
	elif outerforcefield == 26=<50:
		print ("Forcefield integrity approaching critical state. Please tend to as soon as possible.")
	elif outerforcefield == 51=<75:
		print ("Forcefield integrity healthy. Do not forget to recharge when not in use.")
	else:
		print ("Forcefield integrity is safe. No need to recharge currently.")
	
	enginesystem = (randint(1, 100))
	if enginesystem == 
 
def add_crew_member(): 


def handle_random_event():
# TODO: Implement random events that can occur during the simulation 

def use_resource(resource, amount): 
# TODO: Implement resource usage logic 

def replenish_resources(): 

