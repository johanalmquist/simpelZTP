import redis
import rq
import time

def trigger_job(host):
    redis_conn = redis.from_url('redis://')
    q = rq.Queue('ztp_tasks', connection=redis_conn)
    job_id = '{}'.format(host)
    try:
        rq_job = rq.job.Job.fetch(job_id, connection=redis_conn)
        if rq_job._status in ['finished', 'failed', 'ok', 'OK']:
            rq_job.delete()
    except (redis.exceptions.RedisError, rq.exceptions.NoSuchJobError):
        q.enqueue('app.ztp.start', host, job_id=job_id)