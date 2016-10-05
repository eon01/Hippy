# Hippy
A Python Wrapper For Hipchat Api v2

# How To Use Hippy To Send Notifications To A Specefic Room

``` python
from api.notify import Notify

key = ""
room_id = ""
n = Notify(key, room_id)
n.notify( "Testing Hippy", "red", "false", "text")
```
