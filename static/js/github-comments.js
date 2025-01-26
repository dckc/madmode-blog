async function fetchGitHubComments() {
  try {
    // First fetch all issues from each repo
    const repos = ['madmode-blog', 'awesome-ocap', 'finquick'];
    const issuePromises = repos.map((repo) =>
      fetch(
        `https://api.github.com/repos/dckc/${repo}/issues?state=all&per_page=100&sort=updated&direction=desc`,
        {
          headers: { Accept: 'application/vnd.github+json' },
        }
      )
    );
    const issueResponses = await Promise.all(issuePromises);
    const issueArrays = await Promise.all(issueResponses.map((r) => r.json()));

    // Create a map of issue URLs to their titles
    const issueTitles = new Map();
    issueArrays.flat().forEach((issue) => {
      issueTitles.set(issue.url, issue.title);
    });

    // Now fetch comments
    const commentPromises = repos.map((repo) =>
      fetch(
        `https://api.github.com/repos/dckc/${repo}/issues/comments?per_page=25&sort=created&direction=desc`,
        {
          headers: {
            Accept: 'application/vnd.github.html+json',
          },
        }
      )
    );
    const commentResponses = await Promise.all(commentPromises);
    const commentsArrays = await Promise.all(
      commentResponses.map((r) => r.json())
    );

    // Flatten and sort all comments by date
    const comments = commentsArrays
      .flat()
      .filter((comment) => comment.user.login === 'dckc')
      .sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
      .slice(0, 25);

    if (comments.length > 0) {
      const mostRecent = new Date(comments[0].created_at).toLocaleDateString(
        'en-US',
        {
          day: 'numeric',
          month: 'short',
          year: 'numeric',
        }
      );
      document.getElementById(
        'github-comments-date'
      ).textContent = `(${mostRecent})`;
    }

    const list = document.createElement('ul');
    list.className = 'item-list';

    for (const comment of comments) {
      const li = document.createElement('li');
      const date = new Date(comment.created_at).toLocaleDateString('en-US', {
        day: 'numeric',
        month: 'short',
        year: 'numeric',
      });
      const issueNumber = comment.issue_url.split('/').pop();
      const repo = comment.html_url.split('/')[4];
      const issueTitle = issueTitles.get(comment.issue_url) || '(untitled)';
      // Create a temporary div to parse and modify the HTML
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = comment.body_html;

      // Demote headings by 2 levels
      ['h6', 'h5', 'h4', 'h3', 'h2', 'h1'].forEach((oldLevel) => {
        const newLevel = `h${Math.min(6, parseInt(oldLevel.slice(1)) + 2)}`;
        tempDiv.querySelectorAll(oldLevel).forEach((heading) => {
          const newHeading = document.createElement(newLevel);
          newHeading.innerHTML = heading.innerHTML;
          heading.parentNode.replaceChild(newHeading, heading);
        });
      });

      li.innerHTML = `
        <a href="${comment.html_url}" class="issue-title">${issueTitle} · dckc/${repo} #${issueNumber} (${date})</a>
        <div>${tempDiv.innerHTML}</div>`;
      list.appendChild(li);
    }

    document.getElementById('github-comments-list').innerHTML = '';
    document.getElementById('github-comments-list').appendChild(list);
  } catch (error) {
    console.error('Error fetching GitHub comments:', error);
    document.getElementById('github-comments-list').innerHTML =
      'Error loading comments';
  }
}

fetchGitHubComments();
