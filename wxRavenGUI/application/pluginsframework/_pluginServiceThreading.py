'''
Created on 22 déc. 2021

@author: slinux
'''
#
#
#
#    DO NOT USE !
#
#
#
#
from threading import Thread, Event

class KillableThread(Thread):
    def __init__(self, sleep_interval=1, target=None, name=None, args=(), kwargs={}):
        super().__init__(None, target, name, args, kwargs)
        self._kill = Event()
        self._interval = sleep_interval
        print(self._target)

    def run(self):
        while True:
            # Call custom function with arguments
            self._target(*self._args)

            # If no kill signal is set, sleep for the interval,
            # If kill signal comes in while sleeping, immediately
            #  wake up and handle
            is_killed = self._kill.wait(self._interval)
            if is_killed:
                break

        print("Killing Thread")

    def kill(self):
        self._kill.set()
        
    def stop(self):
        self._kill.set()