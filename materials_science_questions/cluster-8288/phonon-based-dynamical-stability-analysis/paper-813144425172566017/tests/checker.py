import os
import json
import csv

# === author imports / helpers ===
import json, math, os, itertools
import numpy as np


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
    def prepare(outputs_dir, spec):
        c_path = os.path.join(outputs_dir, 'step_01_elastic_constants.json')
        c_data = None
        if os.path.exists(c_path):
            with open(c_path) as f:
                c_data = json.load(f)
        steps = {s['id']: s for s in spec.get('steps', [])}
        return {'c_data': c_data, 'steps': steps}


# === block: score_0 (check id='step_01_elastic') ===
def score_0(artifact, step, ctx):
        gold_list = step.get('gold_data', [])
        if not gold_list:
            return 1.0
        if artifact is None or not isinstance(artifact, list):
            return 0.0
        rel_tol = step.get('rel_tol', 0.10)
        fields = ['C11','C12','C13','C33','C44','C66']
        artifact_by_compound = {}
        for item in artifact:
            if not isinstance(item, dict):
                continue
            comp = item.get('compound')
            if comp:
                artifact_by_compound[comp] = item
        ok = 0
        total = len(gold_list)
        for gold in gold_list:
            comp = gold['compound']
            item = artifact_by_compound.get(comp)
            if item is None:
                continue
            all_ok = True
            for fld in fields:
                val = item.get(fld)
                gv = gold.get(fld)
                if val is None or gv is None:
                    all_ok = False
                    break
                if gv == 0:
                    if abs(val) > 1e-9:
                        all_ok = False
                        break
                else:
                    if abs(val - gv) > rel_tol * abs(gv):
                        all_ok = False
                        break
            if all_ok:
                ok += 1
        return ok / max(total, 1)


# === block: score_1 (check id='step_02_phonon') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        stable = artifact.get('stable')
        freq = artifact.get('min_squared_frequency')
        if stable is True and isinstance(freq, (int, float)) and freq >= 0:
            return 1.0
        return 0.0


# === block: score_2 (check id='step_03_poly') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        c_data = ctx.get('c_data')
        if not c_data:
            return 0.0
        tol = step.get('consistency_tol', 0.005)
        # Build C matrices
        from numpy.linalg import inv
        idx_map = {'BeSiP2':0,'MgSiP2':1,'ZnSiP2':2,'CdSiP2':3,'HgSiP2':4}
        # standard Voigt order: xx,yy,zz,yz,xz,xy
        compounds = []
        for item in c_data:
            comp = item.get('compound')
            C11 = item.get('C11'); C12 = item.get('C12'); C13 = item.get('C13')
            C33 = item.get('C33'); C44 = item.get('C44'); C66 = item.get('C66')
            if None in (C11,C12,C13,C33,C44,C66) or comp is None:
                continue
            compounds.append((comp, (C11, C12, C13, C33, C44, C66)))
        if not compounds:
            return 0.0
        ok = 0
        for obj in artifact:
            comp = obj.get('compound')
            # find in compounds
            cv = None
            for cn, v in compounds:
                if cn == comp:
                    cv = v
                    break
            if cv is None:
                continue
            C11, C12, C13, C33, C44, C66 = cv
            # Build 6x6 stiffness
            C = np.zeros((6,6))
            C[0,0]=C[1,1]=C11; C[2,2]=C33
            C[0,1]=C[1,0]=C12; C[0,2]=C[2,0]=C[1,2]=C[2,1]=C13
            C[3,3]=C[4,4]=C44; C[5,5]=C66
            # Compute Voigt-Russ-Hill
            # Voigt bounds for tetragonal
            B_V = (2*C11 + C33 + 2*C12 + 4*C13) / 9.0
            G_V = (2*C11 + C33 - C12 - 2*C13 + 6*C44 + 3*C66) / 15.0
            # Compliance matrix
            S_mat = inv(C)  # 6x6 Voigt
            # For Reuss bounds, use compliance
            S11 = S_mat[0,0]; S22 = S_mat[1,1]; S33 = S_mat[2,2]
            S12 = S_mat[0,1]; S13 = S_mat[0,2]; S23 = S_mat[1,2]
            S44 = S_mat[3,3]; S55 = S_mat[4,4]; S66 = S_mat[5,5]
            B_R = 1.0 / (2*S11 + S33 + 2*S12 + 4*S13)
            G_R = 15.0 / (8*S11 + 4*S33 - 4*S12 - 8*S13 + 6*S44 + 3*S66)
            B_VRH = (B_V + B_R) / 2.0
            G_VRH = (G_V + G_R) / 2.0
            Y_VRH = 9*B_VRH*G_VRH / (3*B_VRH + G_VRH)
            Poisson_VRH = (3*B_VRH - 2*G_VRH) / (2*(3*B_VRH + G_VRH))
            # compare
            eps = 1e-9
            if abs(obj.get('B_VRH',0) - B_VRH) > tol*max(abs(B_VRH), eps):
                continue
            if abs(obj.get('G_VRH',0) - G_VRH) > tol*max(abs(G_VRH), eps):
                continue
            if abs(obj.get('Y_VRH',0) - Y_VRH) > tol*max(abs(Y_VRH), eps):
                continue
            if abs(obj.get('Poisson_VRH',0) - Poisson_VRH) > tol*max(abs(Poisson_VRH), eps):
                continue
            ok += 1
        total = len(artifact) if artifact else 0
        return ok / max(total, 1)


