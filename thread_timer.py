import threading
import time
import logging
import winsound

logging.basicConfig(
    filename="countdown_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s"
)

stop_flag = False 

def countdown_timer(seconds):
    global stop_flag
    for i in range(seconds, 0, -1):
        if stop_flag:
            print("\n❌ Countdown stopped.")
            logging.info("Countdown stopped by user.")
            return
        print(f"⏳ Remaining: {i} sec", end="\r")
        logging.info(f"Time left: {i} sec")
        time.sleep(1)

    print("\n🎉 Time's up!")
    logging.info("Time's up!")
    winsound.Beep(1000, 500)  

def listen_for_stop():
    global stop_flag
    while not stop_flag:
        key = input()
        if key.lower() == "q":
            stop_flag = True


def start_timer():
    global stop_flag
    stop_flag = False 

    seconds = int(input("⏳ Enter countdown time (sec): "))
    timer_thread = threading.Thread(target=countdown_timer, args=(seconds,))
    stop_thread = threading.Thread(
        target=listen_for_stop, daemon=True
    ) 

    timer_thread.start()
    stop_thread.start()

    timer_thread.join()


if __name__ == "__main__":
    try:
        start_timer()
    except KeyboardInterrupt:
        print("\n❌ Countdown interrupted (Ctrl+C).")
        logging.info("Countdown interrupted by Ctrl+C.")
