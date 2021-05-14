from flask import Flask, render_template , request
import csv
app = Flask(__name__)


@app.route('/')
def home():
  return render_template('index.html')

@app.route('/<string:pagename>')
def home_again(pagename):
  return render_template(pagename)

def write_to_csv(data):
    with open('database.csv',newline='', mode ='a') as database2:
      email = data["email"]
      subject = data["subject"]
      message = data["message"]
      csv_writer = csv.writer(database2, delimiter =',' , quotechar='"', quoting=csv.QUOTE_MINIMAL)
      csv_writer.writerow([email,subject,message])

def write_to_file(data):
  with open('database.txt', mode ='a') as database:
      email = data["email"]
      subject = data["subject"]
      message = data["message"]
      file = database.write(f'\n{email} , {subject} , {message}')

@app.route('/submit_form' , methods=['POST', 'GET'])
def submit_form():
  if request.method == 'POST':
    data = request.form.to_dict()
    print(data)
    write_to_csv(data)
    return render_template('thankyou.html')
  else:
    return 'Try agaim'

if __name__ == '__main__':
  app.run()
