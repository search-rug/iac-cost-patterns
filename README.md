# IaC Cost Patterns

This is a collection of patterns and antipatterns that support managing cost in Infrastructure as Code artifacts of cloud software deployments. It is intended to be a living catalog, open to community contributions.

[`patterns.yml`](./thematic-analysis/patterns.yml) is the pattern dataset, including references and occurrences in commits.

## Context

The original set of patterns was extracted using Thematic Analysis on 499 cost-related commits from 403 repositories. These commits were collected as part of [a prior study](https://arxiv.org/abs/2304.07531).

During our analysis, we found 128 codes including one for "no related changes identified", with the remaining 127 codes indicating cost-saving or cost-increasing actions. Of the 499 commits, 342 contained at least one cost-related code, while 179 were coded "no related changes identified".

After validation, 50 codes were integrated into 3 and 7 themes representing patterns and antipatterns respectively, while the remaining 67 codes were discarded due to lack of occurrences. In total, 237 out of 342 commits contain at least one occurrence of an (anti)pattern.

## Patterns

| Type | Name | Description |
| --- | --- | --- |
| Pattern | [Budget](https://search-rug.github.io/iac-cost-patterns/budget/) | Use budgets to receive alerts about charged and forecasted costs and control spending. |
| Pattern | [Spot instances](https://search-rug.github.io/iac-cost-patterns/spot-instances/) | Use spot instances to run interruptible workloads for significant cost savings compared to regular instances. |
| Pattern | [Object storage lifecycle rules](https://search-rug.github.io/iac-cost-patterns/object-storage-lifecycle-rules/) | Define lifecycle rules for object storage to move objects to cheaper storage or drop them entirely. |
| Antipattern | [Expensive instance](https://search-rug.github.io/iac-cost-patterns/expensive-instance/) | Compute instances are often overprovisioned even when a cheaper instance would suffice. |
| Antipattern | [Old generation](https://search-rug.github.io/iac-cost-patterns/old-generation/) | Using newer resource generations gives similar performance for lower cost. |
| Antipattern | [Expensive storage type](https://search-rug.github.io/iac-cost-patterns/expensive-storage-type/) | More expensive storage types are often used even when cheaper storage types would be sufficient. |
| Antipattern | [Expensive network resource](https://search-rug.github.io/iac-cost-patterns/expensive-network-resource/) | Network resources like NAT gateways, elastic IP addresses and subnets tend to be expensive while not being strictly needed. |
| Antipattern | [Overprovisioned resources](https://search-rug.github.io/iac-cost-patterns/overprovisioned-resources/) | Resources like RAM, storage and CPU utilization are often overprovisioned even when lower values are acceptable. |
| Antipattern | [AWS - Expensive DynamoDB](https://search-rug.github.io/iac-cost-patterns/aws-expensive-dynamodb/) | AWS DynamoDB tables often use features that carry cost but are not required,especially for infrequently accessed tables. |
| Antipattern | [Expensive monitoring](https://search-rug.github.io/iac-cost-patterns/expensive-monitoring/) | Monitoring solutions are expensive and might not be needed. |
