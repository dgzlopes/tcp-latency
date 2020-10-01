from tcp_latency import latency_point, measure_latency, generate_statistics


def test_latencyPoint_unreachable_host():
    non_existent_latency = latency_point(host='nonexistenthost')
    assert not non_existent_latency


def test_latencyPoint_return_is_float():
    latency_run = latency_point(host='google.com')
    assert isinstance(latency_run, float)


def test_tcpLatency_negative_runs():
    negative_runs = measure_latency(host='google.com', runs=-1)
    assert not negative_runs


def test_tcpLatency_multiple_runs():
    number_of_iterations = 10
    multiple_runs = measure_latency(
        host='google.com', runs=number_of_iterations,
    )
    assert len(multiple_runs) is number_of_iterations


def test_tcpLatency_valid_list_return():
    latency_run = measure_latency(host='google.com')
    assert isinstance(latency_run, list)

    for element in latency_run:
        assert isinstance(element, float) or None


def test_generate_statistics():
    latency_points = [1.0, None, 1.0, 1.0, None]

    statistics_string = generate_statistics(latency_points)

    assert statistics_string == '5 packets transmitted, 3 packets received, 40.0% packet loss'


def test_generate_statistics_with_100_loss():
    latency_points = [None, None, None, None, None]

    statistics_string = generate_statistics(latency_points)

    assert statistics_string == '5 packets transmitted, 0 packets received, 100.0% packet loss'


def test_generate_statistics_with_0_loss():
    latency_points = [1.0, 2.0, 3.0, 4.0, 5.0]

    statistics_string = generate_statistics(latency_points)

    assert statistics_string == '5 packets transmitted, 5 packets received, 0.0% packet loss'

