class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # example string : ["test.ema.il+alex@leetcode.com"]
        result = set()
        for emailId in emails:
            splittedMail = emailId.split("@")     # will return ['test.ema.il+alex', 'leetcode.com']
            splittedMail[0] = splittedMail[0].replace(".","")  # will return 'testemail+alex'
            plusIndex = splittedMail[0].find("+") # will return the first index of +
            if plusIndex!= -1:
                splittedMail[0] = splittedMail[0][:plusIndex]
            splittedMail = splittedMail[0] + "@" + splittedMail[1]
            result.add(splittedMail)
        return len(result)