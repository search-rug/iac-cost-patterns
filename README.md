# IaC Cost Patterns

This is a collection of patterns and antipatterns that support managing cost in Infrastructure as Code artifacts of cloud software deployments. It is intended to be a living catalog, open to community contributions.

[`patterns.yml`](./thematic-analysis/patterns.yml) is the pattern dataset, including references and occurrences in commits.

## Context

The original set of patterns was extracted using Thematic Analysis on 499 cost-related commits from 403 repositories. These commits were collected as part of [a prior study](https://arxiv.org/abs/2304.07531).

During our analysis, we found 128 codes including one for "no related changes identified", with the remaining 127 codes indicating cost-saving or cost-increasing actions. Of the 499 commits, 342 contained at least one cost-related code, while 179 were coded "no related changes identified".

After validation, 50 codes were integrated into 3 and 7 themes representing patterns and antipatterns respectively, while the remaining 67 codes were discarded due to lack of occurrences. In total, 237 out of 342 commits contain at least one occurrence of an (anti)pattern.

Furthermore, we expanded the methodology previously used in the context of Terraform for a different IaC tool. We collected 262 commits that use AWS CloudFormation and discuss cost considerations in their messages. Next, we applied Thematic Analysis and first attempted to assign one or more of the predecessor 128 codes to describe the code changes in the commits. We identified the cost-related codes 104 times in 93 commits from 86 repositories, while 56 commits from 47 repositories were coded "no related changes identified".

For the AWS CloudFormation changes not observed for Terraform, we defined 98 new codes corresponding to 133 commits from 109 repositories. Based on the codes, we further attempted to match each new commit with one of the ten Terraform (anti)patterns. If none were appropriate, we grouped the commits based on similarities and identified two new patterns: the Cost Report and the Preventative Template.

## Patterns

| Type | Name | Description |
| --- | --- | --- |
| Pattern | [Budget](https://search-rug.github.io/iac-cost-patterns/budget/) | Use budgets to receive alerts about charged and forecasted costs and control spending. |
| Pattern | [Spot instances](https://search-rug.github.io/iac-cost-patterns/spot-instances/) | Use spot instances to run interruptible workloads for significant cost savings compared to regular instances. |
| Pattern | [Object storage lifecycle rules](https://search-rug.github.io/iac-cost-patterns/object-storage-lifecycle-rules/) | Define lifecycle rules for object storage to move objects to cheaper storage or drop them entirely. |
| Pattern     | [Cost report](https://search-rug.github.io/iac-cost-patterns/cost-report/)                                       | Cost report elements can be used to obtain information on the actual spendings over a period of time.                            |
| Pattern     | [Preventative Template](https://search-rug.github.io/iac-cost-patterns/preventative-template/)                   | Templates with predefined configurations that enforce cost-optimizing methods can proactively manage and reduce future expenses. |
| Antipattern | [Expensive instance](https://search-rug.github.io/iac-cost-patterns/expensive-instance/) | Compute instances are often overprovisioned even when a cheaper instance would suffice. |
| Antipattern | [Old generation](https://search-rug.github.io/iac-cost-patterns/old-generation/) | Using newer resource generations gives similar performance for lower cost. |
| Antipattern | [Expensive storage type](https://search-rug.github.io/iac-cost-patterns/expensive-storage-type/) | More expensive storage types are often used even when cheaper storage types would be sufficient. |
| Antipattern | [Expensive network resource](https://search-rug.github.io/iac-cost-patterns/expensive-network-resource/) | Network resources like NAT gateways, elastic IP addresses and subnets tend to be expensive while not being strictly needed. |
| Antipattern | [Overprovisioned resources](https://search-rug.github.io/iac-cost-patterns/overprovisioned-resources/) | Resources like RAM, storage and CPU utilization are often overprovisioned even when lower values are acceptable. |
| Antipattern | [AWS - Expensive DynamoDB](https://search-rug.github.io/iac-cost-patterns/aws-expensive-dynamodb/) | AWS DynamoDB tables often use features that carry cost but are not required,especially for infrequently accessed tables. |
| Antipattern | [Expensive monitoring](https://search-rug.github.io/iac-cost-patterns/expensive-monitoring/) | Monitoring solutions are expensive and might not be needed. |