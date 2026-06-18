import boto3

rds = boto3.client('rds')

def lambda_handler(event, context):

    try:

        response = rds.restore_db_instance_from_db_snapshot(
            DBInstanceIdentifier='recovery-db',
            DBSnapshotIdentifier='primary-backup'
        )

        return {
            'statusCode': 200,
            'message': 'Disaster Recovery Started'
        }

    except Exception as e:

        return {
            'statusCode': 500,
            'message': str(e)
        }