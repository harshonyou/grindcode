class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        uniques = set()

        for email in emails:
            local, domain = email.split("@")
            unique = ""
            for ch in local:
                if ch == ".":
                    continue
                if ch == "+":
                    break
                unique += ch
            uniques.add(f"{unique}@{domain}")

        return len(uniques)
