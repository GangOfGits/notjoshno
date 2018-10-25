from notjoshno import app
from flask import render_template, redirect, session, request, url_for, abort
from notjoshno.authentication import verify_password
from notjoshno.web_pages import web_page, set_alert


web_pages = {}
web_pages["main"] = web_page("main.html", "Home")
web_pages["namegenerator"] = web_page("namegenerator.html", "Name Generator")
web_pages["login"] = web_page("login.html", "Login")
web_pages["main"] = web_page("main.html", "Home")

@app.route("/")
def main():
    rendered_page =  web_pages["main"].render()
    set_alert()
    return rendered_page


@app.route("/app/<string:application_name>")
def name_generator(application_name):
    if application_name in web_pages:
        rendered_page =  web_pages[application_name].render()
        set_alert()
        return rendered_page
    else:
        abort(404)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="GET":
        rendered_page =  web_pages["login"].render()
        set_alert()
        return rendered_page
    elif request.method=="POST":
        if request.form["username"] == "" or request.form["password"] == "":
            set_alert(True, "warning", "Login failed",
                      "Please fill in all fields")
            return redirect(url_for("login"))
        else:
            if verify_password(request.form["username"],
                               request.form["password"]):
                username = request.form["username"]
                #Set the session "username" key to the username put into the form
                session["credentials"] = {}
                session["credentials"]["username"] = username

                set_alert(True, "success", "Logged in",
                          "You are now logged in as " + username)
                return redirect(url_for("main"))
            else:
                set_alert(True, "danger", "Login failed",
                          "Incorrect username or password")
                return redirect(url_for("login"))




@app.route("/sign_out")
def sign_out():
    if request.method=="GET":
        session.pop("credentials", {})
        return redirect("/")
