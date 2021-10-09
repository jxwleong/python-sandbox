# Reference: https://gist.github.com/bradmontgomery/4f4934893388f971c6c5
import time
import contextlib

class Timer():
    def __enter__(self):
        self.start = time.time()
        print("Starting at {}".format(self.start))
        return self

    def __exit__(self, type, value, traceback):
        # This code is guaranteed to run
        if traceback:
            print("type: {}".format(type))
            print("value: {}".format(value))
            print("traceback: {}".format(traceback))

        self.end = time.time()
        total = self.end - self.start
        print("Ending at {} (total: {})".format(self.end, total))


with Timer():
    time.sleep(5)
