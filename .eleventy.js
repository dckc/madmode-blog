const jsdom = require("jsdom");
const { JSDOM } = jsdom;

module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("src/css");

  // Add date filter
  eleventyConfig.addFilter("date", function(date, format) {
    if (date === "now") {
      date = new Date();
    }
    if (format === "yyyy") {
      return date.getFullYear();
    }
    return date.toISOString().slice(0, 10); // Returns date in YYYY-MM-DD format
  });

  // Add summary filter
  eleventyConfig.addFilter("summary", function(content) {
    const dom = new JSDOM(content);
    const summary = dom.window.document.querySelector('p');
    if (summary) {
      return summary.textContent.slice(0, 135) + (summary.textContent.length > 135 ? '...' : '');
    }
    return content.slice(0, 135) + (content.length > 135 ? '...' : '');
  });

  // Create tag pages
  eleventyConfig.addCollection("tagList", function(collection) {
    let tagSet = new Set();
    collection.getAll().forEach(function(item) {
      if ("tags" in item.data) {
        let tags = item.data.tags;
        tags = tags.filter(item => item !== "posts");
        for (const tag of tags) {
          tagSet.add(tag);
        }
      }
    });
    return [...tagSet];
  });

  // Add permalink structure for tag pages
  eleventyConfig.addFilter("tagUrl", function(tag) {
    return `/search/label/${tag}/`;
  });

  // Generate search index
  eleventyConfig.addCollection("searchIndex", function(collection) {
    return collection.getAll().map(page => ({
      id: page.url,
      title: page.data.title,
      url: page.url,
      content: page.template.inputContent
    }));
  });

  eleventyConfig.addPassthroughCopy({
    "src/search-index.json": "search-index.json"
  });

  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes"
    },
    // Configure the permalink for posts
    permalinks: {
      structure: "/blog/:date/:title/",
      date: "yyyy"
    }
  };
};
