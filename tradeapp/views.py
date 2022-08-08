from django.shortcuts import render
import time
import asyncio
import talib
import numpy
import requests
from django.http import JsonResponse
from operator import itemgetter
from django.views.decorators.csrf import csrf_exempt
from .models import Bot, Indicator
import json
from django.forms.models import model_to_dict

def Extract(lst,index = 4):
    return list(map((itemgetter(index)), lst ))

async def index(request):
    #time.sleep(5)
    print("asssd")
    

    #await asyncio.sleep(20)
    return render(request, 'index.html')

def SeeBot(request,see_bot):
    return render(request, 'index2.html',{"id":see_bot})

def GetOneBot(request,see_bot):
    bot = Bot.objects.get(pk=see_bot)
    a = model_to_dict(bot)
    a["indicadores"] = list(bot.indicator_set.values())
    return JsonResponse({"ok":"data","bot":a})

def getBot(request):
    bots = Bot.objects.all()
    bot_r = []
    for bot in bots:
        print(len(bot.indicator_set.all()))
        a = model_to_dict(bot)
        a["indicators"] = list(bot.indicator_set.values())
        print(a)
        bot_r.append(a)
    return JsonResponse({"ok":"data","bots":bot_r})

@csrf_exempt
def saveBot(request):
    data = json.loads(request.body.decode('utf-8'))
    print(data)

    a = Bot()
    a.name = data.get("name")
    a.description = data.get("description")
    a.temp = data.get("temp")
    a.estado = data.get("estado")
    a.save()
    for indicador in data["indicadores"]:
        b = Indicator()
        b.name = indicador["name"]
        b.parameters = indicador["parameters"]
        b.condition = indicador["condition"]
        b.bot = a
        b.save()
    return JsonResponse({"ok":"datasave"})

def getEma(request):
    #broker = Binance() or InterativeBroker()
    #broker.doOrder()
    response = requests.get("https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=100")

    #requests.post("https://api.binance.com/api/v3/order?symbol=BTCUSDT&mount=1m&limit=100",data={credenciales:request.user.credenciales})
    datos = response.json()
    print(Extract(datos))
    data = numpy.array(Extract(datos))
    data = data.astype(numpy.float)
    output = talib.EMA(data,2)
    print(output)
    return JsonResponse({"ema":output[len(output) - 1]})

def CheckEntrada(request,see_bot):
    #broker = Binance() or InterativeBroker()
    #broker.doOrder()
    bot = Bot.objects.get(pk=see_bot)

    response = requests.get(f"https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval={bot.temp}&limit=100")
    
    #requests.post("https://api.binance.com/api/v3/order?symbol=BTCUSDT&mount=1m&limit=100",data={credenciales:request.user.credenciales})
    datos = response.json()
    print(Extract(datos))
    data_close = numpy.array(Extract(datos))
    data_close = data_close.astype(numpy.float)
    data_low = numpy.array(Extract(datos,3))
    data_low = data_low.astype(numpy.float)
    data_high = numpy.array(Extract(datos,2))
    data_high = data_high.astype(numpy.float)
    calculos = []
    for indicador in bot.indicator_set.all():
        if(indicador.name == "ema"):
            output = talib.EMA(data_close,int(indicador.parameters))
            calculos.append(output[len(output) - 1])
        if(indicador.name == "adx"):
            output = talib.ADX(data_high,data_low,data_close,int(indicador.parameters))
            calculos.append(output[len(output) - 1])
    print(output)
    return JsonResponse({"exito":False,"emas":calculos})
'''
class Binance():

    doOrder():
         requests.post("https://api.binance.com/api/v3/order?symbol=BTCUSDT&mount=1m&limit=100",data={credenciales:request.user.credenciales})
'''