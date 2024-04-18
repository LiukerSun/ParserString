# 解析类excel的字符串公式
可以在公式中使用变量，变量名统一为stage+数字或step+数字。
比如
```python
formula = "SUM(2,SUM(1,2),step2.aa.bb)"
data = {"step1": {"aa": {"bb": 1}}, "step2": {"aa": {"bb": 2}}}
```
