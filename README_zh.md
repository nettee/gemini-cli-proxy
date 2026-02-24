# Gemini CLI Proxy

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Mentioned in Awesome Gemini CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/Piebald-AI/awesome-gemini-cli)

将 Gemini CLI 包装成 OpenAI 兼容的 API 服务，让你能够通过 API 享受免费的 Gemini 2.5 Pro 模型！

[English](./README.md) | [简体中文](./README_zh.md)

## ✨ 特性

- 🔌 **OpenAI API 兼容**：实现 `/v1/chat/completions` 端点
- 🚀 **快速安装**：通过 `uvx` 零配置运行
- ⚡ **高性能**：基于 FastAPI + asyncio，支持并发请求

如果你想知道这个工具的原理，可以阅读[我的博客文章](https://www.nettee.io/blog/gemini-cli-proxy)。

## 🚀 快速开始

### 网络配置

由于 Gemini 需要访问 Google 服务，在某些网络环境下可能需要配置终端代理：

```bash
# 配置代理（根据你的代理服务器地址调整）
export https_proxy=http://127.0.0.1:7890
export http_proxy=http://127.0.0.1:7890  
export all_proxy=socks5://127.0.0.1:7890
```

### 安装 Gemini CLI

安装 Gemini CLI
```bash
npm install -g @google/gemini-cli
```

安装后，使用 `gemini` 命令运行 Gemini CLI。你需要首先启动一次，进行登录等初始化配置。

配置完成后，请确认你可以成功运行以下命令：

```bash
gemini -p "Hello, Gemini"
```

### 启动 Gemini CLI Proxy

方法一：直接启动运行
```bash
uvx gemini-cli-proxy
```

方法二：克隆本仓库，然后运行：
```bash
uv run gemini-cli-proxy
```

Gemini CLI Proxy 默认监听 `8765` 端口，你可以通过 `--port` 参数自定义启动端口。

启动后，使用 curl 测试服务是否正常：

```bash
curl http://localhost:8765/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer dummy-key" \
  -d '{
    "model": "gemini-2.5-pro",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

### 调用示例

#### OpenAI 客户端

```python
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:8765/v1',
    api_key='dummy-key'  # 可填任意字符串
)

response = client.chat.completions.create(
    model='gemini-2.5-pro',
    messages=[
        {'role': 'user', 'content': 'Hello!'}
    ],
)

print(response.choices[0].message.content)
```

#### Cherry Studio

在 Cherry Studio 设置中添加 Model Provider：
- Provider Type 选择: OpenAI
- API Host 填写: `http://localhost:8765`
- API Key 填写: 可填任意字符串
- Model Name 填写: `gemini-2.5-pro` 或 `gemini-2.5-flash`

![Cherry Studio Config 1](./img/cherry-studio-1.jpg)

![Cherry Studio Config 2](./img/cherry-studio-2.jpg)

## ⚙️ 配置选项

查看命令行参数：

```bash
gemini-cli-proxy --help
```

可用选项：
- `--host`: 服务器主机地址 (默认: 127.0.0.1)
- `--port`: 服务器端口 (默认: 8765)
- `--rate-limit`: 每分钟最大请求数 (默认: 60)
- `--max-concurrency`: 最大并发子进程数 (默认: 4)
- `--timeout`: Gemini CLI 命令超时时间，单位秒 (默认: 30.0)
- `--debug`: 启用调试模式 (启用调试日志和文件监控)

## ❓ 常见问题

### Q: 请求一直超时怎么办？

A: 这通常是网络连接问题。Gemini 需要访问 Google 服务，在某些地区可能需要配置代理：

```bash
# 配置代理（根据你的代理服务器调整）
export https_proxy=http://127.0.0.1:7890
export http_proxy=http://127.0.0.1:7890
export all_proxy=socks5://127.0.0.1:7890

# 然后启动服务
uvx gemini-cli-proxy
```

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！
