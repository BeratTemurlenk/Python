from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:

y = 1

while robotArm.grab():
    for x in range(y):
        robotArm.moveRight()
    robotArm.drop()
    for b in range(y):
        robotArm.moveLeft()
    y += 1



robotArm.operate()








# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()