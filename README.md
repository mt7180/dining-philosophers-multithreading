# dining-philosophers-multithreading

https://en.wikipedia.org/wiki/Dining_philosophers_problem

### Problem statement:
Five philosophers dine together at the same table. Each philosopher has their own plate at the table. There is a chopstick between each plate. The dish served has to be eaten with two chopsticks. Each philosopher can only alternately think and eat. Moreover, a philosopher can only eat their dish when they have both a left and right chopstick. Thus two chopstick will only be available when their two nearest neighbors are thinking, not eating. After an individual philosopher finishes eating, they will put down both chopstick. The problem is how to design a regimen (a concurrent algorithm) such that no philosopher will starve while beeing stuck with only one chopstick; i.e., each can forever continue to alternate between eating and thinking, assuming that no philosopher can know when others may want to eat or think

### Solution:
working with priorized chopsticks: each philosopher is set-up to pick up the lower (left) chopstick first, except of the last philosopher who does in reverse, so that philosophers won't get stuck. 

The threading library is used for multithreading and the lock/ release mechanism guards against simultaneous access to a chopstick