# 模型凭证评估（2026-08-15 03:2x CST）

## 结论：deepseek 401 非硬阻塞（fallback 路径），每日任务不受影响
- cron 实际运行模型 = zai_auto（8/14 手动 run 实证：model=zai_auto, provider=zai, 4 任务全部执行）
- deepseek 两个 provider（4111173b / 840d2872）apiKey 相同（sk-d88...c493），实测 401 无效；系统环境变量 DEEPSEEK_API_KEY（尾 69c493）同样 401
- fallback 链（zai 402 时切 deepseek）暂时失效 → 主模型偶发 402 时任务会 error，重试可恢复
- 影响面：仅"主模型 402 偶发时的兜底"缺失；不影响正常执行

## 修复优先级：P2（增强项，非阻塞）
- 用户提供新 deepseek key（platform.deepseek.com）→ 更新 openclaw.json 两个 provider（经 gateway config.patch，受保护路径不直接写）
- 在此之前：每日搜索增长 git 管道已加固（node 读 git）；每日联盟运营哨兵脚本失败已确认产物正常

## 待用户项（唯一）：新 deepseek API key（可选，不紧急）