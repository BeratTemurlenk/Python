from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:




a = 9
b = 8

for h in range(5):
    robotArm.grab() 
    for y in range(a): 
        robotArm.moveRight()
    robotArm.drop()
    for x in range(b):
        robotArm.moveLeft()
    a = a - 2
    b = b - 2 




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()