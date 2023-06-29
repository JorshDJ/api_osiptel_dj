from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

######
datos = {
    "imei": [
        {"numImei": 123456789012345, "estadoEquipo": "El imei se encunentra en lista negra", "Operador" : "telefónica", "fecha":"19/06/2023"},
        {"numImei": 123456789012346, "estadoEquipo": "El imei se encunentra en lista negra", "Operador" : "claro", "fecha":"19/06/2023"},
        {"numImei": 123456789012347, "estadoEquipo": "El imei se encunentra en lista negra", "Operador" : "entel", "fecha":"19/06/2023"},
        {"numImei": 123456789012348, "estadoEquipo": "El imei se encunentra en lista negra", "Operador" : "entel", "fecha":"19/06/2023"},
        {"numImei": 123456789012349, "estadoEquipo": "El imei se encunentra en lista negra", "Operador" : "bitel", "fecha":"19/06/2023"},
        {"numImei": 123456789012340, "estadoEquipo": "El imei se encunentra en lista negra", "Operador" : "telefónica", "fecha":"19/06/2023"},
        {"numImei": 123456789012341, "estadoEquipo": "El imei se encunentra en lista negra", "Operador" : "telefónica", "fecha":"19/06/2023"},
    ],
    "problemas_detectados": [
        {"id": 1, "descripcion": "Mi equipo móvil no figura como bloqueado, pese a haberlo reportado a la empresa operadora."},
        {"id": 2, "descripcion": "Mi equipo móvil figura como bloqueado, sin haberlo reportado a la empresa operadora."},
        {"id": 3, "descripcion": "Mi equipo móvil figura como recuperado, sin haberlo reportado a la empresa operadora."},
        {"id": 4, "descripcion": "Mi equipo móvil no figura como recuperado, pese a haberlo reportado a la empresa operadora."},
        {"id": 5, "descripcion": "Mi equipo móvil figura como bloqueado por una empresa distinta a mi operador."},
        {"id": 6, "descripcion": "Mi equipo móvil figura como recuperado por una empresa distinta a mi operador."},
        {"id": 9, "descripcion": "Otros (DETALLAR)"},
    ],
    "empresas": [
        {"id": 0, "nombre": "[Seleccione]"},
        {"id": 20, "nombre": "ENTEL PERU S.A."},
        {"id": 21, "nombre": "AMERICA MOVIL PERU S.A.C."},
        {"id": 22, "nombre": "TELEFONICA DEL PERU S.A.A."},
        {"id": 23, "nombre": ""},
        {"id": 24, "nombre": "VIETTEL PERU S.A.C."},
        {"id": 25, "nombre": "FLASH SERVICIOS PERU S.R.L."},
        {"id": 26, "nombre": "DOLPHIN TELECOM DEL PERU S.A.C."},
        {"id": 27, "nombre": "GUINEA MOBILE S.A.C."},
    ],
    "marcas": [
        {"id": -1, "nombre": "[Seleccione]"},
        {"id": 0, "nombre": "[OTRO]"},
        {"id": 1, "nombre": "ACER"},
        {"id": 2, "nombre": "AEG"},
        {"id": 3, "nombre": "AIRAM"},
        {"id": 4, "nombre": "ALCATEL"},
        {"id": 5, "nombre": "AMAZON"},
        {"id": 6, "nombre": "AMOI"},
        {"id": 7, "nombre": "ANYCOOL"},
        {"id": 8, "nombre": "APPLE"},
        {"id": 9, "nombre": "ASUS"},
        {"id": 10, "nombre": "AZUMI"},
        {"id": 11, "nombre": "BENQ"},
        {"id": 12, "nombre": "BENQ-SIEMENS"},
        {"id": 13, "nombre": "BIRD"},
        {"id": 14, "nombre": "BLACKBERRY"},
        {"id": 15, "nombre": "BLU"},
        {"id": 16, "nombre": "CECT"},
        {"id": 17, "nombre": "DELL"},
        {"id": 18, "nombre": "ETEN"},
        {"id": 19, "nombre": "GEEKSPHONE"},
        {"id": 20, "nombre": "GENERAL MOBILE"},
        {"id": 21, "nombre": "GIGABYTE"},
        {"id": 22, "nombre": "GRADIENTE"},
        {"id": 23, "nombre": "HAIER"},
        {"id": 24, "nombre": "HP"},
        {"id": 25, "nombre": "HTC"},
        {"id": 26, "nombre": "HUAWEI"},
        {"id": 27, "nombre": "I-MATE"},
        {"id": 28, "nombre": "I-MOBILE"},
        {"id": 29, "nombre": "INQ"},
        {"id": 30, "nombre": "LANIX"},
        {"id": 31, "nombre": "LENOVO"},
        {"id": 32, "nombre": "LG"},
        {"id": 33, "nombre": "MICROSOFT"},
        {"id": 34, "nombre": "MODU"},
        {"id": 35, "nombre": "MOTOROLA"},
        {"id": 36, "nombre": "MOVISTAR"},
        {"id": 37, "nombre": "NEC"},
        {"id": 38, "nombre": "NOKIA"},
        {"id": 39, "nombre": "O2"},
        {"id": 40, "nombre": "OLO"},
        {"id": 41, "nombre": "OPPO"},
        {"id": 42, "nombre": "ORANGE"},
        {"id": 43, "nombre": "PALM"},
        {"id": 44, "nombre": "PANASONIC"},
        {"id": 45, "nombre": "PANTECH"},
        {"id": 46, "nombre": "PCD"},
        {"id": 47, "nombre": "PHILIPS"},
        {"id": 48, "nombre": "QTEK"},
        {"id": 49, "nombre": "SAGEM"},
        {"id": 50, "nombre": "SAMSUNG"},
        {"id": 51, "nombre": "SHARP"},
        {"id": 52, "nombre": "SIEMENS MOVILE"},
        {"id": 53, "nombre": "SKYZEN"},
        {"id": 54, "nombre": "SONY"},
        {"id": 55, "nombre": "SONY ERICSSON"},
        {"id": 56, "nombre": "TCL"},
        {"id": 57, "nombre": "TELIT"},
        {"id": 58, "nombre": "TOSHIBA"},
        {"id": 59, "nombre": "UT STARCOM"},
        {"id": 60, "nombre": "VERTU"},
        {"id": 61, "nombre": "VERYKOOL"},
        {"id": 62, "nombre": "VIEWSONIC"},
        {"id": 63, "nombre": "VODAFONE"},
        {"id": 64, "nombre": "ZTE"},
        {"id": 65, "nombre": "SONY ERICSON"},
        {"id": 73, "nombre": "E"},
        {"id": 75, "nombre": "BITEL"},
    ]
}


