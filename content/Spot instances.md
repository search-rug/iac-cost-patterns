+++
title = "Pattern: Spot instances"
weight = 1

[extra]
description = "Use spot instances to run interruptible workloads for significant cost savings compared to regular instances."
count = 12
+++

# Pattern: Spot instances
Use spot instances to run interruptible workloads for significant cost savings compared to regular instances.

## Context
Continuously running compute instances are also continuously billed.
Certain types of workloads which can handle interruption, e.g. batch jobs,
data analysis and optional tasks, do not require on-demand, provisioned instances.


## Solution
Major cloud providers offer excess compute capacity in the form of spot instances.
These provide discounts over on-demand compute instances, with the caveat that instances
can be preempted or deleted at any time when compute capacity needs to be reclaimed.
Users define a price limit and if the spot price falls below this limit, an instance is allocated.
If a user's workloads can handle interruptions, spot instances can offer an economical
alternative to regular instances.


## Example
Use spot instances to run batch jobs: if some of the instances are preempted,
the job is slowed down, but it does not completely stop. For example, request a
worker at a price of 0.03 USD:
```terraform
resource "aws_spot_instance_request" "cheap_worker" {
  # ...
  spot_price    = "0.03"
  instance_type = "c4.xlarge"

  tags = {
    Name = "Worker"
  }
}
```


## References
- [Spot Instances - Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
- [Spot VMs | Compute Engine Documentation | Google Cloud](https://cloud.google.com/compute/docs/instances/spot)
- [Spot Virtual Machines - Spot Pricing and Features | Microsoft Azure](https://azure.microsoft.com/en-us/products/virtual-machines/spot/)
- [Resource: aws_spot_instance_request (Terraform)](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/spot_instance_request)
- [Resource: aws_spot_fleet_request (Terraform)](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/spot_fleet_request)
- [Resource: google_compute_instance (Terraform) - Provisioning model](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance#provisioning_model)
- [Resource: azurerm_linux_virtual_machine (Terraform) - Priority](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/linux_virtual_machine#priority)

## Occurrences
- [https://github.com/openinfrastructure/terraform-google-gitlab-runner/commit/8429375df72b04cc6fedc1ebb5f2c2e4ba18b9f2](https://github.com/openinfrastructure/terraform-google-gitlab-runner/commit/8429375df72b04cc6fedc1ebb5f2c2e4ba18b9f2)
- [https://github.com/kathputli/terraform-aws/commit/321b1aee88f7d15dafe46aede2b86ced70061025](https://github.com/kathputli/terraform-aws/commit/321b1aee88f7d15dafe46aede2b86ced70061025)
- [https://github.com/naciriii/terraform-ec2-gitlab-runner/commit/f8af6bc22bd3d827566e7e65deb63c13cdaf6031](https://github.com/naciriii/terraform-ec2-gitlab-runner/commit/f8af6bc22bd3d827566e7e65deb63c13cdaf6031)
- [https://github.com/Hapag-Lloyd/terraform-aws-bastion-host-ssm/commit/516075e2987bdd1063f22768d451c1c1eb647175](https://github.com/Hapag-Lloyd/terraform-aws-bastion-host-ssm/commit/516075e2987bdd1063f22768d451c1c1eb647175)
- [https://github.com/ToruMakabe/aks-anti-dry-iac/commit/4ba7a9dc3085ab701c85737a4f36dd57fcd7596f](https://github.com/ToruMakabe/aks-anti-dry-iac/commit/4ba7a9dc3085ab701c85737a4f36dd57fcd7596f)
- [https://github.com/paperphyte/terraform-drone/commit/79f4b7c2cf3ad2d1a6d2646eaf27a08fd2611d07](https://github.com/paperphyte/terraform-drone/commit/79f4b7c2cf3ad2d1a6d2646eaf27a08fd2611d07)
- [https://github.com/filhodanuvem/from-dev-to-ops/commit/998be8119321e8812884075b078a1d5fb36cfa69](https://github.com/filhodanuvem/from-dev-to-ops/commit/998be8119321e8812884075b078a1d5fb36cfa69)
- [https://github.com/stephaneclavel/terraform/commit/74b4ba406b9ea761d27298165d0e0de45c9d8491](https://github.com/stephaneclavel/terraform/commit/74b4ba406b9ea761d27298165d0e0de45c9d8491)
- [https://github.com/tale-toul/SingleNodeOpenshiftOnLibvirt/commit/638430604158044fcf123adaf8dfdcc91b1a873e](https://github.com/tale-toul/SingleNodeOpenshiftOnLibvirt/commit/638430604158044fcf123adaf8dfdcc91b1a873e)
- [https://github.com/JaredStufftGD/grok-airflow/commit/7ac9544b0c651fd8193eb063079514d0aa41e290](https://github.com/JaredStufftGD/grok-airflow/commit/7ac9544b0c651fd8193eb063079514d0aa41e290)
- [https://github.com/kaz/kiritan.com/commit/1cd96c7f71e56629ffa07c38e12c4da19fcfc5f7](https://github.com/kaz/kiritan.com/commit/1cd96c7f71e56629ffa07c38e12c4da19fcfc5f7)
- [https://github.com/openinfrastructure/terraform-google-multinic/commit/7a9c468b88d2edee19007cff6529a20a38eeb363](https://github.com/openinfrastructure/terraform-google-multinic/commit/7a9c468b88d2edee19007cff6529a20a38eeb363)
