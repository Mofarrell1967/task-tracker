app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'project-task-tracker'
app.config["MONGO_URI"] = 'mongodb+srv://root:Lismara1@myfirstcluster-gpsqs.mongodb.net/project-task-tracker?retryWrites=true&w=majority'