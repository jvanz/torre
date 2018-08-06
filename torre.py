from requests import get
import requests

URL = "https://bio.torre.co/api/{0}"

def get_bio(personid):
    #  we need a valid person id
    if personid is None:
        return None
    #  get bio info
    res = get(URL.format("bios/{0}".format(personid)))
    if res.status_code == requests.codes.ok:
            return res.json()
    return None
