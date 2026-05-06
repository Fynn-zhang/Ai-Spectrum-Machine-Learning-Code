from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "synthetic_spectra.csv"


def create_dataset_if_missing():
    if DATA_PATH.exists():
        return

    import sys

    sys.path.append(str(ROOT / "exercises"))
    from week02_spectrum_csv import build_synthetic_spectra

    build_synthetic_spectra(DATA_PATH)


def snv(X):
    row_mean = X.mean(axis=1, keepdims=True)
    row_std = X.std(axis=1, keepdims=True)
    row_std[row_std == 0] = 1.0
    return (X - row_mean) / row_std


def load_data():
    create_dataset_if_missing()
    df = pd.read_csv(DATA_PATH)
    wavelength_columns = [column for column in df.columns if column.startswith("wl_")]
    wavelengths = np.array([int(column.replace("wl_", "")) for column in wavelength_columns])
    X = df[wavelength_columns].to_numpy()
    y = df["label"].to_numpy()
    return X, y, wavelengths


def main():
    X, y, wavelengths = load_data()
    X_preprocessed = snv(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_preprocessed,
        y,
        test_size=0.25,
        random_state=21,
        stratify=y,
    )

    baseline = Pipeline(
        [
            ("scale", StandardScaler()),
            ("pca", PCA(n_components=8, random_state=21)),
            ("model", SVC(kernel="rbf", probability=True)),
        ]
    )
    baseline.fit(X_train, y_train)
    baseline_predictions = baseline.predict(X_test)

    forest = RandomForestClassifier(n_estimators=300, random_state=21)
    forest.fit(X_train, y_train)
    forest_predictions = forest.predict(X_test)

    print("最终项目模板：医学光谱组织/病灶识别")
    print(f"样本数: {len(y)}")
    print(f"波段数: {len(wavelengths)}")

    print("\nBaseline: SNV + StandardScaler + PCA + SVM")
    print(confusion_matrix(y_test, baseline_predictions, labels=["normal", "lesion"]))
    print(classification_report(y_test, baseline_predictions, digits=3))

    print("\n可解释性 baseline: Random Forest 重要波段")
    print(confusion_matrix(y_test, forest_predictions, labels=["normal", "lesion"]))
    print(classification_report(y_test, forest_predictions, digits=3))

    top_indices = np.argsort(forest.feature_importances_)[-8:][::-1]
    print("重要波段 Top 8:")
    for index in top_indices:
        print(
            f"  {wavelengths[index]} nm: "
            f"importance={forest.feature_importances_[index]:.4f}"
        )

    print("\n报告写作提醒:")
    print("1. 这些重要波段只是模型统计结果，不等于已经证明的生物机制。")
    print("2. 真实医学数据必须避免同一患者数据同时出现在训练集和测试集。")
    print("3. 用 reports\\final_project_report_template.md 整理结果。")


if __name__ == "__main__":
    main()
