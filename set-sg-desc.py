#!/usr/bin/env python
# -*- coding: utf-8 -*-
import boto3
import pprint
import sys
import re


iplist = {}
ec2 = boto3.client('ec2')
dryrun = False

def _update_sg_desc(sgid, ipp):
    change = False
    new_iprs = []
    for c in ipp['IpRanges']:
        if c['CidrIp'] in iplist.keys():
            c['Description'] = iplist[c['CidrIp']]
            new_iprs.append(c)
            change = True

    if change:
        new_ipp = {}
        new_ipp['IpProtocol'] = ipp['IpProtocol']
        new_ipp['FromPort'] = ipp['FromPort']
        new_ipp['ToPort'] = ipp['ToPort']
        new_ipp['IpRanges'] = new_iprs
        if not dryrun:
            ec2.update_security_group_rule_descriptions_ingress(
                GroupId=sgid,
                IpPermissions=[new_ipp]
                )
        print new_ipp


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("-n", "--dry-run"):
        dryrun = True

    # create iplist from Groupfile
    pattern = re.compile(r'"([\d.]+/\d+)"[,]?\s*\#(.+)')
    for line in sys.stdin:
        m = re.search(pattern, line)
        if m:
            iplist[m.group(1)] = m.group(2)

    paginator = ec2.get_paginator('describe_security_groups')
    page_iterator = paginator.paginate()
    for page in page_iterator:
        for sg in page['SecurityGroups']:
            for ipp in sg['IpPermissions']:
                _update_sg_desc(sg['GroupId'],ipp)

if __name__ == '__main__':
    main()
