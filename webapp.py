from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('introduction.html')
    
@app.route("/company")
def render_page1():
    return render_template('byCompany.html')

@app.route("/year")
def render_page2():
    with open('static/cars.json') as demographicsdata:
        cars = json.load(demographicsdata)
    
    reply_list = get_state_options(cars)
    
    """
    if 'State' in request.args:
        return render_template('home.html', options = reply_list, fact = fact_function(request.args["State"]), reply_state = request.args["State"]) 
    """
    return render_template('home.html' , options = reply_list)
   """
   return render_template('byYear.html')
    """
@app.route("/graph")
def render_page3():
    return render_template('graph.html')
    with open('static/cars.json') as demographicsdata:
        cars = json.load(demographicsdata)
    
    reply_list = get_state_options(cars)
    
    """
    if 'State' in request.args:
        return render_template('home.html', options = reply_list, fact = fact_function(request.args["State"]), reply_state = request.args["State"]) 
    """
    return render_template('home.html' , options = reply_list)
    
if __name__=="__main__":
    app.run(debug=True, port=54321)