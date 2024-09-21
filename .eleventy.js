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
