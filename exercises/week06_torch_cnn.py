def main():
    try:
        import torch
        import torch.nn as nn
        import torch.optim as optim
        from torch.utils.data import DataLoader, TensorDataset
    except ImportError:
        print("没有检测到 PyTorch。")
        print("第 6 周再安装即可，请参考 https://pytorch.org/get-started/locally/")
        print("安装后重新运行: python exercises\\week06_torch_cnn.py")
        return

    torch.manual_seed(3)

    X = torch.randn(200, 1, 28, 28)
    y = (X.mean(dim=(1, 2, 3)) > 0).long()

    dataset = TensorDataset(X, y)
    loader = DataLoader(dataset, batch_size=32, shuffle=True)

    model = nn.Sequential(
        nn.Conv2d(1, 8, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2),
        nn.Conv2d(8, 16, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2),
        nn.Flatten(),
        nn.Linear(16 * 7 * 7, 2),
    )

    loss_fn = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    print("第 6 周练习：最小 CNN 训练循环")
    for epoch in range(5):
        total_loss = 0.0
        correct = 0
        total = 0

        for batch_X, batch_y in loader:
            optimizer.zero_grad()
            logits = model(batch_X)
            loss = loss_fn(logits, batch_y)
            loss.backward()
            optimizer.step()

            total_loss += float(loss.item()) * len(batch_X)
            correct += int((logits.argmax(dim=1) == batch_y).sum().item())
            total += len(batch_X)

        print(
            f"epoch={epoch + 1} loss={total_loss / total:.4f} "
            f"accuracy={correct / total:.3f}"
        )

    print("\n练习任务:")
    print("1. 修改 epoch 数量，观察 accuracy。")
    print("2. 把 28x28 随机图像替换成真实医学图像。")
    print("3. 保存模型参数: torch.save(model.state_dict(), 'model.pt')")


if __name__ == "__main__":
    main()
