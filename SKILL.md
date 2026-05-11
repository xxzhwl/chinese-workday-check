---
name: chinese-workday-check
description: 查询某天是否为中国的法定工作日（含调休补班）
category: productivity
---

# 中国法定工作日查询 (Chinese Workday Check)

使用 [NateScarlet/holiday-cn](https://github.com/NateScarlet/holiday-cn) 开源数据，数据源自国务院官网公告。

## 用法

```bash
python3 is_workday.py [YYYY-MM-DD]
```

- 不加参数：检查今天
- exit 0 = 是工作日，exit 1 = 不是工作日

## 数据源

```
https://raw.githubusercontent.com/NateScarlet/holiday-cn/master/{年份}.json
```

格式示例：
```json
{"name": "元旦", "date": "2026-01-01", "isOffDay": true}
```

## 判断逻辑

1. 在列表中：isOffDay=true → 非工作日（放假），isOffDay=false → 工作日（补班）
2. 不在列表中：周一~五 → 工作日，周末 → 非工作日
3. 网络异常回退到普通周判断
