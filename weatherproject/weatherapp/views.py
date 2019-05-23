from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
import speech_recognition as sr
import requests

def index(request):
    response = " "
    data = ""
    global result
    result = {}
    if request.method == "POST" and request.is_ajax():

        def hello():
          print("this is hello function...!")
          r = sr.Recognizer()
          with sr.Microphone() as source:
            print("Speak Anything :")
            audio = r.listen(source)
            try:
              text = r.recognize_google(audio)
              print("You said : {}".format(text))
              r = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&APPID=50e6b1bb8636f41d5bde15a7528dc044".format(text))
              response = r.json()
              print(response)

              result={
              'country' : response['sys']['country'],
              'city' : response['name'],
              'description' : response['weather'][0]['description'],
              'icon' : response['weather'][0]['icon'],
              'min_temp' : response['main']['temp_min'],
              'max_temp' : response['main']['temp_max'],
              'humidity' : response['main']['humidity'],
                }
              return result

            except:
              print("Sorry could not recognize what you said")


        print("this is ajax request...!")

        data = {
        'hello':hello(),
        }
        print("****************")
        print(data['hello'])
        context = {'result':data['hello']}
        print(context['result'])
        template = loader.get_template('weatherapp/index.html')
        # print(template)
        return HttpResponse(template.render(context, request))
        # print('result out side function:- {}'.format(data['hello']))
        # return render(request,'weatherapp/index.html',context={'result':data['hello']})
    else:
        print("no ajax...!")
        return render(request,'weatherapp/index.html')
    # return render(request,'app/index.html',context={'country':country,'city':city,'description':description,'icon':icon,'min_temp':min_temp,'max_temp':max_temp,'humidity':humidity})

    # print('result out side function:- {}'.format(data['hello']))
    # return render(request,'weatherapp/index.html',context={'result':data['hello']})
