---
title: "Variance Aware Reward Smoothing for Deep Reinforcement Learning"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- Yunlong Dong
- Shengjun Zhang
- Xing Liu
- Yu Zhang
- Ye Yuan

# Author notes (optional)
author_notes:
- ""
- ""

date: "2021-08-21T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: In *IEEE Transactions on Automatic Control (In Submission)*
publication_short: In *IEEE TAC (In Submission)*

abstract: A Reinforcement Learning (RL) agent interacts with the environment to learn a policy with high accumulated rewards through attempts and failures. However, RL suffers from its own trial-and-error learning nature, which results in an unstable learning process. In this paper, we investigate a commom phenomenon called rewards drop at the late-stage RL training session, where the rewards trajectory oscillates dramatically. In order to solve such a problem, we propose a novel rewards shaping technique named Variance Aware Rewards Smoothing (VAR). We show that the proposed method reduces the variance of rewards and mitigates the rewards drop problem without changing the formulation of the value function. Furthermore, the theoretical analysis of convergence of VAR is provided, which is derived from the γ-contraction operator and the fixed point attribute of the value function. Finally, the theoretical results are illustrated by extensive results on various benchmarks and advanced algorithms across different random seeds to demonstrate the effectiveness and the compatibility of VAR.



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
