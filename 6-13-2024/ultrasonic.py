from gpiozero import DistanceSensor
ultra=DistanceSensor(echo=21, trigger=20)
while True:
    print(round(ultra.distance*100,3))
