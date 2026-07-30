#!/usr/bin/env python3
"""Atomic claim/complete queue for parallel QA subagents.

Serializes state mutations with fcntl.flock on a single lock file so no two
agents ever claim the same package. Corpus-agnostic: reads paths from env.

Env:
  QA_ROOT   work/output root (default: /personal/qa_review)
            expects QA_ROOT/corpus_manifest.json  ({"packages": [<pkg-id>, ...]})
            state lives under QA_ROOT/state/
Commands:
  claim   <agent_id> <count>  -> print newline-separated package ids claimed
  done    <pkg>               -> mark complete (also releases the claim)
  release <pkg>               -> release a claim without marking done (on failure)
  status                      -> print counts as JSON
  reap                        -> force-reap stale (>STALE_SEC) unfinished claims
"""
import fcntl, json, os, subprocess, sys, time

ROOT = os.environ.get("QA_ROOT", "/personal/qa_review")
STATE = os.path.join(ROOT, "state")
LOCK = os.path.join(STATE, "queue.lock")
ASSIGNED = os.path.join(STATE, "assigned.json")
DONE = os.path.join(STATE, "done.json")
MANIFEST = os.path.join(ROOT, "corpus_manifest.json")
STALE_SEC = int(os.environ.get("QA_STALE_SEC", "7200"))  # reap unfinished claims older than this


def _load(path):
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        return json.load(f)


def _save(path, obj):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(obj, f)
    os.replace(tmp, path)


def _manifest():
    with open(MANIFEST) as f:
        return json.load(f)["packages"]


class Locked:
    def __enter__(self):
        os.makedirs(STATE, exist_ok=True)
        self.fh = open(LOCK, "w")
        fcntl.flock(self.fh, fcntl.LOCK_EX)
        return self

    def __exit__(self, *a):
        fcntl.flock(self.fh, fcntl.LOCK_UN)
        self.fh.close()


def _is_done_marker(pkg):
    return os.path.exists(os.path.join(ROOT, pkg, ".done"))


def claim(agent_id, count):
    with Locked():
        pkgs = _manifest()
        assigned = _load(ASSIGNED)
        done = _load(DONE)
        now = time.time()
        for k in list(assigned):  # reap stale unfinished claims
            if now - assigned[k]["ts"] > STALE_SEC and k not in done:
                del assigned[k]
        picked = []
        for p in pkgs:
            if len(picked) >= count:
                break
            if p in done or _is_done_marker(p):
                done.setdefault(p, {"ts": now})
                continue
            if p in assigned:
                continue
            assigned[p] = {"agent": agent_id, "ts": now}
            picked.append(p)
        _save(ASSIGNED, assigned)
        _save(DONE, done)
    print("\n".join(picked))


def done(pkg):
    lifecycle = os.path.join(os.path.dirname(__file__), "validate_lifecycle.py")
    subprocess.run([sys.executable, lifecycle, pkg], check=True)
    with Locked():
        marker = os.path.join(ROOT, pkg, ".done")
        os.makedirs(os.path.dirname(marker), exist_ok=True)
        with open(marker, "w"):
            pass
        d = _load(DONE); d[pkg] = {"ts": time.time()}; _save(DONE, d)
        a = _load(ASSIGNED); a.pop(pkg, None); _save(ASSIGNED, a)
    print("ok")


def release(pkg):
    with Locked():
        a = _load(ASSIGNED); a.pop(pkg, None); _save(ASSIGNED, a)
    print("released")


def status():
    with Locked():
        pkgs = _manifest(); assigned = _load(ASSIGNED); done = _load(DONE)
    total = len(pkgs)
    ndone = sum(1 for p in pkgs if p in done or _is_done_marker(p))
    print(json.dumps({"total": total, "done": ndone,
                      "assigned_open": len([k for k in assigned if k not in done]),
                      "remaining": total - ndone}))


def reap():
    with Locked():
        a = _load(ASSIGNED); d = _load(DONE); now = time.time(); n = 0
        for k in list(a):
            if k not in d and not _is_done_marker(k) and now - a[k]["ts"] > STALE_SEC:
                del a[k]; n += 1
        _save(ASSIGNED, a)
    print(f"reaped {n}")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "claim":
        claim(sys.argv[2], int(sys.argv[3]))
    elif cmd == "done":
        done(sys.argv[2])
    elif cmd == "release":
        release(sys.argv[2])
    elif cmd == "status":
        status()
    elif cmd == "reap":
        reap()
    else:
        sys.exit("unknown command: " + cmd)
