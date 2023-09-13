<div align="center">
  <img src="https://raw.githubusercontent.com/Ikomia-hub/train_torchvision_resnet/main/icons/pytorch-logo.png" alt="Algorithm icon">
  <h1 align="center">train_torchvision_resnet</h1>
</div>
<br />
<p align="center">
    <a href="https://github.com/Ikomia-hub/train_torchvision_resnet">
        <img alt="Stars" src="https://img.shields.io/github/stars/Ikomia-hub/train_torchvision_resnet">
    </a>
    <a href="https://app.ikomia.ai/hub/">
        <img alt="Website" src="https://img.shields.io/website/http/app.ikomia.ai/en.svg?down_color=red&down_message=offline&up_message=online">
    </a>
    <a href="https://github.com/Ikomia-hub/train_torchvision_resnet/blob/main/LICENSE.md">
        <img alt="GitHub" src="https://img.shields.io/github/license/Ikomia-hub/train_torchvision_resnet.svg?color=blue">
    </a>    
    <br>
    <a href="https://discord.com/invite/82Tnw9UGGc">
        <img alt="Discord community" src="https://img.shields.io/badge/Discord-white?style=social&logo=discord">
    </a> 
</p>

Train ResNet classification models.

![Rock paper scissors](https://uploads-ssl.webflow.com/645cec60ffb18d5ebb37da4b/64e480470f4a9d7b0a3198fb_Picture23-p-800.jpg)



## :rocket: Use with Ikomia API

#### 1. Install Ikomia API

We strongly recommend using a virtual environment. If you're not sure where to start, we offer a tutorial [here](https://www.ikomia.ai/blog/a-step-by-step-guide-to-creating-virtual-environments-in-python).

```sh
pip install ikomia
```

#### 2. Create your workflow


```python
from ikomia.dataprocess.workflow import Workflow

# Init your workflow
wf = Workflow()    

# Add dataset loader
data_loader = wf.add_task(name="dataset_classification")
data_loader.set_parameters({"dataset_folder": "path/to/dataset/folder"}) 

# Add train algorithm 
train = wf.add_task(name="train_torchvision_resnet", auto_connect=True)

# Launch your training on your data
wf.run()
```

## :sunny: Use with Ikomia Studio

Ikomia Studio offers a friendly UI with the same features as the API.

- If you haven't started using Ikomia Studio yet, download and install it from [this page](https://www.ikomia.ai/studio).

- For additional guidance on getting started with Ikomia Studio, check out [this blog post](https://www.ikomia.ai/blog/how-to-get-started-with-ikomia-studio).

## :pencil: Set algorithm parameters

- **model_name** (str) - default 'resnet18': Name of the pre-trained model. Other models available:
    - resnet34
    - resnet50
    - resnet101
    - resnet152

- **epochs** (int) - default '15': Number of complete passes through the training dataset.
- **batch_size** (int) - default '8': Number of samples processed before the model is updated.
- **learning_rate** (float) - default '0.001': Step size at which the model's parameters are updated during training.
- **weight_decay** (float) - default '1e-4': Amount of weight decay, regularization method.
- **momentum** (float) - default '0.9: Optimization technique that accelerates convergence.
- **input_size** (int) - default '224': Size of the input image.
- **export_pth** (bool) - default 'True'
- **export_onnx** (bool) - default 'False'
- **output_folder** (str, *optional*): path to where the model will be saved. 
- **num_workers** (int) - default '0': How many parallel subprocesses you want to activate when you are loading all your data during your training or validation. 


**Parameters** should be in **strings format**  when added to the dictionary.

```python
from ikomia.dataprocess.workflow import Workflow

# Init your workflow
wf = Workflow()    

# Add dataset loader
data_loader = wf.add_task(name="dataset_classification")
data_loader.set_parameters({"dataset_folder": "path/to/dataset/folder"}) 

# Add train algorithm 
train = wf.add_task(name="train_torchvision_resnext", auto_connect=True)
train.set_parameters({
    "model_name": 'resnet18',
    "batch_size": "8",
    "epochs": "5",
    "input_size": "240",
    "momentum": "0.9",
    "learning_rate": "0.001",
    "weight_decay": "1e-4",
    "export_pth": "True",
    "export_onnx": "False",
}) 

# Launch your training on your data
wf.run()
```
