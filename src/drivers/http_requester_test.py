from .http_requester import HttpRequesterLinks
from .http_requester import HttpRequesterStats
from .html_collector import HtmlCollectorLinks


def test_request_link_from_page():

    http_requester = HttpRequesterLinks()
    request_response = http_requester.request_from_page()
    print(request_response)


def test_request_stats_from_page():
    http_requester = HttpRequesterLinks()
    request_response = http_requester.request_from_page()
    
    html_collector = HtmlCollectorLinks()
    links = html_collector.collect_essential_information(request_response["html"])
    
    http_requester_stats = HttpRequesterStats()
    for link in links:
        print(f"link aqui -= {link['link']}")
        print(type(link))
        http_requester_stats.request_from_page(link['link'])
        print(http_requester_stats['html'])
