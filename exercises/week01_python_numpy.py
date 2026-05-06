from pathlib import Path

import numpy as np


def create_mock_spectrum(start_nm=400, end_nm=900, step_nm=10):
    wavelengths = np.arange(start_nm, end_nm + step_nm, step_nm)
    baseline = 0.4 + 0.0005 * (wavelengths - start_nm)
    peak = 0.25 * np.exp(-((wavelengths - 620) ** 2) / (2 * 35**2))
    noise = np.random.default_rng(7).normal(0, 0.015, size=wavelengths.shape)
    intensity = baseline + peak + noise
    return wavelengths, intensity


def summarize_spectrum(wavelengths, intensity):
    max_index = int(np.argmax(intensity))
    return {
        "num_bands": len(wavelengths),
        "mean_intensity": float(np.mean(intensity)),
        "std_intensity": float(np.std(intensity)),
        "max_wavelength_nm": int(wavelengths[max_index]),
        "max_intensity": float(intensity[max_index]),
    }


def main():
    wavelengths, intensity = create_mock_spectrum()
    summary = summarize_spectrum(wavelengths, intensity)

    print("第 1 周练习：Python + NumPy 光谱基础")
    print(f"工作目录: {Path.cwd()}")
    print("前 5 个波长:", wavelengths[:5])
    print("前 5 个强度:", np.round(intensity[:5], 4))
    print("统计结果:")
    for key, value in summary.items():
        print(f"  {key}: {value}")

    print("\n练习任务:")
    print("1. 修改 start_nm/end_nm，观察波段数量变化。")
    print("2. 修改 peak 中的 620，观察最大强度波长变化。")
    print("3. 新增 min_intensity 统计。")


if __name__ == "__main__":
    main()
