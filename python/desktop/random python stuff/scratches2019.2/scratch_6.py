stars = {3.6: 87, 3.2: 64, 2.2: 136, 1.6: 69, 2.1: 113, 2.8: 38, 2.0: 116, 1.2: 12, 8.3: 9, 5.5: 117, 3.3: 88, 4.2: 71,
         5.6: 92, 2.9: 47, 4.5: 96, 3.7: 83, 5.2: 77, 4.6: 92, 5.3: 62, 4.4: 92, 4.9: 106, 5.1: 90, 4.7: 93, 5.0: 98,
         3.9: 58, 2.5: 59, 5.8: 70, 1.5: 46, 3.8: 66, 2.3: 131, 1.8: 103, 4.1: 65, 1.7: 126, 4.3: 66, 3.4: 102, 6.6: 27,
         2.6: 40, 4.8: 100, 3.5: 104, 1.3: 19, 1.9: 99, 3.0: 56, 2.7: 41, 3.1: 64, 5.7: 91, 4.0: 38, 1.4: 39, 5.4: 89,
         2.4: 77, 6.0: 76, 6.9: 22, 8.0: 4, 1.1: 9, 6.2: 47, 6.1: 73, 7.2: 22, 7.7: 7, 6.5: 31, 5.9: 52, 8.7: 1, 7.8: 2,
         6.4: 34, 8.2: 7, 7.1: 18, 6.7: 24, 7.0: 26, 6.3: 34, 0.9: 2, 6.8: 15, 7.9: 3, 7.3: 12, 0.7: 2, 0.4: 1, 97.7: 1,
         7.4: 15, 0.6: 1, 7.5: 6, 7.6: 10, 8.4: 3, 8.1: 3, 9.5: 3, 8.6: 3, 9.6: 1, 10.1: 2, 10.0: 2, 11.8: 1, 8.9: 2,
         10.2: 1, 0.5: 1, 13.4: 1, 44.3: 1, 10.6: 1, 1.0: 1, 8.8: 1, 9.0: 1}

import plotly.express as px
import pandas as pd
"""newdct = stars.copy()
for i in stars:
    if i > 11 or i < 4.5:
        del newdct[i]
stars = newdct"""

#print(max(stars.keys()))
stars = pd.DataFrame(list(stars.items()), columns=['Stars', '# of maps']).sort_values(by=['Stars']).reindex()
print(stars)
fig = px.histogram(stars)
fig.show()