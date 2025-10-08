#!/usr/bin/env python3
"""
Generate sitemap.xml for the website
Includes all app pages, article pages, and knowledge pages
"""

from pathlib import Path
from datetime import datetime
import xml.etree.ElementTree as ET

# Base URL
BASE_URL = "https://linqixin1003.github.io/website"

def create_url_element(loc, lastmod=None, changefreq="monthly", priority="0.8"):
    """Create a URL element for sitemap"""
    url = ET.Element("url")
    
    loc_elem = ET.SubElement(url, "loc")
    loc_elem.text = loc
    
    if lastmod:
        lastmod_elem = ET.SubElement(url, "lastmod")
        lastmod_elem.text = lastmod
    
    changefreq_elem = ET.SubElement(url, "changefreq")
    changefreq_elem.text = changefreq
    
    priority_elem = ET.SubElement(url, "priority")
    priority_elem.text = priority
    
    return url

def generate_sitemap():
    """Generate complete sitemap.xml"""
    
    # Create root element
    urlset = ET.Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    
    # Current date for lastmod
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Main pages with high priority
    main_pages = [
        ("", "1.0", "weekly"),  # Homepage
        ("/bird-app.html", "1.0", "weekly"),
        ("/rock-app.html", "1.0", "weekly"),
        ("/mushroom-app.html", "1.0", "weekly"),
        ("/knowledge.html", "0.9", "weekly"),
    ]
    
    for page, priority, changefreq in main_pages:
        url = create_url_element(
            f"{BASE_URL}{page}",
            lastmod=today,
            changefreq=changefreq,
            priority=priority
        )
        urlset.append(url)
    
    # Article index pages
    article_indexes = [
        "/en/mushroom-articles-index.html",
    ]
    
    for page in article_indexes:
        url = create_url_element(
            f"{BASE_URL}{page}",
            lastmod=today,
            changefreq="weekly",
            priority="0.9"
        )
        urlset.append(url)
    
    base_dir = Path("/Users/infno/Documents/work-code/bird-web/website")
    
    # Bird articles (en/birdwatching/)
    bird_dir = base_dir / "en" / "birdwatching"
    if bird_dir.exists():
        for html_file in sorted(bird_dir.glob("*.html")):
            url = create_url_element(
                f"{BASE_URL}/en/birdwatching/{html_file.name}",
                lastmod=today,
                changefreq="monthly",
                priority="0.7"
            )
            urlset.append(url)
    
    # Rock articles (en/rock-collecting/, rock-formation/, rock-identification/)
    rock_categories = [
        "rock-collecting",
        "rock-formation",
        "rock-formation-types",
        "rock-identification",
        "rock-mineral-science"
    ]
    
    for category in rock_categories:
        category_dir = base_dir / "en" / category
        if category_dir.exists():
            for html_file in sorted(category_dir.glob("*.html")):
                url = create_url_element(
                    f"{BASE_URL}/en/{category}/{html_file.name}",
                    lastmod=today,
                    changefreq="monthly",
                    priority="0.7"
                )
                urlset.append(url)
    
    # Mushroom articles (mushroom/en/)
    mushroom_categories = [
        "culinary-mushrooms",
        "mushroom-ecology",
        "mushroom-identification",
        "mushroom-safety",
        "mushroom-science"
    ]
    
    for category in mushroom_categories:
        category_dir = base_dir / "mushroom" / "en" / category
        if category_dir.exists():
            for html_file in sorted(category_dir.glob("*.html")):
                url = create_url_element(
                    f"{BASE_URL}/mushroom/en/{category}/{html_file.name}",
                    lastmod=today,
                    changefreq="monthly",
                    priority="0.7"
                )
                urlset.append(url)
    
    # Create tree and write to file
    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ", level=0)  # Pretty print
    
    sitemap_path = base_dir / "sitemap.xml"
    tree.write(sitemap_path, encoding="utf-8", xml_declaration=True)
    
    print(f"✅ Sitemap generated: {sitemap_path}")
    print(f"📊 Total URLs: {len(urlset)}")
    
    # Count by type
    main_count = len(main_pages) + len(article_indexes)
    article_count = len(urlset) - main_count
    
    print(f"   - Main pages: {main_count}")
    print(f"   - Article pages: {article_count}")
    
    return sitemap_path

if __name__ == "__main__":
    generate_sitemap()

