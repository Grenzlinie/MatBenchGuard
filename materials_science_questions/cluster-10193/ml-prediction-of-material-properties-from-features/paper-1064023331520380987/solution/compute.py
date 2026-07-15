import csv, math
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LassoCV, RidgeCV
from sklearn.ensemble import AdaBoostRegressor, ExtraTreesRegressor, RandomForestRegressor, GradientBoostingRegressor
from sklearn.feature_selection import f_regression
from sklearn.model_selection import cross_val_score
import sys, os

def compute_indices():
    rows = []
    for m in range(1, 101):
        for n in range(1, 101):
            # --- original indices (Theorem 2) ---
            R1 = 164*m*n - 40*m - 40*n + 20
            Rm1 = 1.2778*m*n + 0.8333*m + 0.8333*n + 2.1667
            R12 = 47.5118*m*n - 7.3722*m - 7.3722*n + 2.1593
            Rm12 = 4.1950*m*n + 1.0641*m + 1.0641*n + 0.4408
            ABC = 9.4860*m*n + 0.2464*m + 0.2464*n + 0.1911
            GA = 13.07998*m*n + 0.1890*m + 0.1890*n - 0.8728
            F = 430*m*n - 96*m - 96*n + 72
            AZI = 153.3818*m*n - 23.296*m - 23.296*n + 4.796
            M1 = 102*m*n - 16*m - 16*n + 8
            M2 = 164*m*n - 40*m - 40*n + 20
            ReZG1 = 11.6667*m*n + 2*m + 2*n + 2
            ReZG2 = 22.1905*m*n - 3.3905*m - 3.3905*n + 0.2571
            ReZG3 = 1236*m*n - 344*m - 344*n + 232

            # --- coindices (Theorem 3) ---
            CR1 = 358*m*m*n*n - 384*m*m*n + 10*m*n*n + 564*m*n + 8*m*m - 8*n*n - 320*m + 176*n + 124
            CRm1 = 5.556*m*m*n*n - 7.6667*m*m*n + 5.6667*m*n*n + 31.611*m*n + m*m - n*n - 26.333*m + 22.6667*n + 35.8333
            CR12 = 116.7631*m*m*n*n + 16.0897*m*m*n + 65.4523*m*n*n + 241.1257*m*n + 22.6274*m*m - 22.6274*n*n - 157.7649*m - 22.0004*n + 105.7230
            CRm12 = 14.5013*m*m*n*n - 20.3869*m*m*n + 12.4207*m*n*n + 56.8750*m*n + 2.8284*m*m - 2.8284*n*n - 45.1768*m + 38.0554*n + 56.6045
            CABC = 27.708*m*m*n*n + 31.3591*m*m*n + 20.0454*m*n*n + 81.1132*m*n + 5.6569*m*m - 5.6569*n*n - 58.2292*m + 40.7658*n + 53.5490
            CGA = 38.0393*m*m*n*n - 49.8105*m*m*n + 26.8076*m*n*n + 104.8371*m*n + 7.5425*m*m - 7.5425*n*n - 78.9863*m + 56*n + 73.6701
            CF = 928*m*m*n*n - 972*m*m*n + 452*m*n*n + 790*m*n + 16*m*m - 16*n*n - 752*m + 368*n + 248
            CAZI = 379.3077*m*m*n*n - 881*m*m*n + 200.704*m*n*n + 1803.9942*m*n + 64*m*m - 64*n*n - 632.704*m + 486.816*n + 603.204
            CM1 = 248*m*m*n*n - 292*m*m*n + 140*m*n*n + 518*m*n + 48*m*m - 48*n*n - 328*m + 200*n + 360
            CM2 = 358*m*m*n*n - 384*m*m*n + 160*m*n*n + 564*m*n + 8*m*m - 8*n*n - 320*m + 176*n + 124
            CReZG1 = 35.6667*m*m*n*n - 47.6667*m*m*n + 31*m*n*n + 129.6667*m*n + 6*m*m - 6*n*n - 67*m + 74*n + 100
            CReZG2 = 49.1230*m*m*n*n - 65.7908*m*m*n + 30.7429*m*n*n + 112.533*m*n + 10.6667*m*m - 10.6667*n*n - 82.6095*m + 48.0571*n + 67.7429
            CReZG3 = 2504*m*m*n*n - 2368*m*m*n + 928*m*n*n + 3068*m*n + 389*m*m - 389*n*n - 1410*m + 696*n + 1240

            # --- reverse indices (Theorem 4) ---
            RR1 = 136*m*n + 72*m + 72*n - 36
            RRm1 = 1.9*m*n - 0.24*m - 0.24*n + 0.18
            RR12 = 42.2926*m*n + 8.5402*m + 8.5402*n - 4.9239
            RRm12 = 4.9764*m*n - 0.4931*m - 0.4931*n + 0.3954
            RABC = 10.4216*m*n + 0.4957*m + 0.4957*n - 2.5028
            RGA = 12.4134*m*n + 0.1433*m + 0.1433*n - 0.2159
            RF = 374*m*n + 128*m + 128*n - 40
            RAZI = 130.3493*m*n + 9.7612*m + 9.7612*n + 118.8296
            RM1 = 90*m*n + 16*m + 16*n - 8
            RM2 = 136*m*n + 72*m + 72*n + 144
            RReZG1 = 11.7667*m*n + 0.2*m + 0.2*n + 0.8
            RReZG2 = 15.5405*m*n + 6.7540*m + 6.7540*n - 2.9115
            RReZG3 = 976*m*n + 904*m + 904*n - 344

            row = [m,n, R1, Rm1, R12, Rm12, ABC, GA, F, AZI, M1, M2, ReZG1, ReZG2, ReZG3,
                   CR1, CRm1, CR12, CRm12, CABC, CGA, CF, CAZI, CM1, CM2, CReZG1, CReZG2, CReZG3,
                   RR1, RRm1, RR12, RRm12, RABC, RGA, RF, RAZI, RM1, RM2, RReZG1, RReZG2, RReZG3]
            rows.append(row)
    return rows

