from spaceone.core.manager import BaseManager

from ..connector.kospi_file_connector import KospiFileConnector


class DataSourceManager(BaseManager):
    @staticmethod
    def init_response(options: dict) -> dict:
        return {"metadata": {}}

    @staticmethod
    def verify_plugin(options: dict, secret_data: dict, schema: str = None) -> None:
        kospi_file_connector = KospiFileConnector()
        kospi_file_connector.create_session(options, secret_data, schema)
