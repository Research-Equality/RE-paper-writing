# Template Structure

The AI Scientist templates converge on a simple, slot-based scaffold:

```text
\title{TITLE HERE}
\begin{abstract}
ABSTRACT HERE
\end{abstract}

\section{Introduction}
INTRO HERE

\section{Related Work}
RELATED WORK HERE

\section{Background}
BACKGROUND HERE

\section{Method}
METHOD HERE

\section{Experimental Setup}
EXPERIMENTAL SETUP HERE

\section{Results}
RESULTS HERE

\section{Conclusions and Future Work}
CONCLUSIONS HERE
```

Common conventions:

- A local bibliography block appears near the top of the file.
- `\graphicspath{{../}}` points figures at the experiment folder.
- A placeholder figure is often included and should be replaced, not left in place.
- The scaffold assumes the paper is written directly into `template.tex`, not split across many files.

Use this structure when converting notes and artifacts into a template-first manuscript.
