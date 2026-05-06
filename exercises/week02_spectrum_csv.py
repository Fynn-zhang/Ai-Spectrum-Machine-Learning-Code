from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "synthetic_spectra.csv"
PLOT_PATH = ROOT / "reports" / "week02_spectrum_plot.png"


def build_synthetic_spectra(path=DATA_PATH, samples_per_class=40):
    rng = np.random.default_rng(42)
    wavelengths = np.arange(400, 901, 10)
    rows = []

    for label in ["normal", "lesion"]:
        for sample_index in range(samples_per_class):
            baseline = 0.45 + 0.0004 * (wavelengths - 400)
            water_like_dip = -0.08 * np.exp(-((wavelengths - 760) ** 2) / (2 * 30**2))
            tissue_peak = 0.18 * np.exp(-((wavelengths - 620) ** 2) / (2 * 45**2))

            if label == "lesion":
                tissue_peak += 0.12 * np.exp(-((wavelengths - 680) ** 2) / (2 * 35**2))
                baseline += 0.03

            noise = rng.normal(0, 0.025, size=wavelengths.shape)
            intensities = baseline + tissue_peak + water_like_dip + noise

            row = {
                "sample_id": f"{label}_{sample_index:03d}",
                "label": label,
            }
            row.update({f"wl_{wl}": value for wl, value in zip(wavelengths, intensities)})
            rows.append(row)

    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(path, index=False)
    return path


def main():
    if not DATA_PATH.exists():
        build_synthetic_spectra()

    df = pd.read_csv(DATA_PATH)
    wavelength_columns = [column for column in df.columns if column.startswith("wl_")]
    wavelengths = np.array([int(column.replace("wl_", "")) for column in wavelength_columns])

    print("第 2 周练习：读取和绘制光谱 CSV")
    print(f"数据文件: {DATA_PATH}")
    print(f"样本数: {len(df)}")
    print(f"波段数: {len(wavelength_columns)}")
    print("\n按类别统计前 5 个波段均值:")
    print(df.groupby("label")[wavelength_columns[:5]].mean().round(4))

    plt.figure(figsize=(9, 5))
    for label, group in df.groupby("label"):
        mean_curve = group[wavelength_columns].mean(axis=0).to_numpy()
        plt.plot(wavelengths, mean_curve, label=f"{label} mean")

    plt.title("Synthetic Spectra Mean Curves")
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Intensity")
    plt.legend()
    plt.tight_layout()
    PLOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(PLOT_PATH, dpi=160)
    print(f"\n图像已保存: {PLOT_PATH}")

    print("\n练习任务:")
    print("1. 画出每个类别的前 5 个单独样本。")
    print("2. 计算每个波段的 normal/lesion 均值差。")
    print("3. 找出差异最大的 5 个波段。")


if __name__ == "__main__":
    main()
