import json

fin = open("dataWithComments.txt")
redditData = json.load(fin)

commLabels = []

with open("comments.txt") as fin:
    for line in fin:
        commLabels.append(line.strip())

redditLabels = []

with open("reddit.txt") as fin:
    for line in fin:
        redditLabels.append(line.strip())


for data in redditData:
    for comm in data["comments"]:
        commKeys = list(comm.keys())
        for k in commKeys:
            if k not in commLabels:
                del comm[k]

    dataKeys = list(data.keys())
    for k in dataKeys:
        if k not in redditLabels:
            del data[k]

fout = open("dataCleaned.txt", "w")
json.dump(redditData, fout)