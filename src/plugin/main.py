from spaceone.cost_analysis.plugin.data_source.lib.server import DataSourcePluginServer

from src.plugin.manager.cost_manager import CostManager
from src.plugin.manager.data_source_manager import DataSourceManager
from src.plugin.manager.job_manager import JobManager

app = DataSourcePluginServer()


@app.route("DataSource.init")
def data_source_init(params: dict) -> dict:
    """init plugin by options

    Args:
        params (DataSourceInitRequest): {
            'options': 'dict',    # Required
            'domain_id': 'str'
        }

    Returns:
        PluginResponse: {
            'metadata': 'dict'
        }
    """
    options = params.get("options", {})

    data_source_manager = DataSourceManager()
    return data_source_manager.init_response(options)


@app.route("DataSource.verify")
def data_source_verify(params: dict) -> None:
    """Verifying data source plugin

    Args:
        params (CollectorVerifyRequest): {
            'options': 'dict',      # Required
            'secret_data': 'dict',  # Required
            'schema': 'str',
            'domain_id': 'str'
        }

    Returns:
        None
    """
    options = params.get("options", {})
    secret_data = params.get("secret_data", {})
    schema = params.get("schema", None)

    data_source_manager = DataSourceManager()
    data_source_manager.verify_plugin(options, secret_data, schema)


@app.route("Job.get_tasks")
def job_get_tasks(params: dict) -> dict:
    """Get job tasks

    Args:
        params (JobGetTaskRequest): {
            'options': 'dict',      # Required
            'secret_data': 'dict',  # Required
            'schema': 'str',
            'start': 'str',
            'last_synchronized_at': 'datetime',
            'domain_id': 'str'
        }

    Returns:
        TasksResponse: {
            'tasks': 'list',
            'changed': 'list'
        }

    """
    options = params.get("options", {})
    secret_data = params.get("secret_data", {})

    schema = params.get("schema", None)
    start = params.get("start", None)
    last_synchronized_at = params.get("last_synchronized_at", None)

    job_manager = JobManager()
    return job_manager.get_tasks(
        options, secret_data, schema, start, last_synchronized_at
    )


@app.route("Cost.get_data")
def cost_get_data(params: dict) -> dict:
    """Get external cost data

    Args:
        params (CostGetDataRequest): {
            'options': 'dict',      # Required
            'secret_data': 'dict',  # Required
            'schema': 'str',
            'task_options': 'dict',
            'domain_id': 'str'
        }

    Returns:
        Generator[ResourceResponse, None, None]
        {
            'cost': 'float',
            'usage_quantity': 'float',
            'usage_unit': 'str',
            'provider': 'str',
            'region_code': 'str',
            'product': 'str',
            'usage_type': 'str',
            'resource': 'str',
            'tags': 'dict'
            'additional_info': 'dict'
            'data': 'dict'
            'billed_date': 'str'
        }
    """
    options = params.get("options", {})
    secret_data = params.get("secret_data", {})

    schema = params.get("schema", None)
    task_options = params.get("task_options", {})

    cost_manager = CostManager()
    return cost_manager.get_data(options, secret_data, schema, task_options)
