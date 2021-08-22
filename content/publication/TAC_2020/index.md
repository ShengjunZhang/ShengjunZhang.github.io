---
title: "Linear Convergence of First- and Zeroth-Order Primal-Dual Algorithms for Distributed Nonconvex Optimization"

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

date: "2021-08-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2021-08-22T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: In *IEEE Transactions on Automatic Control (To appear 2022)*
publication_short: In *IEEE TAC (To appear 2022)*

abstract: This paper considers the distributed nonconvex optimization problem of minimizing a global cost function formed by a sum of local cost functions by using local information exchange.  We first propose a distributed first-order primal-dual algorithm. We show that it converges sublinearly to a stationary point if each local cost function is smooth and linearly to a global optimum under an additional condition that the global cost function satisfies the Polyak-{\L}ojasiewicz condition. This condition is weaker than strong convexity, which is a standard condition for proving linear convergence of distributed optimization algorithms, and the global minimizer is not necessarily unique. Motivated by the situations where the gradients are unavailable, we then propose a distributed  zeroth-order algorithm, derived from the proposed distributed first-order algorithm by using a deterministic gradient estimator, and show that it has the same convergence properties as the proposed first-order algorithm  under the same conditions. The theoretical results are illustrated by numerical simulations.



# Summary. An optional shortened abstract.
summary:

tags: []

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://arxiv.org/pdf/1912.12110.pdf'
url_code: 'https://github.com/ShengjunZhang/DBC'
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
