from utils.phApi import AnimeScrapper
from flask import Flask, render_template,request,redirect

app = Flask(__name__)

api = AnimeScrapper()

@app.route('/')
def home():
    trendData = api.getTrending(1,15)
    popData = api.getPopular(1,15)
    latData = api.getLatestEpisodes(1,15,"zoro")
    sliders = api.getPopular(1,20)

    return render_template('home.html',str=str,latest=latData.get('results'),trending=trendData.get('results'),popular=popData.get('results'),sliders=sliders.get('results'))

@app.route('/search')
def search():
    if (request.args.get("query")):
        params = dict(request.args)
        searchResult = api.searchAnime(params)
        searchResult['query'] = request.args.get('query')

        return render_template("search.html",boolean=bool,str=str,searches=searchResult)
    else:
        return redirect('/search?query=one piece')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 