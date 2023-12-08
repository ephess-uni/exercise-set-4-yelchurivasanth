""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    # Get the shutdown events from the logfile
    shutdown_events = get_shutdown_events(logfile)

    # Get the datetime objects for the first and last shutdown events
    first_shutdown = logstamp_to_datetime(shutdown_events[0].split()[1])
    last_shutdown = logstamp_to_datetime(shutdown_events[-1].split()[1])

    # Compute the difference in time between the two events and return as timedelta object
    return abs(last_shutdown - first_shutdown)


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')

