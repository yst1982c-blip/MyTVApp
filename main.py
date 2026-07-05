import webview

# 频道列表（官网地址）
CHANNELS = [
    {"name": "CCTV-1", "url": "https://tv.cctv.com/live/cctv1/"},
    {"name": "CCTV-2", "url": "https://tv.cctv.com/live/cctv2/"},
    {"name": "CCTV-3", "url": "https://tv.cctv.com/live/cctv3/"},
    {"name": "CCTV-4", "url": "https://tv.cctv.com/live/cctv4/"},
    {"name": "CCTV-5", "url": "https://tv.cctv.com/live/cctv5/"},
    {"name": "CCTV-6", "url": "https://tv.cctv.com/live/cctv6/"},
    {"name": "CCTV-7", "url": "https://tv.cctv.com/live/cctv7/"},
    {"name": "CCTV-8", "url": "https://tv.cctv.com/live/cctv8/"},
]

# 全局变量
windows = []
current_index = 0

class Api:
    """暴露给 JavaScript 的 API"""
    def switch(self, index):
        global current_index
        if not (0 <= index < len(windows)):
            return f"频道 {index} 无效"
        
        # 隐藏当前窗口
        if windows[current_index]:
            windows[current_index].hide()
        
        # 显示目标窗口
        windows[index].show()
        
        # 注入 JS 自动全屏播放（延迟执行）
        def inject_fullscreen():
            import time
            time.sleep(0.5)  # 等待页面渲染
            windows[index].evaluate_js("""
                (function() {
                    var video = document.querySelector('video');
                    if (video) {
                        video.muted = true;
                        video.play().catch(e => console.log(e));
                        if (video.requestFullscreen) video.requestFullscreen();
                    }
                })();
            """)
        import threading
        threading.Thread(target=inject_fullscreen, daemon=True).start()
        
        current_index = index
        return f"切换到 {CHANNELS[index]['name']}"

def main():
    api = Api()
    
    # 1. 创建频道窗口（第一个显示，其他隐藏）
    for i, ch in enumerate(CHANNELS):
        win = webview.create_window(
            title=ch["name"],
            url=ch["url"],
            hidden=(i != 0),          # 只有第一个不隐藏
            width=1280,
            height=720,
            resizable=True,
            confirm_close=False,
            js_api=api,
        )
        windows.append(win)
    
    # 2. 控制窗口 HTML
    control_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body { font-family: Arial, sans-serif; background: #1a1a1a; color: white; padding: 20px; margin: 0; }
            h2 { margin-top: 0; text-align: center; }
            .btn-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
            .btn {
                background: #333; border: none; color: white; padding: 12px;
                border-radius: 8px; cursor: pointer; font-size: 14px;
                transition: background 0.2s;
            }
            .btn:hover { background: #555; }
            .btn:active { background: #777; }
            #status { text-align: center; margin-top: 15px; color: #aaa; }
        </style>
    </head>
    <body>
        <h2>📺 频道列表</h2>
        <div class="btn-grid" id="buttons"></div>
        <div id="status">点击切换</div>
        <script>
            const channels = """ + str([ch["name"] for ch in CHANNELS]) + """;
            const container = document.getElementById('buttons');
            channels.forEach((name, idx) => {
                const btn = document.createElement('button');
                btn.className = 'btn';
                btn.textContent = name;
                btn.onclick = function() {
                    document.getElementById('status').textContent = '切换中...';
                    window.pywebview.api.switch(idx).then(result => {
                        document.getElementById('status').textContent = result;
                    });
                };
                container.appendChild(btn);
            });
        </script>
    </body>
    </html>
    """
    
    # 3. 创建控制窗口（始终显示）
    control_window = webview.create_window(
        title="频道控制",
        html=control_html,
        width=320,
        height=500,
        resizable=False,
        confirm_close=False,
        hidden=False,
        js_api=api,
    )
    
    # 4. 启动主循环（阻塞）
    webview.start(debug=True)

if __name__ == "__main__":
    main()