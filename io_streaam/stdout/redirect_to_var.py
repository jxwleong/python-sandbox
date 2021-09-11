# https://stackoverflow.com/a/22434594
import io
import sys
from contextlib import redirect_stdout
import logging

with io.StringIO() as buf, redirect_stdout(buf):
    print('redirected')
    output = buf.getvalue()
print(output)




with io.StringIO() as buf, redirect_stdout(buf):
    logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)
    logging.debug('This will get logged')
    output = buf.getvalue()
print(f'Logger:Debug: {output}')
