#!/usr/bin/env python

from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'key1'

print dd['key2']
