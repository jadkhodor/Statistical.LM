import os
import time
from urllib.request import urlopen
import zipfile
import pandas as pd
import networkx


f_name= "git_web_ml.zip"
link = "https://snap.stanford.edu/data/git_web_ml.zip"

print(os.getcwd())

if not os.path.isfile(f_name):
    print("Downloading")
    with urlopen(link) as content, open(f_name, "wb") as file:
        file.write(content.read())

if not os.path.isdir(f_name):
    print("File Found. Unpacking file")
    with zipfile.ZipFile(f_name, 'r') as zip:
        zip.extractall("")

print("Loading found data")

edges = pd.read_csv("git_web_ml/musae_git_edges.csv")
classes = pd.read_csv("git_web_ml/musae_git_target.csv")


graph = networkx.Graph()
graph.add_nodes_from(classes["id"])

for index, row in edges.iterrows():
    graph.add_edge(row["id_1"],row["id_2"])


start_time = time.time() #Count execution time
deg_ml = [0]*len(classes)
deg_web = [0]*len(classes)
ml_target = classes["ml_target"].tolist()


for edge in graph.edges():
    edge_source, edge_destination = edge[0], edge[1]


    if ml_target[edge_destination] == 1:
        deg_ml[edge_source] = 1
    else:
        deg_web[edge_source] = 1


    if ml_target[edge_source] == 1:
        deg_ml[edge_destination] = 1
    else:
        deg_web[edge_destination] = 1


end_time = time.time()
print("Time : %s"%(end_time-start_time))