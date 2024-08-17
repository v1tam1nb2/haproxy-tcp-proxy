# haproxy-tcp-proxy

HAProxyによるTCPプロキシ

# Quick Start

```bash
git clone https://github.com/v1tam1nb2/haproxy-tcp-proxy.git
cd haproxy-tcp-proxy
docker compose up -d
```

接続確認

```bash
python test.py
```
```
[('INFORMATION_SCHEMA',), ('default',), ('information_schema',), ('system',)]
```
