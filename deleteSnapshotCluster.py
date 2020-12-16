import json
import boto3
import datetime
from datetime import timedelta

def lambda_handler(event, context):
    print("Connecting to RDS")
    client = boto3.client('rds')
    dbClusters = ['mysql-dev']
    for dbCluster in dbClusters:
        clusters = client.describe_db_clusters(
            DBClusterIdentifier = dbCluster
        )
        for cluster in clusters['DBClusters']:
            dbInstances = cluster['DBClusterMembers']
            for dbInstance in dbInstances:
                print(dbInstance['DBInstanceIdentifier'])
                #response1 = client.describe_db_instances(
                #    DBInstanceIdentifier=dbInstance    
                #)
                #print(response1)
                dbInstance = dbInstance['DBInstanceIdentifier']
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