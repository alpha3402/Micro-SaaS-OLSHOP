#!/bin/bash
# StockSync Database Backup Script
# Backup PostgreSQL setiap jam 2 pagi ke Cloudflare R2

BACKUP_DIR=/home/ubuntu/stocksync/backups
mkdir -p $BACKUP_DIR

FILENAME=stocksync_$(date +%Y%m%d_%H%M%S).sql.gz

pg_dump stocksync | gzip > $BACKUP_DIR/$FILENAME

# Upload ke R2 (butuh aws cli dengan profile r2)
aws s3 cp $BACKUP_DIR/$FILENAME \
  s3://stocksync-backups/$FILENAME \
  --endpoint-url https://28d40a5150514cfc98ff5d472345772f.r2.cloudflarestorage.com \
  --profile r2

# Hapus backup >7 hari
find $BACKUP_DIR -name "*.sql.gz" -mtime +7 -delete

echo "$(date): Backup $FILENAME selesai"