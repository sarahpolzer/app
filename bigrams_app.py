from flask import Flask, render_template, request
import nltk 
import plotly
import plotly.graph_objects as go

app = Flask(__name__)

@app.route('/')
def home_page():
    #Returns the html template of the homepage
    return render_template('enter_text.html')

@app.route('/', methods=['POST'])
def enter_text():
    #handles the text or file name entered by the user and returns the bar chart of the bigrams
    text = request.form['text']
    bigrams,counts = create_bigrams(text)
    if len(bigrams)==0:
        return  "No Bigrams Found :("
    bigram_bar = go.Figure([go.Bar(x=bigrams, y=counts)])
    bigram_bar.update_layout(title_text='Bigrams and their Counts')
    plotly.offline.plot(bigram_bar, filename='templates/bar.html')
    return render_template('bar.html')

def create_bigrams(text):
    #Takes the text entered by the user and returns a list of bigrams and a list of their counts
    bigrams = []
    counts = []
    if len(text.split(' '))==1 and "." in text:
        f = open(text)
        text = f.read()
    text = text.lower()
    bigrm = list(nltk.bigrams(text.split()))
    for b in list(set(bigrm)):
        bigrams.append(b[0] + "," + b[1])
        counts.append(bigrm.count(b))
    return bigrams, counts
    


if __name__ == '__main__':
    app.run(debug=True)


    
