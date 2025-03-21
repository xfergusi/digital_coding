import pytest
from src.log_parser import get_ip_from_log, get_url_from_log

def test_get_ip_from_log():
    log = "50.112.00.28 - - [11/Jul/2018:15:49:46 +0200] \"GET /faq/how-to-install/ HTTP/1.1\" 200 3574 \"-\" \"Mozilla/5.0 (X11; U; Linux x86_64; ca-ad) AppleWebKit/531.2+ (KHTML, like Gecko) Safari/531.2+ Epiphany/2.30.6\""
    assert get_ip_from_log(log) == "50.112.00.28"

def test_get_url_from_log():
    log = "50.112.00.28 - - [11/Jul/2018:15:49:46 +0200] \"GET /faq/how-to-install/ HTTP/1.1\" 200 3574 \"-\" \"Mozilla/5.0 (X11; U; Linux x86_64; ca-ad) AppleWebKit/531.2+ (KHTML, like Gecko) Safari/531.2+ Epiphany/2.30.6\""
    assert get_url_from_log(log) == "/faq/how-to-install/"