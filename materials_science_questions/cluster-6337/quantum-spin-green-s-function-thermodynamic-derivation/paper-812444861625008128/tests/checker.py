import os
import json
import csv

# === author imports / helpers ===
import csv
import math
from collections import defaultdict

# Pure Python numpy-compatible minimal interface for checker
class _Linalg:
    @staticmethod
    def lstsq(A, b, rcond=None):
        # A and b are _Array instances; convert to lists
        if hasattr(A, 'data'):
            A_list = A.data if isinstance(A.data[0], list) else A.data  # 2D list
        else:
            A_list = A
        if hasattr(b, 'data'):
            b_list = b.data
        else:
            b_list = b
        n = len(A_list)
        if n == 0:
            raise ValueError("Empty matrix")
        m = len(A_list[0])
        # compute C = A^T A
        C = [[0.0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                C[i][j] = sum(A_list[k][i] * A_list[k][j] for k in range(n))
        # compute d = A^T b
        d = [sum(A_list[k][i] * b_list[k] for k in range(n)) for i in range(m)]
        # solve C x = d via Gaussian elimination
        aug = [row[:] + [d[i]] for i, row in enumerate(C)]
        for col in range(m):
            pivot_row = max(range(col, m), key=lambda r: abs(aug[r][col]))
            if abs(aug[pivot_row][col]) < 1e-12:
                raise ValueError("Singular matrix")
            aug[col], aug[pivot_row] = aug[pivot_row], aug[col]
            piv = aug[col][col]
            for j in range(col, m + 1):
                aug[col][j] /= piv
            for r in range(m):
                if r != col:
                    factor = aug[r][col]
                    for j in range(col, m + 1):
                        aug[r][j] -= factor * aug[col][j]
        x = [aug[i][m] for i in range(m)]
        residual_val = math.sqrt(sum((sum(A_list[i][j] * x[j] for j in range(m)) - b_list[i]) ** 2 for i in range(n)))
        return x, [residual_val], m, [1.0] * m


class _Array:
    def __init__(self, data, shape=None):
        if isinstance(data, list) and data and isinstance(data[0], list):
            self.data = data
            self.shape = (len(data), len(data[0]))
        else:
            self.data = data
            self.shape = (len(data),) if data else (0,)

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            i, j = key
            if isinstance(j, slice) and j == slice(None):
                self.data[i] = list(value) if isinstance(value, _Array) else list(value)
            else:
                self.data[i] = value
        else:
            self.data[key] = value

    def __getitem__(self, key):
        if isinstance(key, tuple):
            i, j = key
            if j is None:  # np.newaxis
                if isinstance(self.data[0], list):
                    col = [[row[i]] for row in self.data]
                else:
                    col = [[self.data[i]] for i in range(len(self.data))]
                return _Array(col, (len(col), 1))
            elif isinstance(j, slice):
                return _Array([row[j] for row in self.data],
                              (len(self.data), len(range(*j.indices(len(self.data[0]))))))
            else:
                return self.data[i][j]
        else:
            if isinstance(key, slice):
                return _Array(self.data[key], (len(self.data),))
            else:
                return self.data[key]

    def __mul__(self, other):
        if isinstance(other, _Array):
            if len(self.shape) == 2 and len(other.shape) == 2 and other.shape[1] == 1:
                # broadcast (n,7)*(n,1)
                result = [[self.data[i][j] * other.data[i][0] for j in range(self.shape[1])] for i in range(self.shape[0])]
                return _Array(result, self.shape)
            elif len(self.shape) == 1 and len(other.shape) == 1:
                return _Array([a * b for a, b in zip(self.data, other.data)], self.shape)
            else:
                raise NotImplementedError
        else:
            # scalar
            return _Array([a * other for a in self.data], self.shape)

    def __rmul__(self, other):
        return self.__mul__(other)


class _NumpyLike:
    newaxis = None
    linalg = _Linalg()

    @staticmethod
    def zeros(shape):
        if isinstance(shape, int):
            return _Array([0.0] * shape, (shape,))
        rows, cols = shape
        return _Array([[0.0] * cols for _ in range(rows)], (rows, cols))

    @staticmethod
    def sqrt(arr):
        data = [math.sqrt(v) for v in (arr.data if isinstance(arr, _Array) else arr)]
        return _Array(data, (len(data),))

    @staticmethod
    def mean(arr):
        if isinstance(arr, _Array):
            lst = arr.data
        else:
            lst = list(arr)
        if not lst:
            return 0.0
        return sum(lst) / len(lst)


np = _NumpyLike()


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
    return {}


# === block: score_0 (check id='fit_score') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0

    # Group rows by blocking level
    levels = defaultdict(list)
    for row in artifact:
        try:
            lvl = int(row['level'])
            sigma_val = float(row['sigma'])
            if sigma_val <= 0:
                continue
            coeff = [float(row[f'J{i}_coeff']) for i in range(1,8)]
            xi = float(row['Xi'])
            levels[lvl].append((coeff, xi, sigma_val))
        except (KeyError, ValueError):
            continue

    if not levels:
        return 0.0

    gold_data = step.get('gold', {})
    tol_mult = float(step.get('tolerance_multiplier', 3.0))

    level_scores = []
    N_COUPLINGS = 7

    for lvl_str, rows in sorted(levels.items()):
        lvl_key = str(lvl_str)
        if lvl_key not in gold_data:
            continue
        gold = gold_data[lvl_key]
        gold_J = gold['J']
        gold_err = gold['err']

        n_rows = len(rows)
        if n_rows < N_COUPLINGS:
            # Not enough equations to fit
            level_scores.append(0.0)
            continue

        # Build design matrix and weight vector
        A = np.zeros((n_rows, N_COUPLINGS))
        b = np.zeros(n_rows)
        w = np.zeros(n_rows)
        for i, (coeff, xi, sigma_val) in enumerate(rows):
            A[i, :] = coeff
            b[i] = xi
            w[i] = 1.0 / (sigma_val * sigma_val)

        # Weighted least-squares
        w_sqrt = np.sqrt(w)
        Aw = A * w_sqrt[:, np.newaxis]
        bw = b * w_sqrt
        try:
            J, residuals, rank, s = np.linalg.lstsq(Aw, bw, rcond=None)
        except np.linalg.LinAlgError:
            level_scores.append(0.0)
            continue

        # Compare fitted J to gold
        coup_scores = []
        for i in range(N_COUPLINGS):
            diff = abs(J[i] - gold_J[i])
            tol = tol_mult * gold_err[i]
            if diff <= tol:
                coup_scores.append(1.0)
            else:
                # Linear decay beyond tolerance
                excess = diff - tol
                penalty = min(1.0, excess / tol)  # fraction of tolerance exceeded
                coup_scores.append(max(0.0, 1.0 - penalty))
        level_score = np.mean(coup_scores)
        level_scores.append(level_score)

    if not level_scores:
        return 0.0
    return float(np.mean(level_scores))


_SCORERS = {
    'fit_score': score_0,
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
