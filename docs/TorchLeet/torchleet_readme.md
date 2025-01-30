# Challenge
A compilation of my journey working through the problems on TorchLeet covering day count, task, gaps, key learnings and references

# Progress table

A structured, day-by-day track of "what was done". Each day includes:

---

| **Day** | **Task** | **Gaps** | **Key Learnings** | **Resource Suggestions**|
|:------:|:-----:|:--------:|:-------:|:---:|
| **1**  | Implement Linear Regression (Easy)| Custom loss function definition |- Linear regression is linear in parameters and not necessarily in the input features, a perfectly fine linear regression model $\beta _1 X_1 + \beta _2 {X_1}^2 + \beta_3 X_1 X_2$ <br /> - For multiple output regression, multiple heads are used | |
|**2**| Write a custom Dataset and Dataloader to load from a CSV file| Ensure `dtype` of the input data and the model weights are the same, Dataset` and `DataLoader` reside in `torch.utils.data`, achieve train/test split, an element of a `DataLoader` can be extracted with `next(iter(` |- The instantiation of a `CustomDataset` class is a way to store the features and targets separately for the `__len__` and `__getitem__` methods, `__getitems__` can return any number of variables|[Pytorch official documentation](https://pytorch.org/tutorials/beginner/basics/data_tutorial.html)|
|**3**| Write a Custom Activation Function| Learnable parameters in pytorch, extracting model parameters through `model.parameters()`| Parameters defined with `nn` module are learnable, a custom function defined as `torch.tanh(x) + x` has no learnable ones||
|**4**| Implement Custom Loss Function (Huber Loss) | Performing element-wise `if` and `else` supported conditional operations on tensors, e.g. if the difference of two `1D` vectors is less than a scalar value, threshold for Huber loss| Use `map` and `torch.where` to perform the element-wise check, the `loss` class whether a custom or a built-in, they return a scalar value, typically mean|[Pytorch.where](https://pytorch.org/docs/stable/generated/torch.where.html)|
|**5**| Implement a Deep Neural Network| The `__getitem__` method return structure, `nn.Sequential` as a network, how to plot a surface plot to show the input data, difference between `unsqueeze` and `view`|For a custom dataset class, the `__getitem__` method return a training example and its corresponding label at a given index, a custom loss is typically defined with a `nn.Module` and has a `forward` method that expects predicitons and true labels and returns a scalar value|[Excellent discussion on view and unsqueeze](https://discuss.pytorch.org/t/what-is-the-difference-between-view-and-unsqueeze/1155/6)|
|**6**|Visualize Training Progress with TensorBoard in PyTorch|`tensorboard` setup and concepts, methods of `SummaryWriter`|`tensorboard` is a great ML observability tool, lets one track ML runs and their vitals.|[Neptune Tensorboard Tutorial](https://neptune.ai/blog/tensorboard-tutorial), [SummaryWriter Class](https://github.com/pytorch/pytorch/blob/v2.6.0/torch/utils/tensorboard/writer.py#L172)|