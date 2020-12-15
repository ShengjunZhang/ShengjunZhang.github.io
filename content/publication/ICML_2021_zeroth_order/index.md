---
title: "Zeroth-order Algorithms for Distributed Stochastic Nonconvex Optimization"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- Xinlei Yi
- Shengjun Zhang
- Tao Yang
- Tianyou Chai
- Karl H. Johansson

# Author notes (optional)
author_notes:
- ""
- ""

date: "2021-04-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: In *38th International Conference on Machine Learning (In Submission)*
publication_short: In *ICML 2021 (In Submission)*

abstract: In this paper, we consider stochastic distributed nonconvex optimization with the cost functions be distributed over $n$ agents and only zeroth-order (ZO) information feedback, which emerges in many machine learning applications. We propose two distributed ZO algorithms to solve this problem. In both algorithms, at each iteration each agent samples its local stochastic ZO oracle at two different points with an adaptive smoothing parameter. We show that the proposed algorithms achieve the linear speedup convergence rate $\mathcal{O}(\sqrt{p/(nT)})$ for smooth cost functions and an $\mathcal{O}(p/(nT))$ convergence rate when the global cost function satisfies the Polyak-Lojasiewicz (P-L) condition in addition, where $p$ and $T$ are the dimension of the decision variable and the total number of iterations, respectively. To the best of our knowledge, this is the first linear speedup result for distributed ZO algorithms, which enables us to scale out the computing capability by adding more agents. We also show that the proposed algorithms converge linearly when considering deterministic centralized optimization problems under the P-L condition. We demonstrate through numerical experiments the efficiency of our algorithms in comparison with the baseline and recently proposed centralized and distributed ZO algorithms.


# Summary. An optional shortened abstract.
summary:

tags: []

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# image:
#   caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
#   focal_point: ""
#   preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
# projects:
# - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---

<!-- {{% callout note %}}
Click the *Cite* button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the *Slides* button to check out the example.
{{% /callout %}}

Supplementary notes can be added here, including [code, math, and images](https://wowchemy.com/docs/writing-markdown-latex/). -->
