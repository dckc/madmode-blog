module.exports = function(eleventyConfig) {
  return {
    dir: {
      input: "src",
      output: "_site"
    },
    // Add pages directory to the list of content sources
    addPassthroughCopy: {
      "src/pages": "pages"
    }
  };
};
