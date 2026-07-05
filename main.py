import webview

# 频道列表（央视官网直播）
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

class Api:
    def switch(self, index):
        """由 JavaScript 调用，切换频道 URL"""
        try:
            idx = int(index)
            if 0 <= idx < len(CHANNELS):
                url = CHANNELS[idx]["url"]
                window.evaluate_js(f"window.location.href = '{url}'")
                return f"切换到 {CHANNELS[idx]['name']}"
            else:
                return "频道索引无效"
        except Exception as e:
            return f"错误: {e}"

def main():
    global window
    api = Api()
    # 创建单个窗口，默认加载第一个频道
    window = webview.create_window(
        title="电视直播",
        url=CHANNELS[0]["url"],
        width=1280,
        height=720,
        js_api=api,
        confirm_close=False,
    )
    webview.start(debug=True)

if __name__ == "__main__":
    main()
