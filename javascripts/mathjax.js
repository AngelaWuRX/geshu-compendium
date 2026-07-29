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
    // Ignore everything, then opt back in. `arithmatex` is the span arithmatex
    // wraps body maths in. `md-nav__link` is the table of contents: the toc
    // extension takes a heading's text content *after* arithmatex has already
    // rewritten `$\theta$` into `\(\theta\)`, then strips the tags — so the
    // sidebar ends up holding the delimiters as literal text. 32 headings carry
    // maths, which showed up as 64 entries reading "Lemma: \(\theta\) is the BP
    // survival probability". Nav links without delimiters are untouched.
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex|md-ellipsis"
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
