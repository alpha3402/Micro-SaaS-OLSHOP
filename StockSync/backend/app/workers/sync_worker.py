"""Celery background tasks for periodic & on-demand sync."""

from celery import Celery
from app.config import settings

celery_app = Celery(
    "stocksync",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Jakarta",
    enable_utc=True,
)


@celery_app.task(name="sync_single_product")
def sync_single_product(product_id: str):
    """Background task: sync a single product to all platforms."""
    # TODO: Implement async sync in celery task
    return {"product_id": product_id, "status": "queued"}


@celery_app.task(name="sync_all_products_for_user")
def sync_all_products_for_user(user_id: str):
    """Background task: sync all products for a user."""
    return {"user_id": user_id, "status": "queued"}


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """Schedule periodic sync tasks."""
    # Sync all products every 15 minutes
    sender.add_periodic_task(900.0, sync_all_products_for_user.s(), name="sync-every-15-min")