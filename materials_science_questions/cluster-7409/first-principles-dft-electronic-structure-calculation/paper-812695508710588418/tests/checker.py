import os
import json
import csv

# === author imports / helpers ===
import math
import os


class _ndarray:
    """Minimal numpy.ndarray replacement for this checker."""
    def __init__(self, data):
        if isinstance(data, _ndarray):
            self._data = list(data._data)
        else:
            self._data = list(data)

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, idx):
        if isinstance(idx, list):
            return _ndarray([self._data[i] for i in idx])
        if isinstance(idx, slice):
            return _ndarray(self._data[idx])
        return self._data[idx]

    def __le__(self, other):
        if isinstance(other, (int, float)):
            return _ndarray([x <= other for x in self._data])
        return _ndarray([a <= b for a, b in zip(self._data, other._data)])

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return _ndarray([x >= other for x in self._data])
        return _ndarray([a >= b for a, b in zip(self._data, other._data)])

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return _ndarray([x < other for x in self._data])
        return _ndarray([a < b for a, b in zip(self._data, other._data)])

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return _ndarray([x > other for x in self._data])
        return _ndarray([a > b for a, b in zip(self._data, other._data)])

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return _ndarray([x == other for x in self._data])
        return _ndarray([a == b for a, b in zip(self._data, other._data)])

    def astype(self, dtype):
        if dtype == int:
            return _ndarray([int(x) for x in self._data])
        return _ndarray([dtype(x) for x in self._data])

    def tolist(self):
        return self._data


class _np:
    @staticmethod
    def array(data):
        return _ndarray(data)

    @staticmethod
    def max(a):
        return max(a)

    @staticmethod
    def argsort(a):
        return sorted(range(len(a)), key=lambda i: a[i])

    @staticmethod
    def diff(a):
        return [a[i+1] - a[i] for i in range(len(a)-1)]

    @staticmethod
    def concatenate(seq):
        out = []
        for item in seq:
            if isinstance(item, list):
                out.extend(item)
            elif isinstance(item, _ndarray):
                out.extend(item._data)
            else:
                out.append(item)
        return _ndarray(out)

    @staticmethod
    def where(cond):
        idxs = [i for i, c in enumerate(cond) if c]
        return (idxs,)

    @staticmethod
    def any(bools):
        return any(bools)


np = _np()


import os as _ff_os
import json as _ff_json


def _ff_validate_output_contract():
    """Return a list of shape violations against grading_spec['output_contract']."""
    spec_path = "/tests/grading_spec.json"
    if not _ff_os.path.exists(spec_path):
        return []
    with open(spec_path) as _f:
        _spec = _ff_json.load(_f)
    contract = _spec.get("output_contract", {}) or {}
    outputs = contract.get("outputs", []) or []
    out_dir = "/app/outputs"
    violations = []
    for out in outputs:
        base = str(out.get("file", "")).split("/")[-1]
        if not base:
            continue
        path = _ff_os.path.join(out_dir, base)
        if not _ff_os.path.isfile(path):
            violations.append("missing output_contract file: " + base)
            continue
        fmt = out.get("format", "")
        schema = out.get("schema", {}) or {}
        if fmt == "json":
            try:
                data = _ff_json.load(open(path))
            except Exception as exc:  # noqa: BLE001
                violations.append(base + ": invalid JSON (" + str(exc) + ")")
                continue
            required = schema.get("required", {})
            fields = required.keys() if isinstance(required, dict) else (required or [])
            if isinstance(data, dict):
                for field in fields:
                    if field not in data:
                        violations.append(base + ": missing JSON field '" + str(field) + "'")
        elif fmt in ("csv", "tsv"):
            import csv as _ff_csv
            delim = "\t" if fmt == "tsv" else ","
            try:
                with open(path, newline="") as _f:
                    cols = set((_ff_csv.reader(_f, delimiter=delim).__next__() or []))
            except StopIteration:
                cols = set()
            except Exception as exc:  # noqa: BLE001
                violations.append(base + ": cannot read table (" + str(exc) + ")")
                continue
            required_cols = schema.get("required_columns", []) or []
            for col in required_cols:
                name = col.get("name") if isinstance(col, dict) else col
                if name and name not in cols:
                    violations.append(base + ": missing table column '" + str(name) + "'")
    return violations


def _ff_contract_gate():
    """Zero the reward and exit if the submission violates the output_contract shape."""
    violations = _ff_validate_output_contract()
    if not violations:
        return
    _ff_os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as _f:
        _f.write("0.0")
    with open("/logs/verifier/breakdown.json", "w") as _f:
        _ff_json.dump({"output_contract_violations": violations}, _f, indent=2)
    raise SystemExit(0)


def load_artifact(path):
    if not path or not os.path.exists(path):
        return None
    if path.endswith(".json"):
        try:
            with open(path) as f:
                return json.load(f)
        except Exception:  # noqa: BLE001
            return None
    if path.endswith(".csv") or path.endswith(".tsv"):
        delim = "\t" if path.endswith(".tsv") else ","
        with open(path, newline="") as f:
            return list(csv.DictReader(f, delimiter=delim))
    with open(path) as f:
        return f.read()


