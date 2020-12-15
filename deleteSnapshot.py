import boto3
from datetime import datetime, timedelta
def lambda_handler(event, context):
    print("Connecting to RDS")
    client = boto3.client('rds')
    dbInstances = ['mysql-dev']
    for dbInstance in dbInstances:
        print("RDS stale snapshot deletion started at %s...\n" % datetime.datetime.now())
        response = client.describe_db_snapshots(
            DBInstanceIdentifier=dbInstance
        )
        for i in response('DBSnapshots'):
            delta = datetime.now()-i('SnapshotCreateTime')
            if delta >= (365*2):
                t = i('DBSnapshotIdentifier')
                delete_db_snapshot(
                    DBSnapshotIdentifier=t
                )