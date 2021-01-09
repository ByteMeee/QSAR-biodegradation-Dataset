

#!pip install flask-ngrok

#!pip install flask-restful

"""Imports"""

from sklearn.externals import joblib
from flask_ngrok import run_with_ngrok
from flask import Flask
from flask_restful import Api, Resource, reqparse
from sklearn.externals import joblib
import numpy as np


class Predict(Resource):

    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('SpMax_L')
        parser.add_argument('J_Dz(e)')
        parser.add_argument('nHM')
        parser.add_argument('F01[N-N]')
        parser.add_argument('F04[C-N]')
        parser.add_argument('NssssC')
        parser.add_argument('nCb-')
        parser.add_argument('C%')
        parser.add_argument('nCp')
        parser.add_argument('nO')
        parser.add_argument('F03[C-N]')
        parser.add_argument('SdssC')
        parser.add_argument('HyWi_B(m)')
        parser.add_argument('LOC')
        parser.add_argument('SM6_L')
        parser.add_argument('F03[C-O]')
        parser.add_argument('Me')
        parser.add_argument('Mi')
        parser.add_argument('nN-N')
        parser.add_argument('nArNO2')
        parser.add_argument('nCRX3')
        parser.add_argument('SpPosA_B(p)')
        parser.add_argument('nCIR')
        parser.add_argument('B01[C-Br]')
        parser.add_argument('B03[C-Cl]')
        parser.add_argument('N-073')
        parser.add_argument('SpMax_A')
        parser.add_argument('Psi_i_1d')
        parser.add_argument('B04[C-Br]')
        parser.add_argument('SdO')
        parser.add_argument('TI2_L')
        parser.add_argument('nCrt')
        parser.add_argument('C-026')
        parser.add_argument('F02[C-N]')
        parser.add_argument('nHDon')
        parser.add_argument('SpMax_B(m)')
        parser.add_argument('Psi_i_A')
        parser.add_argument('nN')
        parser.add_argument('SM6_B(m)')
        parser.add_argument('nArCOOR')
        parser.add_argument('nX')


        args = parser.parse_args()  # creates dict
        print(args.values())
        X_new = np.fromiter(args.values(), dtype=float)  # convert input to array
        out = {'Prediction': BIO_MODEL.predict([X_new])[0]}
        print(out)
        return out, 200