def prepare(outputs_dir, spec):
    pdos_path = os.path.join(outputs_dir, "pdos_TiO2_101.dat")
    if not os.path.exists(pdos_path):
        return {"pdos_bandgap": None, "npoints": 0, "has_gap": False}
    energies = []
    total_dos = []
    try:
        with open(pdos_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split()
                if len(parts) < 2:
                    continue
                energies.append(float(parts[0]))
                total_dos.append(float(parts[1]))
    except Exception:
        return {"pdos_bandgap": None, "npoints": 0, "has_gap": False}
    if len(energies) < 10:
        return {"pdos_bandgap": None, "npoints": len(energies), "has_gap": False}
    energies = np.array(energies)
    total_dos = np.array(total_dos)
    npoints = len(energies)
    # sort by energy just in case
    sort_idx = np.argsort(energies)
    energies = energies[sort_idx]
    total_dos = total_dos[sort_idx]
    step_info = None
    for step in spec.get("steps", []):
        if step.get("output_file") == "pdos_TiO2_101.dat":
            step_info = step
            break
    threshold_factor = step_info.get("config", {}).get("dos_threshold_factor", 0.01) if step_info else 0.01
    max_dos = np.max(total_dos)
    if max_dos == 0:
        return {"pdos_bandgap": 0.0, "npoints": npoints, "has_gap": False}
    threshold = threshold_factor * max_dos
    below = total_dos <= threshold
    if not np.any(below):
        return {"pdos_bandgap": 0.0, "npoints": npoints, "has_gap": False}
    # wrap np.diff result in an _ndarray to ensure element-wise comparisons work
    edges = np.array(np.diff(np.concatenate(([0], below.astype(int), [0]))))
    # use list comprehensions instead of np.where to avoid TypeError with integer subtraction
    start_idxs = [i for i, e in enumerate(edges) if e == 1]
    end_idxs   = [i - 1 for i, e in enumerate(edges) if e == -1]
    best_width = 0.0
    best_block = None
    for si, ei in zip(start_idxs, end_idxs):
        if si > ei:
            continue
        w = energies[ei] - energies[si]
        if w > best_width:
            best_width = w
            best_block = (si, ei)
    if best_block is None or best_width < 0.1:
        return {"pdos_bandgap": 0.0, "npoints": npoints, "has_gap": False}
    return {"pdos_bandgap": float(best_width), "npoints": npoints, "has_gap": True}


# === block: score_0 (check id='step_03_pdos') ===
def score_0(artifact, step, ctx):
    target_bandgap = step.get("config", {}).get("target_bandgap", 1.0)
    tolerance = step.get("config", {}).get("tolerance", 0.2)
    min_points = step.get("config", {}).get("min_points", 500)
    pdos_bandgap = ctx.get("pdos_bandgap")
    npoints = ctx.get("npoints", 0)
    has_gap = ctx.get("has_gap", False)
    if pdos_bandgap is None or not has_gap:
        return 0.0
    dev = abs(pdos_bandgap - target_bandgap)
    if dev <= tolerance:
        gap_score = 1.0
    else:
        gap_score = max(0.0, 1.0 - (dev - tolerance) / 0.3)
    points_score = 1.0 if npoints >= min_points else 0.0
    return gap_score * 0.9 + points_score * 0.1


# === block: score_1 (check id='step_04_bandgap') ===
def score_1(artifact, step, ctx):
    consistency_tol = step.get("config", {}).get("consistency_tolerance", 0.05)
    pdos_bandgap = ctx.get("pdos_bandgap")
    if pdos_bandgap is None:
        return 0.0
    try:
        txt_bandgap = None
        for line in artifact.splitlines():
            line = line.strip()
            if line and not line.startswith('#'):
                txt_bandgap = float(line.split()[0])
                break
        if txt_bandgap is None:
            return 0.0
    except Exception:
        return 0.0
    if abs(txt_bandgap - pdos_bandgap) <= consistency_tol:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step_03_pdos': score_0,
    'step_04_bandgap': score_1,
}


def _step_id(step, index):
    sid = str(step.get("id", "")).strip()
    if sid:
        return sid
    output = str(step.get("output_file", "")).split("/")[-1].rsplit(".", 1)[0]
    kind = str(step.get("kind") or step.get("metric") or "score").strip()
    base = "_".join(part for part in (output, kind) if part).strip("_")
    return base or ("check_" + str(index))


def main():
    _ff_contract_gate()
    with open("/tests/grading_spec.json") as f:
        spec = json.load(f)
    outputs_dir = "/app/outputs"
    ctx = prepare(outputs_dir, spec)
    steps = spec.get("steps", spec.get("checks", [])) or []
    breakdown = {}
    total = 0.0
    for index, step in enumerate(steps):
        sid = _step_id(step, index)
        output_file = str(step.get("output_file", "")).split("/")[-1]
        weight = float(step.get("weight", 0.0))
        artifact = load_artifact(os.path.join(outputs_dir, output_file)) if output_file else None
        fn = _SCORERS.get(sid)
        if fn is None:
            score = 0.0
        else:
            try:
                score = float(fn(artifact, step, ctx))
            except Exception as exc:  # noqa: BLE001
                score = 0.0
                breakdown.setdefault("_errors", {})[sid] = repr(exc)
        score = max(0.0, min(1.0, score))
        breakdown[sid or output_file] = {"score": score, "weight": weight}
        total += score * weight
    os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as f:
        f.write(str(round(total, 6)))
    with open("/logs/verifier/breakdown.json", "w") as f:
        json.dump(breakdown, f, indent=2)


if __name__ == "__main__":
    main()
