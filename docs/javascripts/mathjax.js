// Pairs with `pymdownx.arithmatex: {generic: true}`, which rewrites $...$ and
// $$...$$ into \(...\) / \[...\] wrapped in .arithmatex spans before MathJax
// ever sees them. That indirection is why the delimiters below look nothing
// like what the notes are written in.
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// Material loads pages via instant navigation, so MathJax has to be re-run on
// each one rather than only at initial load.
document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.typesetReset();
  MathJax.typesetPromise();
});
