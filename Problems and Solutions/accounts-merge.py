# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails 
# representing emails of the account. Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both 
# accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of 
# accounts initially, but all of their accounts definitely have the same name. After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

# Example 1:

# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and third John's are the same person as they have the common email "johnsmith@mail.com".
# The second John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        emailToName = {}
        group = {}
        ans = []
        
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            parent[parent_y] = parent_x
                
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        for account in accounts:
            emailToName[account[1]] = account[0]
            parent[account[1]] = account[1]
            for e in account[2:]:
                parent[e] = e
                
        for account in accounts:
            email1 = account[1]
            for email2 in account[2:]:
                union(email1, email2)
                
        for email in parent:
            p = find(email)
            if p not in group:
                group[p] = [ email ]
            else:
                group[p].append(email)
                
        for email in group:
            ans.append([emailToName[email]] + sorted(group[email]))
            
        return ans
