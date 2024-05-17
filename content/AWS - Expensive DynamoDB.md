+++
title = "Anti-pattern: AWS - Expensive DynamoDB"
weight = 8

[extra]
description = "AWS DynamoDB tables often use features that carry cost but are not required, especially for infrequently accessed tables. "
count = 25
+++

# Anti-pattern: AWS - Expensive DynamoDB
AWS DynamoDB tables often use features that carry cost but are not required,
especially for infrequently accessed tables.


## Context
DynamoDB tables might use provisioned billing mode, have high (>1) read/write capacity,
or use global secondary indices. These features carry additional cost and are not always
required, especially for infrequently accessed tables.


## Solution
Switching to pay-per-request billing mode, reducing provisioned read/write capacity,
and removing global secondary indices are ways to cost-optimize DynamoDB tables.


## Example
Set billing mode to pay-per-request:
```terraform
resource "aws_dynamodb_table" "example_table" {
  name         = "HighScores"
  billing_mode = "PAY_PER_REQUEST"

  attribute {
    name = "UserID"
    type = "S"
  }

  attribute {
    name = "Score"
    type = "N"
  }
}
```


## References
- [Resource: aws_dynamodb_table (Terraform)](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/dynamodb_table)
- [DynamoDB throughput capacity - Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html)
- [Using Global Secondary Indexes in DynamoDB - Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html)
- [Provisioned capacity mode - Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html)

