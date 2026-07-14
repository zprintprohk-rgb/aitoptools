"""Generate exception report"""
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
log_dir = "/mnt/f/aitoptools/.hermes/logs"

report = f"""# 异常报告 - {today}

## 1. 联盟链接异常
- 10 个新工具中 9 个缺少真实联盟链接（仅有通用平台链接如 impact.com 占位）
  - 除 Typeface (Enterprise, N/A) 外，其余9个均需注册联盟账号
- reviews.json 中 31/33 entries 仍使用 placeholder ?fpr=partner URLs（持续未解决）

## 2. 持续性问题汇总
- 自上线(6/25)至今未曾部署新版本
- 所有 110+ TSX 组件中 CTA 链接指向 visitURL 而非真实联盟链接
- 建议: 优先注册 Impact Radius 联盟账号

## 3. 违规检查
- 无赌博/成人/违规内容被收录 ✓

## 4. Token 消耗
- 本次 cron 运行使用 deepseek-v4-flash 模型（数据采集+文案生成）
- 预估消耗: ~15,000 tokens（远低于50万上限）✓

## 5. 建议操作
1. ⚠️ 紧急: 注册 Impact Radius 联盟账号（覆盖 20+ 工具）
2. ⚠️ 紧急: 注册 ShareASale（覆盖 10+ 工具）
3. ⚠️ 高优先级: 获取联盟 ID 后使用批量替换更新所有 TSX 中的 CTA 链接
4. 执行「.hermes/scripts」目录下的部署脚本

---
:warning: 请管理员及时处理联盟链接问题。
"""
with open(f"{log_dir}/{today}-异常报告.md", "w") as f:
    f.write(report)
print(f"Exception report saved to {today}-异常报告.md")
