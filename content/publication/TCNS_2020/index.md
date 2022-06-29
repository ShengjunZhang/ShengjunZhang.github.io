---
title: "Sublinear and Linear Convergence of Modified ADMM for Distributed Nonconvex Optimization"

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

date: "2022-04-30T00:00:00Z"
doi: "10.1109/TCNS.2022.3186653"

# Schedule page publish date (NOT publication's date).
publishDate: "2022-06-27T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: In *IEEE Transactions on Control of Network Systems*
publication_short: In *IEEE TCNS*

abstract: In this paper, we consider distributed nonconvex optimization over an undirected connected network. Each agent can only access to its own local nonconvex cost function and all agents collaborate to minimize the sum of   these functions by using local information exchange. We first propose a novel distributed alternating direction method of multipliers (ADMM) algorithm. We show that the proposed algorithm sublinearly converges to a stationary point if each local cost function is smooth and the algorithm parameters are chosen appropriately. We also show that the proposed algorithm linearly converges to a global optimum under an additional condition that the global cost function satisfies the Polyak--{\L}ojasiewicz condition. We then propose a distributed linearized ADMM (L-ADMM) algorithm, derived from the proposed ADMM algorithm by linearizing the local cost function at each iteration. We show that the L-ADMM algorithm has the same convergence properties as the ADMM algorithm under the same conditions. Numerical simulations are included to verify the correctness and efficiency of the proposed algorithms.



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
