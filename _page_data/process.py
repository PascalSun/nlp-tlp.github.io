import json
import os
from slugify import slugify


def main():
    filenames = [
        f for f in os.listdir("in") if os.path.isfile(os.path.join("in", f))
    ]

    page_title_map = {
        "collaborations": "name",
        "current_research": "name",
        "news": "title",
        "our_team": "name",
        "presentations": "title",
        "publications": "title",
        "seminars": "title",
        "software_demos": "name",
    }

    for filename in filenames:
        print(filename)
        with open(os.path.join("in", filename), "r", encoding="utf-8") as f:
            data = json.load(f)

        collection = filename.replace(".json", "")
        out_folder = os.path.join("out", slugify(collection))
        out_data = []

        if not os.path.isdir(out_folder):
            os.mkdir(out_folder)

        for group in data:
            for item in group["items"]:
                out_item = item
                if group["group"] != "(Ungrouped)":
                    out_item["group"] = group["group"]
                out_data.append(out_item)
        for i in out_data:
            with open(
                os.path.join(
                    out_folder,
                    slugify_and_truncate_filename(
                        i[page_title_map[collection]]
                    )
                    + ".md",
                ),
                "w",
                encoding="utf-8",
            ) as f:
                f.write("---\n")
                for k, v in i.items():
                    if k == "images":
                        continue
                    if k == "image_filename" and "our_team/" in v:
                        v = v.replace("our_team/", "")
                    f.write(k + ":" + " " + v + "\n")
                f.write("---\n")


def slugify_and_truncate_filename(s: str, maxlen: int = 50):
    """Parse the given string into a filename that does not exist maxlen
    characters, but also does not truncate words. e.g.
    'one two three four five' with a max len of 5 will be 'one',
    but with a max len of 7 will be 'one-two'.

    Args:
        s (str): Description
        maxlen (int): Description

    Returns:
        str: The parsed filename.
    """
    slug_ls = slugify(s)[:maxlen].split("-")
    slug = ""
    for word in slug_ls:
        if len(slug + word + "-") <= maxlen:
            slug += word
            slug += "-"
    slug = slug[:-1]  # Remove final hyphen
    return slug


if __name__ == "__main__":
    main()
