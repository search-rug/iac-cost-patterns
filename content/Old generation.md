+++
title = "Anti-pattern: Old generation"
weight = 4

[extra]
description = "Using newer resource generations gives similar performance for lower cost."
count = 34
+++

# Anti-pattern: Old generation
Using newer resource generations gives similar performance for lower cost.

## Context
Cloud providers occasionally update their offerings to support, for example,
newer CPU generations. These newer generations are often more efficient, making
them a more economical option compared to older generations.


## Solution
Upgrade resources to newer generations to attain comparable or better performance
for a lower price. The most commonly replaced resources include, but are not limited
to, AWS's t2 general-purpose compute instances and gp2 storage volumes.


## Example
Switch from gp2 to gp3 storage, providing comparable performance but lower cost:
```diff
@@ -1,7 +1,7 @@
 resource "aws_instance" "example" {
   # ...
   root_block_device {
-    volume_type = "gp2"
+    volume_type = "gp3"
     # ...
   }
 }
```


## References
- [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)
- [Migrate your Amazon EBS volumes from gp2 to gp3 and save up to 20% on costs](https://aws.amazon.com/blogs/storage/migrate-your-amazon-ebs-volumes-from-gp2-to-gp3-and-save-up-to-20-on-costs/)
- [Compute - EC2 Instance Types - AWS](https://aws.amazon.com/ec2/instance-types/)
- [Amazon EC2 T2 Instances - Amazon Web Services (AWS)](https://aws.amazon.com/ec2/instance-types/t2/)
- [Amazon EC2 T3 Instances - Amazon Web Services (AWS)](https://aws.amazon.com/ec2/instance-types/t3/)

## Occurrences
- [https://github.com/gudlyf/TerraformOpenVPN/commit/be1245d8634025277ba79a4155ee88d7eaffcdfb](https://github.com/gudlyf/TerraformOpenVPN/commit/be1245d8634025277ba79a4155ee88d7eaffcdfb)
- [https://github.com/alphagov/govuk-aws/commit/6cfda6ada5137b232ff442ae9f2aedc8520ee1b4](https://github.com/alphagov/govuk-aws/commit/6cfda6ada5137b232ff442ae9f2aedc8520ee1b4)
- [https://github.com/alphagov/govuk-aws/commit/aeb3bfbe393cdfc02e62b812843ed75cf5f245e4](https://github.com/alphagov/govuk-aws/commit/aeb3bfbe393cdfc02e62b812843ed75cf5f245e4)
- [https://github.com/alphagov/govuk-aws/commit/5fa5da9756f12559b490217dd5b173db48e7f2a9](https://github.com/alphagov/govuk-aws/commit/5fa5da9756f12559b490217dd5b173db48e7f2a9)
- [https://github.com/alphagov/govuk-aws/commit/19d187e4a29147cbcf1cfae456cfcbfa8ad52b45](https://github.com/alphagov/govuk-aws/commit/19d187e4a29147cbcf1cfae456cfcbfa8ad52b45)
- [https://github.com/alphagov/govuk-aws/commit/806b1a2a47f2f4e580e524b2cf8cc5928749d972](https://github.com/alphagov/govuk-aws/commit/806b1a2a47f2f4e580e524b2cf8cc5928749d972)
- [https://github.com/alphagov/govuk-aws/commit/8d7d2ebe0dbe9ebf8009572d1d710c4700cf245e](https://github.com/alphagov/govuk-aws/commit/8d7d2ebe0dbe9ebf8009572d1d710c4700cf245e)
- [https://github.com/greenbrian/musical-spork/commit/24c07bfd5c31438fff6374e9ba3d577e6402d777](https://github.com/greenbrian/musical-spork/commit/24c07bfd5c31438fff6374e9ba3d577e6402d777)
- [https://github.com/dotancohen81/Rancher/commit/90944271b4e8bd46e3d42ac64bc4964a33a8fdc3](https://github.com/dotancohen81/Rancher/commit/90944271b4e8bd46e3d42ac64bc4964a33a8fdc3)
- [https://github.com/cisagov/cyhy_amis/commit/7b8d9247a679295e0e1791b13d6c437c473e44b8](https://github.com/cisagov/cyhy_amis/commit/7b8d9247a679295e0e1791b13d6c437c473e44b8)
- [https://github.com/yardbirdsax/elasticsearch-the-hard-way/commit/521bae59a4002a616eac44c1681ca5066bbd00c8](https://github.com/yardbirdsax/elasticsearch-the-hard-way/commit/521bae59a4002a616eac44c1681ca5066bbd00c8)
- [https://github.com/GBergeret/tf-vpc-module/commit/34d80ece7d0ef598414baffceb074c6580dd819b](https://github.com/GBergeret/tf-vpc-module/commit/34d80ece7d0ef598414baffceb074c6580dd819b)
- [https://github.com/cisagov/vulnerable-instances/commit/f70410061b8c6b9249895571e05dfb7a142efb18](https://github.com/cisagov/vulnerable-instances/commit/f70410061b8c6b9249895571e05dfb7a142efb18)
- [https://github.com/dwp/dataworks-aws-data-egress/commit/14f065e5161fee14c286c34df7db9f5516ef9bb6](https://github.com/dwp/dataworks-aws-data-egress/commit/14f065e5161fee14c286c34df7db9f5516ef9bb6)
- [https://github.com/circleci/enterprise-setup/commit/26cc5295c2bb9d8756e450712e0f5f75af440c4a](https://github.com/circleci/enterprise-setup/commit/26cc5295c2bb9d8756e450712e0f5f75af440c4a)
- [https://github.com/bh1m2rn/gitlab-environment-toolkit/commit/b9750f0bb88bc22256085b6bc8f060055e90a8c4](https://github.com/bh1m2rn/gitlab-environment-toolkit/commit/b9750f0bb88bc22256085b6bc8f060055e90a8c4)
- [https://github.com/travis-ci/terraform-config/commit/4f641b162fa877aef842481631906d5bfe874781](https://github.com/travis-ci/terraform-config/commit/4f641b162fa877aef842481631906d5bfe874781)
- [https://github.com/byu-oit/terraform-aws-rds/commit/86a0795540edb426c3226775d73fcd4ce807d36a](https://github.com/byu-oit/terraform-aws-rds/commit/86a0795540edb426c3226775d73fcd4ce807d36a)
- [https://github.com/poseidon/terraform-azure-kubernetes/commit/633eb938742a43be09612b944c29aaaf70dac119](https://github.com/poseidon/terraform-azure-kubernetes/commit/633eb938742a43be09612b944c29aaaf70dac119)
- [https://github.com/poseidon/terraform-aws-kubernetes/commit/e09126b45746f1c967d1990fa04ce781a0478c6d](https://github.com/poseidon/terraform-aws-kubernetes/commit/e09126b45746f1c967d1990fa04ce781a0478c6d)
- [https://github.com/deadlysyn/terraform-keycloak-aws/commit/1c982ac4120ae3ed5a88c38f2a4d568ad9a83d22](https://github.com/deadlysyn/terraform-keycloak-aws/commit/1c982ac4120ae3ed5a88c38f2a4d568ad9a83d22)
- [https://github.com/ONSdigital/eq-terraform/commit/79845fe095cd87287346f40d2adce9b28a32ef35](https://github.com/ONSdigital/eq-terraform/commit/79845fe095cd87287346f40d2adce9b28a32ef35)
- [https://github.com/kinvolk-archives/lokomotive-kubernetes/commit/f2f4deb8bb44988eeb0b64b919e51fb556aef4fb](https://github.com/kinvolk-archives/lokomotive-kubernetes/commit/f2f4deb8bb44988eeb0b64b919e51fb556aef4fb)
- [https://github.com/smarman85/a_new_hope/commit/de97a6b8033c866c3b711468207aa4890049daaa](https://github.com/smarman85/a_new_hope/commit/de97a6b8033c866c3b711468207aa4890049daaa)
- [https://github.com/kmishra9/PL2-AWS-Setup/commit/0d7b5b0f6f92ff6cfde1f17ad96d1b1459a0957a](https://github.com/kmishra9/PL2-AWS-Setup/commit/0d7b5b0f6f92ff6cfde1f17ad96d1b1459a0957a)
- [https://github.com/cisagov/cool-sharedservices-nessus/commit/5403a8978053a1299b0afe8d7fc59e914fc5e354](https://github.com/cisagov/cool-sharedservices-nessus/commit/5403a8978053a1299b0afe8d7fc59e914fc5e354)
- [https://github.com/guillaumekh/wg-terraform-template/commit/effee9cbc473af5d07cfc3aacece50aa6e59753a](https://github.com/guillaumekh/wg-terraform-template/commit/effee9cbc473af5d07cfc3aacece50aa6e59753a)
- [https://github.com/ninthnails/terraform-aws-camellia/commit/0019704e14723aaf326840ab36c594c3f514a2d4](https://github.com/ninthnails/terraform-aws-camellia/commit/0019704e14723aaf326840ab36c594c3f514a2d4)
- [https://github.com/openaustralia/infrastructure/commit/63ee190c0ae1832bb72681e1e4b1b14a9367b4bb](https://github.com/openaustralia/infrastructure/commit/63ee190c0ae1832bb72681e1e4b1b14a9367b4bb)
- [https://github.com/robertdebock/terraform-aws-vault/commit/e3b6520960a88aacbf03339dc1368f680a8bee9a](https://github.com/robertdebock/terraform-aws-vault/commit/e3b6520960a88aacbf03339dc1368f680a8bee9a)
- [https://github.com/cisagov/cool-assessment-terraform/commit/3138943ab4d15cc256d322e1128862ef11383c73](https://github.com/cisagov/cool-assessment-terraform/commit/3138943ab4d15cc256d322e1128862ef11383c73)
- [https://github.com/pelias/terraform-elasticsearch/commit/21c1827f4507eae217d43d99ad8cb1bbb1337e21](https://github.com/pelias/terraform-elasticsearch/commit/21c1827f4507eae217d43d99ad8cb1bbb1337e21)
- [https://github.com/lowflying/OVPN---TF/commit/be1245d8634025277ba79a4155ee88d7eaffcdfb](https://github.com/lowflying/OVPN---TF/commit/be1245d8634025277ba79a4155ee88d7eaffcdfb)
- [https://github.com/figurate/bedrock/commit/bffc023eeff075ef281b1fd261897f4c7216b354](https://github.com/figurate/bedrock/commit/bffc023eeff075ef281b1fd261897f4c7216b354)
