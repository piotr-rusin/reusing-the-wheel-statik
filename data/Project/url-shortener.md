---
name: URL Shortener
date: 2016-08-05T13:18:43+00:00
source-code-url: https://github.com/piotr-rusin/url-shortener
---

An application for providing shorter aliases for given URLs. It uses my spam-lists library to prevent shortening of URLs recognized as spam or to warn users that an already existing shortened URL has been recognized as spam. The application also handles homoglyphs &#8211; characters and sequences of characters similar to each other &#8211; by internally treating them as identical, saving its users from inconvenience resulting from mistyping or misremembering shortened URLs with potentially confusing characters.

Written in Python 3.4.&#42; and based on Flask 0.11.1 and SQLAlchemy 1.1.3.
