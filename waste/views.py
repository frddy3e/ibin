# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import Dispositivo
from .models import Historico_Dispositivo
# Create your views here.

def sumDig(n): 
    a = 0
    while n > 0: 
        a = a + (n % 10)
        n = int(n/10) 
    return a

def isValidEMEI(n): 
    s = str(n) 
    l = len(s)
    # If length is not 15 then IMEI is Invalid 
    if l != 15: 
        return False
  
    d = 0
    sum = 0
    for i in range(15, 0, -1): 
        d = (int)(n % 10) 
        if (i % 2) == 0: 
            d = 2 * d 
        sum = sum + sumDig(d) 
        n = n / 10
    return ((sum % 10) == 0) 
    

def estados_wasteView(request):
    try:
        if "filtro" in request.GET:
            filtro = str(request.GET["filtro"])
        else:
            filtro = "llenado"
            
        if "limite" in request.GET:
            limite = str(request.GET["limite"])
        else:
            if filtro == "llenado":
                limite = 70
            elif filtro == "bateria":
                limite = 30
            
        dispositivos = Dispositivo.objects.all()
        historico_dispositivos = Historico_Dispositivo.objects.all()
        dict={
            "filtro":filtro,
        }
        dic_dispositivos = []
        n_dispositivos = 0
        for dispositivo in dispositivos:
            historicos_dispositivos=Historico_Dispositivo.objects.filter(Imei = dispositivo.Imei)
            if len(historicos_dispositivos)>0:
                dispositivo_actual = historicos_dispositivos[len(historicos_dispositivos)-1]  #el ultimo registro guardado
                dic_dispositivos.append(dispositivo_actual)
                n_dispositivos+=1
                # if filtro == "llenado" and int(dispositivo_actual.Llenado) >= int(limite):
                    # n_dispositivos+=1
                    # dic_dispositivos.append(dispositivo_actual)
                # elif filtro == "bateria" and float(dispositivo_actual.Bateria) <= float(limite):
                    # n_dispositivos+=1
                    # dic_dispositivos.append(dispositivo_actual)
                # elif filtro == "volcamiento" and int(dispositivo_actual.Volcamiento) == 1:
                    # n_dispositivos+=1
                    # dic_dispositivos.append(dispositivo_actual)
                # elif filtro == "humo" and int(dispositivo_actual.Humo) == 1:
                    # n_dispositivos+=1
                    # dic_dispositivos.append(dispositivo_actual)
                    
        dict["n_dispositivos"] = n_dispositivos
        dict["dispositivos"] = dic_dispositivos
        
    except Exception as e:
        dict={
            "filtro":e,
        }
    return render(request,"estados_waste.html",dict)

def inicio_wasteView(request):
    dict={}
    dispositivos = Dispositivo.objects.all()
    n_dispositivos = 0
    n_dispositivos_llenos = 0
    dic_dispositivos = []
    for dispositivo in dispositivos:
        n_dispositivos+=1
        historicos_dispositivos=Historico_Dispositivo.objects.filter(Imei = dispositivo.Imei)
        if len(historicos_dispositivos)>0:
            # for disp in historicos_dispositivos:
               # dic_dispositivos.append(disp)
               
            #dispositivo_actual = historicos_dispositivos[0]  #el ultimo registro guardado
            dispositivo_actual = historicos_dispositivos[len(historicos_dispositivos)-1]  #el ultimo registro guardado
            dispositivo_actual.Id = n_dispositivos
            dic_dispositivos.append(dispositivo_actual)
        
    dict["n_dispositivos"] = n_dispositivos
    dict["dispositivos"] = dic_dispositivos
    # dict["n_dispositivos_llenos"] = n_dispositivos_llenos
    return render(request,"inicio_waste.html",dict)
	
# def historico_wasteView(request):
	# dict={}
	# dispositivos = Dispositivo.objects.all()
	# n_dispositivos = 0
	# dic_dispositivos = []
	# for dispositivo in dispositivos:
		# n_dispositivos+=1
		# dic_historicos = []
		# historicos_dispositivos=Historico_Dispositivo.objects.filter(Imei = dispositivo.Imei)
		# if len(historicos_dispositivos)>0:
			# for disp in historicos_dispositivos:
				# dic_historicos.append(disp)
			# dict[dispositivo.Imei] = dic_historicos
			   
			# dispositivo_actual = historicos_dispositivos[0]  #el ultimo registro guardado
			# dispositivo_actual = historicos_dispositivos[len(historicos_dispositivos)-1]  #el ultimo registro guardado
			# dispositivo_actual.Id = n_dispositivos
			# dic_dispositivos.append(dispositivo_actual)

	# dict["n_dispositivos"] = n_dispositivos
	# dict["dispositivos"] = dic_dispositivos
    
        # diccionario={}
        # diccionario["informacion"]=dict
    
	# return render(request,"historico_waste.html",diccionario)
    
def historico_wasteView(request):
    dict={}
    dispositivos = Dispositivo.objects.all()
    dic_dispositivos = []
    n_dispositivos = 0
    for dispositivo in dispositivos:
        n_dispositivos+=1
        historicos_dispositivos=Historico_Dispositivo.objects.filter(Imei = dispositivo.Imei)
        if len(historicos_dispositivos)>0:
            dispositivo_actual = historicos_dispositivos[0]  #el ultimo registro guardado
            dispositivo_actual = historicos_dispositivos[len(historicos_dispositivos)-1]  #el ultimo registro guardado
            dispositivo_actual.Id = n_dispositivos
            dic_dispositivos.append(dispositivo_actual)
    dict["n_dispositivos"] = n_dispositivos
    dict["dispositivos"] = dic_dispositivos
    dict["historicos"] = Historico_Dispositivo.objects.all()
    return render(request,"historico_waste.html",dict)

def actualizar_wasteView(request):
    try:
        latitud = str(request.GET["latitud"])
        longitud = str(request.GET["longitud"])
        imei = str(request.GET["imei"])
        llenado = str(request.GET["llenado"])
        bateria = str(request.GET["bateria"])
        humo = str(request.GET["humo"])
        volcamiento = str(request.GET["volcamiento"])
        fecha = str(request.GET["fecha"])
        respuesta = "OK"
        
        dispositivos = Dispositivo.objects.all()
        for dispositivo in dispositivos:
            if dispositivo.Imei == imei:
                if isValidEMEI(int(imei)): 
                    historico_dispositivo = Historico_Dispositivo( Imei = imei, Latitud = latitud, Longitud = longitud, Llenado = llenado, Bateria = bateria, Humo = humo, Volcamiento = volcamiento,  FechaDispositivo = fecha)
                    historico_dispositivo.save()
                    respuesta = "OK WASTE"
        
    except Exception as e:
        respuesta=e
    return HttpResponse(respuesta)