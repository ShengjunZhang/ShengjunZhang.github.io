---
title: "A Primal-Dual SGD Algorithm for Distributed Nonconvex Optimization"

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

date: "2020-10-23T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2020-10-23T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: In *SIAM Journal on Optimization (Under Review)*
publication_short: In *SIOPT (Under Review)*

abstract:   The distributed nonconvex optimization problem of minimizing a global cost function formed by a sum of $n$ local cost functions by using local information exchange is considered. This problem is an important component of many machine learning techniques with data parallelism, such as deep learning and federated learning. We propose a distributed primal-dual stochastic gradient descent (SGD) algorithm,  suitable for arbitrarily connected communication networks and any smooth (possibly nonconvex) cost functions. We show that the proposed algorithm achieves the linear speedup convergence rate $\mathcal{O}(1/\sqrt{nT})$ for general nonconvex cost functions and  the linear speedup convergence rate $\mathcal{O}(1/(nT))$ when the global cost function satisfies the Polyak-Lojasiewicz (P-L) condition, where $T$ is the total number of iterations. We also show that the output of the proposed algorithm with fixed parameters linearly converges to a neighborhood of a global optimum. We demonstrate through numerical experiments the efficiency of our algorithm in comparison with the baseline centralized SGD and recently proposed distributed SGD algorithms.



# Summary. An optional shortened abstract.
summary:

tags: []

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://arxiv.org/pdf/2006.03474.pdf'
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
