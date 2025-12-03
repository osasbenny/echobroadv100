import json
import re

def text_to_html(text):
    # Replace double newlines with paragraph tags
    paragraphs = [f"<p>{p.strip()}</p>" for p in text.split('\n\n') if p.strip()]
    html_content = "\n\n".join(paragraphs)

    # Convert numbered lists to ordered lists
    html_content = re.sub(r'<p>(\d+\.\s+.*?)<\/p>', r'<p>\1</p>', html_content, flags=re.DOTALL)
    
    # Convert headings (assuming bold text followed by a period or just bold text)
    html_content = re.sub(r'<p>(\d+\.\s+.*?)<\/p>', r'<h2>\1</h2>', html_content)
    html_content = re.sub(r'<p>(\d+\.\s+.*?)<\/p>', r'<h2>\1</h2>', html_content)
    
    # Simple list conversion for bullet points (assuming lines starting with - or *)
    # This is a simplification, but should work for the provided content structure
    
    # Replace specific list patterns with ul/li
    def replace_list(match):
        items = match.group(1).split('\n')
        list_items = [f'<li>{item.strip()}</li>' for item in items if item.strip()]
        return '<ul>\n' + '\n'.join(list_items) + '\n</ul>'

    # Convert the "Key Points & Lessons" section to a list
    html_content = html_content.replace("Here are Key Points & Lessons for you.", "<h2>Here are Key Points & Lessons for you.</h2>")
    
    # Convert the Marvel "Key Lessons" section to an ordered list
    html_content = html_content.replace("Key Lessons from Marvel’s Comeback", "<h2>Key Lessons from Marvel’s Comeback</h2>")
    
    # Convert the Ant "THE ANT HAS NO BOSS" and "THE ANT WORKS AHEAD OF TIME" to headings
    html_content = html_content.replace("1. THE ANT HAS NO BOSS", "<h2>1. THE ANT HAS NO BOSS</h2>")
    html_content = html_content.replace("2. THE ANT WORKS AHEAD OF TIME. That's vision. Hindsight.", "<h2>2. THE ANT WORKS AHEAD OF TIME. That's vision. Hindsight.</h2>")
    html_content = html_content.replace("WAKE UP!", "<h2>WAKE UP!</h2>")
    html_content = html_content.replace("POVERTY ISN’T SUDDEN", "<h2>POVERTY ISN’T SUDDEN</h2>")
    
    # Convert the Marvel "A little background story..." to a heading
    html_content = html_content.replace("A little background story...", "<h2>A little background story...</h2>")
    
    # Convert the "Why This Matters for Ads" to a heading
    html_content = html_content.replace("✅ Why This Matters for Ads", "<h2>✅ Why This Matters for Ads</h2>")
    
    # Replace the specific numbered list in Marvel post
    html_content = html_content.replace("1.⁠ ⁠In all you do...have the right people in your team.  Some people actually get two heads.", "<ol><li>In all you do...have the right people in your team.  Some people actually get two heads.</li>")
    html_content = html_content.replace("2.⁠ ⁠You have to risk your life on something.", "<li>You have to risk your life on something.</li></ol>")
    
    # Replace the specific numbered list in Marvel post (Key Lessons)
    html_content = html_content.replace("1.⁠ ⁠Control your assets: Owning IP is critical for long-term growth.", "<ol><li>Control your assets: Owning IP is critical for long-term growth.</li>")
    html_content = html_content.replace("2.⁠ ⁠Don’t fear risk: Borrowing $525 million was risky, but it paid off massively.", "<li>Don’t fear risk: Borrowing $525 million was risky, but it paid off massively.</li>")
    html_content = html_content.replace("3.⁠ ⁠Think long-term: The connected universe strategy built sustained engagement.", "<li>Think long-term: The connected universe strategy built sustained engagement.</li>")
    html_content = html_content.replace("4.⁠ ⁠Innovate where others fail: Instead of licensing, they became producers.", "<li>Innovate where others fail: Instead of licensing, they became producers.</li>")
    html_content = html_content.replace("5.⁠ ⁠Turn failure into strategy: Bankruptcy forced them to redefine the business model.", "<li>Turn failure into strategy: Bankruptcy forced them to redefine the business model.</li>")
    html_content = html_content.replace("6.⁠ ⁠Storytelling drives business: Fans bought into characters and worlds, not just products.", "<li>Storytelling drives business: Fans bought into characters and worlds, not just products.</li></ol>")
    
    # Replace the specific bullet list in Silent Killers post
    html_content = html_content.replace("Leaks don’t always come from ads, sometimes they come from your own website.", "<ul><li>Leaks don’t always come from ads, sometimes they come from your own website.</li>")
    html_content = html_content.replace("Building trust is not optional; it's central to converting “just visiting” into “buying.”", "<li>Building trust is not optional; it's central to converting “just visiting” into “buying.”</li>")
    html_content = html_content.replace("Clear messaging + strong value prop equals fewer scared-off visitors, more buyers.", "<li>Clear messaging + strong value prop equals fewer scared-off visitors, more buyers.</li>")
    html_content = html_content.replace("Addressing these problems is not just “nice to do” it directly multiplies the value of your existing traffic and ads.", "<li>Addressing these problems is not just “nice to do” it directly multiplies the value of your existing traffic and ads.</li></ul>")
    
    # Remove the initial "BLOG POSTS" line
    html_content = re.sub(r'<p>﻿BLOG POSTS<\/p>', '', html_content, 1)
    
    # Clean up multiple newlines
    html_content = re.sub(r'\n\s*\n', '\n\n', html_content).strip()
    
    return html_content

