# -*- coding: utf-8 -*-
#!/usr/bin/python3

import requests


def api_request(end_point, proxies=None, user_agent=None):
    if user_agent is None:
        request_base_headers = {'User-agent': 'mkorkmaz/FR24/2.0'}
    else:
        request_base_headers = {'User-agent': user_agent}
    r = requests.get(end_point, headers=request_base_headers, proxies=proxies)
    if r.status_code is 402:
        raise RuntimeError("Request to " + end_point + " requires payment")
    if r.status_code is 403:
        raise RuntimeError("Request to " + end_point + " is Forbidden")
    if r.status_code is 404:
        raise RuntimeError("Request to " + end_point + " is NotFound")
    if r.status_code is 500:
        raise RuntimeError("Request to " + end_point + " returns InternalServerError")
    return r.json()
