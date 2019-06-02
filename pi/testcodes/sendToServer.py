import urllib.request

def sendToServer(user, numOfFrames):
    req = urllib.request.urlopen("https://stitchqualitychecking.000webhostapp.com/add_data.php?user="+user+"&numOfFrames="+numOfFrames)
    print(req.read())


sendToServer('pola', '1')
