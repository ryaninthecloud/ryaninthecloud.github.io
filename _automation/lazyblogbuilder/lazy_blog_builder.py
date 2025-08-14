'''
I need to automate the blog posting.
I am lazy, but like the simplicity of pure html/css blogging.
'''

import sys
import os
from bs4 import BeautifulSoup
import datetime

index_content_file = sys.argv[1]
new_content_file = sys.argv[2]

with open(index_content_file, 'r', encoding='utf-8') as _:
    index_content_file = _.read()

with open(new_content_file, 'r', encoding='utf-8') as _:
    new_content_file = _.read()

run_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
new_content_div = f'''<div id="latestPost">{new_content_file}</div>'''

index_content_parser = BeautifulSoup(index_content_file, features="html.parser")
new_content_div_rendered = BeautifulSoup(new_content_div, features="html.parser")

current_latest_post = index_content_parser.find(
    "div",
    {
        "id" : "latestPost"
    }
)

archive_post_stack = index_content_parser.find(
    "div",
    {
        "id" : "oldPostStack"
    }
)

last_updated_data = index_content_parser.find(
    "p",
    {
        "id" : "lastUpdatedData"
    }
)

new_blog_post_title = new_content_div_rendered.find(
    "b"
)

last_updated_data.string.replace_with("Last Updated: " + run_time + " by LazyBlogBuilder")

new_blog_post_title.string.replace_with(
    new_blog_post_title.string + f" - Released on [{run_time}]"
)

current_latest_post.attrs["id"] = "_automatedOldPost"

new_archive_post = f'''<div class="oldPost" style="padding-top: 5px;">{current_latest_post}</div>'''
new_archive_post_rendered = BeautifulSoup(new_archive_post, features="html.parser")

current_latest_post.replace_with(
    new_content_div_rendered
)

archive_post_stack.insert(0, new_archive_post_rendered)


with open('new_.html', 'w+') as f:
    f.write(
        str(index_content_parser)
        )
