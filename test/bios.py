import requests

def buildUrl(model):
    url = "https://www.asus.com/my/supportonly/{modelNoStr}/HelpDesk_Bios/".format(modelNoStr=model)
    return url

modelNoInput = input("Enter Model No: \n")

output = buildUrl(modelNoInput)

print(output)