def create_slug(title):
    slug = title.lower().strip()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug) # Remove special characters
    slug = re.sub(r'[\s-]+', '-', slug) # Replace spaces and hyphens with a single hyphen
    return slug.strip('-')

def generate_blog_json(blog_text_path, output_json_path):
    with open(blog_text_path, 'r') as f:
        full_text = f.read()

    # Split the content by the post titles
    # The titles are:
    # 1. 3 Silent Killers of Online Businesses … That You’re Probably Ignoring Right Now
    # 2. Marvel Entertainment built an entire cinematic universe, one hit after another...right from a $700M debt just from one decision.
    # 3. How the Smallest Creature Schools Entrepreneurs.
    
    # Use a regex to split the text based on the post numbers and titles
    # The pattern is: \n\d+\.\s+<Title>
    
    # Split the text into three parts based on the post titles
    parts = re.split(r'\n\d+\.\s+', full_text, maxsplit=3)
    
    # The first part is empty or header, the next three are the posts
    post_contents = parts[1:]

    # Titles from the user request
    titles = [
        "3 Silent Killers of Online Businesses … That You’re Probably Ignoring Right Now",
        "Marvel Entertainment built an entire cinematic universe, one hit after another...right from a $700M debt just from one decision.",
        "How the Smallest Creature Schools Entrepreneurs."
    ]
    
    # Excerpts (first paragraph of each post)
    excerpts = [
        "If you’re pouring money into traffic, ads, and content but your sales are still weak, it’s not always because of the market or your offer being “bad.” Sometimes, the real problems hide in plain sight.",
        "Thoughts are powerful. But more importantly, are men who produce the right actionable thought. A new management came...and a decision was made.",
        "You would wonder... How can something so tiny as the ant holds a masterclass in diligence for humans? The writer says, “Go study the ant.”"
    ]
    
    # Tags
    tags = [
        ["Business", "Marketing", "Conversion", "Website Optimization"],
        ["Business Strategy", "Entrepreneurship", "Risk Management", "Success Stories"],
        ["Entrepreneurship", "Productivity", "Self-Leadership", "Business Lessons"]
    ]

    blog_posts = []
    for i, content in enumerate(post_contents):
        # The content starts with the title, so we need to remove it
        # The titles are already in the `titles` list
        
        # Remove the title from the content
        content_without_title = content.replace(titles[i], '', 1).strip()
        
        # Convert to HTML
        html_content = text_to_html(content_without_title)
        
        # Final cleanup of extra newlines in HTML
        html_content = re.sub(r'\n\s*\n', '\n\n', html_content).strip()
        
        blog_posts.append({
            "id": i + 1,
            "title": titles[i],
            "slug": create_slug(titles[i]),
            "author": "David Uwak | EchoBroad Agency",
            "date": "2025-11-30",
            "excerpt": excerpts[i],
            "content": html_content,
            "featured": True,
            "tags": tags[i]
        })

    with open(output_json_path, 'w') as f:
        json.dump(blog_posts, f, indent=2)

if __name__ == "__main__":
    generate_blog_json("/home/ubuntu/upload/BLOGPOSTS(1).txt", "/home/ubuntu/echobroadv99/data/blog-posts.json")
