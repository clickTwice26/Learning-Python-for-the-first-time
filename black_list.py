import requests as req
import webbrowser as wb
x = req.get("http://38f0b3cb970c.ngrok.io/")
y = x.text.replace("<br>", "\n")
print(x)
print(y)
print("Report")



