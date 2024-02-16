function alert_window(title, content) {
    layer.open({
        type: 1, // page 层类型
        // area: ['500px', '300px'],
        title: title,
        shade: 0.6, // 遮罩透明度
        shadeClose: true, // 点击遮罩区域，关闭弹层
        maxmin: false, // 允许全屏最小化
        anim: 0, // 0-6 的动画形式，-1 不开启
        content: content
    });
}

function show_cor_api_dialog() {
    alert_window(
        undefined,
        `
        <blockquote class="layui-elem-quote layui-text">
            COR_API正在进入dev开发阶段。
        </blockquote>
        `
    )
}

function show_title_explain() {
    alert_window(
        'explain',
        `
        <blockquote class="layui-elem-quote layui-text">
            Make everything possible. <br />
            创造一切，万物可能。
        </blockquote>
        `
    )
}

function show_forum_dialog() {
    alert_window(
        '客户端插件维护中',
        `
        &nbsp
        <br />&nbsp&nbsp&nbsp
        <strong>抱歉，</strong>我们无法提供 Orangesoft论坛 功能，此维护在2024年3月完成。
        &nbsp&nbsp&nbsp<br />
        &nbsp
        `
    )
}