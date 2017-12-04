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
    """
    if 'Company' in request.args:        
        return render_template('byCompany.html', options = reply_list, reply_company = request.args["Company"], fact_dictionary = get_car_facts_company(request.args["Company"]))
    """
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
    companies = sorted(companies,key=str.lower)
    
    for i in companies:
        options += Markup("<option value=\"" + i + "\">" + i + "</option>")
    return options
    
def get_car_options_year(cars):
    years = []
    options = ""
    for c in cars:
        if c["Identification"]["Year"] not in years:
            years.append(c["Identification"]["Year"])
    years = sorted(years)
    
    for i in years:
        options += Markup("<option value=\"" + str(i) + "\">" + str(i) + "</option>")
    return options


def get_car_facts_company(company):
    with open('static/cars.json') as demographicsdata:
        cars = json.load(demographicsdata)
        
    carsMade = 0
    avgMPG_Highway = 0
    avgMPG_City = 0
    avgHorsepower = 0
    numberManual = 0
    numberAutomatic = 0
    
    for c in cars:
        if c["Identification"]["Make"] == company:
            carsMade += 1
            avgMPG_City += c["Fuel Information"]["City mpg"]
            avgMPG_Highway += c["Fuel Information"]["Highway mpg"]
            avgHorsepower += c["Engine Information"]["Engine Statistics"]["Horsepower"]
            if c["Identification"]["Classification"] == "Automatic transmission":
                numerAutomatic += 1
            else:
                numberManual += 1
    avgHorsepower = avgHorsepower / carsMade
    avgMPG_City = avgMPG_City / carsMade
    avgMPG_Highway = avgMPG_Highway / carsMade
    
    return {"Number of Cars Made": carsMade , "Number of Manual Transmission Cars Made": numberManual, "Number of Automatic Transmission Cars Made": numberAutomatic, "Average Highway MPG": avgMPG_Highway, "Average City MPG": avgMPG_City, "Average Horsepower": avgHorsepower}
    """
def get_car_facts_year(cars, year):
    
    """
    
if __name__=="__main__":
    app.run(debug=True, port=54321)