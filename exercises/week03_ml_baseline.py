from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from week02_spectrum_csv import DATA_PATH, build_synthetic_spectra


ROOT = Path(__file__).resolve().parents[1]


def load_spectrum_dataset():
    if not DATA_PATH.exists():
        build_synthetic_spectra()

    df = pd.read_csv(DATA_PATH)
    wavelength_columns = [column for column in df.columns if column.startswith("wl_")]
    X = df[wavelength_columns].to_numpy()
    y = df["label"].to_numpy()
    return X, y, wavelength_columns


def main():
    X, y, wavelength_columns = load_spectrum_dataset()
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=11,
        stratify=y,
    )

    models = {
        "logistic_regression": Pipeline(
            [
                ("scale", StandardScaler()),
                ("model", LogisticRegression(max_iter=1000)),
            ]
        ),
        "svm_rbf": Pipeline(
            [
                ("scale", StandardScaler()),
                ("model", SVC(kernel="rbf", probability=True)),
            ]
        ),
        "random_forest": RandomForestClassifier(n_estimators=200, random_state=11),
    }

    print("第 3 周练习：机器学习 baseline")
    print(f"特征维度: {X.shape}")
    print(f"波段范围: {wavelength_columns[0]} 到 {wavelength_columns[-1]}")

    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        print(f"\n模型: {name}")
        print("混淆矩阵:")
        print(confusion_matrix(y_test, predictions, labels=["normal", "lesion"]))
        print("分类报告:")
        print(classification_report(y_test, predictions, digits=3))

    print("练习任务:")
    print("1. 修改 test_size，观察结果是否稳定。")
    print("2. 给 SVM 换成 linear kernel。")
    print("3. 在第 5 周加入 PCA 后再比较结果。")


if __name__ == "__main__":
    main()
