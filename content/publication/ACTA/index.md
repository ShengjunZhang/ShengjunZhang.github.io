---
title: "Event-triggered Distributed Optimization Algorithms (in Chinese)"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- Tao Yang
- Lei Xu
- Xinlei Yi
- Shengjun Zhang
- Ruijuan Chen
- Yuzhe Li

# Author notes (optional)
author_notes:
- ""
- ""

date: "2021-01-26T00:00:00Z"
doi: "10.16383/j.aas.c200838"

# Schedule page publish date (NOT publication's date).
publishDate: "2021-01-26T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: In *ACTA AUTOMATICA SINICA (自动化学报)*
publication_short: In *ACTA AUTOMATICA SINICA (自动化学报)*

abstract: In this paper, we consider the distributed optimization problem, whose objective is to minimize a global cost function formed by a sum of local private cost functions,  by using local information exchange. In order to avoid continuous communication among agents and reduce communication overheads, we develop event-triggered distributed optimization algorithms for undirected connected graphs based on the proportional-integral control strategy. We show that the proposed algorithms are free of Zeno behavior, and asymptotically converge to one of global minimizers, if the local cost functions are convex and differentiable. Moreover, we show that the proposed algorithms exponentially converge to the unique global minimizer if in addition, the local cost functions have locally Lipschitz gradients, and the global cost function is restricted strongly convex with respect to the global minimizer. The theoretical results are illustrated by numerical simulations.



# Summary. An optional shortened abstract.
summary:

tags: []

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://doi.org/10.16383/j.aas.c200838'
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
