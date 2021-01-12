from pathlib import Path
import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader


device = 'cpu'
map_location='cpu'

dropout_rate = 0.2
num_classes = 50


class IrDataset(Dataset):
    def __init__(self, spectra, transform=None):
        self.spectra = spectra
        self.transform = transform

    def __len__(self):
        return self.spectra.shape[0]

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        xs = self.spectra[idx]
        xs = torch.from_numpy(xs).float()
        sample = {
            'xs': xs
        }

        if self.transform:
            sample = self.transform(sample)

        return sample


def make_data_loader(ys):
    target = np.reshape(ys, (1, 1, -1))
    dataset = IrDataset(spectra=target)
    loader = DataLoader(dataset, batch_size=len(dataset), shuffle=False, num_workers=0)
    return loader


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=1, out_channels=2, kernel_size=11, stride=1, padding=5)
        self.conv1_bn = nn.BatchNorm1d(2)
        self.dropout1 = nn.Dropout(dropout_rate)
        self.conv2 = nn.Conv1d(in_channels=2, out_channels=4, kernel_size=11, stride=1, padding=5)
        self.conv2_bn = nn.BatchNorm1d(4)
        self.dropout2 = nn.Dropout(dropout_rate)
        self.conv3 = nn.Conv1d(in_channels=4, out_channels=8, kernel_size=11, stride=1, padding=5)
        self.conv3_bn = nn.BatchNorm1d(8)
        self.dropout3 = nn.Dropout(dropout_rate)

        self.fc1 = nn.Linear(3400, 1000)
        self.fc1_bn = nn.BatchNorm1d(1000)
        self.dropout_fc1 = nn.Dropout(dropout_rate)
        self.fc2 = nn.Linear(1000, 250)
        self.fc2_bn = nn.BatchNorm1d(250)
        self.dropout_fc2 = nn.Dropout(dropout_rate)
        self.fc3 = nn.Linear(250, 64)
        self.fc3_bn = nn.BatchNorm1d(64)
        self.dropout_fc3 = nn.Dropout(dropout_rate)
        self.fc4 = nn.Linear(64, num_classes)

    def forward(self, x):
        z = self.conv1_bn(
            F.relu(
                self.conv1(x)
            )
        )
        x = self.dropout1(z)
        x = F.max_pool1d(x, 2)

        z = self.conv2_bn(
            F.relu(
                self.conv2(x)
            )
        )
        x = self.dropout2(z)
        x = F.max_pool1d(x, 2)

        z = self.conv3_bn(
            F.relu(
                self.conv3(x)
            )
        )
        x = self.dropout3(z)
        x = F.max_pool1d(x, 2)

        x = torch.flatten(x, 1)

        x = F.relu(self.fc1_bn(self.fc1(x)))
        x = self.dropout_fc1(x)
        x = F.relu(self.fc2_bn(self.fc2(x)))
        x = self.dropout_fc2(x)
        x = F.relu(self.fc3_bn(self.fc3(x)))
        x = self.dropout_fc3(x)
        x = self.fc4(x)

        output = torch.sigmoid(x)

        return output
