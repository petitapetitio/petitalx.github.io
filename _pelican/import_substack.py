import csv
import os
from pathlib import Path

import html2text

SUBSTACK_EXPORT_DIR = "/Users/lxnd/Downloads/HLQFJ6FGROi0NWquSOg_Cg"
PELICAN_CONTENT_DIR = "content"


def load_substack_posts_metadata(posts_path: str) -> list[dict]:
    with open(posts_path, newline="", encoding='utf-8') as csvfile:
        substack_posts = list(csv.DictReader(csvfile))

        # Filter out drafts
        substack_posts = list(
            item for item in substack_posts if item["is_published"] == "true"
        )

        # Add the path to the post HTML file
        for p in substack_posts:
            p["post_html"] = os.path.join(
                SUBSTACK_EXPORT_DIR, "posts", p["post_id"] + ".html"
            )

        print("Found {} published posts".format(len(substack_posts)))
    return substack_posts


if __name__ == '__main__':

    for post in load_substack_posts_metadata(os.path.join(SUBSTACK_EXPORT_DIR, "posts.csv")):
        date_str = post["post_date"].split("T")[0]
        src_path = Path(post["post_html"])
        target_path = Path(PELICAN_CONTENT_DIR, date_str + " - " + post["title"])
        target_path = target_path.with_suffix(".md")

        if os.path.exists(target_path):
            print("WARN: {} already exists. Will not overwrite!".format(target_path))
            continue

        with open(target_path, "w", encoding="utf8") as outf:
            # Write the metadata
            outf.write("---\n")
            outf.write("date: {}\n".format(post["post_date"]))
            outf.write("title: {}\n".format(post["title"]))
            outf.write("subtitle: {}\n".format(post["subtitle"]))

            outf.write("---\n\n")

            # Write the content
            with open(src_path, "r", encoding="utf8") as inf:
                content = inf.read()

                outf.write(html2text.html2text(content))

        print("wrote {}".format(target_path))

