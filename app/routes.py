from app import app
from app.models import Item
from app.database import db_session, init_db
from flask import render_template


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/services")
def services_page():
    init_db()
    offered_services = Item.query.all() 
    return render_template("services.html", services=offered_services )

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

