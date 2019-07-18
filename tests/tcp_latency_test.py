from tcp_latency import latency_point
from tcp_latency import meassure_latency


def test_latencyPoint_unreachable_host():
    non_existent_latency = latency_point(host='nonexistenthost')
    assert not non_existent_latency


def test_latencyPoint_return_is_float():
    latency_run = latency_point(host='google.com')
    assert isinstance(latency_run, float)


def test_tcpLatency_negative_runs():
    negative_runs = meassure_latency(host='google.com', runs=-1)
    assert not negative_runs


def test_tcpLatency_multiple_runs():
    number_of_iterations = 10
    multiple_runs = meassure_latency(
        host='google.com', runs=number_of_iterations,
    )
    assert len(multiple_runs) is number_of_iterations


def test_tcpLatency_valid_list_return():
    latency_run = meassure_latency(host='google.com')
    assert isinstance(latency_run, list)

    for element in latency_run:
        assert isinstance(element, float) or None
