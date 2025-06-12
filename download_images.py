import os
from uuid import uuid4
from icrawler.builtin import BingImageCrawler


class CustomBingCrawler(BingImageCrawler):
    def _get_filename(self, task, default_ext):
        # Use UUIDs for unique filenames
        return f"{uuid4().hex}.{default_ext}"


categories = {
    "hotdog": "dataset/train/hotdog",
    "car": "dataset/train/car",
    "burger": "dataset/train/burger"
}

for keyword, folder in categories.items():
    os.makedirs(folder, exist_ok=True)
    crawler = CustomBingCrawler(storage={'root_dir': folder})
    crawler.crawl(keyword=keyword, max_num=50)  # This will append new files without overwriting
