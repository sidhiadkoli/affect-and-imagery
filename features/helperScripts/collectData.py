import praw
import json

#int(time.mktime(datetime.datetime.strptime("14/02/2017", "%d/%m/%Y").timetuple()))

def convertObj(obj):
    obj = vars(obj)
    obj['_reddit'] = obj['subreddit_id']
    obj['subreddit'] = obj['subreddit'].display_name

    if obj['author']:
        obj['author'] = obj['author'].name

    if '_replies' in obj.keys():
        obj['_replies'] = None

    if '_submission' in obj.keys():
        obj['_submission'] = None

    return obj

# Gets 20k submissions from February 14th 2017 backwards.
def getData(reddit):
    timeStart = 1487048400
    timeStep = 2678400

    idList = []
    rep = False

    t = "timestamp:"
    e = ".."
    listData = []

    while len(listData) < 20000:    
        data = reddit.subreddit("shortscarystories").search(t + str(timeStart - timeStep) + e + str(timeStart), syntax='cloudsearch', limit=1000)
        timeStart = timeStart - timeStep

        for d in data:
            if d.name in idList:
                print("We are repeating ids! " + d.name)
                rep = True
                break
    
            listData.append(convertObj(d))
            idList.append(listData[-1]['name'])

        #print(len(listData))

        if rep:
            break

    with open('data.txt', 'w') as fout:
        json.dump(listData, fout)
        fout.close()
    print(timeStart)

def getComments(reddit):
    with open("data.txt", "r") as fin:
        data = json.load(fin)
        fin.close()

    for d in data:
        comms = reddit.submission(d['id']).comments
        comments = []
        print(d['id'] + ":" + str(len(comms)))
        for c in comms:
            comments.append(convertObj(c))
        d['comments'] = comments

        with open("dataWithComments.txt", "w") as fout:
            json.dump(data, fout)
            fout.close()

if __name__ == '__main__':
    reddit = praw.Reddit(client_id='t8dHmSTB-LTbTw', client_secret='H2tdURMdsvfv2Tvx0033I5i5M9g', password='Awesome123', user_agent='python/nlpInContextProj', username='sadko2828')

    getComments(reddit)
