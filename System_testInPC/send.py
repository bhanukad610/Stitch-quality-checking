import urllib.request   
import urllib.parse      

def sendToServer(user, numOfFrames):
    url = "https://stitchqualitychecking.000webhostapp.com/add_data.php"   
    params = {      "user": user,       
                    "numOfFrames": numOfFrames,       
            }      

    query_string = urllib.parse.urlencode( params )     
    url = url + "?" + query_string      
    with urllib.request.urlopen( url ) as response:        
        response_text = response.read()        
        print( response_text )

sendToServer('disa', 20)