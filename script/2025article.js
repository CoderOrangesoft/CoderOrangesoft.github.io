function start_article_page() {
    let articleId = new URLSearchParams(window.location.search).get('id');
    console.log(articleId);
    if (articleId === null) {
        articleId = 0
    }
    if (isNaN(articleId) || articleId <= 0) {
        let article = document.getElementsByClassName('article_box')[0];
        let article_html = `
            编号为 ${articleId} 的文章不存在或已删除。
        `;
        article.innerHTML += article_html;
    } else {
        start_article(articleId);
    }

    var config = {
        title: 'Orangesoft的文章库', // 标题，默认读取document.title
        desc: '推荐一篇编号为' + new URLSearchParams(window.location.search).get('id') + '的文章', // 描述, 默认读取head标签：<meta name="description" content="desc" />
        types: ['wx', 'wxline', 'qq', 'qzone', 'sina'], // 开启的分享图标, 默认为全部
        infoMap: {
            wx: {
                title: 'Orangesoft的文章库',
                desc: '推荐一篇编号为' + new URLSearchParams(window.location.search).get('id') + '的文章',
                imgUrl: 'https://cdn-community.codemao.cn/47/community/d2ViXzEwMDFfMjU1Nzk0NV8yNTU3OTQ1XzE2OTUyOTc1ODI5MDlfMTVmNjlkYzM.jpeg'
            }
        },
        fnDoShare: function(type) {
            console.log('分享类型：' + type);
        }
    };
    // 基础配置
    Mshare.init(config);
}
