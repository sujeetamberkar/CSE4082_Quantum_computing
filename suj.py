import re
import os

def convert_links_in_file(file_path):
    # Read the original content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression to find Obsidian-style links
    obsidian_link_pattern = r"\[\[([^\]]+)\]\]"

    # Function to convert found Obsidian links to GitHub markdown links
    def link_replacer(match):
        page_name = match.group(1)
        # Replace spaces with %20 for URL encoding and add the .md extension
        github_link = f"[{page_name}]({page_name.replace(' ', '%20')}.md)"
        return github_link

    # Replace all Obsidian links with GitHub markdown links
    updated_content = re.sub(obsidian_link_pattern, link_replacer, content)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

# Get all markdown files in the current directory
current_directory = os.getcwd()
markdown_files = [f for f in os.listdir(current_directory) if f.endswith('.md')]

# Convert links in all markdown files
for md_file in markdown_files:
    convert_links_in_file(os.path.join(current_directory, md_file))
