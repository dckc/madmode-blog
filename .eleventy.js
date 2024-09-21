module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("src/css");

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
