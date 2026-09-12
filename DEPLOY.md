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

**线上地址：https://dianju-fanyi.pages.dev**
（项目名 `dianju-fanyi`，Account `waterbob662@gmail.com` / `3ed3b534b4c06cafb74a56e9ce48b802`）

### 更新站点

**目前没有接 Git 自动构建，每次改动要手动传一次：**

```bash
cd "C:/Users/Joseph/Downloads/点句翻译"
export HTTPS_PROXY=http://127.0.0.1:7890 HTTP_PROXY=http://127.0.0.1:7890
WR=~/AppData/Local/npm-cache/_npx/32026684e21afda6/node_modules/wrangler/bin/wrangler.js
node $WR pages deploy site --project-name=dianju-fanyi --branch=main --commit-dirty=true
```

wrangler 按文件哈希增量上传，只传改动的文件。命令结束会打印本次部署的预览地址
（`<hash>.dianju-fanyi.pages.dev`）。

### 当初创建项目的那条命令（已执行过，勿重复）

```bash
node $WR pages project create dianju-fanyi --production-branch=main --force
```

`--force` 是**必须的**，且只在创建时需要一次。原因见下。

### 关键坑：wrangler 4.131.1 会把 Pages 命令「委派」给 Workers

新版 wrangler 把 Pages 并入 Workers，`pages project create` 默认会委派过去，
转去读 Workers 的 `assets` 配置键，没有就报：

```
✘ [ERROR] Missing entry-point to Worker script or to assets directory
```

**`--force` 绕过委派、直连真正的 Pages。** 项目建好后就不需要了
（wrangler 会提示 "this is the only time you need --force"）。
注意 `pages deploy` 不需要 `--force`，已实测。

### 为什么必须是 Pages 而不是 Workers

**Workers 的默认域名形如 `<worker名>.<账号子域>.workers.dev`，账号子域是结构的一部分，
去不掉**（本账号是 `waterbob662`）。用户明确不想暴露它。
Pages 是 `<项目名>.pages.dev`，**不含账号子域**。

另外 `workers.dev` 在国内被 DNS 污染（实测解析到 `208.77.47.172` / `face:b00c`，
是 Facebook 的地址段），访客大概率打不开；`pages.dev` 解析正常。

### 那个失败的 Worker 项目（同名 `dianju-fanyi`）

控制台里另有一个**同名 Worker**，连了 Git、每次 push 都构建失败。日志：

```
✘ Authentication error [code: 10000]
📎 It looks like you are authenticating Wrangler via a custom API token set in an environment variable.
```

它是 **Workers Builds**（构建机路径 `/opt/buildhome`），用的构建 token 没有 Pages 权限，
且 deploy 命令是 `npx wrangler versions upload`（只上传预览版本，不发布生产）。
**这条路走不通，别再在控制台里试。** 待用户自行删除。

注意它和 Pages 项目**同名但不冲突**（不同命名空间），线上 200 的是 Pages 那个。

### 没有 `wrangler.jsonc`，这是有意的

项目里**不放** wrangler 配置文件。原因：

- `wrangler pages deploy` **完全不读它** —— 静态目录由命令行参数给出
  （`--help` 里没有任何 `--config` 类选项），配置文件对本项目的部署毫无作用。
- 它却会**误导 Workers 命令**：`wrangler deploy` / `wrangler versions upload`
  只认 `assets.directory`，读到 Pages 的 `pages_build_output_dir` 会当没有静态目录，
  报出 "Missing entry-point to Worker script or to assets directory"。
  （曾用过一版 Pages 方言的 `wrangler.jsonc`，2026-09-12 已删除。）
- 控制台里那个 Worker 每次构建都会去读它，留着等于持续误导。

将来若真要走 Workers 或让 Pages 接 Git 自动构建，**再说** —— 届时按当时的
wrangler 版本重新确认该写哪个键，不要照抄已删除的那版。
（Pages 的 Git 集成也可以在控制台 UI 里直接填构建命令与输出目录，不需要配置文件。）

## 验证

```bash
cd work/test
node live.js        # 真实浏览器打开**线上**站点，验证渲染/点句/切篇（走代理）
node httpsmoke.js   # 本地起 http 服务验证（Pages 走 http，非 file://）
node inline.js      # 就地展开等交互
node e2e.js         # 渲染与数据一致性
```

`live.js` / `httpsmoke.js` 是必要的补充：项目此前的验证**全在 `file://` 下做**，
而 Pages 走 `https://`。上线前实测线上站点，`errors` 应为空数组。

## 本机 wrangler

不必重新下载（npm registry 直连会卡死），已在缓存：

```bash
WR=~/AppData/Local/npm-cache/_npx/32026684e21afda6/node_modules/wrangler/bin/wrangler.js
```

版本 4.131.1。所有联网命令都要先 `export HTTPS_PROXY=http://127.0.0.1:7890`，
否则超时（`wrangler whoami`、`deploy --dry-run` 都要联网）。

登录凭据在 `~/AppData/Roaming/xdg.config/.wrangler/config/default.toml`，
OAuth token 会**自动续期**（有过期时间但无需手动重登），含 `pages:write` 权限。
