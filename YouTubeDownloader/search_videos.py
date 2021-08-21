import youtubesearchpython
import ast
def videos_search(query):
    try:
        data = youtubesearchpython.VideosSearch(query,limit=1000)
        set_All = set()
        counter = 0
        for x in range(30):
            if counter >= 200:
                break
            datalist = set()
            datalist = (str(data.result()))
            List_Links = set()
            datalist = ast.literal_eval(datalist)
            for y in datalist["result"]:
                List_Links.add(str(y["link"]))
            for xo in List_Links:
                if xo not in set_All:
                    counter+=1
                    set_All.add(xo)
            try:
                data.next()
            except:
                break
        return set_All
    except:
        pass