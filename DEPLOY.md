# 部署

站点是**纯静态**的（见 `CLAUDE.md`），源码在 `site/`。两条部署路径：

## 一、GitHub（源码托管）

https://github.com/water-joe/dianju-fanyi

本机直连 GitHub 会被 reset，推送需走代理（7890）：

```bash
GH_TOKEN=$(gh auth token) git \
  -c http.proxy=http://127.0.0.1:7890 \
  -c https.proxy=http://127.0.0.1:7890 \
  push origin main
```

`.gitignore` 排除了 PDF 原卷（约 100MB，且涉版权）、`work/txt/` 抽取文本、
`node_modules`。仓库里只有站点 + 生成脚本，约 5MB。

## 二、Cloudflare Pages（线上站点）

**项目名 `dianju-fanyi` → https://dianju-fanyi.pages.dev**

### 首次创建

控制台 → Workers & Pages → Create → **Pages** → Connect to Git → 选
`water-joe/dianju-fanyi`。两个字段：

| 字段 | 值 |
|---|---|
| Build command | **留空**（没有打包步骤） |
| Build output directory | `site` |

`wrangler.jsonc` 里已写 `pages_build_output_dir: ./site`，控制台一般会自动带出。

### 为什么必须是 Pages 而不是 Workers

**Workers 的默认域名形如 `<worker名>.<账号子域>.workers.dev`，账号子域是结构的一部分，
去不掉**（本账号是 `waterbob662`）。Pages 是 `<项目名>.pages.dev`，**不含账号子域**。

另外 `workers.dev` 在国内被 DNS 污染（实测解析到 `208.77.47.172` / `face:b00c`，
是 Facebook 的地址段），访客大概率打不开；`pages.dev` 解析正常。

### 两个已在 `wrangler.jsonc` 上踩过的坑

1. **别把 Workers 的 `assets.directory` 写进 Pages 配置** —— 那是 Workers 语法，
   Pages 项目读到非法键会**构建失败**。Pages 用 `pages_build_output_dir`。
2. `name` 必须与控制台上的项目名一致（`dianju-fanyi`），否则配置不生效。

### 日常更新

推到 GitHub 的 `main` 会自动触发 Pages 重新构建，无需本机操作。

## 验证

```bash
cd work/test
node httpsmoke.js   # 起本地 http 服务，验证站点在 http:// 下正常（Pages 走 http，非 file://）
node inline.js      # 就地展开等交互
node e2e.js         # 渲染与数据一致性
```

`httpsmoke.js` 是个提醒：项目此前的验证**全在 `file://` 下做**，而 Pages 走 `http://`。
两者对相对路径脚本加载的行为不同，上线前值得单独跑一遍。

## 本机 wrangler（备选路径）

缓存里已有 wrangler 4.131.1，无需重新下载（npm registry 直连会卡）：

```bash
WR=~/AppData/Local/npm-cache/_npx/32026684e21afda6/node_modules/wrangler/bin/wrangler.js
node $WR pages deploy site --project-name=dianju-fanyi
```

任何 wrangler 联网命令都需要代理：

```bash
export HTTPS_PROXY=http://127.0.0.1:7890 HTTP_PROXY=http://127.0.0.1:7890
```
