import observers  # to instantiate observers
import requests
from common.observer import observations
from requests_html import HTMLSession


if __name__ == "__main__":
    out = list()

    for obs in observations:
        f_ref = obs['f_ref']
        f_url = obs['url']

        # s = HTMLSession()
        # response = s.get(f_url)
        # response.html.render(wait=5)
        #
        # print(response)
        # breakpoint()

        html = requests.get(f_url)
        result = f_ref(html.text)
        out.append(result)

    for r in out:
        print(r)
