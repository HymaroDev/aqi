import requests
import time

print("""

  _______        _           _ _                 _             _  //\            _            
 |__   __|      | |         | | |               | |           (_)|/ \|          (_)           
    | |_ __ __ _| |__   __ _| | |__   ___     __| | ___    ___ _  ___ _ __   ___ _  __ _ ___  
    | | '__/ _` | '_ \ / _` | | '_ \ / _ \   / _` |/ _ \  / __| |/ _ \ '_ \ / __| |/ _` / __| 
    | | | | (_| | |_) | (_| | | | | | (_) | | (_| |  __/ | (__| |  __/ | | | (__| | (_| \__ \ 
    |_|_|  \__,_|_.__/ \__,_|_|_| |_|\___/   \__,_|\___|  \___|_|\___|_| |_|\___|_|\__,_|___/ 
                                                                                              
                                                                                              


by Gregorio Caetano\n""")

user = input("Olá! Qual o seu Nome: ")

city_name = input("""

=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=\n
Coloque nome de um País: """)

api_key = "67475002e717c6cc0849f37fee7e205776ae6842"
url = f"https://api.waqi.info/feed/{city_name}/?token={api_key}"

response = requests.get(url)
json_data = response.json()
aqi = json_data['data']['aqi']
status = json_data['status']
print(f"""

  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.
:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\
'
Olá {user}, A qualidade do ar em {city_name} é: {aqi}  \n
  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.
:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\
'""")

time.sleep(3)
