# Scrape Distrowatch

Scrape metadata from distrowatch.com

## Example

```
import json
from pulldistros import distinfo, distros

print(json.dumps(distinfo('arch')))

i = 0
for dist in distros():
    i = i + 1
    d = distinfo(dist)['releases']

    print(i)
    for rel, vals in d.items():
        print("{0}:{1}:{2}".format(dist.encode('utf-8'), rel.encode('utf-8'),
                                   vals['Release Date'].encode('utf-8')
                                   if 'Release Date' in vals else 'unknown'))

```

## Author

- Mark Meyer (mark@ofosos.org)

## Thanks

- Tobias Mueller instigated this
