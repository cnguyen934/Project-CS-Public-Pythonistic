import pandas as pd

import mexicoSoup

# Convert list from scraper to xlsx
def toXLSX():
    mexicoStates = mexicoSoup.scrapeMexico()
    print(mexicoStates)
    pd.DataFrame(mexicoStates).to_excel('mexicoSoup.xlsx')
    
if __name__ == "__main__":
    toXLSX()
