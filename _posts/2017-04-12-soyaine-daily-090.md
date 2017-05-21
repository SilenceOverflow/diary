---
layout: post
title: "04-12 踩坑碎片" 
date: 2017-04-12 
category: soyainedaily 
excerpt: ""
---

解决 npm 访问反应比较慢的问题，[参考](http://www.uedbox.com/npm-install-slow-solution/)。

安装 Node 时自带的 npm 地址是 http://registry.npmjs.org，淘宝 NPM 镜像的地址是 https://registry.npm.taobao.org。使用 cnpm 的解决办法如下：

```node
// 安装 cnpm
$ npm install cnpm -g
// 或使用国内镜像
$ npm install cnpm -g --registry=https://registry.npm.taobao.org
// 安装模块
$ cpnm install [name]
// 同步模块（此步需要多等些时间）
$ cnpm sync [name]
```

最后一步成功显示完成同步的包：

```
Sync all packages done, successed: ["vue","vue-router","autoprefixer","babel-core","babel-eslint","babel-loader","babel-plugin-transform-runtime","babel-preset-env","babel-preset-stage-2","babel-register","chalk","connect-history-api-fallback","copy-webpack-plugin","css-loader","eslint","eslint-friendly-formatter","eslint-loader","eslint-plugin-html","eslint-config-standard","eslint-plugin-promise","eslint-plugin-standard","eventsource-polyfill","express","extract-text-webpack-plugin","file-loader","friendly-errors-webpack-plugin","html-webpack-plugin","http-proxy-middleware","webpack-bundle-analyzer","cross-env","karma","karma-coverage","karma-mocha","karma-phantomjs-launcher","karma-phantomjs-shim","karma-sinon-chai","karma-sourcemap-loader","karma-spec-reporter","karma-webpack","lolex","mocha","chai","sinon","sinon-chai","inject-loader","babel-plugin-istanbul","phantomjs-prebuilt","chromedriver","cross-spawn","nightwatch","selenium-server","semver","shelljs","opn","optimize-css-assets-webpack-plugin","ora","rimraf","url-loader","vue-loader","vue-style-loader","vue-template-compiler","webpack","webpack-dev-middleware","webpack-hot-middleware","webpack-merge"], failed: []
```

更新 npm 至最新版本，[参考](https://docs.npmjs.com/getting-started/installing-node)

```node
$ npm install npm@lastest -g
```

JSON 文件中的内容不支持注释。

<div style="display:none">
思路：
将 express 生成的 bin 文件夹中的入口文件 www 移出并命名为 index.js（）
</div>