# 中国法定工作日查询 (Chinese Workday Check)

查询某天是否为中国的法定工作日（含调休补班）。

数据来源 [NateScarlet/holiday-cn](https://github.com/NateScarlet/holiday-cn)，源自国务院官网公告。

## 使用方法

```bash
# 检查今天
python3 is_workday.py

# 检查指定日期
python3 is_workday.py 2026-05-11
```

### 退出码

- `exit 0` = 是工作日
- `exit 1` = 不是工作日

### 输出示例

```
2026-05-11 workday=True reason=normal weekday
2026-01-01 workday=False reason=holiday: 元旦
2025-01-26 workday=True reason=makeup workday: 春节
```

## 判断逻辑

1. 日期在法定节假日列表中：
   - `isOffDay: true` → 非工作日（放假）
   - `isOffDay: false` → 工作日（调休补班）
2. 日期不在列表中：
   - 周一至周五 → 工作日
   - 周六日 → 非工作日
3. 网络异常时回退到普通周一到周五判断

## License

MIT
