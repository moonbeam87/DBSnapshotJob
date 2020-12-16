import json
import boto3

import datetime
from datetime import timedelta

def lambda_handler(event, context):
    print("Connecting to RDS")
    client = boto3.client('rds')
    response = client.describe_db_cluster_snapshots()
    for i in response['DBClusterSnapshots']:
        print(i)
        delta = datetime.datetime.today()-datetime.timedelta(days=730)
        print("Time Delta:")
        print(delta)
        delta = delta.replace(tzinfo=None)
        snaptime = i['SnapshotCreateTime'].replace(tzinfo=None)
        if snaptime < delta:
            t = i['DBSnapshotIdentifier']
            client.delete_db_snapshot(
                DBSnapshotIdentifier=t
            )