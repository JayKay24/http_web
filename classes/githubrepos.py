import requests

class GithubRepos:
    def __init__(self):
        self.url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
        
    def display_greeting(self):
        """
        Formats and prints the program greeting.
        """
        title = " Most popular python repositories "
        
        print("\n{:*^80s}\n".format(title))
        print("\tThis program finds and displays all the popular python projects")
        print("\ton github and displays them")
        print("\n{:*^80s}\n".format("*"))
        
    def display_popular_repos(self):
        """
        This function requests and displays the most popular python projects on
        Github.
        """
        self.display_greeting()
        # Make and API call to github and store the response object that's
        # returned.
        response = requests.get(self.url)
        
        # Determine if the status code of the response object reflects a
        # successful response. A status code of 200 indicates a successful
        # response.
        print("\tStatus code:", response.status_code)
        
        # Convert the information into a python dictionary.
        response_dict = response.json()
        
        # Display the total count of python repositories on Github.
        print("\tTotal repositories:", response_dict['total_count'])
        
        # Get information about the respositories.
        repos_dicts = response_dict['items']
        
        # Display the number of repositories we have information for.
        print("\tRepositories returned:", len(repos_dicts))
        
        # Loop through each dictionary and display selective information
        # about each repository.
        print("\nPopular python repositories on Github are:\n")
        
        for repo in repos_dicts:
            try:
                print()
                print("\tName:", repo["name"])
                print("\tOwner:", repo["owner"]["login"])
                print("\tStars:", repo["stargazers_count"])
                print("\tRepository:", repo["html_url"])
                print("\tDescription:", repo["description"])
            except UnicodeEncodeError:
                continue
        
        return response_dict
        
        