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
    return render_template('byYear.html')

@app.route("/graph")
def render_page3():
    return render_template('graph.html')
    
if __name__=="__main__":
    app.run(debug=True, port=54321)