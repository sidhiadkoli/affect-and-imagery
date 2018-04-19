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
