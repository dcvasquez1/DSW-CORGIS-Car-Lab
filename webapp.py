from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('introduction.html')
    
@app.route("/company")
def render_page1():

    with open('static/cars.json') as demographicsdata:
        cars = json.load(demographicsdata)
    
    reply_list = get_car_options_company(cars)

    return render_template('byCompany.html', options = reply_list)

@app.route("/year")
def render_page2():

    with open('static/cars.json') as demographicsdata:
        cars = json.load(demographicsdata)
    
    reply_list = get_car_options_year(cars)
    
    return render_template('byYear.html', options = reply_list)

@app.route("/graph")
def render_page3():
    return render_template('graph.html')
    
def get_car_options_company(cars):
    companies = []
    options = ""
    for c in cars:
        if c["Identification"]["Make"] not in companies:
            companies.append(c["Identification"]["Make"])
            options += Markup("<option value=\"" + c["Identification"]["Make"] + "\">" + c["Identification"]["Make"] + "</option>")
    return options
    
def get_car_options_year(cars):
    years = []
    options = ""
    for c in cars:
        if c["Identification"]["Year"] not in years:
            years.append(c["Identification"]["Year"])
            options += Markup("<option value=\"" + str(c["Identification"]["Year"]) + "\">" + str(c["Identification"]["Year"]) + "</option>")
    return options
    
if __name__=="__main__":
    app.run(debug=True, port=54321)