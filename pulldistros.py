from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
import json
import requests_cache


requests_cache.install_cache('/tmp/req.cache', backend='sqlite',
                             expire_after=1500)


def distros():
    r = requests.get('https://distrowatch.com')

    soup = BeautifulSoup(r.text, 'html.parser')

    dists = []

    sels = soup.select('select[name=distribution] option[value]')
    for s in sels:
        if s['value'] != '' and s['value'] != 'all':
            dists.append(s['value'])

    return dists


def distinfo(distro):
    r = requests.get('http://distrowatch.com/table.php?distribution={0}'
                     .format(distro))

    soup = BeautifulSoup(r.text, 'html.parser')

    dist = {}

    infotags = soup.find('th', string='Alternative User Forums').parent.parent
    for row in infotags.select('tr[class=Background]'):
        head = row.select('th[class=Info]')
        head_txt = ' '.join([h.text for h in head])
        elem = row.select('td[class=Info]')
        elem_txt = ' '.join([e.text for e in elem])

        dist[head_txt] = elem_txt

    releases = {}

    relnames = []
    reltags = soup.select('td[class=TablesInvert]')
    for reltag in reltags:
        releases[reltag.text] = {}
        relnames.append(reltag.text)

    infotbl = soup.find('th', string='Full Package List').parent.parent
    for row in infotbl.find_all('tr'):
        thel = row.find('th')
        header = thel.text
        vals = row.find_all('td')
        for i in range(len(vals)):
            releases[relnames[i]][header] = vals[i].text

    dist['releases'] = releases
    return dist
