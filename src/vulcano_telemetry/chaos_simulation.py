import time
import random
import logging

logger = logging.getLogger('ChaosEngine')

class ChaosSimulator:
    @staticmethod
    def simulate_network_latency(min_sec=0.1, max_sec=0.5):
        time.sleep(random.uniform(min_sec, max_sec))

    @staticmethod
    def should_inject_poison_pill() -> bool:
        return random.choice([True, False])
