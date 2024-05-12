"""
Example program to demonstrate how to read markers from LSL.
Usage:
    python lsl_receiver.py --timeout 15

The 'timeout' argument specifies how long to wait for a marker before exiting.
"""

from pylsl import StreamInlet, resolve_stream
import sys


def main(argv):

    # read the argument which specifies the timeout
    if argv:
        if argv[0] == '--timeout':
            timeout = int(argv[1])
        else:
            timeout = 10

    # first resolve a marker stream on the lab network
    print("Looking for a marker stream...")
    streams = resolve_stream('type', 'Markers')

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])

    try:
        while True:
            # get a new sample 
            sample, timestamp = inlet.pull_sample(timeout=timeout)
            print(f"Received marker {sample[0]} at time {timestamp}")
    except (KeyboardInterrupt, Exception) as e:
        print(f"Error: {e}, exiting...")
    
    print("Exiting...")

if __name__ == '__main__':
    main(sys.argv[1:])