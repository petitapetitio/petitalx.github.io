import csv
import os
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


def substack_to_pelican(substack_dir: str, pelican_content_dir: str):
    for post in load_substack_posts_metadata(os.path.join(substack_dir, "posts.csv")):
        date_str = post["post_date"].split("T")[0]
        src_path = Path(post["post_html"])
        target_path = Path(pelican_content_dir, date_str + " - " + post["title"])
        target_path = target_path.with_suffix(".md")

        with open(target_path, "w", encoding="utf8") as outf:
            outf.write("---\n")
            outf.write("date: {}\n".format(post["post_date"]))
            outf.write("title: {}\n".format(post["title"]))
            outf.write("subtitle: {}\n".format(post["subtitle"]))

            outf.write("---\n\n")

            # Write the content
            with open(src_path, "r", encoding="utf8") as inf:
                html = inf.read()
                content = collect_images_and_use_local_urls(html, target_path.parent / "images")
                # md_content = html2text.html2text(content)
                outf.write(content)

        print("wrote {}".format(target_path))


def load_substack_posts_metadata(posts_path: str) -> list[dict]:
    with open(posts_path, newline="", encoding='utf-8') as csvfile:
        substack_posts = list(csv.DictReader(csvfile))

        # Filter out drafts
        substack_posts = list(
            item for item in substack_posts if item["is_published"] == "true"
        )

        # Add the path to the post HTML file
        directory = Path(posts_path).parent
        for p in substack_posts:
            p["post_html"] = os.path.join(directory, "posts", p["post_id"] + ".html")

        print("Found {} published posts".format(len(substack_posts)))
    return substack_posts


def collect_images_and_use_local_urls(html_content: str, save_directory: Path):
    soup = BeautifulSoup(html_content, 'html.parser')

    # # Remove source tags
    # for tag in soup.find_all('source'):
    #     tag.decompose()
    #
    # # Remove "expand-image blocs":
    # for tag in soup.find_all('.image-link-expand'):
    #     tag.decompose()

    # for img in soup.find_all('img'):
    #     remote_url = img.get('src')
    #     if remote_url:
    #         local_url = save_directory / os.path.basename(os.path.basename(urlparse(remote_url).path))
    #         download_image(remote_url, local_url)
    #         img['src'] = str(local_url)
    #         del img['srcset']
    #         del img['data-attrs']
    #         print(img)
    #     else:
    #         print("WARN: Image tag without src attribute found")

    for figure in soup.find_all('figure'):
        img_tag = figure.find('img')
        remote_url = img_tag.get('src')

        local_url = save_directory / os.path.basename(os.path.basename(urlparse(remote_url).path))
        download_image(remote_url, local_url)

        figcaption = figure.find('figcaption')
        caption_text = figcaption.get_text(strip=True) if figcaption else ''
        new_caption_tag = soup.new_tag('p', style='text-align: center; font-style: italic; font-size: 0.8em;')
        new_caption_tag.string = caption_text

        # Replace the <figure> tag with the new <img> and <p> tags
        figure.insert_after(new_caption_tag)
        figure.insert_after(soup.new_tag('img', src=Path(*local_url.parts[1:])))
        figure.decompose()

    return str(soup)


def download_image(url: str, save_path: Path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download image from {url}")


if __name__ == '__main__':
    substack_to_pelican("/Users/lxnd/Downloads/HLQFJ6FGROi0NWquSOg_Cg", "content")
