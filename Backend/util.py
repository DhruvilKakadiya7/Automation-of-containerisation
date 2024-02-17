import psutil
import docker
import logging

logger = logging.getLogger(__name__)


def calculate_blkio_bytes(d):
    """

    :param d:
    :return: (read_bytes, wrote_bytes), ints
    """
    bytes_stats = graceful_chain_get(d, "blkio_stats", "io_service_bytes_recursive")
    if not bytes_stats:
        return 0, 0
    r = 0
    w = 0
    for s in bytes_stats:
        if s["op"] == "Read":
            r += s["value"]
        elif s["op"] == "Write":
            w += s["value"]
    return r, w


def calculate_cpu_percent(d):
    cpu_count = len(d["cpu_stats"]["cpu_usage"]["percpu_usage"])
    cpu_percent = 0.0
    cpu_delta = float(d["cpu_stats"]["cpu_usage"]["total_usage"]) - \
                float(d["precpu_stats"]["cpu_usage"]["total_usage"])
    system_delta = float(d["cpu_stats"]["system_cpu_usage"]) - \
                   float(d["precpu_stats"]["system_cpu_usage"])
    if system_delta > 0.0:
        cpu_percent = cpu_delta / system_delta * 100.0 * cpu_count
    return cpu_percent

def calculate_network_bytes(d):
    """

    :param d:
    :return: (received_bytes, transceived_bytes), ints
    """
    networks = graceful_chain_get(d, "networks")
    if not networks:
        return 0, 0
    r = 0
    t = 0
    for if_name, data in networks.items():
        logger.debug("getting stats for interface %r", if_name)
        r += data["rx_bytes"]
        t += data["tx_bytes"]
    return r, t


def graceful_chain_get(d, *args, default=None):
    t = d
    for a in args:
        try:
            t = t[a]
        except (KeyError, ValueError, TypeError, AttributeError):
            logger.debug("can't get %r from %s", a, t)
            return default
    return t


def get_container_stats(container_id):
    client = docker.from_env()
    container = client.containers.get(container_id)
    cpu_stats = container.stats(stream=False)
    print(cpu_stats)
    r,t = calculate_network_bytes(cpu_stats)
    return {
        "name": container.name,
        "cpu_usage": calculate_cpu_percent(cpu_stats),
        "network_io_read": r//1024,
        "network_io_write": t//1024,
        "memory_usage": cpu_stats["memory_stats"]["usage"]//1024**2,
        "process_count":cpu_stats["pids_stats"]["current"]
        }

