# 医学图像与光谱 AI 学习包

这是一个从零基础开始的 12 周学习工作区，目标是把 AI 基础、机器学习代码、医学图像分析和光谱分析连接起来。你可以按周学习，也可以把它当作以后做论文复现和项目实验的模板。

## 目录

- `curriculum/12_week_plan.md`：每周学习目标、任务和产出。
- `curriculum/progress_checklist.md`：可以逐项打勾的进度清单。
- `exercises/`：可运行的 Python 练习脚本。
- `projects/final_project_template.py`：最终项目代码模板。
- `reports/final_project_report_template.md`：最终项目报告模板。
- `data/`：练习数据目录，脚本会自动生成小型模拟光谱数据。

## 环境安装

建议使用 Python 3.10 或更新版本。

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Jupyter 是推荐工具，但不是运行练习脚本的必需项。需要 Notebook 时再安装：

```powershell
python -m pip install -r requirements-optional.txt
```

PyTorch 体积较大，也先不放进基础依赖。学到第 6 周时，再根据你的电脑是否有 NVIDIA GPU，参考官方安装页安装 PyTorch。

## 推荐学习顺序

1. 阅读 `curriculum/12_week_plan.md`。
2. 每周完成对应练习脚本。
3. 用 `curriculum/progress_checklist.md` 记录进度。
4. 第 11-12 周使用 `projects/final_project_template.py` 和报告模板完成综合项目。

## 运行示例

```powershell
python exercises\week01_python_numpy.py
python exercises\week02_spectrum_csv.py
python exercises\week03_ml_baseline.py
python projects\final_project_template.py
```

## 学习原则

- 先能跑通代码，再理解公式。
- 先建立简单模型作为 baseline，再尝试复杂模型。
- 医学 AI 一定要重视数据划分、评价指标和可解释性。
- 所有实验都要记录：数据来源、预处理、模型、参数、结果、失败原因。
