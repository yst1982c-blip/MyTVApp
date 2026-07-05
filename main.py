import webview

CHANNELS = [
    {"name": "CCTV-1", "url": "https://tv.cctv.com/live/cctv1/"},
    # ... 所有频道
]

class Api:
    def switch(self, index):
        idx = int(index)
        if 0 <= idx < len(CHANNELS):
            window.evaluate_js(f"window.location.href = '{CHANNELS[idx]['url']}'")
            return f"切换到 {CHANNELS[idx]['name']}"
        return "无效频道"

def main():
    global window
    api = Api()
    window = webview.create_window(
        title="电视直播",
        url=CHANNELS[0]["url"],
        width=1280,
        height=720,
        js_api=api,
    )
    webview.start(debug=True)

if __name__ == "__main__":
    main()
