---
title: "Linear Convergence for Distributed Optimization Without Strong Convexity"

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

date: "2020-12-14T00:00:00Z"
doi: "10.1109/CDC42340.2020.9304381"

# Schedule page publish date (NOT publication's date).
publishDate: "2020-12-14T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *59th IEEE Conference on Decision and Control*
publication_short: In *CDC 2020*

abstract: This paper considers the distributed optimization problem of minimizing a global cost function formed by a sum of local smooth cost functions by using local information exchange. Various distributed optimization algorithms have been proposed for solving such a problem. A standard condition for proving the linear convergence for existing distributed algorithms is the strong convexity of the cost functions. However, the strong convexity may not hold for many practical applications, such as least squares and logistic regression.  In this paper, we propose a distributed primal-dual gradient descent algorithm and establish its linear convergence under the condition that the global cost function satisfies the Polyak-Lojasiewicz condition. This condition is weaker than strong convexity and the global minimizer is not necessarily unique. The theoretical result is illustrated by numerical simulations.



# Summary. An optional shortened abstract.
summary:

tags: []

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://doi.org/10.1109/CDC42340.2020.9304381'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: 'cdc_2020_slides.pdf'
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
