import os
import shutil
from bs4 import BeautifulSoup

# ================= 配置区域 =================
INPUT_HTML = 'index.html'          # 你的原始 HTML 文件名
OUTPUT_HTML = 'index_updated.html' # 生成的新 HTML 文件名
ASSETS_DIR = 'assets'
IMG_DIR = os.path.join(ASSETS_DIR, 'images')
VID_DIR = os.path.join(ASSETS_DIR, 'videos')

# 创建目标文件夹
os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(VID_DIR, exist_ok=True)
# ============================================

def process_files():
    # 1. 读取 HTML 文件
    with open(INPUT_HTML, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # 2. 删除所有 class="media-overlay" 的元素
    overlays = soup.find_all(class_='media-overlay')
    for overlay in overlays:
        overlay.decompose() # 完全移除该标签及其内容
    print(f"✅ 已删除 {len(overlays)} 个 'media-overlay' 元素。")

    # 用于记录已经处理过的文件，避免同一个文件（如 spinner.svg）被重复复制多次
    processed_images = {}
    processed_videos = {}
    
    img_counter = 1
    vid_counter = 1

    # 3. 处理所有图片 (<img> 的 src 和 <video> 的 poster)
    # 3.1 处理 <img> 标签
    for img in soup.find_all('img'):
        src = img.get('src')
        if src and not src.startswith(('http://', 'https://', 'data:')):
            if src not in processed_images:
                ext = os.path.splitext(src)[1] # 获取后缀名 (如 .png)
                new_filename = f"{img_counter}{ext}"
                new_filepath = os.path.join(IMG_DIR, new_filename)
                
                # 复制文件
                if os.path.exists(src):
                    shutil.copy2(src, new_filepath)
                else:
                    print(f"⚠️ 警告: 找不到图片文件 {src}")
                
                processed_images[src] = f"{ASSETS_DIR}/images/{new_filename}"
                img_counter += 1
            
            # 更新 HTML 中的路径
            img['src'] = processed_images[src]

    # 3.2 处理 <video> 的 poster 属性 (通常是封面图)
    for video in soup.find_all('video'):
        poster = video.get('poster')
        if poster and not poster.startswith(('http://', 'https://', 'data:')):
            if poster not in processed_images:
                ext = os.path.splitext(poster)[1]
                new_filename = f"{img_counter}{ext}"
                new_filepath = os.path.join(IMG_DIR, new_filename)
                
                if os.path.exists(poster):
                    shutil.copy2(poster, new_filepath)
                else:
                    print(f"⚠️ 警告: 找不到封面图文件 {poster}")
                
                processed_images[poster] = f"{ASSETS_DIR}/images/{new_filename}"
                img_counter += 1
            
            video['poster'] = processed_images[poster]

    print(f"✅ 已处理并复制 {len(processed_images)} 张不重复的图片到 {IMG_DIR}。")

    # 4. 处理所有视频 (<video> 的 src)
    for video in soup.find_all('video'):
        src = video.get('src')
        if src and not src.startswith(('http://', 'https://', 'data:')):
            if src not in processed_videos:
                ext = os.path.splitext(src)[1] # 获取后缀名 (如 .mp4)
                new_filename = f"{vid_counter}{ext}"
                new_filepath = os.path.join(VID_DIR, new_filename)
                
                # 复制文件
                if os.path.exists(src):
                    shutil.copy2(src, new_filepath)
                else:
                    print(f"⚠️ 警告: 找不到视频文件 {src}")
                
                processed_videos[src] = f"{ASSETS_DIR}/videos/{new_filename}"
                vid_counter += 1
            
            # 更新 HTML 中的路径
            video['src'] = processed_videos[src]

    print(f"✅ 已处理并复制 {len(processed_videos)} 个不重复的视频到 {VID_DIR}。")

    # 5. 保存修改后的 HTML
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        # str(soup) 可以最大程度保留原有的 HTML 格式
        f.write(str(soup))
    
    print(f"🎉 处理完成！新的 HTML 已保存为: {OUTPUT_HTML}")

if __name__ == "__main__":
    process_files()