import json, math, os, sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
DIMS = ["C01","C02","C03","C04","C05","C06","C07"]
man = json.load(open(os.path.join(ROOT, "identity_manifest_100.json")))
IDS = man["package_ids"]

def finite(x):
    return isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x)

_WORDS = {1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten"}
def _num(n):
    return _WORDS.get(n, str(n))

def side_candidates(d, side):
    """Return candidate root objects that may hold this side's disposition/total/dims."""
    cands = []
    if isinstance(d.get(side), dict):
        cands.append(d[side])
    v = d.get('variants')
    if isinstance(v, dict) and isinstance(v.get(side), dict):
        cands.append(v[side])
    s = d.get('sides')
    if isinstance(s, dict) and isinstance(s.get(side), dict):
        cands.append(s[side])
        if isinstance(s[side].get('disposition'), dict):
            cands.append(s[side]['disposition'])
    p = d.get('pairs')
    if isinstance(p, dict) and isinstance(p.get(side), dict):
        cands.append(p[side])
    return cands

def get_disposition(d, side, cands):
    for root in cands:
        disp = root.get('disposition')
        if isinstance(disp, dict):
            disp = disp.get('disposition')
        if disp is None:
            disp = root.get('review_verdict') or root.get('verdict')
        if disp:
            return disp
    if isinstance(d.get('dispositions'), dict):
        return d['dispositions'].get(side)
    return None

def get_total(cands):
    for root in cands:
        t = root.get('total_score')
        if finite(t):
            return t
        for holder in ('totals', 'summary'):
            h = root.get(holder)
            if isinstance(h, dict):
                for k in ('total_score', 'authoritative_total_score'):
                    if finite(h.get(k)):
                        return h.get(k)
    return None

def _norm_earn(e):
    norm = e.get('normalized_score', e.get('normalized'))
    earn = e.get('earned_points', e.get('points_earned', e.get('earned')))
    return norm, earn

def _dims_from(root):
    out = {}
    byc = root.get('dimensions_v11_by_code')
    if isinstance(byc, dict) and byc:
        for c, e in byc.items():
            if isinstance(e, dict):
                out[c] = _norm_earn(e)
        return out
    dv = root.get('dimensions_v11')
    if dv is None:
        dv = root.get('dimensions')
    if dv is None:
        for k in root:
            if k.lower() == 'c01_c07':
                dv = root[k]; break
    if isinstance(dv, list):
        for e in dv:
            if isinstance(e, dict):
                out[e.get('dimension')] = _norm_earn(e)
    elif isinstance(dv, dict):
        for c, e in dv.items():
            if isinstance(e, dict):
                out[c] = _norm_earn(e)
    return {k: v for k, v in out.items() if k in DIMS}

def get_dims(cands):
    best = {}
    for root in cands:
        cur = _dims_from(root)
        finite_ct = sum(1 for c in cur if finite(cur[c][0]))
        best_ct = sum(1 for c in best if finite(best[c][0]))
        if finite_ct > best_ct:
            best = cur
    return best

records = {}
for idn in IDS:
    d = json.load(open(os.path.join(ROOT, "packages", idn, "pair_result.json")))
    rec = {"schema_version": d.get("schema_version"), "operation": d.get("operation") or "UNSPECIFIED"}
    for side in ("original", "repaired"):
        cands = side_candidates(d, side)
        rec[side] = {
            "disposition": get_disposition(d, side, cands),
            "total": get_total(cands),
            "dims": get_dims(cands),
        }
    records[idn] = rec

def mean(vals):
    return sum(vals)/len(vals) if vals else None

# dimension averages
def dim_avgs(side):
    out = {}
    for c in DIMS:
        norms = [records[i][side]["dims"].get(c,(None,None))[0] for i in IDS]
        earns = [records[i][side]["dims"].get(c,(None,None))[1] for i in IDS]
        nf = [v for v in norms if finite(v)]
        ef = [v for v in earns if finite(v)]
        out[c] = {
            "normalized": {"mean": round(mean(nf),10) if nf else None, "N": len(nf)},
            "earned_points": {"mean": round(mean(ef),10) if ef else None, "N": len(ef)},
        }
    return out

def dispositions(side):
    c = Counter(records[i][side]["disposition"] for i in IDS)
    counts = {k: c.get(k,0) for k in ["PASS","CONDITIONAL","REJECT","NOT_ASSESSABLE"]}
    strict = counts["PASS"]/100
    assessable_denom = counts["PASS"]+counts["CONDITIONAL"]+counts["REJECT"]
    ar = counts["PASS"]/assessable_denom if assessable_denom else 0
    return {
        "counts": counts,
        "strict_PASS": {"count": counts["PASS"], "denominator": 100, "rate": round(strict,10), "rate_percent": round(strict*100,8)},
        "assessable_PASS_excluding_NOT_ASSESSABLE": {"count": counts["PASS"], "denominator": assessable_denom, "rate": round(ar,10), "rate_percent": round(ar*100,8)},
    }

def total_scores(side):
    vals = [records[i][side]["total"] for i in IDS if finite(records[i][side]["total"])]
    return {"mean": round(mean(vals),10) if vals else None, "N": len(vals), "excluded_N": 100-len(vals)}

def dim_changes():
    out = {}
    for c in DIMS:
        blk = {}
        for kind, idx in (("normalized",0),("earned_points",1)):
            changes=[]; rels=[]; zero=0
            for i in IDS:
                o = records[i]["original"]["dims"].get(c,(None,None))[idx]
                r = records[i]["repaired"]["dims"].get(c,(None,None))[idx]
                if finite(o) and finite(r):
                    changes.append(r-o)
                    if o != 0:
                        rels.append(100*(r-o)/o)
                    else:
                        zero += 1
            vpn = len(changes)
            blk[kind] = {
                "mean_change": round(mean(changes),10) if changes else 0.0,
                "mean_absolute_change": round(mean([abs(x) for x in changes]),10) if changes else 0.0,
                "mean_relative_percent_change": round(mean(rels),10) if rels else 0.0,
                "valid_paired_N": vpn,
                "relative_valid_N": len(rels),
                "relative_zero_baseline_N": zero,
                "excluded_paired_N": 100-vpn,
            }
        out[c]=blk
    return out

def total_paired():
    changes=[]; rels=[]; zero=0; inc=dec=unc=0
    for i in IDS:
        o=records[i]["original"]["total"]; r=records[i]["repaired"]["total"]
        if finite(o) and finite(r):
            ch=r-o; changes.append(ch)
            if ch>0: inc+=1
            elif ch<0: dec+=1
            else: unc+=1
            if o!=0: rels.append(100*(r-o)/o)
            else: zero+=1
    vpn=len(changes)
    return {
        "mean_change": round(mean(changes),10) if changes else 0.0,
        "mean_absolute_change": round(mean([abs(x) for x in changes]),10) if changes else 0.0,
        "mean_relative_percent_change": round(mean(rels),10) if rels else 0.0,
        "valid_paired_N": vpn, "relative_valid_N": len(rels),
        "relative_zero_baseline_N": zero, "excluded_paired_N": 100-vpn,
        "change_counts": {"increased": inc, "decreased": dec, "unchanged": unc},
    }

def transition():
    m = {a:{b:0 for b in ["PASS","CONDITIONAL","REJECT","NOT_ASSESSABLE"]} for a in ["PASS","CONDITIONAL","REJECT","NOT_ASSESSABLE"]}
    for i in IDS:
        o=records[i]["original"]["disposition"]; r=records[i]["repaired"]["disposition"]
        if o in m and r in m[o]: m[o][r]+=1
    return m

def detect_malformed():
    out = []
    for i in IDS:
        r = records[i]["repaired"]
        disp = r["disposition"]
        if disp in ("PASS", "CONDITIONAL", "REJECT") and not finite(r["total"]):
            dims = r["dims"]
            missing = [c for c in ("C01","C03","C04") if not finite(dims.get(c,(None,None))[0])]
            issues = ["total_score is missing for an assessable disposition"]
            if missing:
                issues.append("C01, C03, and C04 earned and normalized values are missing while those dimensions are marked NOT_ASSESSABLE")
            out.append({"identity": i, "side": "repaired", "disposition": disp, "issues": issues})
    return out

def missing_na(side):
    out = {}
    for c in DIMS:
        N = sum(1 for i in IDS if finite(records[i][side]["dims"].get(c,(None,None))[0]))
        if N < 100:
            out[c] = {"identity_count": 100 - N, "normalized_N": N, "earned_points_N": N}
    return out

result = {
    "dispositions": {"original": dispositions("original"), "repaired": dispositions("repaired")},
    "dimension_averages": {"original": dim_avgs("original"), "repaired": dim_avgs("repaired")},
    "dimension_changes_repaired_minus_original": dim_changes(),
    "total_scores": {"original": total_scores("original"), "repaired": total_scores("repaired"), "paired_comparison": total_paired()},
    "disposition_transition_matrix": transition(),
    "operation_counts": dict(Counter(records[i]["operation"] for i in IDS)),
    "schema_versions": dict(Counter(records[i]["schema_version"] for i in IDS)),
    "_malformed": detect_malformed(),
    "_missing_na": {"original": missing_na("original"), "repaired": missing_na("repaired")},
}

stale = json.load(open(os.path.join(ROOT, "summary_100.json")))

# ---- Assemble the COMPLETE new summary from stale template + recomputed fields ----
new = json.loads(json.dumps(stale))  # deep copy, preserves static parts + key order
new["dispositions"] = result["dispositions"]
new["dimension_averages"] = result["dimension_averages"]
new["dimension_changes_repaired_minus_original"] = result["dimension_changes_repaired_minus_original"]
new["total_scores"] = result["total_scores"]
new["disposition_transition_matrix"] = result["disposition_transition_matrix"]
new["operation_counts"] = result["operation_counts"]
new["schema_versions"] = result["schema_versions"]

# integrity: malformed list + missing/NA
mal = result["_malformed"]
new["integrity"]["malformed_or_inconsistent_result_count"] = len(mal)
new["integrity"]["malformed_or_inconsistent_results"] = mal
mna = {}
for side in ("original", "repaired"):
    side_out = {}
    for c, v in result["_missing_na"][side].items():
        na_count = sum(1 for i in IDS if records[i][side]["disposition"] == "NOT_ASSESSABLE"
                       and not finite(records[i][side]["dims"].get(c,(None,None))[0]))
        mal_ids = {m["identity"] for m in mal}
        mal_count = sum(1 for i in IDS if i in mal_ids
                        and not finite(records[i][side]["dims"].get(c,(None,None))[0]))
        if side == "original":
            cls = "All seven are disposition NOT_ASSESSABLE." if na_count == v["identity_count"] else f"{na_count} are disposition NOT_ASSESSABLE."
        else:
            if na_count == 0:
                cls = ("It is the single inconsistent repaired REJECT result listed below." if mal_count == 1
                       else "They are the inconsistent repaired REJECT results listed below.")
            else:
                one = "one belongs" if mal_count == 1 else f"{mal_count} belong"
                cls = f"{_num(na_count)} are disposition NOT_ASSESSABLE; {one} to the inconsistent repaired REJECT result{'s' if mal_count!=1 else ''} listed below."
        v = dict(v); v["classification"] = cls
        side_out[c] = v
    mna[side] = side_out
new["integrity"]["missing_or_not_assessable_dimension_values"] = mna

json.dump(new, open(os.path.join(ROOT, "_regen_full.json"), "w"), indent=2)

# ---- leaf diff vs stale ----
def leaves(o, pre=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from leaves(v, pre + "/" + str(k))
    elif isinstance(o, list):
        yield pre, json.dumps(o, sort_keys=True)
    else:
        yield pre, o
sl = dict(leaves(stale)); nl = dict(leaves(new))
print("### VALIDATION: original side must match (all OK) ###")
for c in DIMS:
    a = new["dimension_averages"]["original"][c]["normalized"]; b = stale["dimension_averages"]["original"][c]["normalized"]
    print(f"  O {c}: {'OK' if a==b else 'DIFF %s vs %s'%(a,b)}")
print("\n### CHANGED LEAVES (new vs stale) ###")
allk = sorted(set(sl) | set(nl))
for k in allk:
    if sl.get(k) != nl.get(k):
        print(f"  {k}\n      stale={sl.get(k)!r}\n      new  ={nl.get(k)!r}")
