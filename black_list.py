import requests as req
import webbrowser as wb
x = req.get("http://56a7506c5435.ngrok.io/")
y = x.text.replace("<br>", "\n")
print(x)
print(y)
print("Report")



