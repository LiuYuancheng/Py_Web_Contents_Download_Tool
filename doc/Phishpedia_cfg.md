# Phishpedia Ubuntu 20.04 Config

[TOC]

##### Execution Env

Ubuntu 20.04 

python 3.8 64bit



------

##### Steps to config phishpedia without Nvidia driver installed(CPU mode)

###### 1. Install python3.7 (optional)

https://stackoverflow.com/questions/61430166/python-3-7-on-ubuntu-20-04/61430652



###### 2. Install torch 1.7 (only for CPU)

```
pip install torch==1.8.1+cpu torchvision==0.8.2+cpu torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
```

Install torch 1.6 (not use this)

```
pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

https://pytorch.org/get-started/previous-versions/
```

**2.1 Problem 1**: Detectron 2 offical not support torch 1.6 any more: 

```
ERROR: Command errored out with exit status 1:
     command: /usr/bin/python3 -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-req-build-zbirp7v7/setup.py'"'"'; __file__='"'"'/tmp/pip-req-build-zbirp7v7/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /tmp/pip-req-build-zbirp7v7/pip-egg-info
         cwd: /tmp/pip-req-build-zbirp7v7/
    Complete output (7 lines):
    /usr/lib/python3/dist-packages/requests/__init__.py:89: RequestsDependencyWarning: urllib3 (1.26.7) or chardet (3.0.4) doesn't match a supported version!
      warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-req-build-zbirp7v7/setup.py", line 14, in <module>
        assert torch_ver >= [1, 8], "Requires PyTorch >= 1.8"
    AssertionError: Requires PyTorch >= 1.8
ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
```

**Solution:** install torch==1.7.1+cpu



###### 3. Install Detectron-2 for CPU only 

use the offical pre-build 

```
pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.8/index.html
```



###### 4.Enabled the Phishpedia CPU config 

File: Phishpedia/src/detectron2_pedia line 47: 

```
# uncomment if you installed detectron2 cpu version
# cfg.MODEL.DEVICE = 'cpu'
```



###### 5. Run the program

```
python3 phishpedia_main.py --folder ./datasets/test_sites --results./test.txt
```

Problem 5.1 : error: 

```


det (3.0.4) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "
Traceback (most recent call last):
  File "phishpedia_main.py", line 1, in <module>
    from phishpedia_config import *
  File "/home/yc/Project/Phishpedia/phishpedia_config.py", line 8, in <module>
    ele_model = config_rcnn(cfg_path, weights_path, conf_threshold=0.05)
  File "/home/yc/Project/Phishpedia/src/detectron2_pedia/inference.py", line 49, in config_rcnn
    predictor = DefaultPredictor(cfg)
  File "/home/yc/.local/lib/python3.8/site-packages/detectron2/engine/defaults.py", line 288, in __init__
    checkpointer.load(cfg.MODEL.WEIGHTS)
  File "/home/yc/.local/lib/python3.8/site-packages/detectron2/checkpoint/detection_checkpoint.py", line 52, in load
    ret = super().load(path, *args, **kwargs)
  File "/home/yc/.local/lib/python3.8/site-packages/fvcore/common/checkpoint.py", line 155, in load
    checkpoint = self._load_file(path)
  File "/home/yc/.local/lib/python3.8/site-packages/detectron2/checkpoint/detection_checkpoint.py", line 88, in _load_file
    loaded = super()._load_file(filename)  # load native pth checkpoint
  File "/home/yc/.local/lib/python3.8/site-packages/fvcore/common/checkpoint.py", line 252, in _load_file
    return torch.load(f, map_location=torch.device("cpu"))
  File "/home/yc/.local/lib/python3.8/site-packages/torch/serialization.py", line 593, in load
    return _legacy_load(opened_file, map_location, pickle_module, **pickle_load_args)
  File "/home/yc/.local/lib/python3.8/site-packages/torch/serialization.py", line 762, in _legacy_load
    magic_number = pickle_module.load(f, **pickle_load_args)
_pickle.UnpicklingError: invalid load key, 'v'.
```

**Solution**: Download all the model again(one by one, not use the google drive zip) because the zip will may make the file damaged. 

solution reference link: https://github.com/YBIGTA/pytorch-hair-segmentation/issues/38

------

##### Execution result

python3 phishpedia_main.py --folder ./datasets/test_sites --results ./test.txt
/usr/lib/python3/dist-packages/requests/__init__.py:89: RequestsDependencyWarning: urllib3 (1.26.7) or chardet (3.0.4) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "
The checkpoint state_dict contains keys that are not used by the model:
  pixel_mean
  pixel_std
Load protected logo list
  0%|                                                                                            | 0/277 [00:00<?, ?it/s][W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.
  3%|██▍                                                                                 | 8/277 [00:08<04:54,  1.09s/it]/home/yc/.local/lib/python3.8/site-packages/PIL/Image.py:975: UserWarning: Palette images with Transparency expressed in bytes should be converted to RGBA images
  warnings.warn(
100%|██████████████████████████████████████████████████████████████████████████████████| 277/277 [08:22<00:00,  1.81s/it]
Finish loading protected logo list
(3066, 2048)
  0%|                                                                                              | 0/1 [00:00<?, ?it/s]accounts.g.cdcde.com
Entering phishpedia
plot
Entering siamese
number of logo boxes: 1
Response:  <Response [403]>
VTScan is not working...
100%|██████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:06<00:00,  6.14s/it]
yc@yc-VirtualBox:~/Project/Phishpedia$ 



------

##### Questions 

**Question 1**: Is there any requirement about the screenshot file in dataset(shot.png as shown below). The screenshot needs to have the logo of the website, is that correct ? For some of my test web, if I use different web browser to open the URL, the page shows up will got a little different. Will that make any influence of the result, or you prefer us to use Google-Chrome to do the screenshot. 

**Question 2**: If we want to check some URL/web and its logo is not in the logo folder "Logo-2k"(As shown below), we should copy the logo files with different resolution in a folder and put it in the foler "Logo-2k", am I correct ? 

