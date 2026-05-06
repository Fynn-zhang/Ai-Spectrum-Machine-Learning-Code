# 12 周医学图像、光谱与冷冻电镜 AI 学习计划

每周建议投入 8-12 小时：

- 编程练习：40%
- AI 理论：30%
- 医学图像/光谱/冷冻电镜应用：20%
- 复盘笔记：10%

本计划的具体应用方向调整为三条线并行：

- 光谱分析：从光谱曲线中提取组织、病灶或生物信息。
- 医学图像分析：做分类、分割、错误分析和模型解释。
- 冷冻电镜细胞相位变化图像处理：面向低信噪比 cryo-EM 图像，学习去噪、对比度增强、相位/强度变化量化、细胞结构区域识别和变化检测。

## 第 1 周：Python 入门

目标：能读懂和修改基础 Python 脚本。

学习内容：

- 变量、字符串、数字、列表、字典。
- `for` 循环、`if` 判断、函数。
- 文件路径和简单文件读写。

练习：

```powershell
python exercises\week01_python_numpy.py
```

产出：

- 能解释脚本里每一步在做什么。
- 能改动样本数量、波长范围和统计指标。

## 第 2 周：NumPy、pandas 与光谱 CSV

目标：能读取、清洗、统计和画出光谱曲线。

学习内容：

- NumPy 数组、维度、均值、标准差、切片。
- pandas 读取 CSV、筛选列、分组统计。
- Matplotlib 画折线图。

练习：

```powershell
python exercises\week02_spectrum_csv.py
```

产出：

- `data/synthetic_spectra.csv`
- `reports/week02_spectrum_plot.png`

## 第 3 周：机器学习分类基础

目标：理解训练集、测试集和分类指标。

学习内容：

- 特征 `X`、标签 `y`。
- `train_test_split`。
- Logistic Regression、SVM、Random Forest。
- Accuracy、F1、混淆矩阵。

练习：

```powershell
python exercises\week03_ml_baseline.py
```

产出：

- 一个可以区分两类模拟组织光谱的 baseline 模型。

## 第 4 周：模型评估与交叉验证

目标：避免“只在一次随机划分上看起来很好”的问题。

学习内容：

- K-fold cross validation。
- Precision、Recall、F1、ROC-AUC。
- 过拟合、欠拟合。

练习方向：

- 把第 3 周脚本改成 5 折交叉验证。
- 比较 SVM 和 Random Forest 的 F1 分数。

## 第 5 周：PCA 与光谱降维

目标：能用 PCA 可视化高维光谱，并理解它也可用于图像特征降维。

学习内容：

- PCA 的直觉：把很多波段压缩成几个主成分。
- PCA + SVM 管道。
- 哪些波段对分类更重要。
- 将图像展平成特征向量时，PCA 可以帮助观察不同细胞状态或相位变化样本是否分离。

练习方向：

- 在第 3 周脚本中加入 PCA。
- 画出前两个主成分的散点图。

## 第 6 周：PyTorch 与神经网络

目标：理解深度学习训练循环。

学习内容：

- Tensor、Dataset、DataLoader。
- 前向传播、loss、反向传播、optimizer。
- 保存和加载模型。

练习：

```powershell
python exercises\week06_torch_cnn.py
```

如果没有安装 PyTorch，脚本会提示安装方式。

## 第 7 周：CNN 与医学图像分类

目标：能训练一个简单 CNN 做二分类，并开始接触冷冻电镜图像的基础预处理。

学习内容：

- 卷积、池化、全连接层。
- 医学图像 resize、归一化、数据增强。
- 分类输出和概率解释。
- 冷冻电镜图像常见问题：低信噪比、低对比度、背景不均匀、细胞结构边界模糊。
- 基础图像增强：灰度归一化、直方图均衡、CLAHE、Gaussian/median 去噪。

练习方向：

- 用公开小型图像数据集或自己的医学图像文件夹。
- 文件夹结构建议：`data/images/class_0` 和 `data/images/class_1`。
- 增加一个 cryo-EM 练习文件夹：`data/cryo_em/phase_low` 和 `data/cryo_em/phase_high`，先按相位变化弱/强做二分类。

