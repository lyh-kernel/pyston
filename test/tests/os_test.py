# allow-warning: converting unicode literal to str

# currently broken:
# import os.path

import os

r1 = os.urandom(8)
r2 = os.urandom(8)
print len(r1), len(r2), type(r1), type(r2), r1 == r2
