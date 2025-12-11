import os

class FileReader:
    def getElements(self, path):
        result = []
        
        try:
            with open(path, 'r') as file:
                for line in file:
                    element = line.strip()
                    result.append(element)
                        
            return result
            
        except FileNotFoundError:
            print(f"Not found in '{path}'")
            return []