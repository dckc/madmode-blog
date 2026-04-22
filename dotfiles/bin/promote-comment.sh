#!/bin/bash
# Promote a GitHub issue comment to a blog post
# Usage: promote-comment.sh <comment-url>
# Example: promote-comment.sh https://github.com/dckc/madmode-blog/issues/237#issuecomment-4228178391

set -euo pipefail

BLOG_ROOT="/home/connolly/projects/madmode-blog"
PAGES_DIR="$BLOG_ROOT/pages"

COMMENT_URL="${1:?Usage: promote-comment.sh <comment-url>}"

# Parse the URL to extract repo, issue number, and comment ID
# URL format: https://github.com/<owner>/<repo>/issues/<issue>#issuecomment-<id>
if [[ ! "$COMMENT_URL" =~ ^https://github\.com/([^/]+)/([^/]+)/issues/([0-9]+)#issuecomment-([0-9]+)$ ]]; then
    echo "Error: Invalid comment URL format"
    echo "Expected: https://github.com/<owner>/<repo>/issues/<issue>#issuecomment-<id>"
    exit 1
fi

OWNER="${BASH_REMATCH[1]}"
REPO="${BASH_REMATCH[2]}"
ISSUE_NUM="${BASH_REMATCH[3]}"
COMMENT_ID="${BASH_REMATCH[4]}"

echo "Fetching comment $COMMENT_ID from $OWNER/$REPO#$ISSUE_NUM..."

# Fetch comment via gh API
COMMENT_JSON=$(gh api repos/$OWNER/$REPO/issues/comments/$COMMENT_ID)

# Extract fields
BODY=$(echo "$COMMENT_JSON" | jq -r '.body')
CREATED_AT=$(echo "$COMMENT_JSON" | jq -r '.created_at')
COMMENTER=$(echo "$COMMENT_JSON" | jq -r '.user.login')

# Get issue title for context
ISSUE_TITLE=$(gh api repos/$OWNER/$REPO/issues/$ISSUE_NUM | jq -r '.title')

# Parse date for URL and frontmatter
DATE_FULL=$(date -d "$CREATED_AT" +"%Y-%m-%d %H:%M:%S" 2>/dev/null || date -j -f "%Y-%m-%dT%H:%M:%SZ" "$CREATED_AT" +"%Y-%m-%d %H:%M:%S" 2>/dev/null)
YEAR=$(echo "$DATE_FULL" | cut -d'-' -f1)
MONTH=$(echo "$DATE_FULL" | cut -d'-' -f2)
DAY=$(echo "$DATE_FULL" | cut -d'-' -f3 | cut -d' ' -f1)

# Create directory if it doesn't exist
mkdir -p "$PAGES_DIR/$YEAR/$MONTH"

# Generate filename
FILENAME="${REPO}-${ISSUE_NUM}-issuecomment-${COMMENT_ID}.md"
FILEPATH="$PAGES_DIR/$YEAR/$MONTH/$FILENAME"

# Generate title from issue title
TITLE="$ISSUE_TITLE (comment)"

# Check if file already exists
if [[ -f "$FILEPATH" ]]; then
    echo "Error: File already exists: $FILEPATH"
    exit 1
fi

# Extract first line of body for summary (strip markdown)
SUMMARY=$(echo "$BODY" | head -1 | sed 's/^#* //' | head -c 120)

# Write the blog post with --- delimiters
cat > "$FILEPATH" << HEREDOC_END
---
title: "$TITLE"
date: $YEAR-$MONTH-$DAY
tags: ["github", "syndicated"]
published: true
summary: "$SUMMARY"
---

HEREDOC_END

# Append the comment body
echo "$BODY" >> "$FILEPATH"

# Append syndication link
cat >> "$FILEPATH" << HEREDOC_END

---

*Originally appeared as [a comment on $ISSUE_TITLE]($COMMENT_URL).*
HEREDOC_END

echo "Created blog post: $FILEPATH"
echo "URL will be: /$YEAR/$MONTH/$FILENAME"
echo ""
echo "Next steps:"
echo "1. Review and edit the file if needed"
echo "2. Adjust tags and summary as appropriate"
echo "3. Commit and deploy"
