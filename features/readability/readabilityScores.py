from textstat.textstat import textstat

class ReadabilityScores:
    def flesch(text):
        return textstat.flesch_reading_ease(text)

    def kincaid(text):
        return textstat.flesch_kincaid_grade(text)

    def gunningFog(text):
        return textstat.gunning_fog(text)

    def ari(text):
        return textstat.automated_readability_index(text)

    # Find a way to get the average across all the scores.
    # They are not in the same scale and hence the following won't work.
    def readabilityAvg(text):
        return flesch(text) + kincaid(text) + gunningFog(text) + ari(text)

'''
if __name__ == "__main__":
    # text = "Automated Readability Index outputs a number that approximates the grade level needed to comprehend the text." 
   
    fin = open("../../data/dataCleaned.txt")
    reddit = json.load(fin)

    readability = {}

    for r in reddit:
        try :
            rs = {
                "flesch" : ReadabilityScores.flesch(r["selftext"]),
                "kincaid" : ReadabilityScores.kincaid(r["selftext"]),
                "fog" : ReadabilityScores.gunningFog(r["selftext"]),
                "ari" : ReadabilityScores.ari(r["selftext"])
            }
        except :
            #print(r["name"])
            rs = {
                "flesch" : 0.0,
                "kincaid" : 0.0,
                "fog" : 0.0,
                "ari" : 0.0
            }

        readability[r["name"]] = rs

    fout = open("readability.json", "w")
    json.dump(readability, fout)
'''





    