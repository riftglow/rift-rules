#!/usr/bin/env python3
"""Union MetaCubeX cn + SagerNet cn + sources/cn-extra.txt -> merged rule-set JSON (v2)."""
import json, sys

def domains(path):
    d = json.load(open(path))
    out = set()
    for r in d.get("rules", []):
        out.update(r.get("domain_suffix", []))
        out.update(r.get("domain", []))
    return out

def regexes(path):
    d = json.load(open(path))
    out = set()
    for r in d.get("rules", []):
        out.update(r.get("domain_regex", []))
    return out

meta = domains("meta-cn.json")
sager = domains("sager-cn.json")
merged = meta | sager
extra = set()
for line in open("sources/cn-extra.txt", encoding="utf-8"):
    line = line.strip()
    if line and not line.startswith("#"):
        extra.add(line.lower())
merged |= extra
rules = [{"domain_suffix": sorted(merged)}]
rx = regexes("sager-cn.json")
if rx:
    rules.append({"domain_regex": sorted(rx)})
json.dump({"version": 2, "rules": rules}, open("rift-cn.json", "w"))
print(f"meta={len(meta)} sager={len(sager)} extra={len(extra)} merged={len(merged)} regex={len(rx)}")
