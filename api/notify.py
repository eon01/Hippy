import requests
import json

class Notify():

    def __init__(self, token, room_id):
        self.base = "https://api.hipchat.com"
        self.route = "/v2/room/%s/notification" % (room_id)
        self.url = self.base + self.route
        self.token = token
        self.headers = {
            'Authorization': 'Bearer {}'.format(token),
            'Accept': 'application/json',
            'Content-type': 'application/json',
        }


    def notify(self, message, color='green', notify='true', message_format='text'):

        self.params = json.dumps({
            'message': message,
            'color': color,
            'notify': notify,
            'message_format': message_format
            })

        #print self.params

        x = requests.post(
                self.url,
                self.params,
                headers=self.headers,

            )

        #print x.text
        #print dir(x)
