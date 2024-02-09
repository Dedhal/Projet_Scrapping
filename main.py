import os
import Node
import json
import dill

if not os.path.exists("nodes.pkl"):
    os.system("cd dataset_scrapper & scrapy crawl h_f1 -o dataset_scrapper/dataset/dataset.json")

    Nodes = []

    with open("dataset_scrapper/dataset_scrapper/dataset/dataset.json", "r") as file:
        datas = json.load(file)
        for data in datas:
            Nodes.append(Node.Node(data["url"]))
            
        for data in datas:
            for link in data["links"]:
                for node in Nodes:
                    if node.url == data["url"]:
                        for target_node in Nodes:
                            if target_node.url == link:
                                node.add_link(target_node)
                                break
                    
    os.remove("dataset_scrapper/dataset_scrapper/dataset/dataset.json")
    with open("nodes.pkl", "wb") as file:
        dill.dump(Nodes, file)
    
else:
    with open("nodes.pkl", "rb") as file:
        Nodes = dill.load(file)
        
