+++
title = "Pattern: Budget"
weight = 0

[extra]
description = "Use budgets to receive alerts about charged and forecasted costs and control spending."
count = 27
+++

# Pattern: Budget
Use budgets to receive alerts about charged and forecasted costs and control spending.

## Context
The lack of explicit cost monitoring can often lead to unforeseen and undesirable costs.


## Solution
Major cloud providers support the creation of budgets, which allow users to define alerts
about charged and forecasted costs and control spending. Having one or more budgets can
help monitor and manage the cost of cloud deployments.


## Example
Define a budget for a cost limit of 1200 USD for EC2, and generate an
email notification if the forecasted monthly cost exceeds this amount:
```terraform
resource "aws_budgets_budget" "example" {
  name              = "example"
  budget_type       = "COST"
  limit_amount      = "1200"
  limit_unit        = "USD"
  time_unit         = "MONTHLY"

  cost_filter {
    name = "Service"
    values = [
      "Amazon Elastic Compute Cloud - Compute",
    ]
  }

  notification {
    comparison_operator        = "GREATER_THAN"
    threshold                  = 100
    threshold_type             = "PERCENTAGE"
    notification_type          = "FORECASTED"
    subscriber_email_addresses = ["test@example.com"]
  }
}
```


## References
- [Cloud Cost And Usage Budgets - AWS Budgets - AWS](https://aws.amazon.com/aws-cost-management/aws-budgets/)
- [Create, edit, or delete budgets and budget alerts | Cloud Billing | Google Cloud](https://cloud.google.com/billing/docs/how-to/budgets)
- [Tutorial - Create and manage budgets - Microsoft Cost Management | Microsoft Learn](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets?tabs=psbudget)
- [Resource: aws_budgets_budget (Terraform)](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/budgets_budget)
- [Resource: google_billing_budget (Terraform)](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/billing_budget)
- [Resource: azurerm_consumption_budget_resource_group (Terraform)](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/consumption_budget_resource_group)

## Occurrences
- [https://github.com/AJarombek/global-aws-infrastructure/commit/4a89f4b8235961275fa0e6aaf20848f2b8b7e733](https://github.com/AJarombek/global-aws-infrastructure/commit/4a89f4b8235961275fa0e6aaf20848f2b8b7e733)
- [https://github.com/MartinFeineis/terraform/commit/359ba426393c78b78695797f9bdd6a08c0455720](https://github.com/MartinFeineis/terraform/commit/359ba426393c78b78695797f9bdd6a08c0455720)
- [https://github.com/stuartellis/stuartellis-org-tf-modules/commit/39a9cabac6765c75591ba258fef0d10ba7ae0f9e](https://github.com/stuartellis/stuartellis-org-tf-modules/commit/39a9cabac6765c75591ba258fef0d10ba7ae0f9e)
- [https://github.com/forgotpw/forgotpw-infrastructure/commit/f4363ad27d366385f2388d073ce8af796e035406](https://github.com/forgotpw/forgotpw-infrastructure/commit/f4363ad27d366385f2388d073ce8af796e035406)
- [https://github.com/Katesagay/terraform-repo/commit/9aacfbe12e3e7c1e726b9a3d834211aae01f419c](https://github.com/Katesagay/terraform-repo/commit/9aacfbe12e3e7c1e726b9a3d834211aae01f419c)
- [https://github.com/darogina/terragrunt-aws-modules/commit/9c84d03bde131e7f349dcd493ba5b7e55bf8ae2c](https://github.com/darogina/terragrunt-aws-modules/commit/9c84d03bde131e7f349dcd493ba5b7e55bf8ae2c)
- [https://github.com/chetanbothra/Terraform_AWS_Billing_Alert/commit/43b0d3b4cef0d3f57d4f5d4f1c7aeb9bfc3e362a](https://github.com/chetanbothra/Terraform_AWS_Billing_Alert/commit/43b0d3b4cef0d3f57d4f5d4f1c7aeb9bfc3e362a)
- [https://github.com/ntk1000/aws-terraform-template/commit/d016b96d89370b8039817fabdfa055576cf6b4cc](https://github.com/ntk1000/aws-terraform-template/commit/d016b96d89370b8039817fabdfa055576cf6b4cc)
- [https://github.com/StratusGrid/terraform-aws-single-account-starter/commit/c291c0954c89e1bfbdb76d4c8990baf9db986343](https://github.com/StratusGrid/terraform-aws-single-account-starter/commit/c291c0954c89e1bfbdb76d4c8990baf9db986343)
- [https://github.com/nsbno/terraform-aws-cost-alarm/commit/7e135499d33f0a5c51602a506fefe258cac072c6](https://github.com/nsbno/terraform-aws-cost-alarm/commit/7e135499d33f0a5c51602a506fefe258cac072c6)
- [https://github.com/64kramsystem/ultimate_aws_certified_cloud_practitioner_course_terraform_configuration/commit/2f36b8a5f2f818138da72d218c1f3c9666ed54aa](https://github.com/64kramsystem/ultimate_aws_certified_cloud_practitioner_course_terraform_configuration/commit/2f36b8a5f2f818138da72d218c1f3c9666ed54aa)
- [https://github.com/kelledge/idkfa/commit/25cda0b77ff329a89551cc6f14fe8c62820fd424](https://github.com/kelledge/idkfa/commit/25cda0b77ff329a89551cc6f14fe8c62820fd424)
- [https://github.com/oke-py/aws-tf/commit/ec2982c8742cc7bc294f8a3cc07ae9ba5ffcaced](https://github.com/oke-py/aws-tf/commit/ec2982c8742cc7bc294f8a3cc07ae9ba5ffcaced)
- [https://github.com/cob16/aws_static_website/commit/0d4fbd0a7b296a5c9377a835dff89d1499716082](https://github.com/cob16/aws_static_website/commit/0d4fbd0a7b296a5c9377a835dff89d1499716082)
- [https://github.com/mintak21/terraform-old/commit/c10b476d869282ed6cf55def47445b9c703788fe](https://github.com/mintak21/terraform-old/commit/c10b476d869282ed6cf55def47445b9c703788fe)
- [https://github.com/alphagov/govwifi-terraform/commit/348b52a2ae5d6d242c8802644f9e3a5e6460de1d](https://github.com/alphagov/govwifi-terraform/commit/348b52a2ae5d6d242c8802644f9e3a5e6460de1d)
- [https://github.com/eladidan/speedyhead.xyz-terraform/commit/71f034f3e13e9118a2a954e1fc3c0d35153184f0](https://github.com/eladidan/speedyhead.xyz-terraform/commit/71f034f3e13e9118a2a954e1fc3c0d35153184f0)
- [https://github.com/coremaker/terraform-google-nucleus/commit/11234f631f7370dd80ee5fbc5dd7bdbc12dcbf49](https://github.com/coremaker/terraform-google-nucleus/commit/11234f631f7370dd80ee5fbc5dd7bdbc12dcbf49)
- [https://github.com/robgmills/jumpbox/commit/028bbe114d099b0388be9a46adcab80d9383a518](https://github.com/robgmills/jumpbox/commit/028bbe114d099b0388be9a46adcab80d9383a518)
- [https://github.com/AdrianNeatu/blog-terraform/commit/3ba302c69eb2a491a5b23e94084b4ddd24a4a703](https://github.com/AdrianNeatu/blog-terraform/commit/3ba302c69eb2a491a5b23e94084b4ddd24a4a703)
- [https://github.com/richardhughes/infra-modules/commit/48015a86eda461d99b580b69db5922acbe5bd28e](https://github.com/richardhughes/infra-modules/commit/48015a86eda461d99b580b69db5922acbe5bd28e)
- [https://github.com/patheard/terraform-cantrill-aws-associate/commit/bc7484cd34698f2724e5d9f241fd9f53d953e3a3](https://github.com/patheard/terraform-cantrill-aws-associate/commit/bc7484cd34698f2724e5d9f241fd9f53d953e3a3)
- [https://github.com/alghanmi/terraform-modules/commit/f4e8069ff11b7ca7a15ce25843b26d00fb399ade](https://github.com/alghanmi/terraform-modules/commit/f4e8069ff11b7ca7a15ce25843b26d00fb399ade)
- [https://github.com/cds-snc/cloud-based-sensor/commit/10bb572d477197bd3874532bfd364de1cb496d05](https://github.com/cds-snc/cloud-based-sensor/commit/10bb572d477197bd3874532bfd364de1cb496d05)
- [https://github.com/rmaheshvarma/terraform/commit/c866a7dd2575dd2a3f4af83f5f081a5004d0e478](https://github.com/rmaheshvarma/terraform/commit/c866a7dd2575dd2a3f4af83f5f081a5004d0e478)
- [https://github.com/akerl/aws-account/commit/91967d4089ad9580ceae62f7845581935c892455](https://github.com/akerl/aws-account/commit/91967d4089ad9580ceae62f7845581935c892455)
- [https://github.com/singaporewaketools/iaac/commit/197502b1ac4bab77b9ab017b755c4d75ddaa218b](https://github.com/singaporewaketools/iaac/commit/197502b1ac4bab77b9ab017b755c4d75ddaa218b)