if __name__ == '__main__':
	# serialize model
	#joblib.dump(clf, 'biodeg.mdl')

	app = Flask(__name__)
	run_with_ngrok(app)   #starts ngrok when the app is run only for google colab
	API = Api(app)
	BIO_MODEL = joblib.load('./biodeg.mdl')
	@app.route("/")
	def home():
    		return "<!DOCTYPE html>\
    		<html>\
    		<body>\
    		<h2>HTML Forms</h2>\
   		 <form method='post' action='/predict'>\
    		<label for='SpMax_L'>SpMax_L:</label><br>\
   		 <input type='text' id='SpMax_L' name='SpMax_L' value=''><br>\
    		<label for='J_Dz(e)'>J_Dz(e):</label><br>\
    		<input type='text' id='J_Dz(e)' name='J_Dz(e)' value=''><br>\
    		<label for='nHM'>nHM:</label><br>\
     		<input type='text' id='nHM' name='nHM' value=''><br>\
     		<label for='F01[N-N]'>F01[N-N]:</label><br>\
     		<input type='text' id='F01[N-N]' name='F01[N-N]' value=''><br>\
     		<label for='F04[C-N]'>F04[C-N]:</label><br>\
     		<input type='text' id='F04[C-N]' name='F04[C-N]' value=''><br>\
     		<label for='NssssC'>NssssC:</label><br>\
     		<input type='text' id='NssssC' name='NssssC' value=''><br>\
     		<label for='nCb-'>nCb-:</label><br>\
     		<input type='text' id='nCb-' name='nCb-' value=''><br>\
     		<label for='C%'>C%:</label><br>\
     		<input type='text' id='C%' name='C%' value=''><br>\
     		<label for='nCp'>nCp:</label><br>\
    		<input type='text' id='nCp' name='nCp' value=''><br>\
    		 <label for='nO'>nO:</label><br>\
     		<input type='text' id='nO' name='nO' value=''><br>\
     		<label for='F03[C-N]'>F03[C-N]:</label><br>\
     		<input type='text' id='F03[C-N]' name='F03[C-N]' value=''><br>\
     		<label for='SdssC'>SdssC:</label><br>\
     		<input type='text' id='SdssC' name='SdssC' value=''><br>\
     		<label for='HyWi_B(m)'>HyWi_B(m):</label><br>\
     		<input type='text' id='HyWi_B(m)' name='HyWi_B(m)' value=''><br>\
     		<label for='LOC'>LOC:</label><br>\
     		<input type='text' id='LOC' name='LOC' value=''><br>\
     		<label for='SM6_L'>SM6_L:</label><br>\
     		<input type='text' id='SM6_L' name='SM6_L' value=''><br>\
     		<label for='F03[C-O]'>F03[C-O]:</label><br>\
     		<input type='text' id='F03[C-O]' name='F03[C-O]' value=''><br>\
     		<label for='Me'>Me:</label><br>\
     		<input type='text' id='Me' name='Me' value=''><br>\
     		<label for='Mi'>Mi:</label><br>\
     		<input type='text' id='Mi' name='Mi' value=''><br>\
     		<label for='nN-N'>nN-N:</label><br>\
     		<input type='text' id='nN-N' name='nN-N' value=''><br>\
     		<label for='nArNO2'>nArNO2:</label><br>\
     		<input type='text' id='nArNO2' name='nArNO2' value=''><br>\
     		<label for='nCRX3'>nCRX3:</label><br>\
     		<input type='text' id='nCRX3' name='nCRX3' value=''><br>\
     		<label for='SpPosA_B(p)'>SpPosA_B(p):</label><br>\
     		<input type='text' id='SpPosA_B(p)' name='SpPosA_B(p)' value=''><br>\
     		<label for='nCIR'>nCIR:</label><br>\
     		<input type='text' id='nCIR' name='nCIR' value=''><br>\
     		<label for='B01[C-Br]'>B01[C-Br]:</label><br>\
     		<input type='text' id='B01[C-Br]' name='B01[C-Br]' value=''><br>\
     		<label for='B03[C-Cl]'>B03[C-Cl]:</label><br>\
     		<input type='text' id='B03[C-Cl]' name='B03[C-Cl]' value=''><br>\
     		<label for='N-073'>N-073:</label><br>\
     		<input type='text' id='N-073' name='N-073' value=''><br>\
     		<label for='SpMax_A'>SpMax_A:</label><br>\
     		<input type='text' id='SpMax_A' name='SpMax_A' value=''><br>\
     		<label for='Psi_i_1d'>Psi_i_1d:</label><br>\
     		<input type='text' id='Psi_i_1d' name='Psi_i_1d' value=''><br>\
     		<label for='B04[C-Br]'>B04[C-Br]:</label><br>\
     		<input type='text' id='B04[C-Br]' name='B04[C-Br]' value=''><br>\
     		<label for='SdO'>SdO:</label><br>\
     		<input type='text' id='SdO' name='SdO' value=''><br>\
    		<label for='TI2_L'>TI2_L:</label><br>\
    		<input type='text' id='TI2_L' name='TI2_L' value=''><br>\
    		<label for='nCrt'>nCrt:</label><br>\
    		<input type='text' id='nCrt' name='nCrt' value=''><br>\
    		<label for='C-026'>C-026:</label><br>\
    		<input type='text' id='C-026' name='C-026' value=''><br>\
    		<label for='F02[C-N]'>F02[C-N]:</label><br>\
  		<input type='text' id='F02[C-N]' name='F02[C-N]' value=''><br>\
    		<label for='nHDon'>nHDon:</label><br>\
    		<input type='text' id='nHDon' name='nHDon' value=''><br>\
   		 <label for='SpMax_B(m)'>SpMax_B(m):</label><br>\
    		<input type='text' id='SpMax_B(m)' name='SpMax_B(m)' value=''><br>\
    		<label for='Psi_i_A'>Psi_i_A:</label><br>\
    		<input type='text' id='Psi_i_A' name='Psi_i_A' value=''><br>\
		<label for='nN'>nN:</label><br>\
		<input type='text' id='nN' name='nN' value=''><br>\
		<label for='SM6_B(m)'>SM6_B(m):</label><br>\
		<input type='text' id='SM6_B(m)' name='SM6_B(m)' value=''><br>\
		<label for='nArCOOR'>nArCOOR:</label><br>\
		<input type='text' id='nArCOOR' name='nArCOOR' value=''><br>  \
		<label for='nX'>nX:</label><br>\
		<input type='text' id='nX' name='nX' value=''><br>  \
		<br>\
		<input type='submit' value='Submit'>\
		</form> \
		</body>\
		</html>"

		API.add_resource(Predict, '/predict')

		app.run()