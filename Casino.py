import threading
import time
import random
import itertools

suits = ["hearts, diamonds", "clubs", "spades"]
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


#Casino War is played with normally with 6 standard 52 decks
#First part is creating each deck and adding it to our complete deck


deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))



#random.shuffle(deck)

for i in range(len(deck)):
    print(deck[i][0], "of", deck[i][1])

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print("Starting " + self.name)
      # Get lock to synchronize threads
      threadLock.acquire()
      print_time(self.name, self.counter, 3)
      # Free lock to release next thread
      threadLock.release()

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")