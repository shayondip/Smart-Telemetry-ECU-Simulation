# logger/log_manager.py

from logger.csv_logger import CSVLogger
from logger.json_logger import JSONLogger


class LogManager:

    def __init__(self):
        self.csv_logger = CSVLogger()
        self.json_logger = JSONLogger()

    def save_all(self, packet: dict):
        """
        Save telemetry packet into all logging systems.
        """

        self.csv_logger.save(packet)
        self.json_logger.save(packet)

        print("\n[LOG MANAGER] All logs saved successfully.")