## Occurrences
- [https://github.com/deptno/terraform-aws-modules/commit/49f447bdbb3cf23499e8194e78f852ea1e256d3a](https://github.com/deptno/terraform-aws-modules/commit/49f447bdbb3cf23499e8194e78f852ea1e256d3a)
- [https://github.com/ONSdigital/eq-terraform-dynamodb/commit/40eb651a50d0dfd5cf047ef62c8a6259c1c66e02](https://github.com/ONSdigital/eq-terraform-dynamodb/commit/40eb651a50d0dfd5cf047ef62c8a6259c1c66e02)
- [https://github.com/olliefr/aws-terraform-cloud1/commit/bf753832a519b0649f8d58d93aa643afe3f94fc7](https://github.com/olliefr/aws-terraform-cloud1/commit/bf753832a519b0649f8d58d93aa643afe3f94fc7)
- [https://github.com/garylb2/terraform-example-patterns/commit/6de6d83d930bd9459e1cf8c311fa7b45c3f90987](https://github.com/garylb2/terraform-example-patterns/commit/6de6d83d930bd9459e1cf8c311fa7b45c3f90987)
- [https://github.com/Arkoprabho/TerraformTutorial/commit/ba317d7e402f014589e230fad8c7384016211ba2](https://github.com/Arkoprabho/TerraformTutorial/commit/ba317d7e402f014589e230fad8c7384016211ba2)
- [https://github.com/jkstenzel95/jks.gameservers/commit/411ab992ba07e698cb08b56eb4cfc9d6e001d43f](https://github.com/jkstenzel95/jks.gameservers/commit/411ab992ba07e698cb08b56eb4cfc9d6e001d43f)
- [https://github.com/techservicesillinois/aws-enterprise-vpc/commit/0d21bea79e1936e2bdaee58bd6e328dd08e59b30](https://github.com/techservicesillinois/aws-enterprise-vpc/commit/0d21bea79e1936e2bdaee58bd6e328dd08e59b30)
- [https://github.com/austin1237/gifbot/commit/c11dabf1ea02c0e044c62448986bb3f9abdf3967](https://github.com/austin1237/gifbot/commit/c11dabf1ea02c0e044c62448986bb3f9abdf3967)
- [https://github.com/servers-tf/infrastructure/commit/cc9e50a3864511f9fb9f871293e6a6e7e2719d2c](https://github.com/servers-tf/infrastructure/commit/cc9e50a3864511f9fb9f871293e6a6e7e2719d2c)
- [https://github.com/jsoconno/aws-terraform-remote-state-infrastructure/commit/fed8be2748bc2286a6f9888d282d66763ba612ed](https://github.com/jsoconno/aws-terraform-remote-state-infrastructure/commit/fed8be2748bc2286a6f9888d282d66763ba612ed)
- [https://github.com/ONSdigital/eq-terraform/commit/6eaf697bf9f111214a6d74ee3094e5784a57d1bb](https://github.com/ONSdigital/eq-terraform/commit/6eaf697bf9f111214a6d74ee3094e5784a57d1bb)
- [https://github.com/nikkiwritescode/flask-app-terraform-deployment/commit/af47bb6201f1dcc8264e60da429e4ff8d126e56c](https://github.com/nikkiwritescode/flask-app-terraform-deployment/commit/af47bb6201f1dcc8264e60da429e4ff8d126e56c)
- [https://github.com/kperson/terraform-modules/commit/53bd2d84776f9ed7ae287fc59ed42f87bd7bbc4b](https://github.com/kperson/terraform-modules/commit/53bd2d84776f9ed7ae287fc59ed42f87bd7bbc4b)
- [https://github.com/kody-abe/terraform/commit/169c7768b0b1584945362c035a2b227d2f579466](https://github.com/kody-abe/terraform/commit/169c7768b0b1584945362c035a2b227d2f579466)
- [https://github.com/jenkins-x/terraform-aws-eks-jx/commit/cce6b14692fccd30c027851607a9526151d4c3d2](https://github.com/jenkins-x/terraform-aws-eks-jx/commit/cce6b14692fccd30c027851607a9526151d4c3d2)
- [https://github.com/telia-oss/terraform-aws-terraform-init/commit/e8c7b2eb22d08ddd1a1bb375cb6efa4165c9098f](https://github.com/telia-oss/terraform-aws-terraform-init/commit/e8c7b2eb22d08ddd1a1bb375cb6efa4165c9098f)
- [https://github.com/trajano/terraform-s3-backend/commit/f4b61c7bedae856439f01499de1ec9050b4c40fc](https://github.com/trajano/terraform-s3-backend/commit/f4b61c7bedae856439f01499de1ec9050b4c40fc)
- [https://github.com/poldi2015/chat-app/commit/cb45bf17da799afaa789206e3fcd39d9403e0567](https://github.com/poldi2015/chat-app/commit/cb45bf17da799afaa789206e3fcd39d9403e0567)
- [https://github.com/tesera/terraform-modules/commit/3cd4d7b55ac2003153fd0670151ab395ae182431](https://github.com/tesera/terraform-modules/commit/3cd4d7b55ac2003153fd0670151ab395ae182431)
- [https://github.com/MichaelDeCorte/TerraForm/commit/3799ee8b9677d02254eb6d6f50f3732df4c8374e](https://github.com/MichaelDeCorte/TerraForm/commit/3799ee8b9677d02254eb6d6f50f3732df4c8374e)
- [https://github.com/TalkingFox/SignalWs/commit/935d9d683608b4d8a97ef6ccc2c8ab7c14eec0d0](https://github.com/TalkingFox/SignalWs/commit/935d9d683608b4d8a97ef6ccc2c8ab7c14eec0d0)
- [https://github.com/codequest-eu/terraform-modules/commit/ffe23d4c2cd78035bef0dfb261701e7ed8dd588d](https://github.com/codequest-eu/terraform-modules/commit/ffe23d4c2cd78035bef0dfb261701e7ed8dd588d)
- [https://github.com/dgorbov/terraform-s3-backend-setup/commit/81f82740760a357a86b3a77f9ed400624edcb218](https://github.com/dgorbov/terraform-s3-backend-setup/commit/81f82740760a357a86b3a77f9ed400624edcb218)
- [https://github.com/sbogacz/terraform-aws-state-backend/commit/174486319f3b956807d56e5433880f9978884f93](https://github.com/sbogacz/terraform-aws-state-backend/commit/174486319f3b956807d56e5433880f9978884f93)
- [https://github.com/giuseppeborgese/terraform-locking-s3-state/commit/6b4e59e8b844417dc5c247bdef1b0adb8e2e7028](https://github.com/giuseppeborgese/terraform-locking-s3-state/commit/6b4e59e8b844417dc5c247bdef1b0adb8e2e7028)
