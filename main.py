from pgsql import query
import sql
import json
import requests
from datetime import datetime

def get_movie_data(title):
    headers = {"Authorization": "9855f49b"}
    request_url = f"https://www.omdbapi.com/?t={title}&apikey=686eed26"
    return requests.get(request_url, headers=headers).json()

if __name__ == '__main__':

    #Create complete json pulling from API
    '''
    
                #load in titles from local json file with year >= 2018
    ml = open('/Users/yorkmac049/PycharmProjects/patrick-andresen-python-etl-p2/datasets/json/movies.json','r')
    data = json.load(ml)
    ml.close()
    titles = []
    for i in data:
        if i["year"] >= 2018:
            titles.append(i["title"])

    no_dup = set(titles)                #convert to set to remove any duplicates

                #import movie data from API for each film & store in dictionary
    movie_info = {}
    for j in no_dup:
        movie_info[j] = get_movie_data(j)

                #convert complete dictionary into json file
    f_write = open('datasets/json/filtered_movies.json','w')
    json.dump(movie_info, f_write)
    f_write.close()
    
    '''
    #clean json data - remove any movies without english in language

    fm = open('datasets/json/filtered_movies.json','r')
    fms = fm.read()
    fm.close()
    info = json.loads(fms)
    value = "English"
    english_movies = []
    for k, v in info.items():
        for _k, _v in v.items():
            if _k == "Language":
                if value in _v:
                    english_movies.append(v)

            #limit to needed columns
    limited = []
    need_key = ["Title", "Rated", "Released", "Runtime", "Genre", "Director", "Writer", "Actors", "Plot",
                       "Awards", "Poster"]
    for i in english_movies:
        sub = {key: i[key] for key in need_key}
        limited.append(sub)

            # Remove any movies missing data
    complete_movie = []
    for i in limited:
        if "N/A" not in i.values():
            complete_movie.append(i)

            # Create schema and table
    query(sql.create_schema)
    query(sql.create_table)


    for item in complete_movie:
        to_add = []
        to_add.append(item["Title"])
        to_add.append(item["Rated"])
        date_obj = datetime.strptime(item["Released"], "%d %b %Y")
        to_add.append(date_obj)
        to_add.append(int(item["Runtime"][0:3].strip()))
        to_add.append(item["Genre"].split(","))
        to_add.append(item["Director"])
        to_add.append(item["Writer"].split(","))
        to_add.append(item["Actors"].split(","))
        to_add.append(item["Plot"].strip(','))
        to_add.append(item["Awards"].split(","))
        to_add.append(item["Poster"])
        query(sql.insert_ml, to_add)