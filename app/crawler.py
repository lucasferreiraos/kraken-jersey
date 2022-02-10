from urllib import response
from requests_html import HTMLSession



URL = 'https://alisports.x.yupoo.com/albums?tab=gallery'

session = HTMLSession()

response = session.get(URL)

pagination_lenght = response.html.xpath('/html/body/nav/form/span[2]/input')

pagination_lenght


def get_lenght_pagination(url: str) -> int:
    response = session.get(url)
    pagination_context = response.html.xpath("/html/body/nav/form/span[2]/input")
    pagination_size = int(pagination_context[0].attrs["max"])

    return pagination_size



