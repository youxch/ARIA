<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=800&size=48&duration=3000&pause=1000&color=38BDF8&center=true&vCenter=true&width=500&lines=📡+ARIA;Antenna+AI+%E5%A4%A9%E7%BA%BF+AI" alt="ARIA" />

### Antenna Resonance Intelligence Architect
### 天线谐振智能设计师

**用自然语言描述你的天线，让 AI 完成剩下的一切**

---

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![CST](https://img.shields.io/badge/CST_Studio-2022-FF6B35?style=for-the-badge)](https://www.3ds.com/products/simulia/cst-studio-suite)
[![Claude](https://img.shields.io/badge/Claude-AI-CC785C?style=for-the-badge&logo=anthropic&logoColor=white)](https://anthropic.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/youxch/ARIA?style=for-the-badge&color=FBBF24&logo=github)](https://github.com/youxch/ARIA/stargazers)

<br/>

[🌐 在线演示页](https://youxch.github.io/ARIA) &nbsp;·&nbsp; [⭐ Star 支持](https://github.com/youxch/ARIA/stargazers) &nbsp;·&nbsp; [🐛 提交问题](https://github.com/youxch/ARIA/issues)

</div>

<br/>

---

## 🎯 它能做什么？

你只需要说一句话：

```
设计一个 2.45 GHz 的贴片天线，FR4 基板，优化 S11 带宽
```

ARIA 自动完成以下全部工作：

```
自然语言 → 参数解析 → CST 建模 → 电磁仿真 → 智能优化 → S11 曲线 + 最优参数
```

从描述到结果，**无需手动操作 CST，无需编写仿真脚本**。

---

## ✨ 核心亮点

<table>
<tr>
<td width="50%" valign="top">

**🤖 自然语言驱动**
- Claude AI 解析设计意图
- 支持中英文混合输入
- 参数自动补全与默认值推断

**⚡ CST 全自动仿真**
- Python API 直接调用 CST
- VBA 脚本精确建模（Pick + WCS + Port）
- 时域求解器一键运行

**📊 可视化仪表盘**
- 深色系 Streamlit 界面
- Plotly 交互式 S₁₁ 曲线
- 历史结果多曲线对比

</td>
<td width="50%" valign="top">

**🧠 三种优化算法**
- 贝叶斯 GP — 少量预算精准调谐
- 粒子群 PSO — 中等维度全局搜索
- 差分进化 GA — 高维像素天线

**📡 三类天线支持**
- 🟦 矩形贴片（Pozar 公式初始化）
- 📶 半波振子（0.235λ 自动定长）
- 🔲 像素化贴片（N×M 二值优化）

**📁 结果自动存档**
- S₁₁ CSV + 优化摘要 JSON
- 每次运行自动编号存储

</td>
</tr>
</table>

---

## 🚀 快速开始

### 环境要求

- Windows 10/11
- [CST Studio Suite 2022](https://www.3ds.com/products/simulia/cst-studio-suite)
- Python 3.8+
- Anthropic API Key

### 安装

```bash
git clone https://github.com/youxch/ARIA.git
cd ARIA
pip install -r requirements.txt
```

### 配置

```bash
cp .env.example .env
```

编辑 `.env` 文件：

```env
ANTHROPIC_API_KEY=sk-your-key-here
CST_LIB_PATH=C:\Program Files (x86)\CST Studio Suite 2022\AMD64\python_cst_libraries
```

### 启动

```bash
# 推荐：可视化界面
streamlit run app.py

# 命令行模式
python cst_antenna_ai/main.py
```

打开浏览器访问 `http://localhost:8501`

---

## 💬 使用示例

**自然语言模式（AI 对话页）：**

```
你：设计一个 5.8 GHz 的贴片天线，Rogers 4003C，最大化带宽

ARIA：已理解你的设计需求 ✅
      ┌─────────────────────────────┐
      │ 天线类型  矩形贴片天线        │
      │ 目标频率  5.80 GHz          │
      │ 基板      Rogers4003C       │
      │ εr        3.55              │
      │ 优化目标  最大化带宽          │
      │ 算法      🤖 自动选择        │
      └─────────────────────────────┘
      [🚀 确认并开始仿真]  [✏️ 重新描述]
```

**手动配置模式（表单页）：**

选择天线类型 → 设置频率和基板 → 选择优化算法 → 一键启动

---

## 🏗️ 项目结构

```
ARIA/
├── app.py                       # Streamlit 可视化界面
├── requirements.txt
├── .env.example                 # 配置模板
│
└── cst_antenna_ai/
    ├── main.py                  # 命令行入口
    ├── config.py                # 全局配置
    ├── cst_core/
    │   ├── interface.py         # CST Python API 封装
    │   └── builders/
    │       ├── patch.py         # 矩形贴片建模器
    │       ├── dipole.py        # 半波振子建模器
    │       └── pixel_patch.py   # 像素化天线建模器
    ├── llm/
    │   ├── intent_parser.py     # 自然语言 → 结构化参数
    │   └── reporter.py          # 结果 → 中文分析报告
    └── optimizer/
        ├── engine.py            # 贝叶斯 / PSO / GA 后端
        └── workflow.py          # 优化全流程编排
```

---

## 📐 支持天线类型

| 类型 | 初始化 | 优化参数 | 适用频段 |
|:---:|---|---|:---:|
| 🟦 **矩形贴片** | Pozar 传输线公式 | L, W, 馈线宽, 嵌槽深度 | 0.5–60 GHz |
| 📶 **半波振子** | 0.235λ 估算 | 臂长, 臂宽 | 0.5–30 GHz |
| 🔲 **像素化贴片** | 随机二值初始化 | N×M 像素开关 | 1–30 GHz |

---

## 🧮 优化算法对比

| 算法 | 适用场景 | 特点 |
|---|---|---|
| 🧠 **贝叶斯 GP** | 仿真耗时长、预算 < 100 次 | 样本效率最高 |
| 🐦 **粒子群 PSO** | 3–6 维、预算 ≥ 100 次 | 全局搜索能力强 |
| 🧬 **差分进化 GA** | 高维 / 离散变量（像素天线）| 鲁棒性强 |
| 🤖 **自动选择** | 不确定时使用 | 启发式推荐 |

---

## 📄 License

MIT License © 2026 [youxch](https://github.com/youxch)

---

<div align="center">

**如果这个项目对你有帮助，欢迎点一个 ⭐ Star！**

Made with ❤️ by **尤栖冲 · You Xichong**

`CST 2022` · `Claude AI` · `Python` · `Streamlit`

</div>
