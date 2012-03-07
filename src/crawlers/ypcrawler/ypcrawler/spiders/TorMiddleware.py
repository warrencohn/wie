class TorMiddleware(object): 
    def process_request(self, request, spider): 
        request.meta["proxy"] = "http://172.28.10.20:2222"
