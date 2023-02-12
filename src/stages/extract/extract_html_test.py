from src.drivers.http_requester import HttpRequesterLinks,HttpRequesterStats
from src.drivers.html_collector import HtmlCollector
from src.errors.extract_error import ExtractError

from .extract_html import ExtractHtml


def test_extract():
    http_requester_links = HttpRequesterLinks()
    http_requester_stats = HttpRequesterStats()
    html_collector = HtmlCollector()

    extract_html = ExtractHtml(http_requester_links, http_requester_stats, html_collector)
    response = extract_html.extract()


    print(response)


def test_extract_error():
    http_requester_links = 'IssoVaiDarErro'
    http_requester_stats = HttpRequesterStats()
    html_collector = HtmlCollector()

    extract_html = ExtractHtml(http_requester_links, http_requester_stats, html_collector)

    try:
        extract_html.extract()
    except Exception as exception:
         assert isinstance(exception, ExtractError)
