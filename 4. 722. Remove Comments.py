from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        inBlockComment = False  # Indicates that it is not a block comment
        currentLine = ""

        for line in source:
            i = 0
            while i < len(line):
                if not inBlockComment and line[i:i+2] == "//":
                    # Line comment found, ignore the rest of the line
                    break
                elif not inBlockComment and line[i:i+2] == "/*":
                    # Start of block comment found
                    inBlockComment = True
                    i += 1
                elif inBlockComment and line[i:i+2] == "*/":
                    # End of block comment found
                    inBlockComment = False
                    i += 1
                elif not inBlockComment:
                    # Append character to the current line unless it is a line comment
                    currentLine += line[i]
                i += 1

            if currentLine and not inBlockComment:
                # Add non-empty lines to the result
                result.append(currentLine)
                currentLine = ""

        return result
