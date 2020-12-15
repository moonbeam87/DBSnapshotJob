import boto3
import datetime
def lambda_handler(event, context):
    print("Connecting to RDS")
    client = boto3.client('rds')
    dbInstances = ['mysql-dev']
    for dbInstance in dbInstances:
        print("RDS snapshot backups started at %s...\n" % datetime.datetime.now())
        client.create_db_cluster_snapshot(
            DBClusterIdentifier=dbInstance,
            DBClusterSnapshotIdentifier=dbInstance+'{}'.format(datetime.datetime.now().strftime("%y-%m-%d-%H"))
        )