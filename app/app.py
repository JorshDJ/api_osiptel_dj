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
        {"id": 0, "nombre": "[Seleccione]", "pagina_web": ""},
        {"id": 20, "nombre": "ENTEL PERU S.A.", "pagina_web": "http://www.entel.pe"},
        {"id": 21, "nombre": "AMERICA MOVIL PERU S.A.C.", "pagina_web": "http://www.claro.com.pe"},
        {"id": 22, "nombre": "TELEFONICA DEL PERU S.A.A.", "pagina_web": "http://www.telefonica.com.pe"},
        {"id": 24, "nombre": "VIETTEL PERU S.A.C.", "pagina_web": "http://www.bitel.com.pe"},
        {"id": 25, "nombre": "FLASH SERVICIOS PERU S.R.L.", "pagina_web": "http://www.flashmobile.pe"},
        {"id": 26, "nombre": "DOLPHIN TELECOM DEL PERU S.A.C.", "pagina_web": "http://www.dolphin.pe"},
        {"id": 27, "nombre": "GUINEA MOBILE S.A.C.", "pagina_web": "http://www.guinea.pe"}
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
    ],

    "preguntas_frecuentes": [
        {
            "id": 1,
            "pregunta": "¿Las empresas operadoras pueden suspender mi servicio si es que lo utilizo en un equipo terminal con IMEI inválido?",
            "respuesta": "Sí, la empresa operadora debe suspender tu servicio de telefonía móvil si este se encuentra vinculado a un equipo terminal con IMEI inválido."
        },
        {
            "id": 2,
            "pregunta": "Si me suspendieron mi servicio de telefonía móvil por haberlo utilizado con un equipo terminal con IMEI inválido, ¿qué puedo hacer?",
            "respuesta": "El abonado o titular del servicio puede solicitar la reactivación del servicio hasta los treinta (30) días calendario luego de la ejecución de la suspensión del servicio, para lo cual debe acercarse en forma presencial a una oficina o centro de atención de la empresa operadora que brinda el servicio y presentar por única vez una Declaración Jurada de Compromiso, en la que conste su compromiso de no utilizar equipos terminales móviles con IMEI inválido."
        },
        {
            "id": 3,
            "pregunta": "Al momento de solicitar la reactivación del servicio ante la empresa operadora, ¿debo llevar conmigo el equipo terminal móvil con IMEI inválido?",
            "respuesta": "No. El equipo terminal móvil con IMEI inválido ya fue bloqueado y no es necesario que lo lleves. Lo que debes llevar al acercarte a la oficina o centro de atención de la empresa operadora que te brinda el servicio es tu nuevo equipo terminal el cual deberá contar con un IMEI válido."
        },
        {
            "id": 4,
            "pregunta": "¿En cuánto tiempo se reactivará mi servicio?",
            "respuesta": "La empresa operadora debe proceder a reactivar tu servicio en un plazo máximo de veinticuatro (24) horas, luego de haber recibido la citada Declaración Jurada, y validado satisfactoriamente que cuentas con un equipo terminal móvil con IMEI válido."
        },
        {
            "id": 5,
            "pregunta": "¿Qué sucede si no solicito la reactivación del servicio dentro del plazo de 30 días calendario de haberse ejecutado la suspensión del servicio?",
            "respuesta": "En caso haya vencido el plazo de treinta (30) días calendario sin que hayas solicitado la reactivación del servicio, la empresa operadora debe proceder a dar de baja la línea del servicio público móvil que fue suspendida por utilizar de forma reiterada equipos terminales móviles con IMEI inválidos."
        },
        {
            "id": 6,
            "pregunta": "Si luego de haberse presentado la Declaración Jurada de Compromiso, el abonado vuelve a utilizar su servicio móvil con un equipo terminal móvil con IMEI inválido, ¿Qué sucedería?",
            "respuesta": "En caso se detecte que el abonado ha vuelto a utilizar el servicio vinculado a uno o más equipos terminales móviles con IMEI inválido, de forma posterior a la firma de la Declaración Jurada de Compromiso, la empresa operadora debe proceder a realizar de forma inmediata la baja de la línea del servicio público móvil vinculado a dicho equipo terminal."
        },
        {
            "id": 7,
            "pregunta": "¿Si he utilizado equipos terminales móviles con IMEI inválidos, tendré problemas para contratar servicios posteriormente?",
            "respuesta": "Para el caso de los abonados cuyas líneas fueron suspendidas por haber sido detectados utilizando un servicio vinculado a uno o más equipos terminales móviles con IMEI inválido en más de una oportunidad, sólo se les permitirá la contratación de servicios públicos móviles en oficinas o centros de atención de las empresas operadoras."
        },
        {
            "id": 8,
            "pregunta": "¿Las contrataciones de servicios de telefonía móvil sólo en oficinas será aplicado indefinidamente, considerando que he utilizado el servicio con equipos terminales móviles con IMEI inválido?",
            "respuesta": "No. Para el caso de los abonados cuyas líneas fueron suspendidas por utilizar de forma reiterada equipos terminales móviles con IMEI inválido, este requisito aplica por un año, contado a partir del día siguiente de la detección del último uso de un equipo terminal móvil con IMEI inválido."
        },
        {
            "id": 9,
            "pregunta": "¿Qué acciones deberán realizar las empresas operadoras luego de realizar las suspensiones o baja del servicio de telefonía móvil por haberse utilizado con un equipo terminal con IMEI inválido?",
            "respuesta": "Las empresas operadoras deberán remitir al OSIPTEL la relación de líneas reactivadas y/o dadas de baja. Asimismo, el OSIPTEL podrá informar sobre estos hechos al Ministerio Público para las investigaciones que correspondan."
        }
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


##Preguntas Frecuentes
@app.route('/preguntas_frecuentes', methods=['GET'])
def get_preguntas_frecuentess():
    return jsonify(datos["preguntas_frecuentes"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



