from flask import Flask, render_template, request
import utils, who, where, when
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        question = request.form["question"]
        button = request.form["button"]
        if button == "ask":
            webresults = utils.get_web_results(question)
            if "who" in question.lower():
                answer = who.find_name(webresults)
            elif "where" in question.lower():
                answer = where.find_place(webresults)
            elif "when" in question.lower():
                answer = when.find_time(webresults)
            else:
                answer = "Question has to include who, where, or when."
            return render_template("results.html",ans=answer)
            
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
    
