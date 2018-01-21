# Scrape Distrowatch

Scrape metadata from distrowatch.com

## Example

```
from pulldistros import distinfo, distros

print(json.dumps(distinfo('arch')))

for dist in distros():
    d = distinfo(dist)['releases']

    for rel, vals in d.iteritems():
        print("{0}:{1}:{2}".format(dist, rel, vals['Release Date']))
```

## Author

- Mark Meyer (mark@ofosos.org)

## Thanks

- Tobias Mueller instigated this
