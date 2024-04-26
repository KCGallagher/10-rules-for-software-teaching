# Draw a world map, with lines linking the corresponding authors locations of papers citing Chaste

import matplotlib.pyplot as plt
import cartopy.feature
import cartopy.crs as ccrs
import cartopy.feature as cfeature
 
from matplotlib import image
 
 
def main():
    projection = ccrs.Mercator(max_latitude=80, min_latitude=-65)
    projection._threshold = projection._threshold / 100.0
 
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(1, 1, 1, projection=projection)
    ax.set_global()
 
    ax.add_feature(cartopy.feature.LAND, color='grey', lw=0)
    ax.add_feature(cartopy.feature.OCEAN, color='azure', alpha=0.6, lw=0)
 
    # Obtained manually from Google Scholar 
    # (https://scholar.google.com/scholar?cites=6114254425832338898&as_sdt=2005&sciodt=0,5&hl=en)
    citing_locations = [
        (-74, 41),
        (-118, 34),
        (-86, 39),
        (15, 47),
        (-3, 56),
        (1, 51),
        (144, -38),
        (14, 51),
        (2, 52),
        (4, 51),
        (-79, 36),
        (-82, 28),
        (11, 51),
        (2, 49),
        (-3, 51),
        (-71, 42),
        (175, -37),
        (9, 47),
        (6, 51),
        (-76, 43),
        (-98, 30),
        (12, 50),
        (-81, 43),
        (-77, 39),
        (-88, 42),
        (-122, 48)]
 
    for loc in citing_locations:
        ax.scatter(loc[0],
                   loc[1],
                   color='orangered',
                   s=25,
                   zorder=101,
                   transform=ccrs.PlateCarree(),
                   alpha=0.75)
        
        ax.plot((loc[0], 1),
                (loc[1], 51),
                color='orangered',
                lw=1.25,
                zorder=100,
                transform=ccrs.Geodetic(),
                alpha=0.75)
 
    plt.savefig('community.pdf', bbox_inches='tight')
 
 
if __name__ == '__main__':
    main()