from django.shortcuts import render
from datetime import datetime
from msgapp.models import MsgData
# Create your views here.

def msgproc(request):

    datalist = []

    if request.method == "POST":
        userA = request.POST.get("userA", None)
        userB = request.POST.get("userB", None)
        msg = request.POST.get("msg", None)
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("msgdata.txt", "a+") as f:
            f.write("{}--{}--{}--{}\n".format(userB, userA, msg, time))

    if request.method =="GET":
        userC = request.GET.get("userC", None)
        if userC != None:
            with open("msgdata.txt", "r") as f:
                cnt =0
                for line in f:
                    linedata = line.split("--")
                    if linedata[0] == userC:
                        cnt = cnt +1
                        d = {
                            "userA": linedata[1],
                            "msg":linedata[2],
                            "time":linedata[3]
                        }
                        datalist.append(d)
                    if cnt >=10:
                        break
                
    if request.method == "DELETE":
        with open("msgdata.txt", "w") as f:
            f.truncate()

    return render(request, "msgweb.html", {"data":datalist})

