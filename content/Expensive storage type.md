+++
title = "Anti-pattern: Expensive storage type"
weight = 5

[extra]
description = "More expensive storage types are often used even when cheaper storage types would be sufficient."
count = 17
+++

# Anti-pattern: Expensive storage type
More expensive storage types are often used even when cheaper storage types would be sufficient.

## Context
Developers are able to choose between different storage types (HDD vs SSD, durability guarantees)
for e.g. instances' root disks. However, not all use cases require highly durable SSD storage,
making cheaper storage types a viable way to save cost.


## Solution
Evaluate performance and durability guarantees for storage and switch to
a less expensive type where relevant.


## Example
Switch an OS disk from Premium LRS storage to Standard LRS:
```diff
@@ -1,6 +1,6 @@
 resource "azurerm_linux_virtual_machine" "example" {
   # ...
   os_disk {
-    storage_account_type = "Premium_LRS"
+    storage_account_type = "Standard_LRS"
   }
 }
```


## References
- [Resource: azurerm_linux_virtual_machine (Terraform) - os_disk](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/linux_virtual_machine#os_disk)
- [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)
- [Storage options | Compute Engine Documentation | Google Cloud](https://cloud.google.com/compute/docs/disks/)
- [Azure managed disk types](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types)

## Occurrences
- [https://github.com/thomastodon/jabujabu/commit/02210a3d3ba4a770c29623825b7f54f3ff33f3c7](https://github.com/thomastodon/jabujabu/commit/02210a3d3ba4a770c29623825b7f54f3ff33f3c7)
- [https://github.com/giantswarm/giantnetes-terraform/commit/53ed24b573947c73ea9f0f4f8b477c44b7de2d54](https://github.com/giantswarm/giantnetes-terraform/commit/53ed24b573947c73ea9f0f4f8b477c44b7de2d54)
- [https://github.com/Kalmalyzer/UE-Jenkins-BuildSystem/commit/ee8942b2c5d59546dd3b3be5f2cb88500d0fe1be](https://github.com/Kalmalyzer/UE-Jenkins-BuildSystem/commit/ee8942b2c5d59546dd3b3be5f2cb88500d0fe1be)
- [https://github.com/Leonard-Ta/Sample-Security-service-Terraform/commit/c16481a84d5823b65ce96bd811a265222385b43b](https://github.com/Leonard-Ta/Sample-Security-service-Terraform/commit/c16481a84d5823b65ce96bd811a265222385b43b)
- [https://github.com/falldamagestudio/UE4-GHA-BuildSystem/commit/e58083adbf91e7daa8ddb5db6c3b2e5c8c0a906c](https://github.com/falldamagestudio/UE4-GHA-BuildSystem/commit/e58083adbf91e7daa8ddb5db6c3b2e5c8c0a906c)
- [https://github.com/bculberson/btc2snowflake/commit/9f8227bf53ebc2b1bb0b99d0697f9f66eed7ab6d](https://github.com/bculberson/btc2snowflake/commit/9f8227bf53ebc2b1bb0b99d0697f9f66eed7ab6d)
- [https://github.com/ministryofjustice/hmpps-env-configs/commit/0328838420ac0d3754cf772a7d2f5bb1612193ed](https://github.com/ministryofjustice/hmpps-env-configs/commit/0328838420ac0d3754cf772a7d2f5bb1612193ed)
- [https://github.com/travis-infrastructure/terraform-stuff/commit/1e208af4c83d093c900f4cccedbca6183142a07f](https://github.com/travis-infrastructure/terraform-stuff/commit/1e208af4c83d093c900f4cccedbca6183142a07f)
- [https://github.com/sdcote/cloudsql/commit/dfe44fcf8f5a477e1fbc354f1b1d87af28895c0f](https://github.com/sdcote/cloudsql/commit/dfe44fcf8f5a477e1fbc354f1b1d87af28895c0f)
- [https://github.com/wellcomecollection/archivematica-infrastructure/commit/ce576be106257496e20d946d6eab5f8783dada92](https://github.com/wellcomecollection/archivematica-infrastructure/commit/ce576be106257496e20d946d6eab5f8783dada92)
- [https://github.com/jshcmpbll/Cloud-Mac-KVM/commit/361885d22c0304cb44683f9b005f82ca5e269841](https://github.com/jshcmpbll/Cloud-Mac-KVM/commit/361885d22c0304cb44683f9b005f82ca5e269841)
- [https://github.com/TimonB/tf-azure-example/commit/b49579fbecbe8002932fdfb86146f83efd60bfcf](https://github.com/TimonB/tf-azure-example/commit/b49579fbecbe8002932fdfb86146f83efd60bfcf)
- [https://github.com/phillhocking/aws-ubuntu-irssi/commit/1532e0c298ec4f8d7d749a884f7c46f2a2cf53d3](https://github.com/phillhocking/aws-ubuntu-irssi/commit/1532e0c298ec4f8d7d749a884f7c46f2a2cf53d3)
- [https://github.com/bhfsystem/fogg/commit/81e606a72e7c2e06c2f6d9c204086157aa82eac3](https://github.com/bhfsystem/fogg/commit/81e606a72e7c2e06c2f6d9c204086157aa82eac3)
- [https://github.com/bhfsystem/fogg/commit/7cc487f270d553f819fea0cf96e872c374979305](https://github.com/bhfsystem/fogg/commit/7cc487f270d553f819fea0cf96e872c374979305)
- [https://github.com/cisagov/freeipa-server-tf-module/commit/99fd319a72d25441acf36fd2c167a875e9028935](https://github.com/cisagov/freeipa-server-tf-module/commit/99fd319a72d25441acf36fd2c167a875e9028935)
- [https://github.com/ministryofjustice/cloud-platform-terraform-monitoring/commit/87401ba23af26d379d8132cc09fd7cd212773ba1](https://github.com/ministryofjustice/cloud-platform-terraform-monitoring/commit/87401ba23af26d379d8132cc09fd7cd212773ba1)
