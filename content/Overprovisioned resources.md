+++
title = "Anti-pattern: Overprovisioned resources"
weight = 7

[extra]
description = "Resources like RAM, storage and CPU utilization are often overprovisioned even when lower values are acceptable."
count = 17
+++

# Anti-pattern: Overprovisioned resources
Resources like RAM, storage and CPU utilization are often overprovisioned even when lower values are acceptable.

## Context
In a similar way to overprovisioned instances, it is difficult to estimate
required limits for resources such as root storage upfront, leading developers
to overprovision them, in turn raising costs.


## Solution
Evaluate the resource requirements and lower the relevant values.

## Example
Shrink the root storage size of an instance to reduce storage costs:
```diff
@@ -2,6 +2,6 @@ resource "aws_instance" "example" {
   # ...
   
   root_block_device {
-    volume_size = 20 # GB
+    volume_size = 15 # GB
   }
 }
```


## References


## Occurrences
- [https://github.com/thomastodon/jabujabu/commit/02210a3d3ba4a770c29623825b7f54f3ff33f3c7](https://github.com/thomastodon/jabujabu/commit/02210a3d3ba4a770c29623825b7f54f3ff33f3c7)
- [https://github.com/guilhermerenew/infra-cost/commit/ba858d94e29d03e3e81533df8cd8bc85b9f176f1](https://github.com/guilhermerenew/infra-cost/commit/ba858d94e29d03e3e81533df8cd8bc85b9f176f1)
- [https://github.com/chaspy/terraform-alibaba-isucon8/commit/53588dad5dd4c13903a6c582f74e1afe2671d33e](https://github.com/chaspy/terraform-alibaba-isucon8/commit/53588dad5dd4c13903a6c582f74e1afe2671d33e)
- [https://github.com/dwp/dataworks-aws-data-egress/commit/14f065e5161fee14c286c34df7db9f5516ef9bb6](https://github.com/dwp/dataworks-aws-data-egress/commit/14f065e5161fee14c286c34df7db9f5516ef9bb6)
- [https://github.com/akaron/kubeadm_aws/commit/2e2092ec94b27a4c3f0b9f4ee4d46a1983a72518](https://github.com/akaron/kubeadm_aws/commit/2e2092ec94b27a4c3f0b9f4ee4d46a1983a72518)
- [https://github.com/robertdebock/terraform-azurerm-container-group/commit/c0d6578f1ebbdcc9cab091017259e4d596bfe8c9](https://github.com/robertdebock/terraform-azurerm-container-group/commit/c0d6578f1ebbdcc9cab091017259e4d596bfe8c9)
- [https://github.com/fdns/terraform-k8s/commit/f106917bb7b2d8d4428022bb119585bf9f35769c](https://github.com/fdns/terraform-k8s/commit/f106917bb7b2d8d4428022bb119585bf9f35769c)
- [https://github.com/jackofallops/terraform-aws-mysql-cluster/commit/7b2a446b0915a3ad26093f8234f7493ff152138a](https://github.com/jackofallops/terraform-aws-mysql-cluster/commit/7b2a446b0915a3ad26093f8234f7493ff152138a)
- [https://github.com/alphagov/govwifi-terraform/commit/38d0a67cf70d46c26675ce60a7a647eef0f11e52](https://github.com/alphagov/govwifi-terraform/commit/38d0a67cf70d46c26675ce60a7a647eef0f11e52)
- [https://github.com/pangeo-data/terraform-deploy/commit/f8163bd52bea3774e2f160cff0523c602e65d933](https://github.com/pangeo-data/terraform-deploy/commit/f8163bd52bea3774e2f160cff0523c602e65d933)
- [https://github.com/eduardobaitello/terraform-eks/commit/c11fca6440a5000648f690e6282778fb4ec73309](https://github.com/eduardobaitello/terraform-eks/commit/c11fca6440a5000648f690e6282778fb4ec73309)
- [https://github.com/jshcmpbll/Cloud-Mac-KVM/commit/361885d22c0304cb44683f9b005f82ca5e269841](https://github.com/jshcmpbll/Cloud-Mac-KVM/commit/361885d22c0304cb44683f9b005f82ca5e269841)
- [https://github.com/kaz/kiritan.com/commit/1cd96c7f71e56629ffa07c38e12c4da19fcfc5f7](https://github.com/kaz/kiritan.com/commit/1cd96c7f71e56629ffa07c38e12c4da19fcfc5f7)
- [https://github.com/dylanmtaylor/dylanmtaylor-terraform-aws/commit/44016d6a8e496b69308a81e88af8c9ef8b710ab3](https://github.com/dylanmtaylor/dylanmtaylor-terraform-aws/commit/44016d6a8e496b69308a81e88af8c9ef8b710ab3)
- [https://github.com/roysjosh/terraform-unifi/commit/da9e2869456610a0228cb14f850c6eccddbb15e0](https://github.com/roysjosh/terraform-unifi/commit/da9e2869456610a0228cb14f850c6eccddbb15e0)
- [https://github.com/phillhocking/aws-ubuntu-irssi/commit/1532e0c298ec4f8d7d749a884f7c46f2a2cf53d3](https://github.com/phillhocking/aws-ubuntu-irssi/commit/1532e0c298ec4f8d7d749a884f7c46f2a2cf53d3)
- [https://github.com/ministryofjustice/cloud-platform-terraform-monitoring/commit/87401ba23af26d379d8132cc09fd7cd212773ba1](https://github.com/ministryofjustice/cloud-platform-terraform-monitoring/commit/87401ba23af26d379d8132cc09fd7cd212773ba1)