##IMEI
@app.route('/imei', methods=['GET'])
def get_imeis():
    return jsonify(datos["imei"])

@app.route('/imei', methods=['POST'])
def post_imei():
    nuevo_imei = request.get_json()
    datos["imei"].append(nuevo_imei)
    return jsonify(nuevo_imei), 201

@app.route('/imei/<int:numImei>', methods=['GET'])
def get_imei(numImei):
    imei = next((u for u in datos["imei"] if u["numImei"] == numImei), None)
    if imei is None:
        return jsonify(
            {"numImei": numImei,"error": "El imei no se encuentra asociado a ningun terminal reportado" },), 404
    return jsonify(imei)

##Marcas
@app.route('/marcas', methods=['GET'])
def get_marcas():
    return jsonify(datos["marcas"])

##Modelos
@app.route('/modelos/<int:idMarca>', methods=['GET'])
def get_modelos(idMarca):
    url = f"https://serviciosweb.osiptel.gob.pe/SICEM/Consulta/ListarModelo?idMarca={idMarca}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": "No se pudo obtener los datos"}), 500
    
##Empresas
@app.route('/empresas', methods=['GET'])
def get_empresas():
    return jsonify(datos["empresas"])


##Problemas_detectados
@app.route('/problemas_detectados', methods=['GET'])
def get_problemas_detectados():
    return jsonify(datos["problemas_detectados"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



