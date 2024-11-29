from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Ruta principal para la búsqueda del clima
@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        ciudad = request.form['ciudad']  
        api_key = "759ac2f801965683099d13f546d3022e"   
        url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}"
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            weather_data = {
                'ciudad': datos['name'],
                'temperatura': datos['main']['temp'],
                'descripcion': datos['weather'][0]['description'].capitalize(),
                'latitud': datos['coord']['lat'],
                'longitud': datos['coord']['lon']
            }
        else:
            weather_data = {'error': 'No se encontró información para la ciudad ingresada.'}
    return render_template('index.html', weather_data=weather_data)

# Ruta para la hoja de vida
@app.route('/cv.html')
def cv():
    return render_template('cv.html')

if __name__ == '__main__':
    app.run(debug=True)
