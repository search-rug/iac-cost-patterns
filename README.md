[![DOI](https://zenodo.org/badge/795400974.svg)](https://doi.org/10.5281/zenodo.14501829)

# IaC Cost Patterns

This is a collection of patterns and antipatterns that support managing cost in Infrastructure as Code artifacts of cloud software deployments. It is intended to be a living catalog, open to community contributions.

The catalog is available at [search-rug.github.io/iac-cost-patterns](https://search-rug.github.io/iac-cost-patterns/) and is based on the [`patterns.yml`](./thematic-analysis/patterns.yml) file in this repository. The catalog includes references and occurrences in commits.

## Catalog

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

## Complete Dataset

The patterns and antipatterns were discovered through thematic analyses, as documented under [Dataset History](#dataset-history). The dataset (in its most recent version) is available in the [thematic-analysis](./thematic-analysis) directory and consists of:
* [`patterns.yml`](./thematic-analysis/patterns.yml) - The final set of patterns and antipatterns.
* [`codes.yml`](./thematic-analysis/codes.yml) - The complete set of codes used in the analysis.
* [`indicators.yml`](./thematic-analysis/indicators.yml) - The complete set of analyzed commits.

![IaC Cost Patterns](./thematic-analysis/data-model.png?raw=true)

## Dataset History

### v1.0 - May 2024

The first set of patterns was extracted using Thematic Analysis on 499 cost-related commits that modify [Terraform](https://www.terraform.io/) IaC files from 403 repositories. The set included commits up to 2022 and were collected as part of [a prior study](https://arxiv.org/abs/2304.07531).

During the analysis, 128 codes were defined. One code is used to document *"no cost change"*, while the remaining 127 codes indicate cost-saving or cost-increasing actions. Of the 499 commits, 342 contained at least one cost-related code, while 179 were coded with *"no cost change"*.

After validation, 50 codes were integrated into 3 and 7 themes representing patterns and antipatterns respectively, while the remaining 67 codes were discarded due to lack of occurrences. In total, 237 out of 342 commits contain at least one occurrence of an (anti)pattern. The dataset did not include the commits that were coded with *"no cost change"* (fixed in [v2.0](#v20---july-2024)).

### v1.1 - July 2024

The set of analyzed Terraform commits was updated to include commits up to June 2024 from the previously analyzed repositories. As a result, 23 new commits (from 15 repositories) were identified as containing codes indicating cost-saving or cost-increasing actions. The new commits were analyzed using the same set of codes and themes as in [v1.0](#v10---may-2024). No new codes were necessary, and no new (anti)patterns were identified.

### v2.0 - July 2024

The dataset and its format were updated to include more details, allowing to document commits that were coded with *"no cost change"*, and to specify the IaC tool used in the commits. The main changes comprise: (a) addition of [`codes.yml`](./thematic-analysis/codes.yml), containing the documentation of defined codes; (b) addition of [`indicators.yml`](./thematic-analysis/indicators.yml), containing the documentation of all analyzed commits (incl. coded with *"no cost change"*); and (c) revision of [`patterns.yml`](./thematic-analysis/patterns.yml), to also specify the IaC technology of the commits (under occurrences).

### v2.1 - July 2024

Thematic analysis was applied to a dataset of commits involving a different IaC tool. In total, 262 commits that modify [AWS CloudFormation](https://aws.amazon.com/cloudformation/) files and discuss cost considerations in their messages were collected. First, the original 128 codes were used to describe the code changes in the commits. We identified the cost-related codes 104 times in 93 commits from 86 repositories, while 56 commits from 47 repositories were coded *"no cost change"*.

Next, due to changes not observed for Terraform, we defined 98 new codes, assigned to 133 commits from 109 repositories. Based on the codes, we further attempted to match each new commit with one of the ten Terraform (anti)patterns. If none were appropriate, we grouped the commits based on similarities. This processes resulted in the identification of two new patterns: [Cost report](https://search-rug.github.io/iac-cost-patterns/cost-report/) and [Preventative Template](https://search-rug.github.io/iac-cost-patterns/preventative-template/).

## Licenses

The software in this repository is licensed under the [MIT License](LICENSE).

The data compiled in this repository is licensed under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0) License.
