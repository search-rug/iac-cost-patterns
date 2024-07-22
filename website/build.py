import yaml

with open('../thematic-analysis/patterns.yml', 'r') as f:
    patterns = yaml.safe_load(f)

TECHNOLOGIES = {
    'terraform': 'Terraform',
    'aws cloudformation': 'AWS CloudFormation',
}

for i, p in enumerate(patterns):
    name = p['name']
    ptype = p['patternType'].capitalize()
    description = p['description']
    context = p['context']
    solution = p['solution']
    example = p['example']
    references = p['references']
    occurrences = p['occurrences']

    refs = '\n'.join(f'- [{r["title"]}]({r["url"]})' for r in references)
    occs = ''
    for technology, urls in occurrences.items():
        occs += f'\n### {TECHNOLOGIES[technology]}\n'
        occs += '\n'.join(f'- [{url}]({url})' for url in urls)

    count = sum(len(o) for o in occurrences.values())
    technologies = str(sorted(occurrences.keys())).replace("'", '"')

    with open(f'content/{name}.md', 'w') as f:
        f.write(f'''+++
title = "{ptype}: {name}"
weight = {i}

[extra]
description = "{description.replace('\n', ' ')}"
count = {count}
technologies = {technologies}
+++

# {ptype}: {name}
{description}

## Context
{context}

## Solution
{solution}

## Example
{example}

## References
{refs}

## Occurrences
{occs}
''')
