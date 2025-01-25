# Challenge
A compilation of my journey working through the problems on TorchLeet covering day count, task, gaps, key learnings and references

# Progress table

A structured, day-by-day track of "what was done". Each day includes:

---

| **Day** | **Task** | **Gaps** | **Key Learnings** | **Resource Suggestions**|
|:------:|:-----:|:--------:|:-------:|:---:|
| **1**  | Implement Linear Regression (Easy)| Custom loss function definition |- Linear regression is linear in parameters and not necessarily in the input features, a perfectly fine linear regression model $\beta _1 X_1 + \beta _2 {X_1}^2 + \beta_3 X_1 X_2$ <br /> - For multiple output regression, multiple heads are used | |
|**2**| Write a custom Dataset and Dataloader to load from a CSV file| `Dataset` and `DataLoader` reside in `torch.utils.data`, achieve train/test split, an element of a `DataLoader` can be extracted with `next(iter(` |- The instantiation of a `CustomDataset` class is a way to store the features and targets separately for the `__len__` and `__getitem__` methods, `__getitems__` can return any number of variables|[Pytorch official documentation](https://pytorch.org/tutorials/beginner/basics/data_tutorial.html)|
