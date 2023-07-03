import requests
import json

class AnimeScrapper:
  def __init__(self):
    self.aniListUrl = 'https://api.consumet.org/meta/anilist/'
    self.provider = "zoro"
    self.availGenres = ["Action" ,"Adventure" ,"Cars" ,"Comedy" ,"Drama" ,"Fantasy" ,"Horror" ,"Mahou Shoujo" ,"Mecha" ,"Music" ,"Mystery" ,"Psychological" ,"Romance" ,"Sci-Fi" ,"Slice of Life" ,"Sports" ,"Supernatural" ,"Thriller"]
    self.availProviders = {"gogoanime":{'streamLink':"https://api.consumet.org/anime/gogoanime/watch/EPID?server=SERVER",'availServers':["gogocdn", "streamsb", "vidstreaming"]},'animefox':{'streamLink':'https://api.consumet.org/anime/animefox/watch?episodeId=EPID'},'animepahe':{'streamLink':"https://api.consumet.org/anime/animepahe/watch/EPID"},'zoro':{'streamLink':'https://api.consumet.org/anime/zoro/watch/EPID?server=SERVER','availServers':["vidcloud","streamsb","vidstreaming","streamtape","vidcloud"]},'9anime':{'streamLink':'https://api.consumet.org/anime/9anime/watch/EPID?server=SERVER','availServers':["vidcloud","streamsb","vidstreaming","streamtape","vidcloud"]}}

  def getTrending(self,page:int,pageRate:int)->None:
    """
    Get trending Anime.\n
    Parameters -->\n
    page -- Index of Page\n
    pageRate -- No. Animes Per Page
    """

    url = self.aniListUrl + 'trending'
    response = requests.get(url,stream=True, params={
        "page": page,
        "perPage": pageRate
    })
    data = response.json()
    
    return data


  def getPopular(self,page:int,pageRate:int)->None:
    """
    Get Popular Anime.\n
    Parameters -->\n
    page -- Index of Page\n
    pageRate -- No. Animes Per Page
    """

    url = self.aniListUrl + 'popular'
    response = requests.get(url,stream=True, params={
        "page": page,
        "perPage": pageRate
    })
    data = response.json()
    return data
  

  def getTopAiring(self,page:int,pageRate:int)->None:
    """
    Get Top Airing Anime.\n
    Parameters -->\n
    page -- Index of Page\n
    pageRate -- No. Animes Per Page
    """

    url = self.aniListUrl + 'popular'
    response = requests.get(url,stream=True, params={
        "page": 1,
        "perPage": 20
    })
    data = response.json()
    
    return data


  def searchAnime(self,params:dict={}):
    """SearchAnime Using Filters
    
    Keyword arguments:\n
    query -- Search Query\n
  type -- MANGA or ANIME (Anime 
    default)\n
    page -- Index of Page \n
    perPage -- The number of items /pagen\n
    season -- ["WINTER", "SPRING", "SUMMER", "FALL"]\n
    season -- ["TV","TV SHORT","OVA","ONA","MOVIE","SPECIAL","MUSIC"]\n
    sort -- ["POPULARITY DESC" ,"POPULARITY" ,"TRENDING DESC" ,"TRENDING" ,"UPDATED AT DESC" ,"UPDATED AT" ,"START DATE DESC" ,"START DATE" ,"END DATE DESC" ,"END DATE" ,"FAVOURITES DESC" ,"FAVOURITES" ,"SCORE DESC" ,"SCORE" ,"TITLE ROMAJI DESC" ,"TITLE ROMAJI" ,"TITLE ENGLISH DESC" ,"TITLE ENGLISH" ,"TITLE NATIVE DESC" ,"TITLE NATIVE" ,"EPISODES DESC" ,"EPISODES" ,"ID" ,"ID DESC"]
    \n
    genres -- ["Action" ,"Adventure" ,"Cars" ,"Comedy" ,"Drama" ,"Fantasy" ,"Horror" ,"Mahou Shoujo" ,"Mecha" ,"Music" ,"Mystery" ,"Psychological" ,"Romance" ,"Sci-Fi" ,"Slice of Life" ,"Sports" ,"Supernatural" ,"Thriller"]\n
    year -- Animes in Year query\n
    status -- ["RELEASING" ,"NOT YET RELEASED" ,"FINISHED" ,"CANCELLED" ,"HIATUS"] hiatus means discontinued\n

    Return: List of Anime
    """
    
    url = self.aniListUrl + 'advanced-search'
    response = requests.get(url,stream=True, params=params)
    data = response.json()

    return data
  

  def getAnimeInfo(self,id:str,provider:str='zoro'):
    """
    Get Anime Information.\n
    Parameters -->\n
    id -- id of Anime from Anilist\n
  provider --> ["gogoanime",'animefox','animepahe','zoro','9anime'] "zoro" 
    default
    """

    url = self.aniListUrl + f'info/{id}?provider={provider}'
    response = requests.get(url,stream=True)
    data = response.json()
    data['provider'] = provider

    return data
  

  def getEpStreamLink(self,epId="",provider:str='zoro',server:str=""):
    """Get Anime Stream Links
    
    Keyword arguments:

    epId -- Id of Episode

  provider -- Provider of episodes ["gogoanime",'animefox','animepahe','zoro','9anime'] "zoro" 
    default]
    
    server --\n9anime --> "vidcloud" "streamsb" "vidstreaming" "streamtape" "vidcloud"\n
    animefox --> doesn't need an server\n
    animefox --> doesn't need an server\n
    gogoanime --> "gogocdn" "streamsb" "vidstreaming"\n
    zoro -->"vidcloud" "streamsb" "vidstreaming" "streamtape" "vidcloud"

    Return: Episode streaming links
    """
    
    
    url = f"https://api.consumet.org/anime/zoro/watch/EPID?server=PROVIDER"
    
    response = requests.get(url,stream=True)
    data = response.json()

    return data
  

  def getEpDownloadLink(self,ep=""):
    url = self.aniListUrl + f'watch/{ep}'
    response = requests.get(url,stream=True)
    data = response.json()

    link = data.get('headers').get("Referer").replace('embedplus','download')

    return link
  

  def getLatestEpisodes(self,page:int,pageRate:int,provider="gogoanime")->None:
    url = self.aniListUrl+"recent-episodes"
    response = requests.get(url,stream=True, params={
      "page": page,
      "perPage": pageRate,
      "provider": provider
    })
    data = response.json()
  
    return data