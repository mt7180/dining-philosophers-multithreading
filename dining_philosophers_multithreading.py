"""Problem solution for dining philosophers in python, see also 
    Cracking the Coding Interview Ch. 15 (S. 451)
"""

import threading as trd
import random as rd


NUMBER_OF_PHILOSOPHERS = 5

class Philosopher(trd.Thread):
    """ class representing the philosopher who wants to eat or think """

    bites = 3

    def __init__(self, i, cs_left, cs_right):
        trd.Thread.__init__(self)
        self.index = i
        if cs_left.getNumber() < cs_right.getNumber():
            self.lower = cs_left
            self.higher = cs_right
        else:
            self.lower = cs_right
            self.higher = cs_left

    def __repr__(self):
        return f"P nbr {self.index}"

    def eat(self):
        self.pick_up()
        self.chew()
        self.put_down()

    def pick_up(self):
        print(f'P{self.index} picking up lower {self.lower.number} ...')
        self.lower.pickUp()
        print(f'P{self.index} picking up higher {self.higher.number} ...')
        self.higher.pickUp()

    def chew(self):
        pass

    def put_down(self):
        print(f'P{self.index} putting down lower {self.lower.number} ...')
        self.lower.putDown()
        print(f'P{self.index} putting down higher {self.higher.number} ...')
        self.higher.putDown()

    def run(self):       # needs to be named run (run-method of Thread object is overwritten)
        for _ in range(self.bites):
            self.eat()
        print(f"P{self.index} ready")


class Chopstick:
    """ Class representing the chopstic of the philosophers"""

    num_instances = 0

    def __init__(self, nbr):
        self.__class__.num_instances += 1
        self.number = nbr
        self.lock = trd.Lock()

    def __repr__(self):
        return f"Stick nbr {self.number} locked: {self.lock_stat()}"

    def lock_stat(self):
        """ if able to lock the thread, status is True, which means: 
            was unlocked even if returned immediately with blocking = False,
            thread has to be released (or reused)
        """
        status = not self.lock.acquire(False)
        self.lock.release()
        return status

    def getNumber(self):
        return self.number

    def pickUp(self):
        self.lock.acquire()

    def putDown(self):
        self.lock.release()


if __name__ == "__main__":
    rd.seed()
    chopsticks = [Chopstick(i) for i in range(NUMBER_OF_PHILOSOPHERS)]
    #print(chopsticks)
    philosophers = [
        Philosopher(i, chopsticks[i], chopsticks[i+1] ) 
        for i in range(NUMBER_OF_PHILOSOPHERS-1)
    ]
    philosophers.append(Philosopher(4, chopsticks[4], chopsticks[0]))
    # print(philosophers)
    queue = rd.sample(range(NUMBER_OF_PHILOSOPHERS), NUMBER_OF_PHILOSOPHERS)
    print(queue)

    for rand_num in queue:
        n = rand_num
        while philosophers[n].is_alive():
            # go one further in the circle
            n = (
                n + 1 if n < (NUMBER_OF_PHILOSOPHERS-1)
                else n - (NUMBER_OF_PHILOSOPHERS-1)
            )
        print(f'starting Thread {n}')
        philosophers[n].start()

    print("threads all out ...")
    