from firebase import firebase

firebase = firebase.FirebaseApplication('https://basementautomation.firebaseio.com/')

firstCenter = firebase.get('HomeTheater/Controls/center',None)
firstCorner = firebase.get('HomeTheater/Controls/corner',None)
firstStrip = firebase.get('HomeTheater/Controls/strip',None)

"""def nextStep(center, corner, strip):
    centerNum = str(center)
    cornerNum = str(corner)
    stripNum = str(strip)
    if center != firstCenter:
        print('Change: ' + ' - ' + centerNum)"""


while True:
    center = firebase.get('HomeTheater/Controls/center',None)
    corner = firebase.get('HomeTheater/Controls/corner',None)
    strip = firebase.get('HomeTheater/Controls/strip',None)
    #nextStep(center, corner, strip)
    if center != firstCenter:
        print('Change: ' + str(firstCenter) + ' - ' + str(center))
        firstCenter = center
    if corner != firstCorner:
        print('Change: ' + str(firstCorner) + ' - ' + str(corner))
        firstCorner = corner
    if strip != firstStrip:
        print('Change: ' + str(firstStrip) + ' - ' + str(strip))
        firstStrip = strip