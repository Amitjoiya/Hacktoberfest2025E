import sys,re
if len(sys.argv)<2: print("Usage: python readme-badges.py README.md"); sys.exit(1)
path=sys.argv[1]
with open(path) as f:
    s=f.read()
badge="[![Codecov](https://img.shields.io/badge/coverage-unknown-lightgrey)](https://example.com)"
if badge not in s:
    s = badge + "\n\n" + s
    with open(path,"w") as f: f.write(s)
    print("Badge added")
else:
    print("Badge already present")
