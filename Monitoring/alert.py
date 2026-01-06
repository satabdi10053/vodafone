def notify_failure(context):
    dag_id = context['dag'].dag_id
    task_id = context['task_instance'].task_id
    log_url = context['task_instance'].log_url
    error = context['exception']
