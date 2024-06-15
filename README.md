# github-create-and-add-labels-all-repos-using-python
Create and add GitHub labels to repositories which can be later used for pull requests and issues 

# How code works

* we use _**GitHub REST API**_ to programatically create Labels
* The program `create_new_labels.py` have 2 parts 
    1. It uses GitHub endpoint for listing repos under an organization to list all repositories
    2. It uses create labels end point to create labels in repos
* Proper logs (*error* OR *success messgaes*) are displayed


# Authentication method used

`I am using fine grained personal access token`

 
* The fine-grained token must have at least one of the following permission sets:

    * "Issues" repository permissions (write)
    * "Pull requests" repository permissions (write)

# Reference

[Create Github Labels](https://docs.github.com/en/rest/issues/labels?apiVersion=2022-11-28#create-a-label)