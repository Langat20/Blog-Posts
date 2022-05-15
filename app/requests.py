from urllib import response
from .models import Quote
import urllib.request,json


base_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_random_quote():
    url = base_url 

    response = urllib.request.urlopen(url)
    data= json.loads(response.read())
    quote_details=[]

    author = data.get('author')
    quote = data.get('quote')

    new_quote= Quote(author, quote)
    quote_details.append(new_quote)

    return quote_details