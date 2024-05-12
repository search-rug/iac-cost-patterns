import yaml

with open('../patterns.yml', 'r') as f:
    patterns = yaml.safe_load(f)

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
    occs = '\n'.join(f'- [{o}]({o})' for o in occurrences)

    with open(f'content/{name}.md', 'w') as f:
        f.write(f'''+++
title = "{ptype}: {name}"
weight = {i}

[extra]
description = "{description.replace('\n', ' ')}"
count = {len(occurrences)}
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
