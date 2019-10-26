import torch.nn as nn
import torch.nn.functional as F


class Network4Layers(nn.Module):
   def __init__(self):
       super(Network4Layers, self).__init__()
       self.conv1 = nn.Conv2d(in_channels=1, out_channels=64, kernel_size=3, stride=1, padding=0)
       self.conv2 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=0)
       self.conv3 = nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, stride=1, padding=0)
       self.conv4 = nn.Conv2d(in_channels=256, out_channels=512, kernel_size=3, stride=1, padding=0)
       self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2)

   def forward(self, x):
       x = F.relu(self.conv1(x))
       x = self.maxpool(x)

       x = F.relu(self.conv2(x))
       x = self.maxpool(x)

       x = F.relu(self.conv3(x))
       x = self.maxpool(x)

       x = F.relu(self.conv4(x))
       x = self.maxpool(x)

       return x
