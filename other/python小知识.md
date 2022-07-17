## Tensorflow

###  动态的给变量tf.Variable赋值

如果只需要给Variable赋值一次，可以通过assign这样进行赋值。

```python
x = tf.Variable(0)
y = tf.assign(x,1)
```

