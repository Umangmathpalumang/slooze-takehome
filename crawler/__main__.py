import argparse
import os
import yaml
import csv
from downloader import Downloader
from parser import parse_product

def load_categories(config_path):
    with open(config_path, 'r') as f:
        data = yaml.safe_load(f)
    return data['categories']

def crawl_category(name, urls, downloader, writer):
    for url in urls:
        try:
            html = downloader.fetch(url)
            product = parse_product(html, url)
            product['category'] = name
            writer.writerow(product)
        except Exception as e:
            print(f"[!] Error fetching {url}: {e}")

def main():
    p = argparse.ArgumentParser(description="Slooze Crawler")
    p.add_argument("--config", required=True, help="categories.yaml")
    p.add_argument("--out",    required=True, help="output CSV path")
    args = p.parse_args()

    # ensure output dir exists
    os.makedirs(os.path.dirname(args.out), exist_ok=True)

    categories = load_categories(args.config)
    downloader = Downloader()

    with open(args.out, 'w', newline='', encoding='utf-8') as csvfile:
        fields = ['category','name','price','moq','supplier','location','source_url']
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

        for cat, urls in categories.items():
            crawl_category(cat, urls, downloader, writer)

if __name__ == "__main__":
    main()
