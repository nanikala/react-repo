from distutils.log import debug
from fileinput import filename
from flask import *
app = Flask(__name__,template_folder='templates')

@app.route('/')

def main():
	return render_template("ind.html")

@app.route('/success', methods = ['POST'])
def success():
	if request.method == 'POST':
		f = request.files['file']
		f.save(f.filename)
		r="passed"
		#call the function to predict
		return render_template("ack.html", res=r)#pass the output to this page

if __name__ == '__main__':
	app.run(debug=True) 