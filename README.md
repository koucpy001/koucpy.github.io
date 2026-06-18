# MyNav - 个人综合网址导航

基于 [WebStack](https://github.com/WebStackPage/WebStackPage.github.io) 开源项目搭建的个人导航站。

## 分类

- **常用推荐** - 日常高频使用的网站
- **效率工具** - 搜索引擎、邮箱、云盘、笔记、在线文档
- **开发工具** - 代码托管、前端/后端开发、云服务、实用工具
- **社区资讯** - 技术社区、新闻资讯、博客平台
- **学习资源** - 在线课程、编程学习、文档参考

## 自定义

### 修改网站信息
编辑 `cn/index.html` 中的网站卡片，格式：
```html
<div class="col-sm-3">
  <div class="xe-widget xe-conversations box2 label-info"
       onclick="window.open('https://网址', '_blank')"
       data-toggle="tooltip" data-placement="bottom" title=""
       data-original-title="https://网址">
    <div class="xe-comment-entry">
      <a class="xe-user-img">
        <img data-src="../assets/images/logos/图标.png" class="lozad img-circle" width="40">
      </a>
      <div class="xe-comment">
        <a href="#" class="xe-user-name overflowClip_1">
          <strong>网站名称</strong>
        </a>
        <p class="overflowClip_2">网站描述</p>
      </div>
    </div>
  </div>
</div>
```

### 添加图标
图标放在 `assets/images/logos/` 下，尺寸 120x120px。

### 部署
推送到 GitHub 仓库 `用户名.github.io`，在 Settings → Pages 中启用 GitHub Pages。

## 致谢

- [WebStack](https://github.com/WebStackPage/WebStackPage.github.io) - 原始项目
- [Viggo](https://www.viggoz.com) - 原作者

## License

MIT
