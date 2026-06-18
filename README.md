# Cloud-Based Disaster Recovery Automation using AWS

## Overview

This project implements an automated Disaster Recovery (DR) solution using AWS services.

The system continuously monitors an Amazon RDS database using CloudWatch. When predefined thresholds are exceeded, CloudWatch triggers an AWS Lambda function to initiate disaster recovery actions. Cross-region snapshots are maintained in Singapore for backup and restoration.

## AWS Services Used

* Amazon RDS (MySQL)
* Amazon CloudWatch
* CloudWatch Alarm
* AWS Lambda
* IAM
* RDS Snapshots
* Cross-Region Snapshot Copy

## Workflow

1. Primary database hosted in Mumbai Region.
2. Manual snapshot created.
3. Snapshot copied to Singapore Region.
4. CloudWatch monitors CPU utilization.
5. Alarm triggers when threshold exceeds 10%.
6. Lambda function initiates disaster recovery workflow.

## Recovery Time Objective (RTO)

| Activity          | Time   |
| ----------------- | ------ |
| Failure Detection | 2 min  |
| Alarm Trigger     | 1 min  |
| Lambda Execution  | 1 min  |
| Snapshot Restore  | 8 min  |
| Validation        | 3 min  |
| Total RTO         | 15 min |

## Author

Aditya Bharate

TE Computer Engineering

Savitribai Phule Pune University    
