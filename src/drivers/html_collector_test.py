from .html_collector import HtmlCollector
from .http_requester import HttpRequesterLinks
from .http_requester import HttpRequesterStats


from .mocks.http_requester_mock import mocks_request_from_page


def test_collect_essential_information():
    http_request_links = HttpRequesterLinks()
    
    html_collector_links = HtmlCollector()
    links = html_collector_links.collect_links(http_request_links.request_from_page_links()['html'])

    requester_html = HttpRequesterStats()

    htmls=[]
    for link in links:
        html = requester_html.request_from_page_stats(link['link'])
        htmls.append(html)

    for html in htmls:
        stats = html_collector_links.collect_stats(html['html'])
        print(stats)
