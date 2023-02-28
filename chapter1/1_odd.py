from datetime import datetime
odds = range(1,60,2)
if datetime.today().minute in odds:
    print("this minute seems odd")
else:
    print("nothing odd here.")