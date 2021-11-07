import argparse
import inspect
import textwrap

# Reference: https://stackoverflow.com/questions/29613487/multiple-lines-in-python-argparse-help-display

parser = argparse.ArgumentParser(
    description=textwrap.dedent("""\
                                Test
                                """),
    formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-t', '--time', type=int, 
        help="""\
        Set to time in seconds for that
        app to run...
            """)
parser.add_argument('-v', '--verbose', action='store_true', 
        help=textwrap.dedent("""\
            Display more info on console
            
            Is this what u want? hehe
            """))
parser.add_argument('-d', '--data')
parser.add_argument('-f', '--file')
args = parser.parse_args()
print(args)
