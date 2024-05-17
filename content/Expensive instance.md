+++
title = "Anti-pattern: Expensive instance"
weight = 3

[extra]
description = "Compute instances are often overprovisioned even when a cheaper instance would suffice."
count = 50
+++

# Anti-pattern: Expensive instance
Compute instances are often overprovisioned even when a cheaper instance would suffice.

## Context
A recurring pattern in cloud deployments is that developers initially
choose compute instances which are overprovisioned, because it is
difficult to know the requirements upfront. This leads to situations
where developers deploy, for example on AWS, '2xlarge' instances, when
in fact 'large' or even 'medium' would suffice.


## Solution
Critically evaluate required performance levels and special functionality
(e.g. memory-optimized versus general-purpose instances), and scale down
the provisioned instance types where appropriate.


## Example
Downgrade to a cheaper general-purpose instance in the same family to save costs:
```diff
@@ -1,5 +1,5 @@
 resource "google_compute_instance" "example" {
   name         = "example"
-  machine_type = "n1-standard-1"
+  machine_type = "g1-small"
   # ...
 }
```


## References
- [Resource: aws_instance (Terraform)](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance)
- [Resource: google_compute_instance (Terraform)](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance)
- [Resource: azurerm_linux_virtual_machine (Terraform)](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/linux_virtual_machine)
- [Resource: azurerm_windows_virtual_machine (Terraform)](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/windows_virtual_machine)
- [Compute - EC2 Instance Types - AWS](https://aws.amazon.com/ec2/instance-types/)
- [Machine families resource and comparison guide | Compute Engine Documentation | Google Cloud](https://cloud.google.com/compute/docs/machine-resource)
- [Virtual Machine series | Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/series/)

## Occurrences
- [https://github.com/beaulabs/terraform_aws_ec2_instance/commit/d6df68da5ae58fb5c650c6be15d9d8e676a129db](https://github.com/beaulabs/terraform_aws_ec2_instance/commit/d6df68da5ae58fb5c650c6be15d9d8e676a129db)
- [https://github.com/gudlyf/TerraformOpenVPN/commit/4bc861c153b65a2d7c0d5f3fac30ab72b0fc6942](https://github.com/gudlyf/TerraformOpenVPN/commit/4bc861c153b65a2d7c0d5f3fac30ab72b0fc6942)
- [https://github.com/IncredibleHolg/infra-aws-code/commit/70904707a36ff8e5167e695de3529d8318911ba4](https://github.com/IncredibleHolg/infra-aws-code/commit/70904707a36ff8e5167e695de3529d8318911ba4)
- [https://github.com/ministryofjustice/cloud-platform-infrastructure/commit/e5dd13d33c1e927f932971d067d8f70e9041b5f3](https://github.com/ministryofjustice/cloud-platform-infrastructure/commit/e5dd13d33c1e927f932971d067d8f70e9041b5f3)
- [https://github.com/cisagov/cyhy_amis/commit/4e67a501bb3f5187a3e9af523921ac62b8a88469](https://github.com/cisagov/cyhy_amis/commit/4e67a501bb3f5187a3e9af523921ac62b8a88469)
- [https://github.com/Kalmalyzer/UE-Jenkins-BuildSystem/commit/636097557e403eb1d6b6211b09e30c47e7f39466](https://github.com/Kalmalyzer/UE-Jenkins-BuildSystem/commit/636097557e403eb1d6b6211b09e30c47e7f39466)
- [https://github.com/dshmelev/aws_kube_tc/commit/853298ac74250964aa2d2ea921daa5905528b3a9](https://github.com/dshmelev/aws_kube_tc/commit/853298ac74250964aa2d2ea921daa5905528b3a9)
- [https://github.com/aaaaasam/azure/commit/c7bc0ce6f3fcaffcbbe7753f1a9d8437809bc167](https://github.com/aaaaasam/azure/commit/c7bc0ce6f3fcaffcbbe7753f1a9d8437809bc167)
- [https://github.com/rbabyuk/terra/commit/beae899804779adf914c08f290c5d71b542c9ed1](https://github.com/rbabyuk/terra/commit/beae899804779adf914c08f290c5d71b542c9ed1)
- [https://github.com/Leonard-Ta/Sample-Security-service-Terraform/commit/c16481a84d5823b65ce96bd811a265222385b43b](https://github.com/Leonard-Ta/Sample-Security-service-Terraform/commit/c16481a84d5823b65ce96bd811a265222385b43b)
- [https://github.com/jjffggpp/jjffggpp/commit/93ee12adde6ac773c76b590fe89c24df372f326b](https://github.com/jjffggpp/jjffggpp/commit/93ee12adde6ac773c76b590fe89c24df372f326b)
- [https://github.com/EngineerBetter/kf-infra/commit/fa5f7fb35b0b44020fb81dd5c4e3b9ceaca1f967](https://github.com/EngineerBetter/kf-infra/commit/fa5f7fb35b0b44020fb81dd5c4e3b9ceaca1f967)
- [https://github.com/KoutaroNohira/hashicat/commit/81dc1d3f98034672d5f62f440f2cc3abc58ce2a2](https://github.com/KoutaroNohira/hashicat/commit/81dc1d3f98034672d5f62f440f2cc3abc58ce2a2)
- [https://github.com/wallnerryan/terraform-scaleio/commit/605e74facfa2ff519ba5cda6e57474666901bd8c](https://github.com/wallnerryan/terraform-scaleio/commit/605e74facfa2ff519ba5cda6e57474666901bd8c)
- [https://github.com/UrbanOS-Examples/common/commit/206394bcc75866953f64cbf3bd6214e4e6f96e91](https://github.com/UrbanOS-Examples/common/commit/206394bcc75866953f64cbf3bd6214e4e6f96e91)
- [https://github.com/cookpad/terraform-aws-eks/commit/59c40286757e1fa5cb5391421c5380e5ad506387](https://github.com/cookpad/terraform-aws-eks/commit/59c40286757e1fa5cb5391421c5380e5ad506387)
- [https://github.com/ayltai/hknews-infrastructure/commit/68171be117d3997b84253258f41fad6daedbc76a](https://github.com/ayltai/hknews-infrastructure/commit/68171be117d3997b84253258f41fad6daedbc76a)
- [https://github.com/joelchrist/terraform/commit/bbf18d695bd7597977ea7a97d5434ca7f1a37d57](https://github.com/joelchrist/terraform/commit/bbf18d695bd7597977ea7a97d5434ca7f1a37d57)
- [https://github.com/jg210/aws-experiments/commit/5ff37f12a421fdd902d8eb1e6d7491ee181fd179](https://github.com/jg210/aws-experiments/commit/5ff37f12a421fdd902d8eb1e6d7491ee181fd179)
- [https://github.com/scott45/vof-deployment-scripts/commit/c6b2c1bee4c1e53e87fd3d94fc8c07cf64342d7b](https://github.com/scott45/vof-deployment-scripts/commit/c6b2c1bee4c1e53e87fd3d94fc8c07cf64342d7b)
- [https://github.com/fdns/terraform-k8s/commit/f106917bb7b2d8d4428022bb119585bf9f35769c](https://github.com/fdns/terraform-k8s/commit/f106917bb7b2d8d4428022bb119585bf9f35769c)
- [https://github.com/ministryofjustice/hmpps-env-configs/commit/670c006bad288d0360c3811aa63b3c323753c385](https://github.com/ministryofjustice/hmpps-env-configs/commit/670c006bad288d0360c3811aa63b3c323753c385)
- [https://github.com/ministryofjustice/hmpps-env-configs/commit/954dda617d47007a8a1ff5780d3174e900e95be1](https://github.com/ministryofjustice/hmpps-env-configs/commit/954dda617d47007a8a1ff5780d3174e900e95be1)
- [https://github.com/Linaro/qa-reports.linaro.org/commit/76c8d1ee35046912b6da4f1cc23e8b1dcc12abe9](https://github.com/Linaro/qa-reports.linaro.org/commit/76c8d1ee35046912b6da4f1cc23e8b1dcc12abe9)
- [https://github.com/KieniL/terraform_setups/commit/37f66bc43f57b1b7a5a897c58cefe09900afd7ef](https://github.com/KieniL/terraform_setups/commit/37f66bc43f57b1b7a5a897c58cefe09900afd7ef)
- [https://github.com/digio/terraform-google-gitlab-runner/commit/07f8279fe65a35c0e595f3171f3d75791e49a9ae](https://github.com/digio/terraform-google-gitlab-runner/commit/07f8279fe65a35c0e595f3171f3d75791e49a9ae)
- [https://github.com/jharley/azure-basic-demo/commit/7cd3d202d8723c565704f23c143cae3b1e1d6d2b](https://github.com/jharley/azure-basic-demo/commit/7cd3d202d8723c565704f23c143cae3b1e1d6d2b)
- [https://github.com/pangeo-data/terraform-deploy/commit/f8163bd52bea3774e2f160cff0523c602e65d933](https://github.com/pangeo-data/terraform-deploy/commit/f8163bd52bea3774e2f160cff0523c602e65d933)
- [https://github.com/pangeo-data/terraform-deploy/commit/7244eed07a1008675f45cc4349bf68141bb29edc](https://github.com/pangeo-data/terraform-deploy/commit/7244eed07a1008675f45cc4349bf68141bb29edc)
- [https://github.com/aeternity/terraform-aws-devnet/commit/f4113a8f7e52991dfb75f63688aeba77bac76b01](https://github.com/aeternity/terraform-aws-devnet/commit/f4113a8f7e52991dfb75f63688aeba77bac76b01)
- [https://github.com/schubergphilis/terraform-aws-mcaf-matillion/commit/3b0e2fe42d660664c49d54ae8706de004a9b4176](https://github.com/schubergphilis/terraform-aws-mcaf-matillion/commit/3b0e2fe42d660664c49d54ae8706de004a9b4176)
- [https://github.com/binbashar/le-tf-infra-aws/commit/0208ae3bc238f029b1faf6bdc3552dbe6147657b](https://github.com/binbashar/le-tf-infra-aws/commit/0208ae3bc238f029b1faf6bdc3552dbe6147657b)
- [https://github.com/fpco/terraform-aws-foundation/commit/cfe92035f1b281cddfcf62664ec6b96e85e0ac32](https://github.com/fpco/terraform-aws-foundation/commit/cfe92035f1b281cddfcf62664ec6b96e85e0ac32)
- [https://github.com/Civil-Service-Human-Resources/lpg-terraform-paas/commit/59477d3dc237e72252bde005b783213b7e8ed961](https://github.com/Civil-Service-Human-Resources/lpg-terraform-paas/commit/59477d3dc237e72252bde005b783213b7e8ed961)
- [https://github.com/ibm-cloud-architecture/iks_vpc_lab/commit/629819ce0c440760be155874cb42ab497f0304bd](https://github.com/ibm-cloud-architecture/iks_vpc_lab/commit/629819ce0c440760be155874cb42ab497f0304bd)
- [https://github.com/goodpen/gke-v.1.0/commit/45053a0862bf97f0525862c411fa4da5d59ac397](https://github.com/goodpen/gke-v.1.0/commit/45053a0862bf97f0525862c411fa4da5d59ac397)
- [https://github.com/rshurts/gke-cd-with-spinnaker/commit/3bc712aba0c797053b5cdc113e3e46afb6cff8a5](https://github.com/rshurts/gke-cd-with-spinnaker/commit/3bc712aba0c797053b5cdc113e3e46afb6cff8a5)
- [https://github.com/kaz/kiritan.com/commit/1cd96c7f71e56629ffa07c38e12c4da19fcfc5f7](https://github.com/kaz/kiritan.com/commit/1cd96c7f71e56629ffa07c38e12c4da19fcfc5f7)
- [https://github.com/midl-dev/tezos-auxiliary-cluster/commit/9cbfebaab11cb3466b160d18ef2eb46c0b875d55](https://github.com/midl-dev/tezos-auxiliary-cluster/commit/9cbfebaab11cb3466b160d18ef2eb46c0b875d55)
- [https://github.com/NLnetLabs/rpki-deploy/commit/8bd6e745475f635d6f6b6929a545afa2e1d9dd57](https://github.com/NLnetLabs/rpki-deploy/commit/8bd6e745475f635d6f6b6929a545afa2e1d9dd57)
- [https://github.com/TimonB/tf-azure-example/commit/ce89df3cebc6487146391afe9517661053229f77](https://github.com/TimonB/tf-azure-example/commit/ce89df3cebc6487146391afe9517661053229f77)
- [https://github.com/00inboxtest/terraform-google-vault/commit/1d0b5db7f310dc6a47af3130a97e5373d9cdaddf](https://github.com/00inboxtest/terraform-google-vault/commit/1d0b5db7f310dc6a47af3130a97e5373d9cdaddf)
- [https://github.com/Amberoat/didactic-octo-eureka/commit/494706fc421a0ddda47f7d543b7e7a296c378c26](https://github.com/Amberoat/didactic-octo-eureka/commit/494706fc421a0ddda47f7d543b7e7a296c378c26)
- [https://github.com/robertdebock/terraform-aws-vault/commit/757edca9d6fb2231ebdcf03ec611183c59eaf39b](https://github.com/robertdebock/terraform-aws-vault/commit/757edca9d6fb2231ebdcf03ec611183c59eaf39b)
- [https://github.com/covid-videoplattform/covid-videoplattform/commit/83d8b928ecb3f271a058bb30eaa1e05ce10e0434](https://github.com/covid-videoplattform/covid-videoplattform/commit/83d8b928ecb3f271a058bb30eaa1e05ce10e0434)
- [https://github.com/alphagov/govuk-infrastructure/commit/a51a3bfcd73fd55ecd43aa36ce3f266f0cefc2dc](https://github.com/alphagov/govuk-infrastructure/commit/a51a3bfcd73fd55ecd43aa36ce3f266f0cefc2dc)
- [https://github.com/pelias/terraform-elasticsearch/commit/8454c8ee25e821abde10b73a2fec691269e41822](https://github.com/pelias/terraform-elasticsearch/commit/8454c8ee25e821abde10b73a2fec691269e41822)
- [https://github.com/ironpeakservices/infrastructure/commit/2ca24fa9114b5b4389768d5ab93c1e6d99bb287c](https://github.com/ironpeakservices/infrastructure/commit/2ca24fa9114b5b4389768d5ab93c1e6d99bb287c)
- [https://github.com/robertdebock/git-terraform-demo/commit/5638b1a044215292a5e3fa405b6a0567c6b35436](https://github.com/robertdebock/git-terraform-demo/commit/5638b1a044215292a5e3fa405b6a0567c6b35436)
- [https://github.com/robertdebock/git-terraform-demo/commit/686374095321975d851932a77b139d627f50c7d5](https://github.com/robertdebock/git-terraform-demo/commit/686374095321975d851932a77b139d627f50c7d5)
