from dataclasses import dataclass, field
from math import asin, cos, radians, sin, sqrt

@dataclass
class Position:
	name: str
	lon: float
	lat: float

	"""
	For reference: adding a default value and a metadata about that value
	
	lon: float = field(default=0.0, metadata={'unit': 'degrees'})
	lat: float = field(default=0.0, metadata={'unit': 'degrees'})

	If we define a default value, the subclasses must also 
	define a default value for their attributes (in our example
	Capital should have the country attribute filled with some
	default value, for instance)
	"""

	def distance_to(self, other):
		r = 6371 # Earth radius in kilometers
		lam_1, lam_2 = radians(self.lon), radians(other.lon)
		phi_1, phi_2 = radians(self.lat), radians(other.lat)
		h = (sin((phi_2 - phi_1) / 2) ** 2
		+ cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2) ** 2)
		return 2 * r * asin(sqrt(h))

# dataclass supports inheritance as well
@dataclass
class Capital(Position):
	country: str