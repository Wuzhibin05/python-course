#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2021/5/24
import json
import sys
input = sys.stdin.read()
result = [x["snapshot"]
for x in json.loads(input)["snapshots"]]
    print("\n".join(result[:-60]));

