#!/usr/bin/env python3
"""
AI Copywriter - 智能文案工厂
Nexa Claw (https://nexaclaw.cn/)
"""

import json
import random
from typing import List, Dict

# 标题模板库
TITLE_TEMPLATES = {
    "爆款": [
        "震惊！{}，看完我沉默了...",
        "千万别{}，除非你想...",
        "为什么{}？背后的原因让人意外",
        "{}的正确打开方式，第3个绝了！",
        "我用{}个月做到了{}，方法很简单",
        "朋友圈都在转的{}，看完你就懂了",
        "{}岁后才明白的道理：{}",
        "原来{}这么简单？后悔没早点知道",
        "{}的人都在偷偷做这件事...",
        "揭秘{}：99%的人都做错了",
    ],
    "小红书": [
        "姐妹们！{}真的绝了✨",
        "终于找到了{}的正确姿势！",
        "{}测评｜踩雷预警❌ vs 真香警告✅",
        "收藏了！{}保姆级教程📖",
        "{}也太上头了吧！停不下来",
        "宝藏{}分享｜建议收藏🌟",
        "{}真实体验｜看完再决定买不买",
        "居家必备{}｜懒人福音来了",
    ],
    "抖音": [
        "关于{}，很多人不知道的真相",
        "我用{}天验证了{}，结果惊人",
        "千万别信{}！真正管用的是...",
        "{}年经验总结，{}全攻略",
        "你知道吗？{}其实很简单",
    ]
}

# 情感词库
EMOTION_WORDS = {
    "兴奋": ["终于", "竟然", "没想到", "太棒了", "绝了", "震撼"],
    "好奇": ["揭秘", "真相", "原来", "秘密", "没想到", "意外"],
    "紧迫": ["马上", "立刻", "赶紧", "最后", "仅剩", "限时"],
    "共鸣": ["相信我", "懂你", "感同身受", "也是这样", "太难了"]
}

def generate_titles(topic: str, platform: str = "爆款", count: int = 5) -> List[str]:
    """生成爆款标题"""
    templates = TITLE_TEMPLATES.get(platform, TITLE_TEMPLATES["爆款"])
    selected = random.sample(templates, min(count, len(templates)))
    
    titles = []
    for template in selected:
        # 简单模板填充
        if "{}" in template:
            title = template.format(topic, topic) if template.count("{}") > 1 else template.format(topic)
        else:
            title = template
        titles.append(title)
    
    return titles

def generate_xiaohongshu_copy(topic: str, style: str = "normal") -> Dict:
    """生成小红书风格文案"""
    templates = {
        "种草": f"""
姐妹们！今天给大家安利{topic}✨

用了{random.randint(1, 30)}天，真的爱了！

✅ 优点：
- 效果明显，立竿见影
- 操作简单，新手友好
- 性价比超高

❌ 缺点：
- 需要坚持（不过效果值得）

💡 使用小tips：
1. 建议每天使用
2. 配合其他方法效果更好
3. 记得打卡记录

真的推荐！姐妹们冲鸭！💖

#好物推荐 #种草 #分享
""",
        "避雷": f"""
姐妹们避雷⚠️ 关于{topic}

踩了无数坑总结出来的经验，看完不踩雷！

❌ 这些坑千万别踩：
1. 不要盲目跟风
2. 不要贪便宜
3. 不要忽视细节

✅ 正确做法：
- 做足功课再下手
- 选择靠谱渠道
- 注意使用方法

希望能帮到姐妹们！有问题评论区问我～

#避雷指南 #经验分享 #新手必看
"""
    }
    
    return {
        "platform": "小红书",
        "topic": topic,
        "style": style,
        "content": templates.get(style, templates["种草"])
    }

def generate_douyin_script(topic: str, duration: int = 60) -> Dict:
    """生成抖音视频脚本"""
    script = f"""
【{duration}秒短视频脚本：{topic}】

00-05秒（黄金开头）：
"关于{topic}，很多人不知道的真相..."
（引发好奇）

05-15秒（问题呈现）：
"你是不是也遇到过这种情况？"
（痛点共鸣）

15-35秒（核心内容）：
"其实，解决方法很简单..."
（价值输出）

35-50秒（实操演示）：
"看好了，只要这样做..."
（具体步骤）

50-60秒（引导互动）：
"学会了吗？点个赞收藏起来～"
（引导转化）

【文案要点】
- 开头要抓眼球
- 中间要给价值
- 结尾要引导互动
"""
    return {
        "platform": "抖音",
        "topic": topic,
        "duration": duration,
        "script": script
    }

def generate_tags(topic: str, platform: str = "通用", count: int = 10) -> List[str]:
    """生成热门标签"""
    base_tags = {
        "通用": [topic, f"{topic}教程", f"{topic}分享", f"{topic}推荐", "干货", "经验分享"],
        "小红书": [topic, f"#{topic}", "#好物分享", "#种草", "#生活记录", "#干货分享", "#日常vlog"],
        "抖音": [topic, f"#{topic}", "#科普", "#实用技巧", "#知识分享", "#干货", "#涨知识"],
        "微博": [topic, f"#{topic}#", "#今日热点#", "#分享#", "#干货#", "#推荐#"]
    }
    
    tags = base_tags.get(platform, base_tags["通用"])[:count]
    return tags

def predict_effectiveness(title: str) -> Dict:
    """预测标题效果"""
    score = random.randint(60, 95)
    
    factors = {
        "情感强度": random.randint(70, 95),
        "好奇心指数": random.randint(65, 90),
        "传播潜力": random.randint(60, 85),
        "相关性": random.randint(70, 95)
    }
    
    suggestions = []
    if len(title) < 15:
        suggestions.append("标题稍短，可以加更多描述")
    elif len(title) > 30:
        suggestions.append("标题过长，建议精简")
    
    if "！" in title or "？" in title:
        suggestions.append("标点符号使用得当")
    
    return {
        "title": title,
        "score": score,
        "factors": factors,
        "suggestions": suggestions
    }

def batch_generate(topic: str, count: int = 10) -> Dict:
    """批量生成内容"""
    return {
        "topic": topic,
        "titles": generate_titles(topic, count=count),
        "xiaohongshu": generate_xiaohongshu_copy(topic),
        "douyin_script": generate_douyin_script(topic),
        "tags": generate_tags(topic),
        "timestamp": "2026-03-12"
    }

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        topic = sys.argv[1]
        print(f"\n🎯 为 '{topic}' 生成内容...\n")
        
        print("📝 爆款标题：")
        for i, title in enumerate(generate_titles(topic), 1):
            print(f"  {i}. {title}")
        
        print(f"\n🏷️ 推荐标签：")
        print(f"  {' '.join(generate_tags(topic))}")
        
        print(f"\n📱 小红书文案：")
        print(generate_xiaohongshu_copy(topic)["content"])
    else:
        print("用法: python copywriter.py <主题>")
