import unittest
import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)

from classes.githubrepos import GithubRepos

class GithubReposTest(unittest.TestCase):
    def setUp(self):
        self.github_repos = GithubRepos()
        self.response_dict = self.github_repos.display_popular_repos()
        
    def test_response_dict_is_a_dictionary(self):
        self.assertTrue(type(self.response_dict) is dict, 
        "response dict should be a dictionary")
        
if __name__ == '__main__':
    unittest.main()