# === block: score_3 (check id='step_04_transition') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_list = step.get('gold_data', [])
        if not gold_list:
            return 1.0
        rel_tol = step.get('rel_tol', 0.15)
        fields = ['Pt_I42d_Pna21', 'Pt_I42d_Fm3m']
        artifact_by_compound = {}
        for item in artifact:
            comp = item.get('compound')
            if comp:
                artifact_by_compound[comp] = item
        ok = 0
        total = len(gold_list)
        for gold in gold_list:
            comp = gold['compound']
            item = artifact_by_compound.get(comp)
            if item is None:
                continue
            all_ok = True
            for fld in fields:
                val = item.get(fld)
                gv = gold.get(fld)
                if val is None or gv is None:
                    all_ok = False
                    break
                if gv == 0:
                    if abs(val) > 1e-9:
                        all_ok = False
                        break
                else:
                    if abs(val - gv) > rel_tol * abs(gv):
                        all_ok = False
                        break
            if all_ok:
                ok += 1
        return ok / max(total, 1)


# === block: score_4 (check id='step_05_anisotropy') ===
def score_4(artifact, step, ctx):
        c_data = ctx.get('c_data')
        if not c_data:
            return 0.0
        from numpy.linalg import inv
        # Relax tolerance to at least 0.05 relative to avoid penalizing coarser angular grids
        tol = max(step.get('consistency_tol', 0.05), 0.05)
        compounds = []
        for item in c_data:
            comp = item.get('compound')
            C11 = item.get('C11'); C12 = item.get('C12'); C13 = item.get('C13')
            C33 = item.get('C33'); C44 = item.get('C44'); C66 = item.get('C66')
            if None in (C11,C12,C13,C33,C44,C66) or comp is None:
                continue
            compounds.append((comp, (C11, C12, C13, C33, C44, C66)))
        if not compounds:
            return 0.0
        # Precompute extremes
        ntheta = 100; nphi = 200
        theta = np.linspace(0, np.pi, ntheta)
        phi = np.linspace(0, 2*np.pi, nphi)
        TH, PH = np.meshgrid(theta, phi, indexing='ij')
        # direction vectors
        a1 = np.sin(TH) * np.cos(PH)
        a2 = np.sin(TH) * np.sin(PH)
        a3 = np.cos(TH)
        expected = {}
        for comp, cv in compounds:
            C11, C12, C13, C33, C44, C66 = cv
            C = np.zeros((6,6))
            C[0,0]=C[1,1]=C11; C[2,2]=C33
            C[0,1]=C[1,0]=C12; C[0,2]=C[2,0]=C[1,2]=C[2,1]=C13
            C[3,3]=C[4,4]=C44; C[5,5]=C66
            S_mat = inv(C)  # Voigt compliance
            # Convert to full 3x3x3x3 compliance Sijkl
            S = np.zeros((3,3,3,3))
            def voigt_to_tensor(ii,jj):
                if ii==0: i=0
                elif ii==1: i=1
                elif ii==2: i=2
                elif ii==3: i=1; j=2
                elif ii==4: i=0; j=2
                elif ii==5: i=0; j=1
                if jj==0: k=0
                elif jj==1: k=1
                elif jj==2: k=2
                elif jj==3: k=1; l=2
                elif jj==4: k=0; l=2
                elif jj==5: k=0; l=1
                return (i,j,k,l)
            for I in range(6):
                for J in range(6):
                    s_val = S_mat[I,J]
                    if I>=3: s_val/=2.0
                    if J>=3: s_val/=2.0
                    i,j,k,l = voigt_to_tensor(I,J)
                    S[i,j,k,l] = s_val
                    S[j,i,k,l] = s_val
                    S[i,j,l,k] = s_val
                    S[j,i,l,k] = s_val
            # Compute Young's modulus and linear compressibility surface
            Y = np.zeros_like(a1)
            beta = np.zeros_like(a1)
            for id in range(a1.size):
                ax = a1.flat[id]; ay = a2.flat[id]; az = a3.flat[id]
                # Young's modulus: 1/(a_i a_j a_k a_l S_ijkl)
                a_vec = np.array([ax,ay,az])
                denom = np.einsum('i,j,k,l', a_vec, a_vec, a_vec, a_vec, S.reshape(3,3,3,3))
                Y.flat[id] = 1.0 / denom if denom != 0 else 0.0
                # linear compressibility: S_ijkk a_i a_j
                beta_denom = 0.0
                for i in range(3):
                    for j in range(3):
                        trace_S = sum(S[i,j,k,k] for k in range(3))
                        beta_denom += a_vec[i]*a_vec[j]*trace_S
                beta.flat[id] = beta_denom
            Y_min = np.min(Y); Y_max = np.max(Y)
            beta_min = np.min(beta); beta_max = np.max(beta)
            expected[comp] = (Y_min, Y_max, beta_min*1e-3, beta_max*1e-3)  # convert GPa^-1 to TPa^-1
        # Now compare
        ok = 0
        for obj in artifact:
            comp = obj.get('compound')
            if comp not in expected:
                continue
            eYmin, eYmax, ebmin, ebmax = expected[comp]
            eps = 1e-9
            if abs(obj.get('Y_min',0) - eYmin) > tol * max(abs(eYmin), eps):
                continue
            if abs(obj.get('Y_max',0) - eYmax) > tol * max(abs(eYmax), eps):
                continue
            if abs(obj.get('beta_min',0) - ebmin) > tol * max(abs(ebmin), eps):
                continue
            if abs(obj.get('beta_max',0) - ebmax) > tol * max(abs(ebmax), eps):
                continue
            ok += 1
        total = len(artifact) if artifact else 0
        return ok / max(total, 1)


_SCORERS = {
    'step_01_elastic': score_0,
    'step_02_phonon': score_1,
    'step_03_poly': score_2,
    'step_04_transition': score_3,
    'step_05_anisotropy': score_4,
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
