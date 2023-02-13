# This script creates an object of type Energy for doing energy save tasks
# To run this script type the following:
#     python -i start_energy.py
# The -i is needed to keep Python running, otherwise it will create the object and exit
from energy.energy_32id import Energy32ID
ts = Energy32ID(["../../db/energy_settings.req", 
			 "../../db/energy_32ID_settings.req"], 
			 {"$(P)":"32id:", "$(R)":"Energy:"})
