import sys
import time
import threading


"""
Runs the spinner using a seperate thread (So that it can run while another task is going on)

States of the spinner:
[■□□□□□□□□□] , [■■□□□□□□□□] , [■■■□□□□□□□] , [■■■■□□□□□□] , [■■■■■□□□□□] , [■■■■■■□□□□] , [■■■■■■■□□□] , [■■■■■■■■□□] , [■■■■■■■■■□] , [■■■■■■■■■■]

"""


# --------------------- Implemented using multithreading --------------------- #
class Spinner:
    busy = False

    # delay between two cursor changes
    delay = 0.2

    # ------------------- Static method that yields the cursor ------------------- #
    @staticmethod
    def spinning_cursor():

        while True:
            for cursor in ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]:
                # --------------- This loop yields a generator ---------------- #
                yield cursor

    def __init__(self, delay=None):

        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay):
            self.delay = delay

    def spinner_task(self):
        # --------------- Moving to the next item in the generator list -------------- #

        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b'*12)
            sys.stdout.flush()

    def __enter__(self):
        """
         Starts the cursor 
        """

        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        """
        Once the thread is done executing remove the last residual by moving cursor back by 12 characters and then erasing it
        """

        sys.stdout.write('\b'*12)
        sys.stdout.write('[■■■■■■■■■■]\n')
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
