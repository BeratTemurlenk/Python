from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:


for x in range(8):
    robotArm.moveRight()


robotArm.speed = 3

for x in range(9):
    robotArm.grab()
    scanKleur = robotArm.scan()
    if scanKleur == 'red':
        robotArm.moveRight()
        robotArm.drop()
        if x < 8:
            robotArm.moveLeft()
            robotArm.moveLeft()
    else:
        robotArm.drop()
        if x < 8:
            robotArm.moveLeft()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()