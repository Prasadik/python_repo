data={
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "cloudtrail:GetTrail",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:GetServiceLastAccessedDetails",
                "iam:GenerateServiceLastAccessedDetails"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket",
                "arn:aws:s3:::amzn-s3-demo-bucket/*"
            ],
            "Condition":{
  "Bool": {
      "aws:SecureTransport": "true"
   }
}
        }
    ]
}
print(data["Version"])
print(data["Statement"][0]["Effect"])
print(data["Statement"][2]["Action"][1])
print(data["Statement"][2]["Resource"][1])
print(data["Statement"][2]["Condition"]["Bool"]["aws:SecureTransport"])
data2={
    "region": "us-east-2",
    "accountId": "111222333444",
    "eventTriggerName": "trigger-group-us-east-instance-succeeded",
    "deploymentId": "d-75I7MBT7C",
    "instanceId": "arn:aws:ec2:us-east-2:444455556666:instance/i-496589f7",
    "lastUpdatedAt": "1446744207.564",
    "instanceStatus": "Succeeded",
    "lifecycleEvents": [
        {
            "LifecycleEvent": "ApplicationStop",
            "LifecycleEventStatus": "Succeeded",
            "StartTime": "1446744188.595",
            "EndTime": "1446744188.711"
        },
        {
            "LifecycleEvent": "BeforeInstall",
            "LifecycleEventStatus": "Succeeded",
            "StartTime": "1446744189.827",
            "EndTime": "1446744190.402"
        }
#More lifecycle events might be listed here
    ]
}
print(data2["region"])
print(data2["instanceStatus"])
print(data2["instanceId"])
print(data2["lifecycleEvents"][0]["EndTime"])
print(data2["lifecycleEvents"][0]["StartTime"])
print(data2["lifecycleEvents"][1]["LifecycleEvent"])
print(data2["lifecycleEvents"][1]["LifecycleEventStatus"])
