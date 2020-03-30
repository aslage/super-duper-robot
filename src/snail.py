
# Here we will devise a function to find the number of days for the snail to escape

WELL_HEIGHT=125
CLIMB_SPEED=30
CLIMB_SLIPPERY=20

def escapeSnail(height,climb,slip):
    days=0
    diff=height
    while diff>0:
        diff=diff-(climb-slip)
        days=days+1
    return days

print(escapeSnail(WELL_HEIGHT,CLIMB_SPEED,CLIMB_SLIPPERY))