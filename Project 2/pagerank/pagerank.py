import copy
import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    all_pages = corpus.keys()
    pages_to_pick = corpus[page]
    tran_model = {}

    for ogPage in all_pages: tran_model[ogPage] = (1-damping_factor)/len(all_pages)
    for probPage in pages_to_pick: tran_model[probPage] += damping_factor*1/len(pages_to_pick)

    return tran_model


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    visited = {}
    pageRank = {}
    fake_corpus = copy.deepcopy(corpus)
    all_pages = list(fake_corpus.keys())
    for ogPage in all_pages: visited[ogPage] = 0

    # picking first page
    current_page = random.choice(all_pages)
    tran_model = transition_model(corpus, current_page, damping_factor)

    gg = 0
    while gg < n+1:
        gg += 1
        visited[current_page] += 1
        current_page = random.choices(list(tran_model.keys()), weights=tran_model.values(), k=1)[0] # picks random new page to sample, based on transition model probabilities
        tran_model = transition_model(corpus, current_page, damping_factor)

    # calculate ranks
    for page in visited: pageRank[page] = visited[page]/n

    return pageRank

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pageRank = {}
    fake_corpus = copy.deepcopy(corpus)
    all_pages = list(fake_corpus.keys())
    all_pages_iteration = copy.deepcopy(all_pages)
    for ogPage in all_pages: pageRank[ogPage] = 1/len(all_pages)
    while len(all_pages_iteration) != 0:

        startVal =


    raise NotImplementedError

def numLinks(page, corpus):
    return len(corpus[page])

if __name__ == "__main__":
    main()
