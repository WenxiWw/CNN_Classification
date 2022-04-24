import torchvision
import torch.nn as nn


class Model(nn.Module):
    def __init__(self, feat_dim = 2048, output_dim =10):
        super(Model, self).__init__()

        self.feat_dim = feat_dim
        self.output_dim = output_dim

        self.backbone = torchvision.models.resnet50(pretrained=True)

        self.backbone.fc = nn.Linear(feat_dim, output_dim)

        # for param in self.backbone.conv1.parameters():
        #       param.requires_grad_(False)
        
        child_counter = 0
        for child in self.backbone.children():
            if child_counter < 3:
               print("child ",child_counter," was frozen")
               for param in child.parameters():
                     param.requires_grad = False
            else:
               print("child ",child_counter," was not frozen")
  
            child_counter += 1
              


    def forward(self, img):
        out = self.backbone(img) 
        return out