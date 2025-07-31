#!/usr/bin/env python3
import os

# 定义所有需要重定向的路径和文件
redirect_paths = {
    'knowledge': [
        '01-beginners-guide.html',
        '02-essential-equipment.html', 
        '03-identification-techniques.html',
        '04-best-locations.html',
        '05-behavior-observation.html',
        '06-song-identification.html',
        '07-photography-tips.html',
        '08-seasonal-guide.html',
        '09-journal-keeping.html',
        '10-ethics-conservation.html'
    ],
    'birdwatching': [
        '01-getting-started.html',
        '02-essential-equipment.html',
        '03-identification-techniques.html', 
        '04-best-locations.html',
        '05-seasonal-guide.html',
        '06-photography-tips.html',
        '07-behavior-observation.html',
        '08-song-identification.html',
        '09-ethics-conservation.html',
        '10-journal-keeping.html'
    ],
    'pet-care': [
        '01-choosing-right-bird.html',
        '02-nutrition-feeding.html',
        '03-housing-environment.html',
        '04-health-veterinary.html',
        '05-training-behavior.html',
        '06-breeding-reproduction.html',
        '07-emergency-first-aid.html',
        '08-seasonal-care.html',
        '09-enrichment-activities.html',
        '10-species-profiles.html'
    ],
    'ecology': [
        '01-habitat-ecosystems.html',
        '02-food-webs-chains.html',
        '03-migration-patterns.html',
        '04-breeding-ecology.html',
        '05-climate-change-impact.html',
        '06-urban-ecology.html',
        '07-conservation-biology.html',
        '08-island-biogeography.html',
        '09-pollination-seed-dispersal.html',
        '10-community-dynamics.html'
    ],
    'scientific-wonders': [
        '01-bird-flight-mechanics.html',
        '02-magnetic-navigation.html',
        '03-hummingbird-mechanics.html',
        '04-bird-intelligence.html',
        '05-feather-structure.html',
        '06-bird-vision.html',
        '07-egg-development.html',
        '08-bird-communication.html',
        '09-migration-physiology.html',
        '10-biomechanics.html'
    ]
}

# 重定向HTML模板
redirect_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redirecting...</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f5f5f5;
        }}
        .redirect-container {{
            text-align: center;
            padding: 2rem;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .spinner {{
            border: 4px solid #f3f3f3;
            border-top: 4px solid #3498db;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 1rem;
        }}
        @keyframes spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
    </style>
    <script>
        // 获取URL参数
        const urlParams = new URLSearchParams(window.location.search);
        const lang = urlParams.get('lang') || 'en'; // 默认英语
        
        // 立即重定向到正确的语言路径
        window.location.replace(`/${{lang}}/{section}/{filename}`);
    </script>
</head>
<body>
    <div class="redirect-container">
        <div class="spinner"></div>
        <h2>正在重定向...</h2>
        <p>如果页面没有自动跳转，请<a href="/{section}/{filename}" id="manualLink">点击这里</a></p>
    </div>
</body>
</html>'''

# 创建重定向文件
def create_redirect_files():
    for section, files in redirect_paths.items():
        # 创建目录
        os.makedirs(section, exist_ok=True)
        
        for filename in files:
            # 生成重定向HTML内容
            content = redirect_template.format(section=section, filename=filename)
            
            # 写入文件
            filepath = os.path.join(section, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Created redirect file: {filepath}")

# 创建主页面重定向文件
main_pages = [
    'knowledge.html',
    'birdwatching.html', 
    'pet-care.html',
    'ecology.html',
    'scientific-wonders.html'
]

main_redirect_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redirecting...</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f5f5f5;
        }}
        .redirect-container {{
            text-align: center;
            padding: 2rem;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .spinner {{
            border: 4px solid #f3f3f3;
            border-top: 4px solid #3498db;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 1rem;
        }}
        @keyframes spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
    </style>
    <script>
        // 获取URL参数
        const urlParams = new URLSearchParams(window.location.search);
        const lang = urlParams.get('lang') || 'en'; // 默认英语
        
        // 立即重定向到正确的语言路径
        window.location.replace(`/${{lang}}/{pagename}`);
    </script>
</head>
<body>
    <div class="redirect-container">
        <div class="spinner"></div>
        <h2>正在重定向...</h2>
        <p>如果页面没有自动跳转，请<a href="/{pagename}" id="manualLink">点击这里</a></p>
    </div>
</body>
</html>'''

def create_main_page_redirects():
    for page in main_pages:
        content = main_redirect_template.format(pagename=page)
        
        # 如果文件已存在且不是重定向文件，则跳过
        if os.path.exists(page):
            with open(page, 'r', encoding='utf-8') as f:
                existing_content = f.read()
                if 'window.location.replace' not in existing_content:
                    print(f"Skipping {page} - already exists and is not a redirect file")
                    continue
        
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Created main page redirect: {page}")

if __name__ == "__main__":
    print("Creating redirect files...")
    create_redirect_files()
    print("Creating main page redirects...")
    create_main_page_redirects()
    print("All redirect files created successfully!")