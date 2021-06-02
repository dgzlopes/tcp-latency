#!/usr/bin/python
import argparse
import socket
from statistics import mean
from time import sleep
from time import time
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
        default=1,
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
    latency_points = []
    packet_statistics = {'transmitted': 0, 'received': 0, 'success_percentage': 0, 'loss_percentage': 0, 'total_time': 0}

    for i in range(runs):
        sleep(wait)
        last_latency_point = latency_point(
            host=host, port=port, timeout=timeout,
        )

        packet_statistics =calculate_packets_statistics(last_latency_point, packet_statistics, timeout)

        if human_output:
            if i == 0:
                print('tcp-latency {}'.format(host))
            _human_output(
                host=host, port=port, timeout=timeout,
                latency_point=last_latency_point, seq_number=i,
            )
            if i == len(range(runs))-1:
                print(f'--- {host} tcp-latency statistics ---')
                print(f'{i+1} packets transmitted')
                show_packet_statistics(packet_statistics)
                if latency_points:
                    print(
                        f'rtt min/avg/max = {min(latency_points)}/{mean(latency_points)}/{max(latency_points)} ms',   # noqa: E501
                    )

        latency_points.append(last_latency_point)

    return latency_points


def calculate_packets_statistics(last_calculated_value: float, packet_statistics: dict, timeout: float) -> dict:
    '''
    :rtype: Returns the statistics dictionary
    Calculate the packet statisctics
    '''
    if not packet_statistics:
        packet_statistics = {'transmitted': 0, 'received': 0, 'success_percentage': 0, 'loss_percentage': 0, 'total_time': 0}

    packet_statistics['transmitted'] += 1
    if last_calculated_value:
        packet_statistics['received'] += 1
        packet_statistics['total_time'] += last_calculated_value
    else:
        packet_statistics['total_time'] += timeout
    packet_statistics['success_percentage'] = packet_statistics['received'] * 100 / packet_statistics['transmitted']
    packet_statistics['loss_percentage'] = 100 - packet_statistics['success_percentage']

    return packet_statistics

def show_packet_statistics(packet_statistics: dict):
    '''
    Prints the packets statistics
    '''
    if packet_statistics:
        print (f' {packet_statistics["transmitted"]} packets transmitted, {packet_statistics["received"]} packets received, {packet_statistics["loss_percentage"]}% packet loss, time {packet_statistics["total_time"]}ms ')

def latency_point(host: str, port: int = 443, timeout: float = 5) -> Optional[float]:
    '''
    :rtype: Returns float if possible
    Calculate a latency point using sockets. If something bad happens the point returned is None
    '''
    # New Socket and Time out
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)

    # Start a timer
    s_start = time()

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
    s_runtime = (time() - s_start) * 1000

    return float(s_runtime)


def _human_output(host: str, port: int, timeout: int, latency_point: float, seq_number: int):
    '''fstring based output for the console_script'''
    # In case latency_point is None
    if latency_point:
        print(
            f'{host}: tcp seq={seq_number} port={port} timeout={timeout} time={latency_point} ms',
        )
    else:
        print(f'{host}: tcp seq={seq_number} port={port} timeout={timeout} failed')


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
