+++
title = "Anti-pattern: Expensive monitoring"
weight = 9

[extra]
description = "Monitoring solutions are expensive and might not be needed."
count = 10
+++

# Anti-pattern: Expensive monitoring
Monitoring solutions are expensive and might not be needed.

## Context
Cloud providers offer ways to monitor deployed infrastructure and
collect metrics and logs. These solutions add cost for e.g. health checks
and log storage, and the benefits may not outweigh this cost.


## Solution
Removing monitoring or logs for noncritical infrastructure is an effective way to save cost.

## Example
Remove a Route 53 health check for a private Plex instance to save costs:
```diff
@@ -1,6 +0,0 @@
-resource "aws_route53_health_check" "example" {
-  fqdn = "plex.example.com"
-  port = 443
-  request_interval = "30"
-  failure_threshold = "5"
-}
```


## References
- [Resource: aws_route53_health_check (Terraform)](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route53_health_check)
- [CloudWatch billing and cost - Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_billing.html)
- [Amazon Route 53 pricing - Amazon Web Services](https://aws.amazon.com/route53/pricing/)
- [Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary)
- [Cost Optimization in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-cost)

## Occurrences
- [https://github.com/Eximchain/terraform-aws-quorum-cluster/commit/6a56f400f7de3f4d5cef646d92e3f848608031c1](https://github.com/Eximchain/terraform-aws-quorum-cluster/commit/6a56f400f7de3f4d5cef646d92e3f848608031c1)
- [https://github.com/Accurate0/infrastructure/commit/06889e08148d258f329118d43734f8c8dcff994e](https://github.com/Accurate0/infrastructure/commit/06889e08148d258f329118d43734f8c8dcff994e)
- [https://github.com/cloudspout/Gefjun/commit/665692a86bb65ddfa6c001f296c76c17288e2944](https://github.com/cloudspout/Gefjun/commit/665692a86bb65ddfa6c001f296c76c17288e2944)
- [https://github.com/terraform-google-modules/terraform-example-foundation/commit/8391f1bd4322fec04fda7509b537c5f66cddbbd9](https://github.com/terraform-google-modules/terraform-example-foundation/commit/8391f1bd4322fec04fda7509b537c5f66cddbbd9)
- [https://github.com/tdooner/flynn/commit/a9ea9d09727825f9a047e70d94caf73c99e6b2a8](https://github.com/tdooner/flynn/commit/a9ea9d09727825f9a047e70d94caf73c99e6b2a8)
- [https://github.com/elliotpryde/personal-infrastructure/commit/772c5ad20818738b09d01cd70ca3de80cbf66dcb](https://github.com/elliotpryde/personal-infrastructure/commit/772c5ad20818738b09d01cd70ca3de80cbf66dcb)
- [https://github.com/elliotpryde/personal-infrastructure/commit/7c4205cd130c5463d7f39aa6f281e198c143d0d9](https://github.com/elliotpryde/personal-infrastructure/commit/7c4205cd130c5463d7f39aa6f281e198c143d0d9)
- [https://github.com/alghanmi/terraform-modules/commit/570d3d8440ed399ed8b30bffe1fd7a2adc197771](https://github.com/alghanmi/terraform-modules/commit/570d3d8440ed399ed8b30bffe1fd7a2adc197771)
- [https://github.com/thoughtbot/flightdeck/commit/c784bc0a3f747b66ab7cd01f23bbbdbad3bfe705](https://github.com/thoughtbot/flightdeck/commit/c784bc0a3f747b66ab7cd01f23bbbdbad3bfe705)
- [https://github.com/chapas/tf-az-kubernetes/commit/bcc6e190b8f8a12b590089fb755c4f552f179ad0](https://github.com/chapas/tf-az-kubernetes/commit/bcc6e190b8f8a12b590089fb755c4f552f179ad0)
