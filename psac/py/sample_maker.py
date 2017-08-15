
# coding: utf-8

# In[5]:


import os
import numpy as np
import tools


# In[6]:


def make_front_and_back_examples(in_dir, out_dir):
    """生成每个样本的正面和背面两个角度的图像矩阵
    """
    for f in os.listdir(in_dir):
        fp = os.path.join(in_dir, f)
        fn = f.split('.')[0]
    
        data = tools.read_data(fp)
        np.save(os.path.join(out_dir, fn + '_front.npy'), np.rot90(data[:,:,0]))
        np.save(os.path.join(out_dir, fn + '_back.npy'), np.rot90(data[:,:,31]))


# In[9]:


def make_region_examples(in_idr, out_dir, x1, x2, y1, y2):
    """生成区域样本，输入为make_front_and_back_examples输出的正面图和背面图
    """
    for f in os.listdir(in_path):
        data = np.load(os.path.join(in_path, f))
        if 'back' in f:
            # 背面图像需要做水平翻转，统一坐标系
            data = np.fliplr(data)
        np.save(os.path.join(out_dir, fi), data[x1:x2,y1:y2])


# In[15]:


def make_binary_one_hot_labels(in_file, out_file, zone_num):
    li = []
    with open(in_file, 'r') as f:
        first = True
        for line in f:
            if first == True:
                first = False
                continue
            line = line.strip()
            tmp, target = line.split(',')
            sid, zone = tmp.split('_')
            if zone != 'Zone' + str(zone_num):
                continue
            if target == '0':
                li.append([1,0])
            else:
                li.append([0,1])
    a = np.array(li)
    np.save(out_file, a)

