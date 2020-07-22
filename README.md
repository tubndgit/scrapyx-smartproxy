# scrapy-smartproxy

SmartProxy middleware for Scrapy (http://scrapy.org/)

Required
--------

    python version >= 2.7


Install
--------

Checkout the source and run

    python setup.py install


settings.py
-----------

    # Activate the middleware
    SMARTPROXY_ENABLED = True
    
    # The SmartProxy URL
    SMARTPROXY_URL = 'http://user:pass@gate.smartproxy.com:10000'

    DOWNLOADER_MIDDLEWARES = {
        'scrapyx_smartproxy.SmartProxyMiddleware': 610,
    }
