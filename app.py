from flask import Flask
from config.database_config import DatabaseConnector
from dosendanprodi.prodiroutes import prodi_routes
from dosendanprodi.dosenroutes import dosen_routes
from mahasiswa.mahasiswaroutes import mahasiswa_routes
from kaprodi.kaprodiroutes import kaprodi_routes
from management_pembimbing.managementroutes import management_routes
from user.userroutes import user_routes
from user.adminroutes import admin_routes
from skripsi.skripsiroutes import skripsi_routes
from Logbook.logbookroutes import logbook_routes
app = Flask (__name__)

db_connector = DatabaseConnector()
db_connector.test_connection()

app.register_blueprint(prodi_routes)
app.register_blueprint(dosen_routes)
app.register_blueprint(mahasiswa_routes)
app.register_blueprint(kaprodi_routes)
app.register_blueprint(management_routes)
app.register_blueprint(user_routes)
app.register_blueprint(admin_routes)
app.register_blueprint(skripsi_routes)
app.register_blueprint(logbook_routes)



if __name__ == '__main__':
    app.run(debug=True)