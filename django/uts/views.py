from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
import paho.mqtt.client as mqtt
import sqlite3
from joblib import load

from .serializers import SensorSerializer, SensorSerializer2, SensorSerializer3, ActuatorSerializer
from .models import Sensor, Sensor2, Sensor3, Actuator

def webview(request):
    """A view of all bands."""
    view = Sensor.objects.all().values()
    view2 = Sensor2.objects.all().values()
    view3 = Sensor3.objects.all().values()

    act1 = Actuator.objects.filter(name__icontains='valve')
    act2 = Actuator.objects.filter(name__icontains='circuit_breaker')
    act3 = Actuator.objects.filter(name__icontains='vsd')
    return render(request, 'webview.html', {'views1': view, 'views2':view2, 'views3':view3, 'views_act1':act1, 'views_act2':act2, 'views_act3':act3})

class SensorDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()
    def retrieve(self, request, *args, **kwargs):
        temp = Sensor.objects.get(name="temp")
        frik = Sensor.objects.get(name="frik")
        dl = Sensor.objects.get(name="dl")
        sensor_value={"Sensor Temperatur": int(temp.value), "Sensor Friksi": int(frik.value),"Sensor Daya Listrik": int(dl.value)}
        return Response(sensor_value)     


def add_act():
    sensors = []
    temp = []
    data_base = "db.sqlite3"

    # Connect to database
    conn = sqlite3.connect(data_base)
    c = conn.cursor()

    test = ["uts_sensor", "uts_sensor2", "uts_sensor3"]

    for t in test:
        for i in range(3):
            query = f'Select * from {t}'

            c.execute(query)
            data1 = c.fetchall()

            temp.append(int(data1[i][2]))
        # print(temp)
        sensors.append(temp)
        temp = []

    models = ["system1.joblib", "system2.joblib", "system3.joblib"]
    acts = ["valve", "circuit_breaker", "vsd"]
    for i in range(len(models)):
        temp_query = f'uts/models/{models[i]}'
        model = load(temp_query)

        # Use the model to make predictions
        predicted_value = model.predict([sensors[i]])[0]

        predicted_value_json = predicted_value.tolist()

        # Create a dictionary with the predicted value
        data = {
            'value': predicted_value_json
        }
        
        act = Actuator.objects.get(name=acts[i])
        serializer = ActuatorSerializer(act, data=data, partial=True)
        # print("test")
        if serializer.is_valid():
            serializer.save()
            # print('added a new Actuator data', i, " ", predicted_value)


def on_message_temp(client, userdata, msg):
    temp = Sensor.objects.get(name="temp")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(temp, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new Temperatur data ', msg.payload.decode('utf-8'))
    
    return Response({"value": msg.payload.decode('utf-8')}) 
    
def on_message_frik(client, userdata, msg):
    frik = Sensor.objects.get(name="frik")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(frik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new Friksi data ', msg.payload.decode('utf-8'))   
    return Response({"value": msg.payload.decode('utf-8')})
    
def on_message_dl(client, userdata, msg):
    dl = Sensor.objects.get(name="dl")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new Daya Listrik data ', msg.payload.decode('utf-8'))    
    add_act()   
    return Response({"value": msg.payload.decode('utf-8')})

#------------------------------------------------------------------------------------------------------#

def on_message_temp2(client, userdata, msg):
    temp = Sensor2.objects.get(name="temp")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer2(temp, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new Temperatur 2 data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')}) 
    
def on_message_frik2(client, userdata, msg):
    frik = Sensor2.objects.get(name="frik")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer2(frik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new Friksi 2 data ', msg.payload.decode('utf-8'))   
    return Response({"value": msg.payload.decode('utf-8')})
    
def on_message_dl2(client, userdata, msg):
    dl = Sensor2.objects.get(name="dl")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer2(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new Daya Listrik 2 data ', msg.payload.decode('utf-8')) 
    add_act()   
    return Response({"value": msg.payload.decode('utf-8')})


#------------------------------------------------------------------------------------------------------#

def on_message_temp3(client, userdata, msg):
    temp = Sensor3.objects.get(name="temp")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer3(temp, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new Temperatur 3 data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')}) 
    
def on_message_frik3(client, userdata, msg):
    frik = Sensor3.objects.get(name="frik")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer3(frik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new Friksi 3 data ', msg.payload.decode('utf-8'))   
    return Response({"value": msg.payload.decode('utf-8')})
    
def on_message_dl3(client, userdata, msg):
    dl = Sensor3.objects.get(name="dl")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer3(dl, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new Daya Listrik 3 data ', msg.payload.decode('utf-8'))    
    add_act()
    return Response({"value": msg.payload.decode('utf-8')})


client = mqtt.Client("sms")
client.message_callback_add('sms/spp/ps', on_message_temp)
client.message_callback_add('sms/spp/fs', on_message_frik)
client.message_callback_add('sms/spp/lls', on_message_dl)

client.message_callback_add('sms/ps/vs', on_message_temp2)
client.message_callback_add('sms/ps/cs', on_message_frik2)
client.message_callback_add('sms/ps/fd', on_message_dl2)

client.message_callback_add('sms/ac/ts', on_message_temp3)
client.message_callback_add('sms/ac/hs', on_message_frik3)
client.message_callback_add('sms/ac/co2', on_message_dl3)

client.connect('localhost', 1883)
client.loop_start()
client.subscribe('sms/#')