## 第 8 周：医学图像评价与错误分析

目标：知道模型为什么错，错在哪里，并能初步分析冷冻电镜相位变化区域。

学习内容：

- 混淆矩阵。
- 假阳性、假阴性。
- 类别不平衡。
- 简单可解释性：查看错分样本、热力图概念。
- 冷冻电镜应用中的变化检测：同一区域前后图像差分、局部对比度变化、细胞结构边界变化。
- 区分“真实相位/结构变化”和“成像噪声、漂移、曝光差异”的风险。

练习方向：

- 保存预测错误的图像路径。
- 对每类错误写一句可能原因。
- 对一组 cryo-EM 图像做灰度归一化后，计算局部区域的平均强度、标准差和边缘强度变化。

## 第 9 周：光谱预处理

目标：知道光谱建模前为什么要预处理。

学习内容：

- 平滑。
- 标准化。
- SNV。
- 基线校正。
- 一阶/二阶导数。

练习方向：

- 比较“原始光谱”和“预处理光谱”的分类 F1。

## 第 10 周：光谱专项模型

目标：掌握医学光谱常用 baseline，并形成冷冻电镜相位变化识别 baseline。

学习内容：

- PCA + SVM。
- PLS-DA。
- Random Forest 波段重要性。
- 1D-CNN 概念。
- cryo-EM baseline：图像预处理 + 手工特征 + SVM/Random Forest。
- 手工特征建议：局部均值、标准差、梯度强度、纹理特征、结构边缘密度。
- 深度学习方向：CNN 分类相位变化强弱，或 U-Net 分割变化区域。

练习方向：

- 画出 Random Forest 重要波段。
- 解释这些波段可能对应的生物信息，明确标注“推测”。
- 比较 cryo-EM 原始图像、去噪图像、对比度增强图像对分类效果的影响。

## 第 11 周：综合项目实现

目标：完成一个端到端项目。

推荐题目：

基于医学图像、光谱数据与冷冻电镜相位变化的组织/细胞状态识别模型。

任务：

- 准备数据。
- 预处理数据：光谱做 SNV/PCA，医学图像做归一化/增强，冷冻电镜图像做去噪、对比度增强和漂移检查。
- 建立 baseline。
- 训练模型。
- 评估结果。
- 输出图表。
- 对 cryo-EM 图像输出相位变化相关指标：变化区域比例、局部强度变化、边缘/纹理变化。

模板：

```powershell
python projects\final_project_template.py
```

## 第 12 周：报告与复盘

目标：把实验整理成可展示材料。

报告结构：

- 研究问题。
- 数据来源。
- 方法。
- 结果。
- 错误分析。
- 冷冻电镜相位变化解释：哪些区域发生变化，是否可能来自噪声或成像条件变化。
- 局限性。
- 下一步计划。

模板：

`reports/final_project_report_template.md`

## 推荐资料

- Python 官方教程：https://docs.python.org/3/tutorial/
- NumPy beginner guide：https://numpy.org/doc/stable/user/absolute_beginners
- pandas getting started：https://pandas.pydata.org/docs/dev/getting_started/index.html
- scikit-learn user guide：https://scikit-learn.org/stable/user_guide.html
- PyTorch tutorials：https://docs.pytorch.org/tutorials/
- MONAI：https://monai.io/
- Spectral Python：https://www.spectralpython.net/index.html

## 冷冻电镜专项补充路线

第 1-4 周仍以 Python、NumPy、机器学习为主，不提前上复杂 cryo-EM 理论。第 5 周开始把图像看作矩阵，第 7 周进入冷冻电镜图像预处理，第 8-10 周做相位变化特征和 baseline，第 11-12 周纳入综合项目。

建议先完成一个最小任务：

1. 读取一张 cryo-EM 灰度图。
2. 做归一化、去噪和对比度增强。
3. 计算局部区域平均强度、标准差和边缘强度。
4. 如果有前后状态图像，做差分图并找出变化较大的区域。
5. 用简单模型判断“相位变化弱/强”，再逐步升级到 CNN 或 U-Net。
