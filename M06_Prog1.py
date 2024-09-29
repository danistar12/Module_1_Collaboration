import multiprocessing
import time
import random
from datetime import datetime

def print_time():
    wait_time = random.uniform(0, 1)  
    time.sleep(wait_time)
    print(f"Current time: {datetime.now()}")

if __name__ == "__main__":
   
    process1 = multiprocessing.Process(target=print_time)
    process2 = multiprocessing.Process(target=print_time)
    process3 = multiprocessing.Process(target=print_time)

    # Start the processes
    process1.start()
    process2.start()
    process3.start()

    # Wait for the processes to complete
    process1.join()
    process2.join()
    process3.join()