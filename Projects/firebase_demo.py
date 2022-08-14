from firebase import firebase

firebase = firebase.FirebaseApplication('https://fir-demo-4db43.firebaseio.com/')


def nextStep(result):
    if result == "hello":
        print('nice')

    else:
        print('')

while True:
    result = firebase.get('/creations/bday',None)
    print(result)

