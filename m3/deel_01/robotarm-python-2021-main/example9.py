from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
for x in range(1, 5):    
    for a in range(1, x+1):
        robotArm.grab()
        for j in range(5):
            robotArm.moveRight()
        robotArm.drop()
        if x == a:
            aantal = 4
        else:
            aantal = 5
        for j in range(aantal):
            robotArm.moveLeft()

        
       
        




    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()