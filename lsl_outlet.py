"""
Example program to demonstrate how to send markers into LSL.
Usage:
    python lsl_outlet.py --n 30
"""

import random
import time
from pylsl import StreamInfo, StreamOutlet
import sys

def main(argv):

    # read the argument which specifies the number of markers
    if argv:
        if argv[0] == '--n':
            num_markers = int(argv[1])
        else:
            num_markers = 30

    # first create a new stream settings 
    info = StreamInfo(name="marker_stream", 
                      type="Markers", 
                      channel_count=1, 
                      channel_format='int32', 
                      source_id='example_stream_999')

    # next make an outlet
    outlet = StreamOutlet(info)

    print("Sending markers...")
    markernames = list(range(1, 11))
    n = 0

    while True:
        n += 1
        # pick a random marker to send and push to LSL
        marker = random.choice(markernames)
        outlet.push_sample([marker])
        print(f"{n}. Sent marker {marker}")
        time.sleep(1)
        if n >= num_markers:
            break

if __name__ == "__main__":
    main(sys.argv[1:])