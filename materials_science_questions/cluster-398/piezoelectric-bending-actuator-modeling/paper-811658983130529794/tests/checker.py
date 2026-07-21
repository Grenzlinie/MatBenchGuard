import os
import json
import csv

# === author imports / helpers ===
import numpy as np
try:
    import pandas as pd
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "pandas"])
    import pandas as pd


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
    voltage_path = os.path.join(outputs_dir, 'voltage_vs_frequency.csv')
    location_path = os.path.join(outputs_dir, 'location_vs_frequency.csv')
    df_voltage = pd.read_csv(voltage_path) if os.path.exists(voltage_path) else None
    df_location = pd.read_csv(location_path) if os.path.exists(location_path) else None
    return {'df_voltage': df_voltage, 'df_location': df_location}


# === block: score_0 (check id='voltage_frequency') ===
def score_0(artifact, step, ctx):
    df_v = pd.DataFrame(artifact)
    df_loc = ctx.get('df_location')

    # Check for required columns and return 0.0 if missing
    required = ['amplitude_ratio', 'frequency_ratio', 'voltage']
    if not all(col in df_v.columns for col in required):
        return 0.0

    # Ensure numeric types; drop rows with missing essential columns
    for col in required:
        df_v[col] = pd.to_numeric(df_v[col], errors='coerce')
    df_v = df_v.dropna(subset=required)

    if df_v.empty:
        return 0.0

    # 1. Monotonicity per voltage
    mono_scores = []
    for volt, grp in df_v.groupby('voltage'):
        grp_sorted = grp.sort_values('amplitude_ratio')
        freq = grp_sorted['frequency_ratio'].values
        if len(freq) > 1:
            mono_scores.append(float(np.all(np.diff(freq) >= -1e-9)))
        else:
            mono_scores.append(1.0)
    mono_fraction = np.mean(mono_scores) if mono_scores else 0.0

    # 2. Voltage ordering (higher voltage ⇒ higher frequency)
    present_voltages = sorted(df_v['voltage'].unique())
    pair_checks = []
    for i in range(len(present_voltages)):
        for j in range(i+1, len(present_voltages)):
            v1 = present_voltages[i]
            v2 = present_voltages[j]
            df1 = df_v[df_v['voltage']==v1].sort_values('amplitude_ratio')
            df2 = df_v[df_v['voltage']==v2].sort_values('amplitude_ratio')
            amp1 = df1['amplitude_ratio'].values
            amp2 = df2['amplitude_ratio'].values
            min_amp = max(amp1.min(), amp2.min())
            max_amp = min(amp1.max(), amp2.max())
            if max_amp - min_amp >= 0.01:
                common_amps = np.arange(min_amp, max_amp, 0.02)
                f1_int = np.interp(common_amps, amp1, df1['frequency_ratio'].values)
                f2_int = np.interp(common_amps, amp2, df2['frequency_ratio'].values)
                valid = np.all(f2_int >= f1_int - 1e-6)
                pair_checks.append(float(valid))
            else:
                pair_checks.append(0.0)
    order_score = np.mean(pair_checks) if pair_checks else 1.0

    # 3. Cross‑consistency with location file (V=0 vs top_bottom)
    cross_score = 0.0
    if df_loc is not None and not df_loc.empty:
        # Make a copy and coerce numeric columns to avoid string-type crashes
        df_loc = df_loc.copy()
        for col in ['amplitude_ratio', 'frequency_ratio']:
            if col in df_loc.columns:
                df_loc[col] = pd.to_numeric(df_loc[col], errors='coerce')
        df_loc = df_loc.dropna(subset=['amplitude_ratio', 'frequency_ratio'])
        if not df_loc.empty:
            df_v0 = df_v[df_v['voltage']==0].sort_values('amplitude_ratio')
            df_top = df_loc[df_loc['lamination_case']=='top_bottom'].sort_values('amplitude_ratio')
            if not df_v0.empty and not df_top.empty:
                amp_v0 = df_v0['amplitude_ratio'].values
                freq_v0 = df_v0['frequency_ratio'].values
                amp_top = df_top['amplitude_ratio'].values
                freq_top = df_top['frequency_ratio'].values
                amp_min = max(amp_v0.min(), amp_top.min())
                amp_max = min(amp_v0.max(), amp_top.max())
                if amp_max - amp_min >= 0.02:
                    common_amps = np.arange(amp_min, amp_max, 0.02)
                    freq_v0_int = np.interp(common_amps, amp_v0, freq_v0)
                    freq_top_int = np.interp(common_amps, amp_top, freq_top)
                    max_diff = np.max(np.abs(freq_v0_int - freq_top_int))
                    cross_score = max(0.0, 1.0 - (max_diff - 0.01) / 0.09)
                else:
                    cross_score = 0.5
            else:
                cross_score = 0.0
        else:
            cross_score = 0.0
    else:
        cross_score = 0.0

    w_mono, w_order, w_cross = 0.3, 0.3, 0.4
    total = w_mono * mono_fraction + w_order * order_score + w_cross * cross_score
    return float(total)


# === block: score_1 (check id='location_frequency') ===
def score_1(artifact, step, ctx):
    df_loc = pd.DataFrame(artifact)
    if df_loc.empty:
        return 0.0

    # Monotonicity per lamination case
    cases = ['top_bottom', 'middle', 'inner']
    mono_scores = []
    for case in cases:
        grp = df_loc[df_loc['lamination_case']==case].sort_values('amplitude_ratio')
        if len(grp) > 1:
            freq = grp['frequency_ratio'].values
            mono_scores.append(float(np.all(np.diff(freq) >= -1e-9)))
        else:
            mono_scores.append(1.0)
    mono_fraction = np.mean(mono_scores) if mono_scores else 0.0

    # Ordering: top_bottom > middle > inner
    order_pair_checks = []
    for higher, lower in [('top_bottom','middle'), ('middle','inner')]:
        df_high = df_loc[df_loc['lamination_case']==higher].sort_values('amplitude_ratio')
        df_low = df_loc[df_loc['lamination_case']==lower].sort_values('amplitude_ratio')
        if not df_high.empty and not df_low.empty:
            amp_high = df_high['amplitude_ratio'].values
            amp_low = df_low['amplitude_ratio'].values
            freq_high = df_high['frequency_ratio'].values
            freq_low = df_low['frequency_ratio'].values
            min_amp = max(amp_high.min(), amp_low.min())
            max_amp = min(amp_high.max(), amp_low.max())
            if max_amp - min_amp >= 0.01:
                common_amps = np.arange(min_amp, max_amp, 0.02)
                f_high_int = np.interp(common_amps, amp_high, freq_high)
                f_low_int = np.interp(common_amps, amp_low, freq_low)
                valid = np.all(f_high_int >= f_low_int - 1e-6)
                order_pair_checks.append(float(valid))
            else:
                order_pair_checks.append(0.0)
        else:
            order_pair_checks.append(0.0)
    order_score = np.mean(order_pair_checks) if order_pair_checks else 0.0

    w_mono, w_order = 0.3, 0.7
    total = w_mono * mono_fraction + w_order * order_score
    return float(total)


_SCORERS = {
    'voltage_frequency': score_0,
    'location_frequency': score_1,
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
