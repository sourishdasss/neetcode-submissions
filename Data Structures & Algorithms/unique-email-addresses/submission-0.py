class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for e in emails:
            local_name, domain_name = e.split("@")

            tmp = ""
            for c in local_name:
                if c == ".":
                    continue
                elif c == "+":
                    break
                else:
                    tmp += c

            cleaned_email = tmp + "@" + domain_name
            unique_emails.add(cleaned_email)

        return len(unique_emails)