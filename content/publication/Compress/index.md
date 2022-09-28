---
title: "Communication Compression for Distributed Nonconvex Optimization"

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

date: "2022-01-15T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2022-01-15T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: In *IEEE Transactions on Automatic Control (Under Review)*
publication_short: In *IEEE TAC (Under Review)*

abstract: This paper considers decentralized nonconvex optimization with the cost functions being distributed over agents. Noting that information compression is a key tool to reduce the heavy communication load for decentralized algorithms as agents iteratively communicate with neighbors, we propose three decentralized primal--dual algorithms with compressed communication. The first two algorithms are applicable to a general class of compressors with bounded relative compression error and the third algorithm is suitable for two general classes of  compressors with bounded absolute compression error. We show that the proposed decentralized algorithms with compressed communication have comparable convergence properties as state-of-the-art algorithms without communication compression. Specifically, we show that they can find first-order stationary points with sublinear convergence rate $\mathcal{O}(1/T)$ when each local cost function is smooth, where $T$ is the total number of iterations, and find global optima with linear convergence rate under an additional condition that the global cost function satisfies the Polyak--{\L}ojasiewicz condition. Numerical simulations are provided to illustrate the effectiveness of the theoretical results.

# Summary. An optional shortened abstract.
summary:

tags: []

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://arxiv.org/pdf/2201.03930.pdf'
url_code: 'https://github.com/ShengjunZhang/Compression_distributed_nonconvex'
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
