# -*- coding: utf-8 -*-
__author__ = 'Henry B. <tubnd.younet@gmail.com>'

from scrapy.exceptions import NotConfigured
from scrapy.utils.misc import arg_to_iter
import itertools
import base64
from six.moves.urllib.request import getproxies, proxy_bypass
from six.moves.urllib.parse import unquote

try:
    from urllib2 import _parse_proxy
except ImportError:
    from urllib.request import _parse_proxy
from six.moves.urllib.parse import urlunparse

from scrapy.utils.httpobj import urlparse_cached
from scrapy.exceptions import NotConfigured

from w3lib.http import basic_auth_header
import logging

log = logging.getLogger('scrapyx.smartproxy')

class SmartProxyMiddleware(object):
    def __init__(self, settings):
        if not settings.getbool('SMARTPROXY_ENABLED', True):
            raise NotConfigured
        self.proxies = itertools.cycle(arg_to_iter(settings.get('SMARTPROXY_URL', 'http://127.0.0.1:24000')))        

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.settings)
        return o

    def _get_proxy(self, url):
        proxy_type, user, password, hostport = _parse_proxy(url)
        proxy_url = urlunparse((proxy_type, hostport, '', '', '', ''))

        if user and password:
            user_pass = '%s:%s' % (unquote(user), unquote(password))
            creds = base64.b64encode(user_pass).strip()
        else:
            creds = None

        return creds, proxy_url

    def process_request(self, request, spider):
        if not request.meta.get('bypass_proxy', False) and request.meta.get('proxy') is None:
            try:
                creds, proxy = self._get_proxy(next(self.proxies))
            except:
                creds, proxy = self._get_proxy(self.proxies.next())            
            request.meta['proxy'] = proxy
            if creds:                
                request.headers['Proxy-Authorization'] = b'Basic ' + creds