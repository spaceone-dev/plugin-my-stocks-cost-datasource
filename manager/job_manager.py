from datetime import datetime

from spaceone.core.manager import BaseManager

from ..connector.kospi_file_connector import KospiFileConnector


class JobManager(BaseManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kospi_file_connector = KospiFileConnector()

    def get_tasks(
        self,
        options: dict,
        secret_data: dict,
        schema: str = None,
        start: str = None,
        last_synchronized_at: datetime = None,
    ) -> dict:
        self.kospi_file_connector.create_session(options, secret_data, schema)

        tasks = []
        changed = []

        for base_url in self.kospi_file_connector.base_url:
            task_options = {"base_url": base_url}

            tasks.append({"task_options": task_options})
            changed.append({"start": "1900-01"})

        return {"tasks": tasks, "changed": changed}
