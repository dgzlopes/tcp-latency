#!/usr/bin/python
import argparse
import socket
import time
from timeit import default_timer as timer

from typing import Optional


def _parse_arguments():
    '''Argument parsing for the console_script'''
    parser = argparse.ArgumentParser(
        description='Measure latency using TCP.',
    )
    parser.add_argument(
        'host',
        metavar='host',
    )
    parser.add_argument(
        '-p',
        '--port',
        metavar='p',
        nargs='?',
        default=443,
        type=int,
        help='(default: %(default)s)',
    )
    parser.add_argument(
        '-t',
        '--timeout',
        metavar='t',
        nargs='?',
        default=5,
        type=float,
        help='(seconds, %(type)s, default: %(default)s)',
    )
    parser.add_argument(
        '-r',
        '--runs',
        metavar='r',
        nargs='?',
        default=5,
        type=int,
        help='number of latency points (%(type)s, default: %(default)s)',
    )
    parser.add_argument(
        '-w',
        '--wait',
        metavar='w',
        nargs='?',
        default=0,
        type=float,
        help='between each run (seconds, %(type)s, default: %(default)s)',
    )

    return parser.parse_args()


def measure_latency(
    host: str,
    port: int = 443,
    timeout: float = 5,
    runs: int = 1,
    wait:
    float = 1,
    human_output: bool = False,
) -> list:
    '''
    :rtype: list
    Builds a list composed of latency_points
    '''
    list_of_latency_points = []

    for i in range(runs):
        time.sleep(wait)
        last_latency_point = latency_point(
            host=host, port=port, timeout=timeout,
        )
        if human_output:
            if i == 0:
                print('tcp-latency {}'.format(host))
            _human_output(
                host=host, port=port, timeout=timeout,
                latency_point=last_latency_point, seq_number=i,
            )
            if i == len(range(runs))-1:
                print('--- {} tcp-latency statistics ---'.format(host))
                print('{} packets transmitted'.format(i+1))

        list_of_latency_points.append(last_latency_point)

    return list_of_latency_points


def latency_point(host: str, port: int = 443, timeout: float = 5) -> Optional[float]:
    '''
    :rtype: Returns float if possible
    Calculate a latency point using sockets. If something bad happens the point returned is None
    '''
    # New Socket and Time out
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)

    # Start a timer
    s_start = timer()

    # Try to Connect
    try:
        s.connect((host, int(port)))
        s.shutdown(socket.SHUT_RD)

    # If something bad happens, the latency_point is None
    except socket.timeout:
        pass
        return None
    except OSError:
        pass
        return None

    # Stop Timer
    s_stop = timer()
    s_runtime = '%.2f' % (1000 * (s_stop - s_start))

    return float(s_runtime)


def _human_output(host: str, port: int, timeout: int, latency_point: float, seq_number: int):
    '''fstring based output for the console_script'''
    # In case latency_point is None
    if latency_point:
        print('{}: tcp seq={} port={} timeout={} time={} ms'.format(
            host, seq_number, port, timeout, latency_point,
        ))
    else:
        print('{}: tcp seq={} port={} timeout={} failed'.format(
            host, seq_number, port, timeout,
        ))


def _main():
    args = _parse_arguments()
    measure_latency(
        host=args.host,
        port=args.port,
        timeout=args.timeout,
        runs=args.runs,
        human_output=True,
        wait=args.wait,
    )


if __name__ == '__main__':
    _main()
