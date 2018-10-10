set-sg-desc (set security group descriptions)
====

# What's this?
https://docs.aws.amazon.com/cli/latest/reference/ec2/update-security-group-rule-descriptions-ingress.html

- input: text file (cidr & description)
- output: SG-IPPermision's Descriptions
- how?: simply, this tool update __all__ descriptions, that same input-file's ciders.

This tool ___DO NOT___ modify SecurityGroup itself. So, you should create sg via any other tools (piculet / terraform)

# input file
```
"10.10.10.10/32"  #test site A
"11.10.10.10/32"  #test site B
```

# dry-run & apply

dry-run
`docker-compose run --rm set-sg-desc.py --dry-run < sample-list`

apply
`docker-compose run --rm set-sg-desc.py < sample-list`
