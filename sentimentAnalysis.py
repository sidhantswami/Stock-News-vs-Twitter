from foxnews import getArticle
import paralleldots


paralleldots.set_api_key("cwLrVXjXdbk7BzlBVPNsar8lbnukPXxDgeEdu8MAmFM ")


# for single sentence

def runSentAnalysis(text):
    lang_code="en"
    response = paralleldots.sentiment(text,lang_code)
    return response

