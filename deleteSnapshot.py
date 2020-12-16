import json
import boto3
from datetime import timedelta
import datetime

def lambda_handler(event, context):
    print("Connecting to RDS")
    client = boto3.client('rds')
    dbInstances = ['mysql-dev']
    for dbInstance in dbInstances:
        print(dbInstance)
        #response1 = client.describe_db_instances(
        #    DBInstanceIdentifier=dbInstance    
        #)
        #print(response1)
        print("RDS stale snapshot deletion started at %s...\n" % datetime.datetime.now())
        response = client.describe_db_snapshots(
            DBInstanceIdentifier=dbInstance
            #DBSnapshotIdentifier = 'mysql-dev'
        )
        print(response)
        for i in response['DBSnapshots']:
            print(i)
            delta = datetime.date.today()-i['SnapshotCreateTime']
            print("Time Delta:")
            print(delta)
            if delta >= (365*2):
                t = i['DBSnapshotIdentifier']
                client.delete_db_snapshot(
                    DBSnapshotIdentifier=t
                )