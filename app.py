from flask import Flask, render_template
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        question = request.form["question"]
        button = request.form["button"]
        if button == "submit":
            webresults = utils.get_web_results(question)
            if "who" in question:
                answer = find_name(webresults)
            else if "where" in question:
                answer = find_place(webresults)
            else if "when" in question:
                answer = find_time(webresults)
            else:
                answer = "Question has to include who, where, or when."
            return render_template("results.html",ans=answer)
            
