from api.notify import Notify

key = ""
room_id = ""
n = Notify(key, room_id)
n.notify( "Testing Hippy", "red", "false", "text")
