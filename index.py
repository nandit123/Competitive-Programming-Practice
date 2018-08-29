import math

print('Welcome to Telemetry')

#defining key variables

# Vehicle Parameters
frontalArea = float(input('enter frontalArea: '))
coefficientOfDrag = float(input('enter coefficientOfDrag: '))
numberOfWheels = float(input('enter numberOfWheels: '))
wheelDiameter = float(input('enter wheelDiameter: ')) # in m
weight = float(input('enter weight: '))
ambientTemperature = float(input('enter ambientTemperature: '))
fuelDensity = float(input('enter fuelDensity: '))
trackInclination = float(input('enter trackInclination: ')) # in degrees
coefficientOfRollingResistance = float(input('enter coefficientOfRollingResistance: '))
momentOfInertiaOfWheel = float(input('enter momentOfInertiaOfWheel: ')) # Kg-m**2

# Engine Parameters
engine = "x" #4 types of engines
engineVolume = float(input('enter engineVolume: ')) # in cc
engineMaxPower = float(input('enter engineMaxPower: ')) # in Kw
engineMaxTorque = float(input('enter engineMaxTorque: ')) # in N-M
engineMaxRPM = float(input('enter engineMaxRPM: ')) # (Rev/Min)
engineTransmissionRatio = float(input('enter engineTransmissionRatio: '))
engineTransmissionEfficiency = float(input('enter engineTransmissionEfficiency: '))
momentOfInertiaOfEngine = float(input('enter momentOfInertiaOfEngine: ')) # Kg/m**2
engineRPMatMaxTorque = float(input('enter engineRPMatMaxTorque: ')) # (Rev/min)
engineRPMatMaxPower = float(input('enter engineRPMatMaxPower: ')) # (Rev/min)

# Gear Box Parameters
gearBoxUsed = float(input('enter gearBoxUsed: ')) # 0 for not used, 1 for used
gearRatio = float(input('enter gearRatio: '))
gearEfficiency = float(input('enter gearEfficiency: '))
gearMOI = float(input('enter gearMOI: '))

# Engine Cycles Parameters
drivingDistance = 0
coastingDistance = 0

# Simulated Output Parameters
Mileage = 0 # in Km/L
totalDistance = 0 # in Km
fuelConsumed = 0 # in L

# other key variables and formulaes
TRQ = ((engineMaxPower*1000*60) / (2*3.14*engineRPMatMaxPower))
AD = 1.225 # to be checked if it is string or not
gear = engineTransmissionRatio*gearRatio
velocity = 0

F = ((TRQ * engineTransmissionEfficiency * gear) / (0.5 * wheelDiameter))
M = (weight) + (4/(wheelDiameter*wheelDiameter)) * ((momentOfInertiaOfEngine*engineTransmissionRatio*engineTransmissionRatio)/engineTransmissionEfficiency + (gearMOI*gearRatio*gearRatio)/gearEfficiency + momentOfInertiaOfWheel)
# R changes with velocity, F & R remains constant
R = (9.81 * weight * coefficientOfRollingResistance) + (coefficientOfDrag * AD * frontalArea * velocity * velocity * 0.5) + (9.81 * weight * math.sin(trackInclination*2*3.14/360)) # conversion of degree to radians for sign function

t = 0.5

BSFCVALUE = 0.5529 # for HONDA GX25 Engine (value varies with the engine)
while(totalDistance < 500):
	I = (4.2 / (F-R)/M)
	acceleration = 0;
	
	if(velocity > 8.4):
		acceleration = ((-R)/M)
	
	if(velocity < 4.2):
		acceleration = ((F - R)/M)

	velocity = velocity + acceleration*t
	distance = (velocity*t) + (0.5 * acceleration * (t**2))
	totalDistance += distance
	fuelConsumed += (BSFCVALUE * engineMaxPower * t)/fuelDensity

	if(acceleration == (-R/M)):
		coastingDistance += distance
	else:
		drivingDistance += distance

print('totalDistance = ', totalDistance)
print('drivingDistance = ', drivingDistance)
print('coastingDistance = ', coastingDistance)

Mileage	= (totalDistance/fuelConsumed)