def main():
    outdir = sys.argv[1]

    columns = ["m","n","R1","Rm1","R12","Rm12","ABC","GA","F","AZI","M1","M2","ReZG1","ReZG2","ReZG3",
               "CR1","CRm1","CR12","CRm12","CABC","CGA","CF","CAZI","CM1","CM2","CReZG1","CReZG2","CReZG3",
               "RR1","RRm1","RR12","RRm12","RABC","RGA","RF","RAZI","RM1","RM2","RReZG1","RReZG2","RReZG3"]

    rows = compute_indices()
    df = pd.DataFrame(rows, columns=columns)
    df.to_csv(os.path.join(outdir, "indices_values.csv"), index=False)

    target = ((df["m"] + df["n"]) ** 2 * (-795.8)) / 60.22
    feature_names = columns[2:]

    scaler = StandardScaler()
    X_norm = scaler.fit_transform(df[feature_names])

    # --- feature selection ranking (EFS, max_features=1) ---
    scores = {}
    for i, feat in enumerate(feature_names):
        X_single = X_norm[:, i].reshape(-1, 1)
        score = np.mean(cross_val_score(LinearRegression(), X_single, target, scoring='r2', cv=5))
        scores[feat] = score
    sorted_features = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    with open(os.path.join(outdir, "feature_selection_ranking.csv"), "w") as f:
        f.write("idx,score\n")
        for name, sc in sorted_features:
            f.write(f"{name},{sc}\n")

    # --- regression model importance ranking ---
    models = {
        'AdaBoost': AdaBoostRegressor(random_state=42),
        'ExtraTrees': ExtraTreesRegressor(random_state=42),
        'RandomForest': RandomForestRegressor(random_state=42),
        'GradientBoosting': GradientBoostingRegressor(random_state=42),
        'LassoCV': LassoCV(random_state=42),
        'RidgeCV': RidgeCV(),
        'LinearRegression': LinearRegression()
    }
    weights = {name: 0.0 for name in feature_names}
    count = 0

    for model in models.values():
        model.fit(X_norm, target)
        if hasattr(model, 'coef_'):
            coef = np.abs(model.coef_)
            if coef.ndim > 1:
                coef = coef.mean(axis=0)
        elif hasattr(model, 'feature_importances_'):
            coef = model.feature_importances_
        else:
            coef = np.zeros(len(feature_names))
        for i, w in enumerate(coef):
            weights[feature_names[i]] += w
        count += 1

    f_scores, _ = f_regression(X_norm, target)
    for i, w in enumerate(f_scores):
        weights[feature_names[i]] += np.abs(w)
    count += 1

    avg_weights = {name: weights[name] / count for name in feature_names}
    sorted_weights = sorted(avg_weights.items(), key=lambda x: x[1], reverse=True)

    with open(os.path.join(outdir, "regression_ranking.csv"), "w") as f:
        f.write("idx,avg_weight\n")
        for name, w in sorted_weights:
            f.write(f"{name},{w}\n")

if __name__ == "__main__":
    main()
