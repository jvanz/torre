from os import environ
from urlparse import parse_qs

from flask import Flask, render_template, request
from linkedin.linkedin import (LinkedInAuthentication, LinkedInApplication,
        PERMISSIONS)

from torre import get_bio

cache = {}

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/torrebio/<string:personid>", methods=["GET"])
def get_torrebio_html(personid):
    torrebio = get_bio(personid)
    print(torrebio)
    return render_template("torrebio.html", bio=torrebio)

@app.route("/linkedin/authurl/<string:linkedinid>", methods=["GET"])
def get_linkedin_authurl(linkedinid):
    API_KEY = environ.get('LINKEDIN_API_KEY')
    API_SECRET = environ.get('LINKEDIN_API_SECRET')
    RETURN_URL = 'http://localhost:5000/linkedin/authorized'
    authentication = LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL,
        [PERMISSIONS.BASIC_PROFILE, PERMISSIONS.EMAIL_ADDRESS])
    url = authentication.authorization_url
    state = parse_qs(url)['state'][0]
    cache[state] = authentication
    return url

@app.route("/linkedin/authorized", methods=["GET"])
def get_linkedin_authorized():
    code = request.args.get("code")
    state = request.args.get("state")
    cache[state].authorization_code = code
    token = cache[state].get_access_token()
    application = LinkedInApplication(token=token)
    profile = application.get_profile(selectors=[
        'id', 'first-name', 'last-name', 'maiden-name', 'formatted-name',
        'phonetic-first-name', 'phonetic-last-name', 'formatted-phonetic-name',
        'headline', 'location', 'industry', 'current-share', 'num-connections',
        'num-connections-capped', 'summary', 'specialties', 'positions',
        'picture-url', 'picture-urls', 'site-standard-profile-request',
        'api-standard-profile-request', 'public-profile-url', 'email-address'] )
    return render_template("index.html", linkedin_profile=application.get_profile())
