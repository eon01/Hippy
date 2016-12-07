# Hippy
A Python Wrapper For Hipchat Apiv2

## Sending Notifications

Get you access token and find the room id.
You can choose the color (yellow, green, red, purple, gray, random), to notify the room or not (True, False) and the type of the message you're sending.

You can send messages to HipChat rooms as text, html, or cards.
- The HTML will be curated by HipChat.
- Allowed HTML tags: a, b, i, strong, em, br, img, pre, code, lists, tables.

``` python
from api.notify import Notify

key = ""
room_id = ""
n = Notify(key, room_id)
n.notify( "Testing Hippy", "red", "false", "text")
```

More documentation could be found on the official Hipchat website:
https://developer.atlassian.com/hipchat/guide/sending-messages




