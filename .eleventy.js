module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("src/css");

  // Add date filter
  eleventyConfig.addFilter("date", function(date, format) {
    return new Date(date).toLocaleDateString('en-US', {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit'
    });
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
