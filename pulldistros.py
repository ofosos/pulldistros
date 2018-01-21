from bs4 import BeautifulSoup
import requests
import requests_cache


requests_cache.install_cache('/tmp/req.cache', backend='sqlite',
                             expire_after=3600)


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

    soup = BeautifulSoup(r.text, 'html5lib')

    dist = {}

    summary = [td for td in soup.find_all('td') if td.get('class') ==
               ["TablesTitle"]][0]
    for li in summary.find_all("li"):
        tpl = li.text.split(':')
        if len(tpl) > 1:
            text = tpl[0].strip()
            value = tpl[1].strip()
            dist[text] = value

    infotags = soup.find('th', string='Alternative User Forums').parent.parent
    for row in infotags.select('tr[class=Background]'):
        head = row.select('th[class=Info]')
        head_txt = ' '.join([h.text for h in head])
        elem = row.select('td[class=Info]')
        elem_txt = ' '.join([e.text for e in elem])

        dist[head_txt] = elem_txt

    releases = {}

    relnames = []
    reltag = soup.find('td', attrs={'class': 'TablesInvert'})

    releases[reltag.text] = {}
    relnames.append(reltag.text)

    while reltag.find_next_sibling('td'):
        reltag = reltag.find_next_sibling('td')

        releases[reltag.text] = {}
        relnames.append(reltag.text)

    try:
        infotbl = soup.find('th', string='Full Package List').parent.parent
        for r in infotbl.find_all('tr'):
            thel = r.find('th')
            header = thel.text
            vals = r.find_all('td')

            for i in range(len(vals)):
                releases[relnames[i]][header] = vals[i].text
    except:
        pass

    dist['releases'] = releases
    return dist
