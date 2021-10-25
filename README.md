# shakespeare-sonnet-generator

This repo contains code for randomly generating sonnets from Shakespeare's sonnets. It works by retrieving all Shakespeare sonnets (source: https://shakespeare.folger.edu/shakespeares-works/shakespeares-sonnets/download/) and extracting the rhyming lines from the sonnets (knowing the form is ABABCDCDEFEFGG). Then, the code randomly chooses 7 rhyming couplets and arranges them into a new sonnet.

## Running the website

To run this website, first clone and cd into the repo. Note you must have Flask installed for Python. If not, you can run `pip install flask` in your terminal. If pip is not installed, run `conda install pip`. If Anaconda is not installed, you can install it here: https://www.anaconda.com/products/individual.

Once Flask is installed, you can run `flask run` in this folder. The link to access the website is http://127.0.0.1:5000/. Have fun!
