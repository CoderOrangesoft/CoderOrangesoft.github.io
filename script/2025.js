let Server = {
    "host": "https://orshost1.pythonanywhere.com/"
        // "host": "http://localhost:64012/"
}

let page = {
    "blog_url": "./",
    "show_banner": "https://zuoyerizhi.pythonanywhere.com/"
}


function start_index() {
    console.log("Common script [2025]");
    show_page_selector();
    showArticle();
    show_info_box();
}

function getArticleList() {
    return fetch(Server.host + "api/articles?page=" + get_current_page()).then(response => response.json());
}
/*
    example return:
    [
        {
            "id":1,
            "title":"Article 1",
            "content":"Today I will tell you something about my blo......"
        },
        {
            "id":2,
            "title":"Article 2",
            "content":"I am a programmer and I love coding. I......."
        },
        {
            "id":3,
            "title":"Article 3",
            "content":"I am a student and I love learning new things...."
        }
    ]
*/

function getArticle(id) {
    return fetch(Server.host + "api/articles/" + id).then(response => response.json());
}
/*
    example return:
    {
        "id":1
        "title":"Article 1",
        "content":"<p>Today I will tell you something about my blog.My blog is a place where I can write about my programming journey, my hobbies, and my thoughts on various topics.</p>"
    }
*/

function get_current_page() {
    let current_page = parseInt(new URL(document.location.href).searchParams.get("pageid")); // 获取当前页数
    if (isNaN(current_page) || current_page <= 1) { current_page = 1; }
    get_article_count().then(
        (result) => {
            let total_pages = parseInt(result['count']); // 获取总页数
            if (current_page > total_pages) { current_page = total_pages; } // 防止超出总页数
        }
    );
    return current_page;
}

function showArticle() {
    let article_list = getArticleList();
    article_list.then(
        result => {
            console.log('article_list', result)
            let article_box = document.getElementsByClassName("article_box")[0];
            for (let i = 0; i < result.length; i++) {
                let article = result[i];
                let show_content = (article.content.length > 15 ? article.content.substring(0, 15) + '<font style="color:lightblue;">......<font>' : article.content)
                let botton_content = `浏览 <font style="color:black;">(全文大约${article.content.length}字)</font>`;
                let article_html = `
                    <div class="article_item">
                        <h2>#${article.id}  ${article.title}</h2>
                        <p>文章预览：${show_content}</p>
                        <button onclick="enterArticle(${article.id})">${botton_content}</button>
                    </div>
                `;
                article_box.innerHTML += article_html;
            }
        }
    );
}

function enterArticle(id) {
    document.location.href = page.blog_url + 'article.html?id=' + id;
}

function start_article(id) {
    let article = getArticle(id);
    article.then(
        result => {
            console.log('article', article)
            if (result.title == 'Not Found') {
                let article = document.getElementsByClassName('article_box')[0];
                let article_html = `
                    编号为 ${id} 的文章不存在或已删除。
                `;
                article.innerHTML += article_html;
            } else {
                let article_box = document.getElementsByClassName("article_box")[0];
                let article_html = `
                <div class="article_item">
                    <h1>#${result.id}  文章标题：${result.title}</h1>
                    <p>${result.content}</p>
                </div>
            `;
                article_box.innerHTML = article_html;
            }
        }
    );
}

function show_info_box() {
    let info_box = document.getElementsByClassName("info_box")[0];
    let nowpageid = new URL(document.location.href).searchParams.get("pageid");
    if (isNaN(nowpageid) || nowpageid <= 1) {
        info_box.innerHTML += "<div class='info_item'><h4>欢迎来到我的文章库!😀</h4></div>"
        info_box.innerHTML += `<iframe style='width:100%;height:300px;' src='${page.show_banner}'></iframe>`
    } else {
        info_box.remove()
    }
}

function get_article_count() {
    return fetch(Server.host + "api/articles/count").then(response => response.json());
}

function show_page(page_num) {
    window.location.href = page.blog_url + 'index.html?pageid=' + page_num
}


function show_page_selector() {
    let page_selector = document.getElementsByClassName("page_selector")[0];
    let page_count = get_article_count()

    page_count.then(
        (result) => {
            console.log('page_count', result['count']);
            let total_pages = parseInt(result['count']); // 获取总页数
            let current_page = get_current_page(); // 获取当前页数
            // 创建分页的 HTML 内容
            let page_html = `
            <div class="page_item">
                <font>第 ${current_page} 页 /共 ${total_pages} 页</font>
                <button onclick="show_page(${current_page - 1})" ${current_page <= 1 ? 'disabled' : ''}>上一页</button>
                <button onclick="show_page(${current_page + 1})" ${current_page >= total_pages ? 'disabled' : ''}>下一页</button>
                <input type="number" value="${current_page}" id="page_jump" style="width:70px">
                <button onclick="show_page(document.getElementById('page_jump').value)">跳转</button>
            </div>
        `;

            // 将生成的分页 HTML 添加到页面中
            page_selector.innerHTML = page_html;

            // 更新按钮状态，根据当前页数和总页数
            function update_button_status() {
                // 更新各按钮的 disabled 状态
                document.querySelector("button[onclick='show_page(" + (current_page - 1) + ")']").disabled = current_page === 1;
                document.querySelector("button[onclick='show_page(" + (current_page + 1) + ")']").disabled = current_page === total_pages;
                document.getElementById("page_jump").value = current_page; // 更新输入框的当前页数
            }


            // 初始状态更新按钮
            update_button_status();
        }
    );


}
