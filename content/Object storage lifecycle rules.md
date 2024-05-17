+++
title = "Pattern: Object storage lifecycle rules"
weight = 2

[extra]
description = "Define lifecycle rules for object storage to move objects to cheaper storage or drop them entirely."
count = 6
+++

# Pattern: Object storage lifecycle rules
Define lifecycle rules for object storage to move objects to cheaper storage or drop them entirely.

## Context
By default, objects stored in cloud object storage are retained,
and therefore billed, indefinitely. Objects also have a storage class or access tier,
which can be used to balance access performance and cost depending on the use case.


## Solution
By configuring lifecycle rules or policies, objects can be transitioned to
cheaper storage classes or deleted after a certain amount of time.


## Example
Transition objects under the "log/" prefix to the Glacier storage class after 60 days, and expire after 90 days:
```terraform
resource "aws_s3_bucket_lifecycle_configuration" "example" {
  bucket = aws_s3_bucket.bucket.id

  rule {
    id = "log"

    expiration {
      days = 90
    }

    filter {
      prefix = "log/"
    }

    status = "Enabled"

    transition {
      days          = 60
      storage_class = "GLACIER"
    }
  }
}
```


## References
- [Resource: aws_s3_bucket_lifecycle_configuration](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_lifecycle_configuration)
- [Resource: google_storage_bucket (Terraform) - Life cycle settings](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket#example-usage---life-cycle-settings-for-storage-bucket-objects)
- [Resource: azurerm_storage_management_policy (Terraform)](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_management_policy)

## Occurrences
- [https://github.com/alphagov/govuk-aws/commit/f844cd8e254b161bebef04101f8ce177bcd0840c](https://github.com/alphagov/govuk-aws/commit/f844cd8e254b161bebef04101f8ce177bcd0840c)
- [https://github.com/alphagov/govuk-terraform-provisioning/commit/ac105ab0a5ae38fbf69167e072f8970a4a61c3e8](https://github.com/alphagov/govuk-terraform-provisioning/commit/ac105ab0a5ae38fbf69167e072f8970a4a61c3e8)
- [https://github.com/ExpediaGroup/apiary-data-lake/commit/47e62f2fc73a96611606cd619c084d1ded9d844d](https://github.com/ExpediaGroup/apiary-data-lake/commit/47e62f2fc73a96611606cd619c084d1ded9d844d)
- [https://github.com/SamTowne/BasketballDrillBot/commit/4ec6d54e4d36ab02b0a7daf042e727717371eaec](https://github.com/SamTowne/BasketballDrillBot/commit/4ec6d54e4d36ab02b0a7daf042e727717371eaec)
- [https://github.com/utilitywarehouse/tf_telecom/commit/17007456991c1a8faa26b1f4ac993883f577d124](https://github.com/utilitywarehouse/tf_telecom/commit/17007456991c1a8faa26b1f4ac993883f577d124)
- [https://github.com/trajano/terraform-s3-backend/commit/cb9f00a2f6f23b44f7db08863ef5fb0b9ea0bc0c](https://github.com/trajano/terraform-s3-backend/commit/cb9f00a2f6f23b44f7db08863ef5fb0b9ea0bc0c)
