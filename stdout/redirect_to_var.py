# https://stackoverflow.com/a/22434594

import io
from contextlib import redirect_stdout

with io.StringIO() as buf, redirect_stdout(buf):
    print('redirected')
    output = buf.getvalue()
print(output)