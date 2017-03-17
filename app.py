from github import Github
import sys,os
from flask import Flask



app = Flask(__name__)

@app.route("/v1/<filename>")
def displayfilecontent(filename):
 cli = (sys.argv[1]).split("/")
 config_file=filename
 repo_name=cli[4]
 username=cli[3]
 repo=Github().get_user(username).get_repo(repo_name)
 extensions = '.yml','.json'
 output=[]
 if (filename == config_file):
  if filename.endswith(extensions):
   f=repo.get_contents(filename)
   output.append(f.decoded_content)
   return "<br/>".join(output)
  else:
   return "file cannot open! No access rights--**Please enter files with correct extension!!**"
 else:
   return "Page not found.Wrong URL Request(Error 404)"  


@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!! "


if __name__ == "__main__":
 app.run(debug=True,host='0.0.0.0') 
 