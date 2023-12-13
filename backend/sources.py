import requests

api_key = "aDtCNQDaFSnQlFjOQFlmd78WGQLCJ4x0214L1I4o"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like

class WatchMode():
    def __init__ (self, search_input):
        if search_input is not None:
            self.search_input = search_input
        else:
            raise IOError
        search_string = self.transform_search(search_input)
        WatchMode.ID(search_input, search_string)
    
    def transform_search(self, search_input):
        search_string = search_input.replace(" ", "%20")
        return search_string

    class ID():
        def __init__ (self, search_input, search_string):
            if search_input is not None:
                self.search_input = search_input
            else:
                raise IOError
            if search_string is not None:
                self.search_string = search_string
            else:
                raise IOError
            id = self.getID(search_input, search_string)
            WatchMode.Sources(search_input, id)

        def getID(self, search_input, search_string):
            id_url = "https://api.watchmode.com/v1/search/?apiKey="+api_key+"&search_field=name&search_value="+search_string+"&types=tv,movie"
            
            response = requests.get(id_url, headers)
            title_results = response.json()['title_results']
            for i in range(len(title_results)):
                if title_results[i]['name'] == search_input:
                    id = str(title_results[i]['id'])
                    return id
                
    class Sources():
        def __init__ (self, search_input, id):
            if search_input is not None:
                self.search_input = search_input
            else:
                raise IOError
            if id is not None:
                self.id = id
            else:
                raise IOError
            # global long_chat_response
            # long_chat_response = self.getSources(search_input, id)
            global short_chat_response
            short_chat_response = self.getSources(search_input, id)

        def getSources(self, search_input, id):
            source_url = "https://api.watchmode.com/v1/title/"+id+"/sources/?apiKey="+api_key
            response = requests.get(source_url, headers)
            source_results = response.json()
            # long_chat_response = search_input + ": \n"
            source_list = []
            for result in source_results:
                # long_chat_response += "\t" + result['name'] + ": " + result['web_url'] + "\n"
                if result['name'] not in source_list: source_list.append(result['name'])
            # print(long_chat_response)
            # return long_chat_response
            short_chat_response = "\nWatch \"" + search_input + "\" on "
            for i in range(len(source_list)):
                if i == len(source_list)-1:
                    short_chat_response = short_chat_response + "and " + source_list[i] + "."
                else:
                    short_chat_response = short_chat_response + source_list[i] + ", "
            return short_chat_response

def main(search_input):
    if search_input is not None and type(search_input) == list:
        # full_chat = ""
        full_short_response = ""
        for i in search_input:
            WatchMode(i)
            # full_chat = full_chat + long_chat_response
            full_short_response = full_short_response + short_chat_response
    else:
        raise IOError
    print(full_short_response)
    return full_short_response

if __name__ == "__main__":
    # I am inputting example TV Shows
    main(["Criminal Minds", "Sherlock"])