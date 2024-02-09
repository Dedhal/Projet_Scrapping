
class Node:
    def __init__(self, url):
        self.url = url
        self.links = []
        
    def add_link(self, link):
        self.links.append(link)