import sys
import time
import threading

"""
Spinner :

An easy spinner for consoles with less codec support

Use Case : (when on using spinner the program fails giving this error)
'charmap' codec can't encode characters

States of the Spinner :
| , / , - , \\ (backslash)
"""


class Spinner:
    busy = False

    # delay between two cursor changes
    delay = 0.2

    # ------------------- Static method that yields the cursor ------------------- #
    @staticmethod
    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
                # --------------- This loop yields a generator ---------------- #
                yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay):
            self.delay = delay

    def spinner_task(self):
        while self.busy:
            # --------------- Moving to the next item in the generator list -------------- #
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def __enter__(self):
        """
         Starts the cursor 
        """
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        """
        Once the thread is done executing remove the last residual by moving cursor back by 1 char and then erasing it
        """
        sys.stdout.write('\b')
        sys.stdout.write(' ')
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False


"""
with Spinner():
    # time consuming task
    for _ in range(1):
        time.sleep(5)
"""
