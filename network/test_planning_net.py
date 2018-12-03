from network.planing_net import PlanningNet
from torch.autograd import Variable
import unittest
import torch


class TestSimpleFCN(unittest.TestCase):
    def test_main(self):
        net = PlanningNet()
        net.eval()
        input = Variable(torch.randn(1, 10, 80, 80))
        output = net(input)
        print(output.shape)


if __name__ == '__main__':
    unittest.main()
