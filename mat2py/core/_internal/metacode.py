# type: ignore
from lib2to3.fixer_base import BaseFix
from lib2to3.refactor import RefactoringTool


# see https://stackoverflow.com/questions/58720279/python-inspect-stacks-code-context-only-returns-one-line-of-context
class StatementScraper(BaseFix):
    PATTERN = "simple_stmt"

    def __init__(self, lineno):
        super().__init__(None, None)
        self.lineno = lineno
        self.statement = ""

    def transform(self, node, result):
        if not self.statement and self.lineno - node.get_lineno() < str(node).count(
            "\n"
        ):
            prev_sibling = str(node.prev_sibling)
            if prev_sibling.isspace():
                self.statement += prev_sibling.lstrip("\n")
            self.statement += str(node)
        return node


class GetStatement(RefactoringTool):
    def __init__(self, source, lineno):
        self.source = source
        self.scraper = StatementScraper(lineno)
        super().__init__(None)

    def get_fixers(self):
        return [self.scraper], []

    def __str__(self):
        self.refactor_string(self.source, "")
        return self.scraper.statement
