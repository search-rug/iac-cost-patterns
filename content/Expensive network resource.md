+++
title = "Anti-pattern: Expensive network resource"
weight = 6

[extra]
description = "Network resources like NAT gateways, elastic IP addresses and subnets tend to be expensive while not being strictly needed."
count = 51
+++

# Anti-pattern: Expensive network resource
Network resources like NAT gateways, elastic IP addresses and subnets tend to be expensive while not being strictly needed.

## Context
Due to their interdependence, the cost of certain types of networking resources
often adds up. For example, a developer may create multiple subnets, each having
its own NAT gateway, each of which in turn is assigned an IPv4 address. In other
cases, network resources are used which are not strictly required, e.g. load balancers.


## Solution
It is often possible to forego the use of the expensive resources entirely.
Solutions include subnets sharing a single NAT gateway, reducing the number of
subnets or removing the use of load balancers.


## Example
Remove resources that are not strictly required, or reduce the number of networking resources.
For example, the commonly used module terraform-aws-modules/vpc has an option to use a single
NAT gateway instead of creating one per subnet:
```terraform
module "vpc" {
  source = "terraform-aws-modules/vpc"

  # ...

  enable_nat_gateway = true
  single_nat_gateway = true

  # ...
}
```


## References
- [AWS VPC Terraform module](https://registry.terraform.io/modules/terraform-aws-modules/vpc/aws/latest)
- [Logically Isolated Virtual Network - Amazon VPC Pricing - Amazon Web Services](https://aws.amazon.com/vpc/pricing/)
- [Pricing | Cloud NAT | Google Cloud](https://cloud.google.com/nat/pricing)
- [All networking pricing | Virtual Private Cloud | Google Cloud](https://cloud.google.com/vpc/network-pricing#lb)

## Occurrences
- [https://github.com/stealthHat/k8s-terraform/commit/681a3f8b4942be495b3f2528fb9ee40d7a4eb08a](https://github.com/stealthHat/k8s-terraform/commit/681a3f8b4942be495b3f2528fb9ee40d7a4eb08a)
- [https://github.com/thomastodon/jabujabu/commit/02210a3d3ba4a770c29623825b7f54f3ff33f3c7](https://github.com/thomastodon/jabujabu/commit/02210a3d3ba4a770c29623825b7f54f3ff33f3c7)
- [https://github.com/structurefall/jamulus-builder/commit/7190744187e0aed2df8ce84f2a944294d6d4fc5b](https://github.com/structurefall/jamulus-builder/commit/7190744187e0aed2df8ce84f2a944294d6d4fc5b)
- [https://github.com/joshuaspence/infrastructure/commit/d8e1979ea7954076f64ab4d3337b95f14a06fc31](https://github.com/joshuaspence/infrastructure/commit/d8e1979ea7954076f64ab4d3337b95f14a06fc31)
- [https://github.com/joshuaspence/infrastructure/commit/b9b9465314e3b5ada78340d06b90703136cdf3dc](https://github.com/joshuaspence/infrastructure/commit/b9b9465314e3b5ada78340d06b90703136cdf3dc)
- [https://github.com/dexterchan/Terraform_Webserver/commit/af5af0b8e6a59a9c5879fde7eaaa86d694c2bfa2](https://github.com/dexterchan/Terraform_Webserver/commit/af5af0b8e6a59a9c5879fde7eaaa86d694c2bfa2)
- [https://github.com/austin1237/clip-stitcher/commit/4eed76f9bfd4f93181660178ea689d98cd6d66d5](https://github.com/austin1237/clip-stitcher/commit/4eed76f9bfd4f93181660178ea689d98cd6d66d5)
- [https://github.com/IoT-Data-Marketplace/mp-infrastructure/commit/5afcf39a85fc972eb9bb3486e5dc8aeeba77d3ee](https://github.com/IoT-Data-Marketplace/mp-infrastructure/commit/5afcf39a85fc972eb9bb3486e5dc8aeeba77d3ee)
- [https://github.com/InvictrixRom/website-infrastructure/commit/09e400452c1bde25fe393dd56c2fd608b84a18ac](https://github.com/InvictrixRom/website-infrastructure/commit/09e400452c1bde25fe393dd56c2fd608b84a18ac)
- [https://github.com/InvictrixRom/website-infrastructure/commit/44d66328ea4467d05d7fb8092631aff5afbd8b26](https://github.com/InvictrixRom/website-infrastructure/commit/44d66328ea4467d05d7fb8092631aff5afbd8b26)
- [https://github.com/pvandervelde/infrastructure.azure.core.network.hub/commit/0ecf0a154918bd9bdc0f53557bc1f80920da6b14](https://github.com/pvandervelde/infrastructure.azure.core.network.hub/commit/0ecf0a154918bd9bdc0f53557bc1f80920da6b14)
- [https://github.com/Midas-Protocol/webtwo-infra/commit/25ed0319bf8099f0cc79eceba9104c73d9507e0d](https://github.com/Midas-Protocol/webtwo-infra/commit/25ed0319bf8099f0cc79eceba9104c73d9507e0d)
- [https://github.com/GBergeret/tf-vpc-module/commit/5e63c8390cb1001daf4ad74bb2926cc060c0de08](https://github.com/GBergeret/tf-vpc-module/commit/5e63c8390cb1001daf4ad74bb2926cc060c0de08)
- [https://github.com/GBergeret/micro-service-as-code/commit/46f76d50b8569f450ce909e04f3c5fa81b97737a](https://github.com/GBergeret/micro-service-as-code/commit/46f76d50b8569f450ce909e04f3c5fa81b97737a)
- [https://github.com/ecsworkshop2018/expertalk-2018-ecs-workshop/commit/034908d914982eacea51b0ac61f2781069387412](https://github.com/ecsworkshop2018/expertalk-2018-ecs-workshop/commit/034908d914982eacea51b0ac61f2781069387412)
- [https://github.com/kitchen/personal-terraform/commit/fe1f2665b198308a438ec3d46b24843089df1a2a](https://github.com/kitchen/personal-terraform/commit/fe1f2665b198308a438ec3d46b24843089df1a2a)
- [https://github.com/robertlupinek/rh-ex407/commit/0c679d7adfa5bf38d5c7846958f3508fc036b3e9](https://github.com/robertlupinek/rh-ex407/commit/0c679d7adfa5bf38d5c7846958f3508fc036b3e9)
- [https://github.com/skehlet/aws-batch-processing/commit/decdbce98d33cf2599aee554779ef5d8b5361d8f](https://github.com/skehlet/aws-batch-processing/commit/decdbce98d33cf2599aee554779ef5d8b5361d8f)
- [https://github.com/poseidon/terraform-aws-kubernetes/commit/ef0372d2684ef920c6e54cf8b9f80d87db90e636](https://github.com/poseidon/terraform-aws-kubernetes/commit/ef0372d2684ef920c6e54cf8b9f80d87db90e636)
- [https://github.com/paperphyte/terraform-drone/commit/f62bfebb54530c9466cfdb21336794f24bcd63a7](https://github.com/paperphyte/terraform-drone/commit/f62bfebb54530c9466cfdb21336794f24bcd63a7)
- [https://github.com/nisunisu/AWS_Blue_Green_Deployment/commit/d0741cddb32ed7970904693e3a697603fa21bbbb](https://github.com/nisunisu/AWS_Blue_Green_Deployment/commit/d0741cddb32ed7970904693e3a697603fa21bbbb)
- [https://github.com/ryanlg/ryhino-public/commit/e51b9583b2df3154b5c82da361d411d65ed23bab](https://github.com/ryanlg/ryhino-public/commit/e51b9583b2df3154b5c82da361d411d65ed23bab)
- [https://github.com/masterpointio/terraform-aws-nuke-bomber/commit/33fbb76715ce6e35565b5f83f7ece0f9df37d282](https://github.com/masterpointio/terraform-aws-nuke-bomber/commit/33fbb76715ce6e35565b5f83f7ece0f9df37d282)
- [https://github.com/kinvolk-archives/lokomotive-kubernetes/commit/0c4d59db87b67d7c7a0a0f54677961a01ed8fbe4](https://github.com/kinvolk-archives/lokomotive-kubernetes/commit/0c4d59db87b67d7c7a0a0f54677961a01ed8fbe4)
- [https://github.com/alhardy-net/terraform-core-aws-alhardynet-networking/commit/30be6aa1969e37d512153b558540fe714b635c4c](https://github.com/alhardy-net/terraform-core-aws-alhardynet-networking/commit/30be6aa1969e37d512153b558540fe714b635c4c)
- [https://github.com/alhardy-net/terraform-core-aws-alhardynet-networking/commit/f7b96f0b28008f8aed881cc211a5f3fdb3ae67ac](https://github.com/alhardy-net/terraform-core-aws-alhardynet-networking/commit/f7b96f0b28008f8aed881cc211a5f3fdb3ae67ac)
- [https://github.com/alhardy-net/terraform-core-aws-alhardynet-networking/commit/b26b9e5d1b13602a4c192d9697a12df7770906b2](https://github.com/alhardy-net/terraform-core-aws-alhardynet-networking/commit/b26b9e5d1b13602a4c192d9697a12df7770906b2)
- [https://github.com/imma/fogg-env/commit/7de45302cfa8a7dca88ab61b3021091cc480b495](https://github.com/imma/fogg-env/commit/7de45302cfa8a7dca88ab61b3021091cc480b495)
- [https://github.com/schubergphilis/terraform-aws-mcaf-matillion/commit/3b0e2fe42d660664c49d54ae8706de004a9b4176](https://github.com/schubergphilis/terraform-aws-mcaf-matillion/commit/3b0e2fe42d660664c49d54ae8706de004a9b4176)
- [https://github.com/binbashar/le-tf-infra-aws/commit/a873443bd618ac9c14d12210ed4d12a11cc1f733](https://github.com/binbashar/le-tf-infra-aws/commit/a873443bd618ac9c14d12210ed4d12a11cc1f733)
- [https://github.com/binbashar/le-tf-infra-aws/commit/19c37f7e4e65d14e760f1ff8cf60cfd1e98c1a8b](https://github.com/binbashar/le-tf-infra-aws/commit/19c37f7e4e65d14e760f1ff8cf60cfd1e98c1a8b)
- [https://github.com/binbashar/le-tf-infra-aws/commit/bbfbd2484ace2819ffceac9155b995ab870ee3a3](https://github.com/binbashar/le-tf-infra-aws/commit/bbfbd2484ace2819ffceac9155b995ab870ee3a3)
- [https://github.com/mads-hartmann/cloud.mads-hartmann.com/commit/667f5715c19534bfe5b01ad692979447412fd033](https://github.com/mads-hartmann/cloud.mads-hartmann.com/commit/667f5715c19534bfe5b01ad692979447412fd033)
- [https://github.com/opszero/terraform-aws-kubespot/commit/decc9706133af9978ada6cf58a1a63343468e8a0](https://github.com/opszero/terraform-aws-kubespot/commit/decc9706133af9978ada6cf58a1a63343468e8a0)
- [https://github.com/stSoftwareAU/sts-network/commit/bf59a4c995822ccfdeee64781345c12ebefa967f](https://github.com/stSoftwareAU/sts-network/commit/bf59a4c995822ccfdeee64781345c12ebefa967f)
- [https://github.com/lean-delivery/terraform-module-aws-core/commit/25bbff736936b64a6120ef9608498830ecec33c0](https://github.com/lean-delivery/terraform-module-aws-core/commit/25bbff736936b64a6120ef9608498830ecec33c0)
- [https://github.com/CheesecakeLabs/django-drf-boilerplate/commit/e4003aa3c51b789e2a2b5828768a7d0f34659209](https://github.com/CheesecakeLabs/django-drf-boilerplate/commit/e4003aa3c51b789e2a2b5828768a7d0f34659209)
- [https://github.com/covidapihub/terraform-covidapihub/commit/3c5d381a20fbd287f1003271ee1ba64272325074](https://github.com/covidapihub/terraform-covidapihub/commit/3c5d381a20fbd287f1003271ee1ba64272325074)
- [https://github.com/simplygenius/atmos-recipes/commit/d27b48345a3827b8a10cb5388e42bd5cbea484bb](https://github.com/simplygenius/atmos-recipes/commit/d27b48345a3827b8a10cb5388e42bd5cbea484bb)
- [https://github.com/hellupline/terraform-eks-cluster/commit/2bd01358b3a30d1680074f9bbd120da3a1456450](https://github.com/hellupline/terraform-eks-cluster/commit/2bd01358b3a30d1680074f9bbd120da3a1456450)
- [https://github.com/tsub/ecs-sandbox/commit/8501fafbba186919c9e9b55a6a3fc72b4fb80909](https://github.com/tsub/ecs-sandbox/commit/8501fafbba186919c9e9b55a6a3fc72b4fb80909)
- [https://github.com/schubergphilis/terraform-aws-mcaf-vpc/commit/6ca41e5ad697201a1d225e5d15134e547ee6ced3](https://github.com/schubergphilis/terraform-aws-mcaf-vpc/commit/6ca41e5ad697201a1d225e5d15134e547ee6ced3)
- [https://github.com/davidcallen/parkrunpointsleague/commit/21627e4057b3446b511e4369ca366e297cfc87eb](https://github.com/davidcallen/parkrunpointsleague/commit/21627e4057b3446b511e4369ca366e297cfc87eb)
- [https://github.com/HarsheshShah08/HS-Terraform/commit/e0d0f044c54ebf491c122664d03e0cfe5d2b0823](https://github.com/HarsheshShah08/HS-Terraform/commit/e0d0f044c54ebf491c122664d03e0cfe5d2b0823)
- [https://github.com/nagpach/terraform-example-aws-vpc/commit/35d26fd046185ae079e09fa6435c41ae685e679e](https://github.com/nagpach/terraform-example-aws-vpc/commit/35d26fd046185ae079e09fa6435c41ae685e679e)
- [https://github.com/appbricks/cloud-inceptor/commit/782a0a3c30cf83bcaeacc942789ccc903576fe8a](https://github.com/appbricks/cloud-inceptor/commit/782a0a3c30cf83bcaeacc942789ccc903576fe8a)
- [https://github.com/firehawkvfx/firehawk-prototype-deprecated/commit/894fb1d80c7a3953b7a51d7acd5e9b942faced8f](https://github.com/firehawkvfx/firehawk-prototype-deprecated/commit/894fb1d80c7a3953b7a51d7acd5e9b942faced8f)
- [https://github.com/Xin00163/terraform/commit/f69ce3812180a20bbda69ff1432a1cd36342bc3b](https://github.com/Xin00163/terraform/commit/f69ce3812180a20bbda69ff1432a1cd36342bc3b)
- [https://github.com/jeffawang/infrastructure/commit/9f610811aea8c523332e9dccad9bb0800b70691e](https://github.com/jeffawang/infrastructure/commit/9f610811aea8c523332e9dccad9bb0800b70691e)
- [https://github.com/stephengrier/my-infra/commit/e5742d6f4f93dd432c9d8d0a31493d43c45aaff1](https://github.com/stephengrier/my-infra/commit/e5742d6f4f93dd432c9d8d0a31493d43c45aaff1)
- [https://github.com/naftulikay/titan/commit/a0ea4fd84a409fe4ee853effa9f309a005b0efc1](https://github.com/naftulikay/titan/commit/a0ea4fd84a409fe4ee853effa9f309a005b0efc1)